#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств.


n=(int(input("Введите количество элементов первого множества: ")))
list_1=[]
for i in range(n):
    num = int(input("Введите число "))
    list_1.append(num)
print(list_1)


m=(int(input("Введите количество элементов второго множества: ")))
list_2 = []
for i in range(m):
    num = int(input("Введите число "))
    list_2.append(num)
print(list_2)


list3 = list_1 + list_2

checked_nums_list = []
for i in list3:
    if list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print(i)