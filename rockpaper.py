while(True):
    n = input("choose-")
    list_1= ['rock','paper','scissor']
    a = 'you loose'
    b = 'you win'
    import random
    l = random.choice(list_1)
    print(f"computer choose-{l}")
    if n=='rock' and l=='paper':
        print(a)
    elif n=='paper' and l=='scissor':
        print(a)
    elif n=='scissor' and l == 'rock':
        print(a)
    elif n==l:
        print("Tie")
    else:
        print(b)
    x = input("Do you wanna play again yes/no = ")
    if (x == 'yes'):
        continue
    else:
        break