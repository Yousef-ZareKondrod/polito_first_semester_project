# The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a
# given month and day.
# If month is 1, 2, or 3, season = "Winter"
# Else if month is 4, 5, or 6, season = "Spring"
# Else if month is 7, 8, or 9, season = "Summer"
# Else if month is 10, 11, or 12, season = "Fall"
#   If month is divisible by 3 and day >= 21
#   If season is "Winter", season = "Spring"
#   Else if season is "Spring", season = "Summer"
#   Else if season is "Summer", season = "Fall"
#   Else season = "Winter"
# Draw a flowchart for the algorithm. Please verity if the algorithm behaves correctly
# using series of test inputs [R3.13]


month = int(input())
day = int(input())

if month in [1, 2, 3]:
    season = 'winter'
elif month in [4, 5, 6]:
    season = 'spring'
elif month in [7, 8, 9]:
    season = 'summer'
elif month in [10, 11, 12]:
    season = 'fall'
if month % 3 == 0 and day >= 21:
    if season == 'winter':
        season = 'spring'
    elif season == 'spring':
        season = 'summer'
    elif season == 'summer':
        season = 'fall'
    else:
        season = 'winter'

print(season)
