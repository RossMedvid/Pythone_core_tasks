#.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# a=[]
# b=int(input('Введіть скільки чисел ви хочите ввести:'))
# for i in range(b):
#     a.append(int(input("Please enter the element: ")))
# max = a[0]
# min = a[0]
# for i in range(b):
#    if a[i] > max:
#        max = a[i]
#    if a[i] < min:
#        min = a[i]
# print("Maximum number = {}. Minimum number = {}.".format(max,min))



# a=[int(input("Enter int {}:".format(max,min)))]

#2.  В інтервалі від 1 до 10 визначити числа 
#•  парні, які діляться на 2,
#•  непарні, які діляться на 3, 
#•  числа, які не діляться на 2 та 3.

#for i in range(1,11):
#if i%2==0:
#        print("Парні:", i,end='\n')
#    elif i%3==0:
#       print('Непарні:', i,end='\n')
#    else:
#        print('Не ділиться на 2 та 3:', i,end='\n')


#3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

# n=int(input("Введіть число для обчислення факторіалу:"))
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)


#44.  Напишіть скрипт, який перевіряє логін, який вводить користувач. Якщо логін вірний (First), то привітайте користувача. Якщо ні, то виведіть повідомлення про помилку. (використайте цикл while)

# LOGIN=input("Please enter your login:")
# i=0
# while True:
#     if LOGIN=='First':
#         print("Welcome back First")
#         break
#     else:
#         LOGIN=input('EROR: Please enter your login again:')


