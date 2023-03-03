# Imagine that you and a number (M) of friends go to a luxury restaurant, and when you
# ask for the bill, you want to split the total amount and the tip (15 percent) between all.
# Your program should print the amount of the bill, the tip, the total cost, and the amount
# each person has to pay. It should also print how much of what each person pays is for
# the bill and for the tip. Try to execute the follow code and understand as it work. Use
# the debug during the analysis. [R1.20]


NUMBER_OF_FRIENDS = int(input('Please count your friends: '))
total_people = NUMBER_OF_FRIENDS + 1
BILL = float(input('Please enter the amount of your bill: '))
TIP = BILL * 15 / 100
total_cost = BILL + TIP
each_persons_bill = BILL / total_people
each_persons_tip = TIP / total_people
total_for_each_person = each_persons_bill + each_persons_tip
print(
    f'Bill = {BILL} \n'
    f'Tip = {TIP} \n'
    f'Total cost = {total_cost} \n'
    f'Total amount each person hsa to pay = {total_for_each_person} \n'
    f'The amount each person hsa to pay for the bill = {each_persons_bill} \n'
    f'The amount each person hsa to pay for the tip = {each_persons_tip} \n'

)
