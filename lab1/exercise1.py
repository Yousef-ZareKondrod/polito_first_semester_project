# The proposed program stores two integers as two constants defined inside the code,
# and then display:
# i. Their sum
# ii. Their difference
# iii. Their product
# iv. Their average value
# v. Their distance (i.e. the absolute value of the difference)
# vi. The maximum value (i.e. the greater of the two)
# vii. The minimum value (i.e. the lesser of the two)


FISRTNUMBER = int(input('ENTER THE FIRST NUMBER(INTEGER):'))
SECONDNUMBER = int(input('ENTER THE SECOND NUMBER(INTEGER):'))


def mysum(firstnum, secondnum): return firstnum + secondnum


def mydifference(firstnum, secondnum): return firstnum - secondnum


def myproduct(firstnum, secondnum): return firstnum * secondnum


def myaverage(firstnum, secondnum): return (firstnum + secondnum) / 2


def mydiatance(firstnum, secondnum): return abs(mydifference(firstnum, secondnum))


def mymax(firstnum, secondnum): return max(firstnum, secondnum)


def mymin(firstnum, secondnum): return min(firstnum, secondnum)


print(f'sum = {mysum(FISRTNUMBER, SECONDNUMBER)} \n \
difference = {mydifference(FISRTNUMBER, SECONDNUMBER)} \n \
product = {myproduct(FISRTNUMBER, SECONDNUMBER)} \n \
average = {myaverage(FISRTNUMBER, SECONDNUMBER)} \n \
distance = {mydiatance(FISRTNUMBER, SECONDNUMBER)} \n \
max = {mymax(FISRTNUMBER, SECONDNUMBER)} \n \
min = {mymin(FISRTNUMBER, SECONDNUMBER)}')
