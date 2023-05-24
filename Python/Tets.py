while True:
    print("What is your name?")
    name = input()

    print("What is your age?")
    age = input()

    print("So you are:", name, "and your age is:", age)
    print("Is that correct?(y/n)")
    answer_1 = input()

    if answer_1.lower() == "y":
        print("Welcome", name)
        break
    else:
        print("Please introduce your corrected Name and Age")


#This is coment for testing
        