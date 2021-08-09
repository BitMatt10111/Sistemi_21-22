'''
Name: Matteo Lamberti
Data: 28/07/21

Talk to Bob
Bob answers 'Sure.' if you ask him a question, such as "How are you?".
He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.
'''

def main():
    s=input("Tell something to Bob: ")
    all_caps=True
    if s != "":
        for letter in s:
            if ord(letter)>=97:
                all_caps=False
        if all_caps==True:
            if s[-1] != '?':
                print("Whoa, chill out!")
            else:
                print("Calm down, I know what I'm doing!")
        elif s == "How are you?":
            print("Sure")
        else:
            print("Whatever.")
    else:
        print("Fine. Be that way!")

if "__main__"==__name__:
    main()