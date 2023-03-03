num1 = 8
num2 = 1
num3 = 35
num4 = 20

my_min = 0
my_max = 0
first = 0
second = 0

if num1 < num2 and num1 < num3 and num1 < num4:
    my_min = num1
elif num2 < num1 and num2 < num3 and num2 < num4:
    my_min = num2
elif num3 < num1 and num3 < num2 and num3 < num4:
    my_min = num3
elif num4 < num1 and num4 < num3 and num4 < num2:
    my_min = num4

if num1 > num2 and num1 > num3 and num1 > num4:
    my_max = num1
elif num2 > num1 and num2 > num3 and num2 > num4:
    my_max = num2
elif num3 > num1 and num3 > num2 and num3 > num4:
    my_max = num3
elif num4 > num1 and num4 > num3 and num4 > num2:
    my_max = num4

if num1 == my_min and num2 == my_max:
    if num3 < num4:
        first = num3
        second = num4
    else:
        first = num4
        second = num3

elif num1 == my_min and num3 == my_max:
    if num2 < num4:
        first = num2
        second = num4
    else:
        first = num4
        second = num2
elif num1 == my_min and num4 == my_max:
    if num2 < num3:
        first = num2
        second = num3
    else:
        first = num3
        second = num2

if num2 == my_min and num1 == my_max:
    if num3 < num4:
        first = num3
        second = num4
    else:
        first = num4
        second = num3

elif num2 == my_min and num3 == my_max:
    if num1 < num4:
        first = num1
        second = num4
    else:
        first = num4
        second = num1
elif num2 == my_min and num4 == my_max:
    if num1 < num3:
        first = num1
        second = num3
    else:
        first = num3
        second = num1

if num3 == my_min and num1 == my_max:
    if num2 < num4:
        first = num2
        second = num4
    else:
        first = num4
        second = num2

elif num3 == my_min and num2 == my_max:
    if num1 < num4:
        first = num1
        second = num4
    else:
        first = num4
        second = num1
elif num3 == my_min and num4 == my_max:
    if num1 < num2:
        first = num1
        second = num2
    else:
        first = num2
        second = num1

if num4 == my_min and num1 == my_max:
    if num2 < num3:
        first = num2
        second = num3
    else:
        first = num3
        second = num2

elif num4 == my_min and num2 == my_max:
    if num1 < num3:
        first = num1
        second = num3
    else:
        first = num3
        second = num1
elif num4 == my_min and num3 == my_max:
    if num1 < num2:
        first = num1
        second = num2
    else:
        first = num2
        second = num1

print(my_min)
print(first)
print(second)
print(my_max)

# better way :
#
#
# my_list = [num1, num2, num3, num4]
# my_list = sorted(my_list)
# for i in my_list:
#     print(i)
