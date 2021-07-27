from os import truncate


Title = '------GAMES------'
print("*"*len(Title))
print(Title)
print("*"*len(Title))
print("Please Enter Details in Valid Format")
user_db = {"abhiram":["abhiram45","abhi@5544.co.uk"]}
global username

option=input("""
Menu:
1.Register
2.Login 
select an option: """)

#Login is only possible for the creator of Program.

while option == '1':
	print("=====Register====")

	while True:
		reg_user=input("Enter UserName: ")

		if(reg_user in user_db):
			print("\n username already exist")
		elif len(reg_user)<4 or len(reg_user)>20:
			print("\n username must be between 4-20 characters")
		elif reg_user[0].isalpha()!=True:
			print('\n username must start with letter')
		elif reg_user.isalnum() == False:
			print("\n username can only contain numbers and letters")
		else:
			break

	while True:
		reg_pass = input("Enter Password: ")

		if len(reg_pass) < 6:
			print("password must be greater than 6 letters")
		elif reg_pass.isdigit() == True or reg_pass.isalpha() == True:
			print("password must not contain numbers and letters")
		else:
			break
	while True:
		reg_email = input("Enter your Mail Address:")
		reg_email = reg_email.lower()

		for lists in user_db.values():
			if lists[1] == reg_email:
				print("Email ddress already exists.")
			elif reg_email.count('@')!=1 or reg_email.count(".") == 0 or len(reg_email)<10:
				 print("invalid Email_Address")
				 break
		else:
			break
	

	print(f"{reg_user} you may login")
	break
	
while option == '2':
	while True:
		username=input("enter username: ")

		if username not in user_db:
			print("no such username1")
		else:
			break

	while True:
			password = input("Enter password: ")

			if password != user_db[username][0]:
				print("incorrect password!")
			else:
				break
	

	print(f"welcome {username}")
	break

option1 = input("""
Menu
1.Hand_Cricket
2.Rock_Paper_Scissor
3.MadLibs
4.Guess_Number
Select your choice: """)


while option1 == "1":
		print("===== Hand_Cricket =====")
		score = 1

		def u_input():
				global user_input
				print(f"player score is {score}")
				user_input = input("player scored : ")

		def player_move():
				if user_input in ('1','one'):
					return '1'
				elif user_input in ('2','two'):
					return '2'
				elif user_input in ('3','three'):
					return '3'
				elif user_input in ('4','four'):
					return '4'
				elif user_input in ('5','five'):
					return '5'
				elif user_input in ('6','six'):
					return '6'
				else :
					return False

		def computer_move():
				import random
				number = ('1','2','3','4','5','6')
				comp = random.choice(number)
				return comp

		def check_winner():
				global score
				player = player_move()
				computer = computer_move()

				if player == False:
					print("Enter the numbers")
				elif player == '1' and computer == '1' :
					print("you: " ,player)
					print("computer:", computer)
					print('player is out')
					score = 0
				elif player == '2' and computer == '1':
					score +=1
					print("you: " ,player)
					print("computer:", computer)
					print("play the game")
				elif player == '3' and computer == '1':
					score +=1
					print("you: " ,player)
					print("computer:", computer)
					print("play the game")
				elif player == '4' and computer == '1':
					score +=1
					print("you: " ,player)
					print("computer:", computer)
					print("play the game")
				elif player == '5' and computer == '1':
					score +=1
					print("you: " ,player)
					print("computer:", computer)
					print("play the game")
				elif player == '6' and computer == '1':
					score +=1
					print("you: " ,player)
					print("computer:", computer)
					print("play the game")

				elif player == '1' and computer == '2' :
					print("you: " ,player)
					print("computer:", computer)
					print('play the game')
					score +=1
				elif player == '2' and computer == '2':
					print("you: " ,player)
					print("computer:", computer)
					score = 0
					print("player is out")
				elif player == '3' and computer == '2':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '4' and computer == '2':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '5' and computer == '2':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '6' and computer == '2':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")

				elif player == '1' and computer == '3' :
					print("you: " ,player)
					print("computer:", computer)
					print('play the game')
					score +=1
				elif player == '2' and computer == '3':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '3' and computer == '3':
					print("you: " ,player)
					print("computer:", computer)
					score = 0
					print("player is out")
				elif player == '4' and computer == '3':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '5' and computer == '3':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '6' and computer == '3':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")

				elif player == '1' and computer == '4' :
					print("you: " ,player)
					print("computer:", computer)
					print('play the game')
					score += 1
				elif player == '2' and computer == '4':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '3' and computer == '4':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '4' and computer == '4':
					print("you: " ,player)
					print("computer:", computer)
					score = 0
					print("player is out")
				elif player == '5' and computer == '4':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '6' and computer == '4':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")

				elif player == '1' and computer == '5' :
					print("you: " ,player)
					print("computer:", computer)
					print('play the game')
					score += 1
				elif player == '2' and computer == '5':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '3' and computer == '5':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '4' and computer == '5':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '5' and computer == '5':
					print("you: " ,player)
					print("computer:", computer)
					score = 0
					print("player is out")
				elif player == '6' and computer == '5':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")

				elif player == '1' and computer == '6' :
					print("you: " ,player)
					print("computer:", computer)
					print('play the game')
					score += 1
				elif player == '2' and computer == '6':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '3' and computer == '6':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '4' and computer == '6':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '5' and computer == '6':
					print("you: " ,player)
					print("computer:", computer)
					score +=1
					print("play the game")
				elif player == '6' and computer == '6':
					print("you: " ,player)
					print("computer:", computer)
					score = 0
					print("player is out")
				else :
					print(end=' ')
	

		title = """ *** Cricket *** """
		print('*'*len(title))
		print(title)
		print('*'*len(title))
		print('The initial socre of the player is "1"')

		while score > 0 :
			u_input()
			player_move()
			computer_move()
			check_winner()
		break


while option1 == '2':

	print("====Rock_Paper_Scissor====")
	money = 15

	def balance():
			global user_input
			print(f"you have {money}")
			print("it's $5 to play")
			user_input = input("pick rock,paper,scissor: ")

	def player_move():
			if user_input in ("ROCK","rock","r","R"):
				return "rock"
			elif user_input in ("PAPER",'P','paper','p'):
				return "paper"
			elif user_input in ("SCISSOR",'S','scissor','s'):
				return "scissor"
			else :
				return False

	def computer_move():
			import random
			rps = ("rock","paper","scissor")
			comp = random.choice(rps)
			return comp

	def check_winner():
			global money
			player = player_move()
			computer = computer_move()

			if player == False:
				print("Pick Rock or Paper or Scissor")
				
			elif player == "rock" and computer == "rock":
				print('you:' ,player)
				print('computer: ', computer, '\nDraw.\n')
			elif player == "scissor" and computer == "rock":
				print("you: " ,player)
				print("computer:", computer,"\nComputer Wins.\n")
				money -= 5
			elif player =="paper" and computer == "rock":
				print("you:", player)
				print('computer:',computer,"\nPlayer Wins.\n")
				money += 5

			elif player == "paper" and computer == "paper":
				print('you:' ,player)
				print('computer: ', computer, '\nDraw.\n')
			elif player == "rock" and computer == "paper":
				print("you: " ,player)
				print("computer:", computer,"\nComputer Wins.\n")
				money -= 5
			elif player =="scissor" and computer == "paper":
				print("you:", player)
				print('computer:',computer,"\nPlayer Wins.\n")
				money += 5

			elif player == "scissor" and computer == "scissor":
				print('you:' ,player)
				print('computer: ', computer, '\nDraw.\n')
			elif player == "paper" and computer == "scissor":
				print("you: " ,player)
				print("computer:", computer,"\nComputer Wins.\n")
				money -= 5
			elif player =="rock" and computer == "scissor":
				print("you:", player)
				print('computer:',computer,"\nPlayer Wins.\n")
				money += 5

			
	title = " *** Rock-Paper-Scissors ***"
	print("-"*len(title))
	print(title)		
	print("-"*len(title))


	while money > 0:
		balance()
		player_move()
		computer_move()
		check_winner()
	
	print("you don't have any money left")
	break
while option1 == '3':
	print("Choose from these options")
	print(["wrestle", "sticky", "moldy", "scary", "scream", "football", "snakes"])
	score = 0
	print("===== MadLibs =====")
	op1 = input()
	if op1 == "sticky":
		score+=1
		print(f"{score}		Correct Answer")
	elif op1!= "sticky":
		score+=0
		print(f"{score}		Incorrect Answer")
	op2 = input()
	if op2 == "wrestle":
		score+=1
		print(f"{score}		Correct Answer")
	elif op2 != "wrestle":
		score+=0
		print(f"{score}		Incorrect Answer")
	op3 = input()
	if op3 == "moldy":
		score+=1
		print(f"{score}		Correct Answer")
	elif op3 != "moldy":
		score+=0
		print(f"{score}		Incorrect Answer")
	op4 = input()
	if op4 == "snakes":
		score+=1
		print(f"{score}		Correct Answer")
	elif op4 != "snakes":
		score+=0
		print(f"{score}		Incorrect Answer")
	op5 = input()
	if op5 == "scream":
		score+=1
		print(f"{score}		Correct Answer")
	elif op5 == "scream":
		score+=0
		print(f"{score}		Incorrect Answer")
	op6 = input()
	if op6 == "scary":
		score+=1
		print(f"{score}		Correct Answer")
	elif op6 != "scary":
		score+=0
		print(f"{score}		Incorrect Answer")
	op7 = input()
	if op7 == "football":
		score+=1
		print(f"{score}		Correct Answer")
	elif op7 != "football":
		score+=0
		print(f"{score}		Incorrect Answer")

	print(f"Your total score is: {score}")

	print("Your answer is: ")
	
	Madlib = f"""Our school cafeteria has really {op1} food. Just thinking about it makes my stomach {op2}. The sapghetti is {op3} and tastes like {op4}. One day, I swear one of my meat balls started to {op5}! Theturkey tacos are totally {op6} and look like old {op7}"""

	
	print(Madlib)
	break

print("===== Number_Guess =====")

while option1 == '4':
	import random
	#You have only one choice
	def n_guess(x):
		random_num = random.randint(1,x)
		print(random_num)
		n_guess = 0
		while n_guess!= random_num:
			n_guess = int(input("Guess the number between 1 and {x}: "))
			if n_guess > random_num:
				print(f"{n_guess} is greater than the {random_num}")
			elif n_guess < random_num:
				print(f"{n_guess} is less than {random_num}")

		print(f"Congrats!!! {n_guess} is same as {random_num}")

	n_guess(10)
	break 
	