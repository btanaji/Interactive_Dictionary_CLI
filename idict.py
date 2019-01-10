import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
	w=w.lower()
	if word in data:
		return data[w]
	elif len(get_close_matches(word,data.keys()))>0:
		yn=input("Did you mean %s instead? press 'y' if YES, press 'n' if NO: " %get_close_matches(word,data.keys())[0])
		if yn=="y":
			return data[get_close_matches(word,data.keys())[0]]
		elif yn=='n':
			return "word doesn't exist, please re-check it."
				
		else:
			return "sorry, we didn't understand your entry"
			
	else:
		return "word doesn't exist, please re-check it."
word=input("enter the word: ")
output=translate(word)

if type(output)==list:
	for i in output:
		print(i)
else:
	print(output)

