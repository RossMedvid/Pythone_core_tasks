# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# def arifmetic_mean(*args):
#     """This function calculate arifmetic mean of a non-empty arbitrary numbers"""
#     return(sum(args))/len(args)
# print(arifmetic_mean(1,3,6))

# 2.  Написати функцію, яка повертає абсолютне значення числа
# def return_absolute_number(a):
#     """This function returns absolute mean of numbers"""
#     if a>0:
#         print(a)
#     else:
#         return (a*-1)
# print(return_absolute_number(-54))

# 3.3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
# def max_numbers(a,b):
#     """This function returns maximum in output between two numbers"""
#     if a>b:
#         print(a)
#     else:
#         return b
# print(max_numbers(5,9))


#44.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
# def rectangel(a,b):
# """This function calculate area of rectangel"""
#     s_rectangel=a*b
#     return s_rectangel

# def triangle(a,b,c):
# """This function calculate area of triangle"""
#     p=(a+b+c)/2
#     return ((p*(p-a)*(p-b)*(p-c))** 0.5)

# def circle(r):
# """This function calculate area of circle"""
#     return(3.14*(r**2))

# area=input("Please enter what area of figure you want to count:")
# if area=="rectangel":
#     a=int(input("Enter the lenght of the first side:"))
#     b=int(input("Enter the lenght of another side:"))
#     print(rectangel(a,b))
# elif area=="triangle":
#     a=int(input("Enter the lenght of the side a:"))
#     b=int(input("Enter the lenght of the side b:"))
#     c=int(input('Enter the lenght of the side c:'))
#     print(triangle(a,b,c))
# elif area=="circle":
#     r=int(input("Please enter the radius of circle:"))
#     print(circle(r))
# else:
#     print("EROR: You are entering inncorect value, please try again")
#     area=input("Please enter what area of figure you want to count:")

# 55.  Написати функцію, яка обчислює суму цифр введеного числа.
# def list_of_numbers(*kwargs):
#     """This function calculates the sum of entered numbers"""
#     a=0
#     for i in kwargs:
#         a=i+a
#     return a
# print(list_of_numbers(431,5213,2321))


# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, 
# після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def sum_of_numbers(a,b):
    """This function calculates sum of entered numbers"""
    a=a+b
    return a

def multiplication_(a,b):
    """This function calculates multiplication of entered numbers"""
    a=a*b
    return a

def subtraction_(a,b):
    """This function calculates subtraction between two values"""
    a=a-b
    return a

def division_(a,b):
    """This function calculates division between two values"""
    a=a/b
    return a


# Calculator
h=input("Hello, please type start for the next step, or exit for the end:")
if h=="start":
    a=int(input("Please choose your first number:"))
    s=input("Please choose the operation between +, *, -, / :")
    b=int(input("Please choose your second number:"))
    while True:
        if s=="+" or s=="*" or s=="-"or s=="/":
            while True:
                if s=="+":
                    print(sum_of_numbers(a,b))
                    s=input("If you want exit out of this program tape EXIT or choose another operation:")
                    if s=="exit":
                        break
                    if s=="+" or s=="*" or s=="-" or s=="/":
                        a=int(input("Please choose your first number:"))
                        b=int(input("Please choose your second number:"))
                        continue
                    else:
                        break
                if s=="*":
                    print(multiplication_(a,b))
                    s=input("If you want exit out of this program tape EXIT or choose another operation:")
                    if s=="exit":
                        break
                    if s=="+" or s=="*" or s=="-" or s=="/":
                        a=int(input("Please choose your first number:"))
                        b=int(input("Please choose your second number:"))
                        continue
                    else:
                        break
                if s=="-":
                    print(subtraction_(a,b))
                    s=input("If you want exit out of this program tape EXIT or choose another operation:")
                    if s=="exit":
                        break
                    if s=="+" or s=="*" or s=="-" or s=="/":
                        a=int(input("Please choose your first number:"))
                        b=int(input("Please choose your second number:"))
                        continue
                    else:
                        break
                if s=="/":
                    while True:
                        if a>0 and b>0:
                            print(division_(a,b))
                            s=input("If you want exit out of this program tape EXIT or choose another operation:")
                            if s=="/":
                                a=int(input("Please choose your first number:"))
                                b=int(input("Please choose your second number:"))
                                continue
                            if s=="exit":
                                break
                            if s=="+" or s=="*" or s=="-":
                                a=int(input("Please choose your first number:"))
                                b=int(input("Please choose your second number:"))
                                break
                            else:
                                break
                        if a==0 or b==0:
                            print("EROR:Please type your values without 0 if you want do divison operation:")
                            a=int(input("Please choose your first number:"))
                            b=int(input("Please choose your second number:"))
                            continue
                        else:
                            break
                else:
                    break
        if s=="exit":
                print("Thank you that you choose our software. Have a nice day.")
                break
        else:
            print("Something gone wrong please try again.")
            break
else:
    print("Thank you that you choose our software. Have a nice day.")

