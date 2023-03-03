number = input('enter your number:')

sum = 0
if number.find('.'):
    number = number.replace('.', '')

# my way
for i in number:
    sum += int(i)

print(f'{sum=} with my way')

# second way
sum = 0
while int(number) > 0:
    digit = int(number) % 10
    sum += digit
    number = int(number) // 10
print(f'{sum=} with second way')
