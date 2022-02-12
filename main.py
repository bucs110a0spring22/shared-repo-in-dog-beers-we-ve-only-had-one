# empty list
my_list=[]
i = 0
x = int(input("input a number "))
z = int(input("input another number "))
y = int(input("input another number "))
w = int(input("input another number "))
my_list.append(x)
my_list.append(z)
my_list.append(y)
my_list.append(w)
print(my_list)
for i in my_list:
  print(i)

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)