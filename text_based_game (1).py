import time

from datetime import date

import calendar

import random

import os

timetosleep = .1

def printandsleep(message):
	print(message)
	time.sleep(timetosleep)

def printandsleep2(message):
	print(message)
	time.sleep(timetosleep/2)

# lines 22-27 not my own work; taken from https://www.delftstack.com/howto/python/python-clear-console/
def clear():
	time.sleep(1)
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)
	time.sleep(.5)

def quit():
	clear()
	exit()

#ascii art taken from: https://patorjk.com/software/taag

def lose():
	clear()
	print("""
	 .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
	| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
	| |  ____  ____  | || |     ____     | || | _____  _____ | | | |   _____      | || |     ____     | || |    _______   | || |  _________   | || |       _      | |
	| | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| | | |  |_   _|     | || |   .'    `.   | || |   /  ___  |  | || | |_   ___  |  | || |      | |     | |
	| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | | | |    | |       | || |  /  .--.  \  | || |  |  (__ \_|  | || |   | |_  \_|  | || |      | |     | |
	| |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | | | |    | |   _   | || |  | |    | |  | || |   '.___`-.   | || |   |  _|  _   | || |      | |     | |
	| |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | | | |   _| |__/ |  | || |  \  `--'  /  | || |  |`\____) |  | || |  _| |___/ |  | || |      | |     | |
	| |   |______|   | || |   `.____.'   | || |    `.__.'    | | | |  |________|  | || |   `.____.'   | || |  |_______.'  | || | |_________|  | || |      (_)     | |
	| |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | |
	| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 	 '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 """)
	exit()

def win():
	clear()
	print("""
	 .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .-----------------. .----------------. 
	| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
	| |  ____  ____  | || |     ____     | || | _____  _____ | | | | _____  _____ | || |     _____    | || | ____  _____  | || |       _      | |
	| | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| | | ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || |      | |     | |
	| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | | | |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || |      | |     | |
	| |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | | | |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || |      | |     | |
	| |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | | | |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || |      | |     | |
	| |   |______|   | || |   `.____.'   | || |    `.__.'    | | | |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || |      (_)     | |
	| |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
	| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
	 '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' 
	""") 
	exit()

def inputchecker(msg, options):
	global timetosleep
	answer = input("\033[0;33m" + msg + "\033[0;0m").lower()
	if answer == "!exit":
		quit()
	elif answer in options:
		return answer
	elif answer == "!help":
		printandsleep2("Here your commands!")
		printandsleep("!waystowin (shows you the ways to win the game), !waystolose (shows you the ways to lose the game), !options (shows you your options), !exit (quits the program), !slowdown (slows down the game), and !speedup (speeds up the game)")
	elif answer == "!options":
		printandsleep("Your options are " + str(options))
	elif answer == "!waystowin":
		printandsleep("You can win if you: Successfully survive one whole day as Carson, make 10,000 dollars, get an A+ on each assessment in school, beat Kane in wrestling, or make either of your parents proud.")
	elif answer == "!waystolose":
		printandsleep("You lose if you die, fail an assessment, sustain an injury wrestling, or displease your parents.")
	elif answer == "!slowdown":
		timetosleep = (timetosleep+(1/4)*(timetosleep))
		printandsleep("The game will now print text slower.")
	elif answer == "!speedup":
		timetosleep = (timetosleep-(1/4)*(timetosleep))
		printandsleep("The game will now print text faster.")
	else:
		printandsleep("Please enter a valid option. Use !options to see your valid options.")
	return inputchecker(msg, options)

clear()
printandsleep("Hello and welcome to my text based game. Thanks for playing.")
printandsleep("First off: Do you want to use a special color for when you talk?")
coloruse = inputchecker("Please type either 'Yes' or 'No'!", ["yes", "no"])
if coloruse == "yes":
	printandsleep("Your special color can be either red, green, blue, purple, or cyan.")
	color = inputchecker("What is your favorite simple color?", ["red", "green", "blue", "purple", "cyan"])
	if color == "cyan":
		colorvar = 36
	elif color == "red":
		colorvar = 31
	elif color == "green":
		colorvar = 32
	elif color == "blue":
		colorvar = 34
	elif color == "purple":
		colorvar = 35
	printandsleep("Great! Your special color has been set!")
elif coloruse == "no":
	printandsleep("Okay! No special color for you.")
	colorvar = 0
	
def youprintandsleep(message):
	printandsleep("\033[0;" + str(colorvar) + "mYOU: " + message + "\033[0;0m")

name = input("Now, what is your name?")

if name == "Carson" or name == "carson":
	printandsleep("Cool, that's my name too! You get to skip the first test.")
	printandsleep("So sup, Carson. This game is simple. You're living an average day in my life. There's a few ways to win. And a few ways to lose. If you ever need help with anything, just type !help.")
	printandsleep("So, let's talk about the ways to win. You can win if you: Successfully survive one whole day as Carson, get an A+ on each assessment in school, beat Kane in wrestling, or make either of your parents proud.")
else:
	printandsleep("Well, hello, " + name + ". This game is simple. You're living an average day in someone's life. Carson's life. So forget '" + name + "', your new name is Carson. There are a few ways to win. And a few ways to lose.")
	nametest_necessary = True
	
	if nametest_necessary == True:
		nametest = input("Wait, I forgot. What's your name again?").lower()
	else:
		printandsleep("So, let's talk about the ways to win. You can win if you: Successfully survive one whole day as Carson, Get an A+ on each assessment in school, Beat Kane in wrestling, or make either of your parents proud.")

	if nametest == "carson":
		printandsleep("Congratulations. You passed the first test.")
		printandsleep("So, let's talk about the ways to win. You can win if you: Successfully survive one whole day as Carson, Get an A+ on each assessment in school, Beat Kane in wrestling, or make either of your parents proud.")
	elif nametest == name:
		printandsleep("I told you to forget " + name + "! Your name is Carson. You lose.")
		lose()
	else:
		printandsleep("I just told you! Your name is Carson. You lose.")
		lose()


printandsleep("Losing's a thing too. If you had entered your real name in your first test, you would have lost and the game would have been over. You lose if you die, fail an assessment, sustain an injury wrestling, or displease your parents.")

printandsleep("Remember - you can always use !help to see your list of commands. It's super helpful if you're stuck or if you forget something!")

input("When you are ready to start the game, please press enter.")

print("And the game begins in...")
time.sleep(timetosleep/3)

def print10times(number):
	for x in range(0, 10):
		print(number)
		time.sleep(.1)

print10times(5)
print10times(4)
print10times(3)
print10times(2)
print10times(1)
clear()

printandsleep("Your alarm sound goes off and you're woken up to light Jamacian music. You role out of bed, and eyes still bleary, go into the shower.")

printandsleep("After showering, doing your hair, and sprinting to the bus, you're overwhelmed with choices - you could sit next to anyone.")

printandsleep("You usually sit next to Jared, but you could also sit next to Nikki, Ahaan, or a stranger")

helpastranger = 0

sitnextto = inputchecker("Who do you want to sit next to?", ["jared", "ahaan", "nikki", "stranger", "a stranger"])

if sitnextto == "jared":
	printandsleep("You walk up to Jared and he moves his bags for you to sit next to him")
	printandsleep2("JARED: Sup")
	youprintandsleep("I'm so tired. I went to bed at like 2 last night")
	printandsleep2("JARED: Why? I finished my homework early and went to bed early")
	youprintandsleep("I have to turn in my history essay today... and I procrastinated a bit")
	printandsleep2("JARED: That sucks")
	
elif sitnextto == "nikki":
	printandsleep("You walk up to Nikki. Her brother is in the seat across from her, but he doesn't even notice you sit down as he is staring at his phone.")
	printandsleep2("NIKKI: Is that Carson??")
	youprintandsleep("No")
	printandsleep2("Nikki: Why do you always sit next to Jared, sit up here with me more")
	youprintandsleep("Sure")
	youprintandsleep("Did you turn in the history essay yet?")
	printandsleep2("NIKKI: Of course! It's due in a few hours")
	youprintandsleep("I did a ton of work on it last night, but I'm going to turn it in later")
	printandsleep2("NIKKI: Okay - Good luck!")
	
elif sitnextto == "ahaan":
	printandsleep("You walk up to Ahaan. He is sitting silently in the back of the bus, watching something on his phone.")
	printandsleep2("AHAAN: Yo!!! My boy!")
	youprintandsleep("Sup Ahaan! I'm so tired")
	printandsleep2("AHAAN: Yeah man me too I had so much work last night")
	youprintandsleep("Yeah same. Are we still hanging out this weekend?")
	printandsleep2("AHAAN: Hell yeah. I'm so excited.")

elif sitnextto == "stranger" or sitnextto == "a stranger":
	printandsleep("You walk up to a girl who looks to be 16 or so years old.")
	youprintandsleep("Hey, Can I sit here?")
	printandsleep("The girl nods yes and moves her bags, making space for you to sit down.")
	convowithgirl = inputchecker("Do you want to initiate a conversation with the girl?", ["yes", "y", "no", "n"])
	if convowithgirl == "yes" or convowithgirl == "y":
		youprintandsleep("Hey, I'm Carson. Do I recognize you from somewhere?")
		printandsleep("MARY: It's Mary! I'm in your Python class.")
		youprintandsleep("Oh, Mary, that's right. I'm sorry!")
		printandsleep("MARY: Don't worry about it! Did you do the homework due tomorrow?")
		didthepythonhw = inputchecker("You didn't do the homework, but you don't want Mary to think you're a procrastinator, and you want something to talk to her about. Do you tell her you did the homework?", ["yes", "y", "no", "n"])
		if didthepythonhw == "yes" or didthepythonhw == "y":
			youprintandsleep("Yeah, it took me forever.")
			helpmarywithhomework = inputchecker("Mary: I tried so hard on it but I just couldn't figure it out. Could you help me with it later?", ["yes", "y", "no", "n"])
			if helpmarywithhomework == "yes" or helpmarywithhomework == "y":
				youprintandsleep("Sure! How's D period?")
				printandsleep2("Mary: Sounds great! Thanks so much! Do you want to just meet in our normal classroom?")
				youprintandsleep("Sure.")
				helpastranger = 1
			elif helpmarywithhomework == "no" or helpmarywithhomework == "n":
				youprintandsleep("Sorry, I'm super busy today and I won't have time.")
				printandsleep ("Mary: Don't worry about it. See you in class, then.")
		elif didthepythonhw == "no" or didthepythonhw == "n":
			youprintandsleep("I haven't done it yet.")
			printandsleep("Mary: Okay! It's super hard. Make sure to do it later because it's due tomorrow haha!")
	elif convowithgirl == "no" or convowithgirl == "n":
		printandsleep("You decide to be a recluse.")

printandsleep("You insert your headphones and turn on some music. You let yourself begin to fall asleep - you've got some time before arriving at school.")
printandsleep("You wake up to gentle sounds of The Notorious B.I.G and the loud movements of dozens of high schoolers ariving at school.")
printandsleep("You march into Lutnick and up the stairs. Your first class, biology, starts in 5 minutes. You've got a quiz, but the teacher said it would be easy.")
biostudy = 0
prebioactivity = inputchecker("What do you want to do before class starts? You can sit and study or talk to some friends.", ["sit", "sit and study", "study", "talk", "talk to some friends", "talk to friends"])
if prebioactivity == "sit" or "prebioactivity" == "sit and study"or prebioactivity == "study":
	biostudy = 1
	printandsleep("You sadly sit down in a chair outside your biology classroom and stare into pages of your biology notes.")
elif prebioactivity == "talk" or prebioactivity == "talk to some friends" or prebioactivity == "talk to friends":
	whichfriendsnerd = inputchecker("Which friend do you want to talk to? You can talk to Charlie Davis, Oliver, or Odirin.", ["odirin", "oliver", "guyer", "charlie", "charlie d", "charlie d.", "charlie davis"])
	if whichfriendsnerd == "odirin":
		printandsleep("You walk up to Odirin and tap him on the shoulder.")
		youprintandsleep("Sup, Odirin.")
		printandsleep2("ODIRIN: Hey Carson, what's up?")
		youprintandsleep("Not much, we have a test right?")
		printandsleep2("ODIRIN: No, it's a quiz. I heard its on the human body - and I also heard that Ms. Feigin's quizzes are easy.")
		youprintandsleep("Thank God.")
		printandsleep2("You excitedly walk into the classroom, prepared to ace the quiz.")
	elif whichfriendsnerd == "charlie" or whichfriendsnerd == "charlie davis" or whichfriendsnerd == "charlie d" or whichfriendsnerd == "charlie d.":
		printandsleep("As soon as you look to Charlie, he starts walking towards you.")
		printandsleep2("CHARLIE: Hey man, did you study?")
		printandsleep2("CHARLIE: I was up till, like, 2 A.M.")
		youprintandsleep("No, it's supposed to be easy. Anyways, I'm a good guesser")
		printandsleep2("CHARLIE: Bro. You're so dumb. I heard this was the hardest quiz of the year!")
		printandsleep2("You mutter an expletive and thank Charlie for the information.")
		printandsleep2("You slump into the classroom and prepare for your 'impossible' quiz.")
	elif whichfriendsnerd == "oliver" or whichfriendsnerd == "guyer":
		printandsleep("You walk up to Guyer and tap him on the shoulder.")
		youprintandsleep("Sup guyer")
		printandsleep2("GUYER: What's up kiggity Carson")
		youprintandsleep("Man, I hope this test is easy like everyone said it would be.")
		printandsleep2("GUYER: It's a quiz, not a test. Gotta use that big brain of yours!")
		youprintandsleep("Wowwww. What a hilarious joke. Good luck with the test.")
		printandsleep("You walk into the classroom and prepare to take the quiz.")

clear()

printandsleep("Ms. Feigin hands out the tests; you get yours first, meaning you will have the most time.")
printandsleep("Before you start the test, remember the ways to lose! Getting less than a 50% on a test is one of them!")
printandsleep("You write your name on the top of the quiz and you are delighted to see that the quiz is all multiple choice. You are instructed to write the letter correponding to the correct answer. There are five questions. Each question is worth 20 points.")

printandsleep("The first question is: What is the powerhouse of the cell?")
printandsleep2("A: Mitochondria")
printandsleep2("B: Cell Membrane")
printandsleep2("C: Chloroplast")
printandsleep2("D: Nucleus")
q1 = inputchecker("What is your answer to question one?", ["a", "b", "c", "d"])

printandsleep("The second question is: What is larger, a population or a community?")
printandsleep2("A: Population")
printandsleep2("B: Community")
printandsleep2("C: Neither a population nor a community is necessarily larger than the other")
printandsleep2("D: Populations and communities are always the same sizes")
q2 = inputchecker("What is your answer to question two?", ["a", "b", "c", "d"])

printandsleep("The third question is: What type of cells can be found in animals?")
if biostudy == 1:
	printandsleep("You remember this question from your studying before class! You think that it's Eukaryotic.")
printandsleep2("A: Nucleoid")
printandsleep2("B: Prokaryotic")
printandsleep2("C: Chromosome")
printandsleep2("D: Eukaryotic")
q3 = inputchecker("What is your answer to question three?", ["a", "b", "c", "d"])

printandsleep("The fourth question is: What is your biology teacher's name?")
printandsleep2("A: Mr. Camba")
printandsleep2("B: Ms. Mo")
printandsleep2("C: Ms. Feigin")
printandsleep2("D: Mr. Mojica")
q4 = inputchecker("What is your answer to question four?", ["a", "b", "c", "d"])

printandsleep("What do we call a relationship where both organisms benefit?")
printandsleep2("A: Mutualism")
printandsleep2("B: Commensalism")
printandsleep2("C: Predation")
printandsleep2("D: Competition")
q5 = inputchecker("What is your answer to question five?", ["a", "b", "c", "d"])

grade = 0
if q1 == "a":
	grade = grade + 20
if q2 == "b":
	grade = grade + 20
if q3 == "d":
	grade = grade + 20
if q4 == "c":
	grade = grade + 20
if q5 == "a":
	grade = grade + 20

if grade < 50:
	printandsleep("You breathe a sign of release as you have finished and you think you did well. You turn the paper around to the other side just in case.")
	printandsleep("You are happy to see that there's an extra credit question. You don't think you'll need to get it right, but it's still nice!")
else:
	printandsleep("You are freaking out as you think that you bombed that test. You turn the paper around, praying that there isn't any more difficult questions.")
	printandsleep("Thank God! There's an extra credit question. It could save your quiz!")

printandsleep("Right before you begin to read the extra credit question, you hear an announcement from your teacher.")
printandsleep("MS. FEIGIN: Everyone, there is an extra credit question on the back, and getting it correct will increase your score by 20 points. Make sure to answer the question carefully!")
printandsleep("Twenty points is a ton. Make sure to get this right!")
printandsleep("Your extra credit question is: What day of the week is it today?")
extraq = inputchecker("What is your answer to the extra credit question?", ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])

#these two lines not my own work, taken from https://www.delftstack.com/howto/python/python-datetime-day-of-week/
curr_date = date.today()
currentday = calendar.day_name[curr_date.weekday()]

if extraq == currentday.lower():
	grade = grade + 20

printandsleep("You hand in your test and anxiously wait for the results.")
printandsleep("Ms. Feigin starts grading right away and says your grades will all be ready in a few minutes.")
printandsleep("A few minutes later, Ms. Feigin hands you your graded test.")
printandsleep("The grade on the top is " + str(grade) + "%!")

if grade >= 100:
	printandsleep("You are ecstatic! You got an amazing score!")
	printandsleep("You take out your iPad and text your parents.")
	youprintandsleep("I aced the biology quiz!")
	printandsleep("DAD: Hard work is the only way.")
	printandsleep("DAD: Keep it up.")
	printandsleep("MOM: OMG Carson amazing!!!! You are doing so well this year! I am so proud of you!")
	printandsleep("You put away your iPad and quiz with a slight grin. The class is over and you hastily pack your bags and begin to sprint to Geometry class, which is all the way in Tillinghast!")
elif grade == 80:
	printandsleep("Alright. Could have gone better, that's for sure. Not Harvard material, but you still did well!")
	printandsleep("You pack up your quiz and start to walk over to your next class, Geometry.")
elif grade == 60 and extraq == currentday.lower():
	printandsleep("You just barely passed. Thank God for that extra credit question!")
	printandsleep("You throw your quiz away and slowly walk towards your next class, Geometry.")
elif grade == 60:
	printandsleep("You just barely passed. If only you could have gotten a few more right and made your parents proud.")
	printandsleep("You crinkle up your quiz and throw it into the recycling bin like you're Stephen Curry")
	printandsleep("You start running towards your next class, Geometry.")
else:
	printandsleep("Well... you failed.")
	printandsleep("I told you what would happen if you failed an assessment.")
	printandsleep("Well, goodbye, " + name + ". I guess you are called that again now.")
	lose()

clear()

printandsleep("You see your friends, Pietro and Max, in the hallway outside geometry class.")
pregeoactivity = inputchecker("Do you want to talk to them or go right to class?", ["talk", "talk to them", "class", "go to class"])
if pregeoactivity == "talk" or pregeoactivity == "talk to them":
	printandsleep("You walk up to Max and Pietro.")
	printandsleep2("PIETRO: Bro where were you last night you have to play Call of Duty sometime")
	youprintandsleep("Couple tests today. Had to study")
	printandsleep2("PIETRO: Oh yeah. You ready for the math test today? I had to reach out to Ms. Gao a lot, I don't know anything.")
	youprintandsleep("We don't have a test today bro.")
	printandsleep2("MAX: He totally got you though.")
	youprintandsleep("I don't know about that man.")
	printandsleep2("MS. GAO: Come on in, everyone!")
	printandsleep("The three of you walk into class and sit down in your regular seats.")
elif pregeoactivity == "class" or pregeoactivity == "go to class":
	printandsleep("You walk into class, brushing by your friends, and sit down in your regular seat.")

printandsleep2("MS. GAO: Okay guys, let's get started.")
printandsleep2("MS. GAO: Today we are going to define and prove the triangle angle sum theorem.")
printandsleep("You feel bored as you already know the theorem. Your eyes drift to your backpack where you have your iPad.")
printandsleep("You could take out your iPad and do work for other classes or play games instead of focusing.")
boredduringgeo = inputchecker("Do you want to take out your iPad?", ["yes", "y", "no", "n"])

def boredduringgeofunction():
	if doesshecatchyou < 4 and boredduringgeo in ["yes", "y"]:
		ipaduse = inputchecker("What would you like to do?", ["homework", "work on homework", "game", "video game", "play", "play a video game", "draw", "draw something", "put away the ipad", "put away", "text", "text your parents", "super secret option"])
		if ipaduse == "homework" or ipaduse == "work on homework":
			printandsleep("You open google classroom and you see that you have no homework assigned.")
			printandsleep("You even check your school email and see that it's blanked.")
			printandsleep("You swipe out of classroom and you're back at the homescreen.")
			boredduringgeofunction()
		elif ipaduse == "game" or ipaduse == "video game" or ipaduse == "play a video game" or ipaduse == "play":
			printandsleep("Which video game would you like to play? Your two favorite games, and the only games on your phone, are Clash Royale and Clash of Clans.")
			isursoundon = random.randint(1, 2)
			gamegeo = inputchecker("What game do you want to play?", ["clash royale", "clash of clans"])
			if gamegeo == "clash royale":
				if isursoundon == 1:
					printandsleep("You open up Clash Royale but decide not to click 'battle'.")
					printandsleep("Battling is risky as you could be forced to stop playing mid-round, causing you to lose valuable trophies")
					printandsleep("You spend the next 10 minutes playing Clash Royale talking to your friends in game and twiddling your thumbs.")
					boredduringgeofunction()
				elif isursoundon == 2:
					printandsleep("Your sound is on. As soon as you open Clash Royale, the familiar loud noise disrupts the class.")
					printandsleep("MS. GAO: Carson, I'm not sure that we need our computers out right now to prove this.")
					youprintandsleep("Oh, okay. I'm sorry!")
					printandsleep("You disgruntledly put away the iPad and begin blankly waiting until class ends.")
			elif gamegeo == "clash of clans":
				if isursoundon == 1:
					printandsleep("You open up Clash of Clans and you are informed that your base has been attacked.")
					randomvalue1 = random.randint(1, 1000000)
					randomvalue2 = random.randint(1, 1000000)
					randomvalue3 = random.randint(1, 1000000)
					randomvalue4 = random.randint(1, 1000000)
					devalue1 = random.randint(1, 5000)
					devalue2 = random.randint(1, 5000)
					printandsleep("In the attack, you lost " +str(randomvalue1) + " elixir, " + str(randomvalue2) + " gold, and " + str(devalue1) + " dark elixir.")
					printandsleep("You can get revenge on your attacker by attacking his base with your trained army.")
					attackback = inputchecker("Do you do it?", ["yes", "y", "no", "n"])
					if attackback == "yes" or attackback == "y":
						printandsleep("You launch a successful revenge attack against the person who attacked you previously.")
						printandsleep("In the attack, you gained " + str(randomvalue3) + " elixir, " + str(randomvalue4) + " gold, and " + str(devalue2) + " dark elixir.")
						printandsleep("Feeling satisfied with your revenge, you close Clash of Clans.")
						boredduringgeofunction()
					elif attackback == "no" or attackback == "n":
						printandsleep("You decide to take the loss of resources and not attack back the person who stole them.")
						printandsleep("Feeling satisfied but a bit eeked, you close Clash of Clans.")
						boredduringgeofunction()
				elif isursoundon == 2:
					printandsleep("Your sound is on. As soon as you open Clash of Clans, the familiar loud noise disrupts the class.")
					printandsleep("MS. GAO: Carson, I'm not sure that we need our computers out right now to prove this.")
					youprintandsleep("Oh, okay. I'm sorry!")
					printandsleep("You disgruntledly put away the iPad and begin blankly waiting until class ends.")
		elif ipaduse == "draw" or ipaduse == "draw something":
			list_of_choices = ["dolphin", "panda", "zebra", "house", "dog", "face", "computer", "glass of water", "cookie", "blueberry", "banana", "bowl", "pineapple", "dragon", "ghost", "city", "beach", "ufo", "teddy bear", "candy cane", "tricycle", "snowman", "tree", "leaf", "diamond", "starscape", "pizza", "zombie", "mummy", "man with a scar", "duck", "ninja", "spaceship", "flaming skull", "pig", "queen" "hot air balloon", "king kong", "godzilla", "fairy", "castle", "horse", "shooting star", "flute", "piano", "violin", "birdhouse", "train", "dog wearing pants", "dancer", "singer", "python teacher", "student", "school"]
			drawduringgeo = random.choice(list_of_choices)
			printandsleep("You open up Procreate and open a new file. You're feeling inspired to draw a " + drawduringgeo + ".")
			printandsleep("You spend about 20 minutes on your " + drawduringgeo + " and you feel like your work is excellent. You think it is so good that you post it on reddit.")
			updoots = random.randint(1, 100000)
			upvotes = str(updoots)
			printandsleep("20 minutes later, you check on reddit. It has received " + upvotes + " upvotes.")
			if updoots > 75000:
				drawformoney = random.choice(list_of_choices)
				printandsleep("Wow. That's a ton of upvotes. So many that you got noticed by a major art company which offered you $10,000 to draw a " + drawformoney + ".")
				printandsleep("They said the drawing had to be really good, however, and if it isn't they aren't going to pay you.")
				printandsleep("You can skip your next few classes to work on your drawing. Doing so would risk your parents being mad at you but could net you $10,000.")
				drawitornah = inputchecker("Do you do it?", ["yes", "y", "no", "n"])
				if drawitornah == "yes" or drawitornah == "y":
					printandsleep("You spend the next four hours working on your drawing and you finally submit it to the art company.")
					printandsleep("You need to have done a good job for the art company to pay you; if you did a bad job, you will get nothing.")
					printandsleep("After minutes of waiting, a notification from the art company arrived...")
					goodornah = random.randint(1, 3)
					if goodornah == 1:
						printandsleep("THE ART COMPANY: We really like your artwork. Here's your $10,000, as promised.")
						printandsleep("BANK OF AMERICA: You have received 10,000 dollars from the Art Company.")
						printandsleep("Congratulations, you have made $10,000, meaning you win!")
						printandsleep("The end! I hope you enjoyed my game!")
						win()
					else:
						printandsleep("THE ART COMPANY: This is the worst drawing we have ever seen. It looks like a fourteen year old drew it in just a few hours.")
						printandsleep("THE ART COMPANY: We're not paying you anything for this garbage.")
						printandsleep("During your time spent drawing, your parent's found out that you skipped classes.")
						printandsleep("Needless to say, they are more than displeased.")
						printandsleep("Since you have displeased your parents, you lose.")
						lose()
				elif drawitornah == "no" or drawitornah == "n":
					printandsleep("You pass the art company up on their offer.")
					boredduringgeofunction()
			elif updoots > 50000:
				printandsleep("Wow, great work! Your artwork got over 50,000 upvoteds. That's a ton!")
				printandsleep("For all of your hard effort, you were awarded by a stranger reddit gold, worth $2.50 in real money!")
				printandsleep2("Huzzah!")
				boredduringgeofunction()
			elif updoots > 10000:
				printandsleep("Wow, great work. You drew something that a ton of people liked!")
				boredduringgeofunction()
			elif updoots > 10:
				printandsleep("Your drawing was 'meh' at best. A couple of people upvoted your post.")
				boredduringgeofunction()
			elif updoots > 0:
				printandsleep("Wow. Everyone hated your drawing. Your post has one comment, which tells you never to draw again.")
				boredduringgeofunction()
		elif ipaduse == "put away the ipad" or ipaduse == "put away":
			printandsleep("You decide to be a good boy and focus on your schoolwork. You put away your iPad and begin taking notes on the boring class material.")
		elif ipaduse == "text" or ipaduse == "text your parents":
			printandsleep("You open iMessages and start to text a group chat with your mom and dad.")
			youprintandsleep("Hey guys. I'm having a great day at school. My biology quiz went really well. I'm in math right now. Love you guys!")
			printandsleep("DAD: Focus on your schoolwork.")
			printandsleep("MOM: That's great, honey! See you later today!")
			printandsleep("You close messages, not wanting to bother your parents more.")
			boredduringgeofunction()
		elif ipaduse == "super secret option":
			printandsleep("Congratulations!")
			printandsleep("You have selected the super secret option.")
			printandsleep("The super secret option doesn't do anything.")
			boredduringgeofunction()

def geofunction1():
	if boredduringgeo == "yes" or boredduringgeo == "y":
		if doesshecatchyou == 4:
			printandsleep("While choosing what you want to do, you hear your name from across the room.")
			printandsleep("MS. GAO: Carson, I'm not sure that we need our computers out right now to prove this.")
			youprintandsleep("Oh, okay. I'm sorry!")
			printandsleep("You disgruntledly put away the iPad and begin blankly waiting until class ends.")
		else:
			printandsleep("You zip open your backpack and pull out your iPad.")
			printandsleep("You turn your iPad on and you have a variety of things you can do.")
			printandsleep("You can work on homework, play a video game, draw something, put away the iPad, or text your parents.")
			boredduringgeofunction()
	elif boredduringgeo == "no" or boredduringgeo == "n":
		printandsleep("You begin blankly waiting until class ends.")

doesshecatchyou = random.randint(1, 4)
geofunction1()

printandsleep("After the boring and arduous geometry class ends, it is finally time for break.")
printandsleep("It's your lucky day, because it's cookies for snack!")

printandsleep("Just outside the snack tent, you see some of your friends.")
presnackactivity = inputchecker("Do you want to talk to them or just get snack?", ["talk", "friends", "talk to them", "snack", "get snack", "just get snack"])
if presnackactivity == "talk" or presnackactivity == "talk to them":
	printandsleep("You can either talk to Gillian and Emma, or Charlie and his friends.")
	presnackfriends = inputchecker("Which friends do you want to talk to?", ["gillian", "charlie", "gillian and emma", "emma", "charlie's friends"])
	if presnackfriends == "gillian" or presnackfriends == "gillian and emma" or presnackfriends == "emma":
		printandsleep("You walk up to Gillian and Emma, who are in a deep conversation about one of Gillian's crushes.")
		convowithgillian = inputchecker("Do you want to mess with them or just say hi?", ["mess with them", "mess", "just say hi", "say hi", "hi"])
		if convowithgillian == "mess with them" or convowithgillian == "mess":
			printandsleep("Instead of saying hi to them, you decide to mess with Gillian by taking her phone.")
			printandsleep("GILLIAN: Oh my gawd!!")
			youprintandsleep("Emma, catch!")
			printandsleep("You throw the phone to Emma.")
			doesshecatchit = random.randint(1, 3)
			if doesshecatchit == 1:
				printandsleep("Emma catches the phone and hands it back to Gillian.")
				youprintandsleep("It's cookies for snack, right?")
				printandsleep("GILLIAN: Yes.")
				youprintandsleep("Fantastic.")
				printandsleep("You don't have time to hang out with Gillian and Emma more - you have to make sure that you get one of those cookies!")
			elif doesshecatchit == 2:
				printandsleep("Your throw was horrible and it misses Emma by a longshot.")
				printandsleep("In addition to having horrible aim, you threw the phone way too hard.")
				youprintandsleep("Oh crap.")
				printandsleep("GILLIAN: Bro!!! It's completely shattered!")
				printandsleep("You look at the phone and it really is shattered.")
				youprintandsleep("My bad...")
				printandsleep("Gillian smacks you in the face and you awkwardly leave to go get snack.")
			elif doesshecatchit == 3:
				printandsleep("Emma fumbles the phone, but it ends up falling right into a pile of mud.")
				printandsleep("GILLIAN: Dude!")
				youprintandsleep("My bad, I thought Emma didn't have the reflexes of a one year old!")
				printandsleep("EMMA: That was... a horrible throw.")
				youprintandsleep("No, it wasn't.")
				printandsleep("GILLIAN: Carson, fix it.")
				youprintandsleep("What do you want me to do?? Lick the mud off?")
				printandsleep("GILLIAN AND EMMA: Ew.")
				youprintandsleep("Snack is cookies right?")
				printandsleep("GILLIAN: Yeah.")
				printandsleep("You leave to go get snack.")
		elif convowithgillian == "just say hi" or convowithgillian == "say hi" or convowithgillian == "hi":
			youprintandsleep("Hey guys.")
			printandsleep("EMMA: Yo.")
			youprintandsleep("Gillian are we going to the debate tournament on December 10th?")
			printandsleep("GILLIAN: Yeah, I signed us up for it a few days ago.")
			youprintandsleep("Thanks")
			youprintandsleep("Snack is cookies, right?")
			printandsleep("EMMA: Yeah.")
			printandsleep("You leave to go get snack.")
	elif presnackfriends == "charlie" or presnackfriends == "charlie's friends":
		printandsleep("You walk up to Charlie, Pietro, Nigel, Mich, Menya, Logan, Sawyer, Yash, Ahaan, Surya, and Thomas.")
		printandsleep("They're crowded around Sawyer's phone and they are watching some video on TikTok.")
		printandsleep("You try to break into the circle and look at Sawyer's phone, but people won't budge")
		printandsleep("Pietro breaks out of the circle to talk to you about Call of Duty.")
		printandsleep("PIETRO: Sup, bozo")
		youprintandsleep("Sup, man. COD tonight?")
		printandsleep("PIETRO: Nah... Only on weekends bro.")
		youprintandsleep("Bro.")
		printandsleep("You leave Pietro to go get snack.")
elif presnackactivity == "snack" or presnackactivity == "just get snack" or presnackactivity == "get snack":
	printandsleep("You brush past your friends and walk towards the snack test.")

printandsleep("At the snack tent, Ms. Bartels blankly hands you a snickerdoodle cookie while talking to another person handing out snack.")
printandsleep("You eat the small cookie in one bite and go towards your C period class, acting.")

clear()

printandsleep("On your way to acting class, you see Oliver in the lobby.")
printandsleep("OLIVER: Hey man. I wish we had a free today - I have so much work!")
youprintandsleep("Yeah, I guess. Acting has been fun lately, though.")
printandsleep("OLIVER: No... it hasn't.")
printandsleep("You and Oliver walk into Gross theater, and to your surprise, class has already started.")
printandsleep("ROSS: Come on guys you are always so late.")
wittyresponse = inputchecker("Want to give Ross a witty response?", ["yes", "y", "no", "n"])
if wittyresponse == "yes" or wittyresponse == "y":
	printandsleep("After thinking for a second, you come up with the perfect witty response.")
	youprintandsleep("Well, it's better to arrive late than to arrive unprepared.")
	printandsleep("OLIVER: Yeah, Ross! Where's your pencil, huh?")
	printandsleep("Ross frantacilly searches for a pencil but comes up empty handed.")
	printandsleep("Your response was very effective. What a zinger.")
elif wittyresponse == "no" or wittyresponse == "n":
	youprintandsleep("Yup.")
	printandsleep("OLIVER: Sorry for being late, we were just preparing for the mental anguish of having a class with you.")
	printandsleep("Oliver's response was super effective and completely dismantled Ross.")

printandsleep("You and Oliver make your way up to the stage and sit down.")
printandsleep("MR. POSNER: Helllooo everyone. Today we are going to be reading over this script.")
printandsleep("Mr. Posner hands out a thick script to everyone.")
printandsleep("After you glance at your script, Mr. Posner tells you that you will be playing Bessie, a Jewish matriarch living in the Bronx.")
printandsleep("Your friends begin to read their lines outloud.")
printandsleep("You don't have lines for a few minutes, so you mentally check-out.")
printandsleep("You find yourself drifting away and falling asleep.")

areyouscrewed = 0
fighttheurgetosleep = inputchecker("Do you try to stop yourself?", ["yes", "y", "no", "n"])
if fighttheurgetosleep == "yes" or fighttheurgetosleep == "y":
	printandsleep("You pinch yourself on the neck to try to wake yourself up")
	doyousleep = random.randint(1, 2)
	if doyousleep == 1:
		printandsleep("Your efforts are ineffective and you fall asleep.")
		asleep = True
	else:
		printandsleep("Congratulations. You stop yourself from falling asleep.")
		asleep = False
elif fighttheurgetosleep == "no" or fighttheurgetosleep == "n":
	printandsleep("You give no effort to stop yourself as you fall into a deep slumber.")
	asleep = True

if asleep == True:
	doeshehelp = random.randint(1, 2)
	if doeshehelp == 1:
		printandsleep("Just seconds after you fall asleep, you are shook awake.")
		printandsleep("Your friend, Oliver, noticed you falling asleep and saved you from getting a harsh talking-to, courtesy of your teacher.")
		youprintandsleep("Thanks, bro.")
		printandsleep("After waiting a minute for your turn, you read your line.")
		printandsleep("Your invigorating performance moved your teacher and peers.")
		printandsleep("If Leonardo DiCaprio was in the room with you, he would have given you his Oscar.")
	elif doeshehelp == 2:
		printandsleep("Nobody comes to your aide for a few minutes.")
		printandsleep("When it is time for your lines, Mr. Posner looks to you.")
		doyouwake = random.randint(1, 2)
		if doyouwake == 1:
			printandsleep("He loudly says your name, and jolts you awake.")
			printandsleep("MR. POSNER: Carson. I know you didn't have lines, but you need to stay focused.")
			printandsleep("MR. POSNER: Now, you don't know what happened and what your character is even talking about.")
			printandsleep("MR. POSNER: It's hard to perform when you don't know your characters motivations. Do you understand?")
			youprintandsleep("Yes. I'm really sorry, Mr. Posner. I got no sleep last night.")
			printandsleep("MR. POSNER: Alright. Your line is at the top of page 56.")
			printandsleep("You read the line.")
		elif doyouwake == 2:
			printandsleep("He loudly says your name, but you stay asleep.")
			printandsleep("He walks over to you and claps loudly right infront of you.")
			printandsleep("You finally wake up, and mutter confusedly.")
			youprintandsleep("Oh, I'm sorry. I think I might have fell asleep for a few seconds.")
			youprintandsleep("I got, like, no sleep last night.")
			printandsleep("MR. POSNER: Carson. That isn't acceptable. Acting is an important class which you chose to take.")
			printandsleep("MR. POSNER: We are going to need to have a longer conversation about this.")
			youprintandsleep("I know. I'm so sorry.")
			printandsleep("MR. POSNER: Stay for a bit after class. I'll see if I can get your parents on the call, as well.")
			printandsleep("Everyone is staring at you and Mr. Posner in surprise.")
			printandsleep("OLIVER: He was only asleep for a second!")
			printandsleep("MR. POSNER: Thanks, Oliver, but that doesn't change the reality of the situation.")
			printandsleep("MR. POSNER: Moving on. We are on the top of page 56.")
			printandsleep("You read your line poorly with little emotion.")
			areyouscrewed = 1
elif asleep == False:
	printandsleep("After waiting for a few minutes, it is time for your line.")
	printandsleep("OLIVER with a russian accent: And we have to tell Schlosser!")
	youprintandsleep("No. We must keep Schlosser and the kids in the dark.")
	printandsleep("You did a great job delivering your line.")

printandsleep("After you read your line, you drop your script on the ground.")
youprintandsleep("Oops. I'm sorry.")
printandsleep("You pick up your script and navigate back to page 56.")
printandsleep("You focus on your lines and really end up bringing your character to life.")
printandsleep("At the end of class, everyone piles out of the room.")

if areyouscrewed == 1:
	printandsleep("MR. POSNER: Falling asleep in class is completely inapproprate.")
	youprintandsleep("I know. I'm sorry.")
	printandsleep("I'm going to go to office to find your parent's phone number. Stay here.")
	youprintandsleep("I will.")
	printandsleep("Mr. Posner leaves you alone in the room.")
	doyoudip = inputchecker("Do you leave the room?", ["yes", "y", "no", "n"])
	if doyoudip == "yes" or doyoudip == "y":
		printandsleep("You pick up your stuff and sprint out the side door.")
		printandsleep("A few minutes later, Mr. Posner walks back into the room with your parent's phone number.")
		printandsleep("By now, you're long gone to lunch. You know you're screwed, but your excited to at least have lunch before getting in trouble.")
		areyouscrewed = 2
	elif doyoudip == "no" or doyoudip == "n":
		printandsleep("You stay on stage, waiting for Mr. Posner.")
		printandsleep("A few minutes later, he returns, holding a piece of paper with your mom's phone number.")
		printandsleep("You feel inclined to make your case and save yourself from your parent's wrath.")
		doyoustophimfromcallingyourparents = inputchecker("Do you stop him from calling your parents?", ["yes", "y", "no", "n"])
		if doyoustophimfromcallingyourparents == "yes" or doyoustophimfromcallingyourparents == "y":
			youprintandsleep("Mr. Posner, I was really just asleep for a second. I was super, super tired.")
			youprintandsleep("I've never fell asleep before and I won't do it again.")
			youprintandsleep("Could you please let it slip this one time and not call my parents?")
			printandsleep("MR. POSNER: Carson, I think you understand that this behaviour is unacceptable.")
			printandsleep("MR. POSNER: Alright, I'll let it go this time. But if it happens again, I'm going to need to talk to your grade dean and your parents.")
			youprintandsleep("Thank you so much!")
			printandsleep("Overjoyed, you leave the theater.")
		elif doyoustophimfromcallingyourparents == "no" or doyoustophimfromcallingyourparents == "n":
			printandsleep("Mr. Posner called your parents and told them that you fell asleep.")
			printandsleep("He puts you on the phone.")
			printandsleep2("DAD: Carson?")
			youprintandsleep("Hey, Dad.")
			printandsleep("DAD: This is completely unacceptable. You need to focus in your classes.")
			printandsleep("MOM: Honey, you need to go to sleep earlier.")
			printandsleep("DAD: You think 8 hours a day everyday?")
			youprintandsleep("No.")
			printandsleep("DAD: You think I'm falling asleep in meetings?")
			youprintandsleep("No. I'm sorry.")
			printandsleep("DAD: I'm so disappointed in you. This is rediculous.")
			printandsleep("As you have disappointed your parents, you have lost the game.")
			lose()

clear()

printandsleep("Now, it is D period. Lunch time!")

if helpastranger == 1:
	printandsleep("On the bus this morning, you promised Mary to help her with the python homework this period.")
	printandsleep("You can be a no-show for your appointment, though...")
	helpastranger2 = inputchecker("Do you still want to help her?", ["yes", "y", "no", "n"])
	if helpastranger2 == "yes" or helpastranger2 == "y":
		printandsleep("You walk from the theater to the basement of Tillinghast for your meeting with Mary.")
		doyoufall = random.randint(1, 50)
		if doyoufall == 50:
			printandsleep("There is a banana peel on the stairs going down to the basement.")
			printandsleep("You comically slip on it in an extremely embarassing fashion.")
			printandsleep("Your slip causes you to fall down 8 steps.")
			doyoudie = random.randint(1, 50)
			if doyoudie == 50:
				printandsleep("You sustain major injuries during your fall.")
				printandsleep("You are rushed to the nurses office, then the hospital.")
				printandsleep("Three days later, you are announced dead from your injuries.")
				printandsleep("That's what you get for trying to help someone with their homework.")
				printandsleep("You lose.")
				lose()
			else:
				printandsleep("Unfortunately, your crush was standing nearby and saw you slip.")
				printandsleep("Instead of helping you, your crush laughed in your face.")
				printandsleep("Nice job.")
				printandsleep("You pick yourself up and walk to your python classroom, where Mary is anxiously waiting for you.")
		else:
			printandsleep("On the stairs going down to the basement, you narrowly avoid slipping on a banana peel.")
			printandsleep("You walk down the stairs and go to your classroom, where Mary is anxiously waiting for you.")
		youprintandsleep("Hey, Mary!")
		printandsleep2("MARY: Hey, Carson. Thanks so much for helping me with the homework!")
		youprintandsleep("Of course!")
		printandsleep("MARY: Alright, so, I mainly had problems with question one, what was your answer to it?")
		printandsleep("You recall that you lied to Mary; you haven't actually done the homework.")
		youprintandsleep("Umm, I don't remember which one that was, can I see it on your computer?")
		printandsleep("Mary pulls out her computer and opens the problem.")
		printandsleep("The probem reads:")
		printandsleep("Mike has x bananas. Joe has y bananas. Write a program in python which asks the users for how many bananas Joe and Mike have, then tells the user the total numbers of bananas.")
		time.sleep(timetosleep)
		printandsleep("You think about the problem for a bit and realize that it should be super easy.")
		youprintandsleep("Okay. This shouldn't be too hard.")
		youprintandsleep("So first, you need to create variables x and y, so just x = and y =.")
		printandsleep("MARY: Okay, that makes sense.")
		youprintandsleep("Now, you need to get input from the user for the value of those variables.")
		youprintandsleep("So it should be x = input('How many bananas does Mike have') and y = input('How many bananas does Joe have?')")
		printandsleep("MARY: Alright, I understand this.")
		printandsleep("MARY: So now I should just do x + y, right? But it doesn't work!")
		youprintandsleep("Well, right now it's just calculating x + y. It should be print (x + y).")
		printandsleep("MARY: Okay. I'll try that.")
		printandsleep("Mary types everything into her computer and tries it out. An error message pops up.")
		printandsleep("MARY: It still doesn't work!")
		youprintandsleep("Oh, I know the reason! Right now, it is taking the value of x as 'four' or '4' instead of the number 4. It can't add words!")
		printandsleep("MARY: Okay, how can I fix it?")
		youprintandsleep("Just do print(int(x) + int(y))!")
		printandsleep("Mary tries this solution out, and it works!")
		printandsleep("MARY: Oh, great, thanks Carson!")
		youprintandsleep("You're welcome! Did you have any other questions?")
		printandsleep("MARY: No, that's all! Thank you so much!")
		printandsleep("You wave Mary goodbye and head towards the cafeteria for lunch.")
	elif helpastranger2 == "no" or helpastranger2 == "n":
		printandsleep("You decide not to go to your appointment with Mary.")
		printandsleep("She probably forgot about it, anyways.")
		printandsleep("You start heading to the cafeteria for lunch.")
		printandsleep("Mary sits in the python classroom, crying as you did not show up and now she will certainly fail the class.")
else:
	printandsleep("You head towards the cafeteria for lunch.")

printandsleep("You run down the stairs and into the cafeteria for lunch.")
printandsleep("All the delicious food looks enticing, however you know that you need to keep your weight down for wrestling.")

whatdyoueat = 1
foodfunction()
 #remember to make this count for wrestling!

def foodfunction():
	printandsleep("You can get hot food, vegetables, a salad, a sandwich, breakfast food, or desert.")
	whatyoueating = inputchecker("What do you want to eat?", ["hot food", "vegetables", "salad", "sandwich", "breakfast food", "desert"])
	if whatyoueating == "hot food":
		printandsleep("Today, there are lots of choices for hot food.")
		printandsleep("You can get a burger, pizza, chicken, a pretzel, rice, or a quesadilla.")
		printandsleep("If you decide you no longer want hot food, just say you want something else!")
		whatyoueatinghotfood = inputchecker("What do you want to eat?", ["pretzel", "rice", "quesadilla", "pizza", "burger", "chicken", "something else"])
		if whatyoueatinghotfood == "pretzel":
			printandsleep("You walk up to the station and grab a pretzel. It looks perfect and has just the right amount of salt.")
			printandsleep("Remembering how caloric and unhealthy pretzels are, you decide not to get any other food.")
		elif whatyoueatinghotfood == "rice":
			printandsleep("You walk around the pretzels and the burgers and ask for rice.")
			printandsleep("You get a heaping mountain of plain rice on your plate. Delicious, but bland.")
			printandsleep("You put some unkown sauce on the rice, and since you have so much, you decide not to get any other food.")
		elif whatyoueatinghotfood == "pizza":
			printandsleep("You dash to the pizza line as it's increasing by the second.")
			printandsleep("Right before it's your turn to get pizza, they run out.")
			printandsleep("You wait for what feels like forever before they restock the pizza.")
			if areyouscrewed == 2:
				printandsleep("While waiting, Mr. Posner spots you.")
				printandsleep("He forcefully tells you to come with him and takes you to the front office.")
				printandsleep("There await your grade dean, who is talking to your parents on the phone.")
				printandsleep("After a lengthy conversation, you are sent home for the day.")
				printandsleep("Your parents are more than displeased.")
				printandsleep("You lose.")
				lose()
			else:
				time.sleep(2)
				printandsleep("Finally, someone comes out holding the pizza.")
				howmanyslices == inputchecker("How many slices do you want? You can have up to three." ["1", "2", "3"])
				if howmanyslices == "1":
					printandsleep("You take one slice of pizza.")
				elif howmanyslices == "2":
					printandsleep("You take two slices of pizza.")
				elif howmanyslices == "3":
					printandsleep("You take three slices of pizza.")



#new stuff below

wherewechomping = inputchecker("Where do you want to eat?", )

#feedback from Elise: Make an option for users to change timetosleep (done), fix typos (done)