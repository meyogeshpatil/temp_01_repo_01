def fact(n):
    return 1 if n==1 else n*fact(n-1)
    


def mod_name(func):
    def inner(a):
    if a=='Yogesh':
        print('Hello Yoegsh Greetings of the day!!')
    else:
        return func(a)
       
    return inner



@mod_name
def name(a):
    print(f'Hello {a}')