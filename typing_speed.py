import time
import random
import sqlite3
from colorama import init,Fore, Back, Style
init()

total_words=10
def random_words():
	temp='shiver,monk,platform,seller,casualty,employ,crown,coat,cinema,level,civilization,lamb,policeman,meeting,rest,football,traffic,food,unfair,stimulation,audience,banquet,lion,soprano,pick,missile,hospital,sound,result,soil,galaxy,brave,far,tray,unlike,expenditure,church,gravel,honor,slide,endorse,default,silver,genuine,frank,equation,weight,orange,acquisition,concrete'
	words=temp.split(',')
	global main_string
	global main_list
	main_list=[]
	main_string=''
	main_list = random.sample(words, total_words)
	main_string=main_string+" ".join(main_list)
	return main_string

def test(main_string):
	global count,t_start,t_end
	try:
		print(Fore.RED + main_string)
		print(Fore.BLUE)
		t_start = time.time() #start time
		inputText = input()
		t_end = time.time() #stop time
		print(Style.RESET_ALL)
		input_list=inputText.split()
		main_enum=list(enumerate(main_list))
		input_enum=list(enumerate(input_list))
		count=0
		for i,c in main_enum:
			if c==input_list[i]:
				count+=1
	except:
		print('Enter whole sentence')
		exit()
def calculation():
	diff=t_end-t_start
	acc=count/total_words*100
	timeTaken = t_end - t_start
	wpm=(count*60)//diff
	return acc,wpm

def database(name,wpm,acc):
	conn=sqlite3.connect('game.db')
	print("Opened Database successfully")

	cursor = conn.cursor()
	#cursor.execute('DROP TABLE TYPING')
	cursor.execute('CREATE TABLE IF NOT EXISTS TYPING(NAME TEXT UNIQUE NOT NULL,WPM INT NOT NULL,ACC INT NOT NULL);')
	print('Table created successfully')

	cursor.execute('INSERT OR REPLACE INTO TYPING(NAME,WPM,ACC) VALUES(?,?,?)',(name,wpm,acc))
	conn.commit()
def display():
	conn=sqlite3.connect('game.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM TYPING ORDER BY WPM DESC')
	rows=cursor.fetchall()
	print('Typing Scores')
	print('=============')
	for row in rows:
		if row[2]>85:
			print(str(row[1])+" WPM - "+str(row[0]))
	conn.commit()

print("ABC's Typing Speed Game")
print("=======================")
print("\nTyping the following sentence and then hit enter:\n")
main_string=random_words()
test(main_string)
acc,wpm=calculation()
print(Fore.GREEN+"Accuracy: ",acc)
print(Fore.GREEN+"Typing Speed: ",wpm,"wpm")
print(Style.RESET_ALL)
save=input('Do you want to save this score(y or n)?: ')
if save=='y':
	name=input('Enter name:')
	database(name,wpm,acc)
leaderboard=input('Would you like to see the leaderboard (y or n)?: ')
if leaderboard=='y':
	display()

