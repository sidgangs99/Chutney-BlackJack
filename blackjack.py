from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import random
from models import Deck, UserHand, ComputerHand
import hashlib
from mysql.connector import MySQLConnection, Error
from database import db_session, init_db

app = Flask(__name__)

CARD_SCORES = {
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'K': 10,
    'J': 10,
    'Q': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    'Ace': 11
}

app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('user_id', None)
        session.pop('username', None)
        
        pwd=hashlib.md5((request.form['password']).encode())
        pwd=str(pwd.hexdigest())
        queryExist="SELECT name, password, id, chips FROM user WHERE name = %s" 
        print("query exist : ", queryExist)
        try:
            cursor.execute(queryExist, (request.form['username'] ,))
            rowExist = cursor.fetchone()
            print("row exist: ", rowExist)
            if rowExist:
                if ((rowExist[0]==(request.form['username'])) and (rowExist[1]==pwd)):
                    print("heeelo")
                    session['username'] = rowExist[0]
                    session['user_id'] = rowExist[2]
                    session['chips'] = rowExist[3]
                    return redirect(url_for('profile'))
                else:
                    return redirect(url_for('login'))
        except Error as error:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        password=hashlib.md5(str(request.form['password']).encode())
        password=str(password.hexdigest())
    
        data = (
            str(request.form['username']),
            int(request.form['chip']),
            str(password),
        )
        sql="INSERT INTO user (name,chips,password) VALUES(%s,%s,%s)"
        try:
                    print(sql, data)
                    cursor.execute(sql, data)
                    print("yo")
                    conn.commit()
                    return redirect(url_for('login'))
        except Error as error:
            print("hello")    

    return render_template("signup.html") 


@app.route('/start_game')
def start_game():
    init_or_flush_cards()
    generate_deck()
    session['chips'] = session['chips']-10
    i = 0
    while i < 2:  # Both gamers get 2 cards from deck to start the game
        add_user_card(get_card_from_deck())
        add_computer_card(get_card_from_deck())
        i += 1
    user_cards = get_user_cards()

    return render_template('game.jinja2', user_cards=user_cards, user_score=calc_score(user_cards))


@app.route('/profile')
def profile():
    return render_template('profile.html', name=session['username'], chips = session['chips'])


@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print('Hello')
        print((str)(request.form['starting']))
        session['game_chips'] = (int)(request.form['starting'])
        session['chips'] = session['chips'] - (int)(request.form['starting'])
        sql = "UPDATE user SET chips = %s WHERE id = %s"
        data = (
            session['chips'],
            session['user_id'],
        )

        cursor.execute(sql, data)
        conn.commit()
        return redirect(url_for('start_game'))
    return render_template('index.html', chips=session['chips'])

@app.route('/get_card')
def get_card():
    add_user_card(get_card_from_deck())
    computer_score = calc_score(get_computer_cards())
    if computer_score < 17 or (21 - computer_score > 2):  # Computer should get card in case of it's score < 17
        add_computer_card(get_card_from_deck())
    user_cards = get_user_cards()
    if calc_score(user_cards) > 21:
        return redirect(url_for('stop'))
    return render_template('game.jinja2', user_cards=user_cards, user_score=calc_score(user_cards))


@app.route('/stop')
def stop():
    user_score = calc_score(get_user_cards())
    computer_score = calc_score(get_computer_cards())
    if (user_score > 21 and computer_score > 21) or user_score == computer_score:
        result = 'Friendship won'
    elif user_score <= 21 and computer_score > 21:
        result = 'You won'
    elif user_score > 21 and computer_score <= 21:
        result = 'You lose'
    elif user_score > computer_score:
        result = 'You won'
    else:
        result = 'You lose'
    win_chips = 0
    if result == 'You won':
        session['chips'] = session['chips'] + ((int)(session['game_chips']) * 3)
        win_chips = " + " + (str)((int)(session['game_chips']) * 2)
    elif result == 'You lose':
        win_chips = " - " + (str)(session['game_chips'])
    data = (
            session['chips'],
            session['user_id'],
        )
    return render_template('score.jinja2', result=result, computer_score=computer_score, user_score=user_score, win_chips=win_chips , chip=session['chips'])


def init_or_flush_cards():
    '''
    Creates tables and clears them
    '''
    init_db()
    for database in [UserHand, ComputerHand, Deck]:
        database.query.delete()
    save()


def generate_deck():
    '''
    Generates list of cards and stores it to model
    '''
    deck = [a for a in CARD_SCORES.keys()] * 4
    random.shuffle(deck, random.random)
    for card in deck:
        card = Deck(str(card))
        db_session.add(card)
    save()


def get_deck():
    return Deck.query.all()


def get_user_cards():
    return UserHand.query.all()


def get_computer_cards():
    return ComputerHand.query.all()


def add_user_card(card):
    card = UserHand(card)
    db_session.add(card)
    save()


def add_computer_card(card):
    card = ComputerHand(card)
    db_session.add(card)
    save()


def get_card_from_deck():
    '''
    Gets top card and removes it from deck
    :return: card String
    '''
    deck = get_deck()
    card = str(deck.pop(0))
    db_session.delete(Deck.query.filter_by(card=card).first())
    save()
    return card


def save():
    try:
        db_session.commit()
    except Exception as e:
        print (e)


def calc_score(cards):
    '''
    :param cards: List of cards
    :return: Score of given cards set
    '''
    score = 0
    for card in cards:
        score += CARD_SCORES[str(card)]
    return score


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    print (exception)


if __name__ == '__main__':
    conn = MySQLConnection(
    host="127.0.0.1",
    user="root",
    password="",
    database="blackjack"
    )

    cursor = conn.cursor(buffered=True)

    app.run()
