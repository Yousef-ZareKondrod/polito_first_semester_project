# Algorithm:
# ▪ Declare and initialize a ‘total’ variable to 0
# ▪ Declare and initialize a ‘count’ variable to 0
# ▪ Declare and initialize a ‘salary’ variable to 0
# ▪ Prompt user with instructions
# ▪ Loop until sentinel value is entered
#   o Save entered value to input variable (‘salary’)
#   o If salary is not -1 or less (sentinel value)
#       • Add salary variable to total variable
#       • Add 1 to count variable
# ▪ Make sure you have at least one entry before you divide!
#   o Divide total by count and output.
#   o Done!


total = 0
count = 0
salary = 0
while salary >= 0.0:
    salary = float(input('enter your salary or -1 to finish:'))
    if salary >= 0.0:
        total += salary
        count += 1
if count > 0:
    average = total / count
    print(f'{average=}')

else:
    print('no data avalible')
