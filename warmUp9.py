#Caleb Callaway
#3/1/18
#warmUp9.py- printing text with vowels capitalized

text = input ("Enter some text: ")


for ch in text:
    if ch == ("i") or ch == ("a") or ch == ("e") or ch == ("o") or ch == ("u"):
        print (ch.upper())
    else:
        print (ch)