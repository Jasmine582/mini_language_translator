#Create a few words to translate
translator = {
    "hello" : "bonjour",
    "thank you": "merci",
    "sorry": "desole",
    "love" : "amour",
    "friend": "amie (feminine)  ami (masculine)",
    "food": "aliments",
    "good bye":"au revoir"
}

done = False
print(' Type "done" at any time to exit ')

while not done:
    word = input("Type an English word for translation: ")
    word = word.lower()
    if word == "done":
        done = True
    elif word in translator:
        print(translator[word])
    else:
        print("This word is not in the translator")
