# You want to find out which fraction of your car’s use is for going to work, and which
# is for personal use. You know the one-way distance from your home to work. For a
# particular period, you recorded the beginning and ending kilometers on the odometer
# and the number of working days. Try to execute the follow code able of computing the
# fraction of car’s use for work and personal. Use the debug during the analysis. [R1.16]
HOME_TO_WORK_DISTANCE = int(input('Enter the distance between your home and work:'))
BEGINNING_KILOMETER = int(input('Enter the beginning of your odometer:'))
ENDING_KILOMETER = int(input('Enter the end of your odometer:'))
WORKING_DAYS = int(input('Enter the working days:'))

total = ENDING_KILOMETER - BEGINNING_KILOMETER
total_home_to_work = WORKING_DAYS * (HOME_TO_WORK_DISTANCE * 2)
total_other = total - total_home_to_work

total_home_to_work = 100 * (total_home_to_work / total)
total_other = 100 * (total_other / total)

print(f'car use for personal:{total_other}%\n \
car use for work:{total_home_to_work}%')
