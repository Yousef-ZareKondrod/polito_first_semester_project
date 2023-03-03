# Write a program that prints the balance of an account after the first, second, and third
# year. The account has an initial balance of $1,000 and earns 5 percent interest per year.

balance = 1000
YEARLY_INTEREST = 0.05

for i in range(1, 4):
    balance = balance + (balance * YEARLY_INTEREST)
    print(f'your {i} year balance is : {balance}')
