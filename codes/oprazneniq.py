word=input()
while word!='End':
    if word!= "SoftUni":
        new_word=''
        for ok  in word:
            new_word+=ok*2
        print(new_word)
    word=input()