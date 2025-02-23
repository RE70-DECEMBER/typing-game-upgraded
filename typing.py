import random
path = input("pick a wordlist (words.txt) --> ")
path = open(f"{path}", "r")

words_correct = 0
words_incorrect = 0


words_found = path.readlines()


while True:
    words = (random.choice(words_found)).strip()
    print(words)
    typing = input("typing --> ")
    if typing == words:
        print("correct")
        words_correct += 1
    elif typing == "q":
        print(f"words correct: {words_correct}\nincorrect words: {words_incorrect}")
        exit()
    else:
        print(f"incorrect {words}")
        words_incorrect += 1
