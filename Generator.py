#!/usr/bin/python3
#coding=utf-8

print('Welcome to the Spanish Random Word Generator. \n This Generator is based on a frequency dictionary of Spanish written by Mark Davies. \n It is designed to help you study the 500 most frequent words in the Spanish language. \n Press x to receive a new word. \n Press y to define a word. \n \n ') 

def main(): 

	import random 
	from Spanish500FreqWords import Spanish_500Freq_Words
	key = random.choice(list(Spanish_500Freq_Words))
	print(Spanish_500Freq_Words[key])
	answer=input('')
	if answer=="y": 
		print(key)
		signal=input('').lower()
		if signal=="x": 
			main()
		else:
			exit()
	elif answer=="x": 
		main()
	else:
		signal2=input("Type x for another word. Type anything else to exit this program." ).lower()
		if signal2=="x": 
			main()
		else: 
			exit()
main()