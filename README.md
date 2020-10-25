README.md
- SIDDHARTH GANGWAR
- LPU 11711321

Pre Requisite:
	0. Python: pip install python
	1. Flask: pip install flask
	2. SQLalchemy: pip install flask-sqlalchemy
	3. MySQLdb: pip install flask-mysqldb
	4. MySql: pip install mysql
	5. MySqlConnector: pip install mysql-connector

After installing above packages:
	1. Import the blackjack.db file into your PHPmyadmin database.
	2. Run the blackjack.py command -- python blackjack.py
	3. Open 127.0.0.1 (LocalHost)

USING APP:
	
	1. SignUp: At the singup phase, just enter the details required and after submitting you will be redirected to login page.

	2. Login: Enter the details which was used to sign in, after successful login you will be directer to the profile page.

	3. Profile: This displays the info of the user, the chips left in his account and you can either choose to play the game or hit the logout button to successfully get logged out.

	4. Play: in the play section, after hitting START button you will be redirected to GAME WINDOW, with the entered bet by the user.

	5. In Game: you can choose to HIT or STAND according to your preference. If you HIT then another card gets added to your score and it you stand dealer reveals his cards.

	6. Score: after the game is ended it would simply return your chips and display the message whether you won or lost. You can now choose to play again or go back to profile.


IMP POINTS:
	1. Each game cost is 10 coins. Once you hit start button 10 chips are deduced form your account.
	2. The bet amount is automatically deleted from account as soon as he hits start button.
	3. The winning amount is doubled of the bet and if the player lost, he had to give all the chips.
