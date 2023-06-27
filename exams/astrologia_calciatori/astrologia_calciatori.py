def zodiac_month():
    with open('zodiaco.csv', 'r') as zo:
        months = zo.read()
        months = months.split('\n')
        # print(months)
        m = {}
        for z in months:
            # print(z)
            z = z.split(',')
            # print(z)
            if len(z) > 1:
                start_date = z[1].split('/')
                start_date = start_date[1] + start_date[0]

                end_date = z[2].split('/')
                end_date = end_date[1] + end_date[0]

                my_months = {z[0]: {'start': start_date, 'end': end_date, 'goal': 0}}
            m.update(my_months)
    return m


def zodiac_specifiere(string):
    our_formating_birthday_sign = None
    # print(f'string = {string}')
    date = string.split('/')
    # print(date)
    our_formating_birthday = date[1] + date[0]
    # print(our_formating_birthday)

    z_months = zodiac_month()
    # print(z_months)
    for key, value in z_months.items():
        # print(f'{key} = {value}')
        if int(value['start']) <= int(our_formating_birthday) <= int(value['end']):
            # print(f'{our_formating_birthday} = {key}')
            our_formating_birthday_sign = key
        if our_formating_birthday_sign == None:
            our_formating_birthday_sign = 'Capricorn'

    return our_formating_birthday_sign


def main():
    with open('sportivi.csv', 'r') as blabla:
        my_file = blabla.read()
        # print(my_file)
        my_file = my_file.split('\n')
        # print(my_file)
        z_m = zodiac_month()
        print(z_m)
        for i in my_file:
            # print(i)
            i = i.split(',')
            # print(i)
            if len(i) > 1:
                player = {'name': i[0], 'goal': i[1], 'country': i[2], 'birthday': i[3]}
                # print(player)

                birthday = player['birthday']
                goal = int(player['goal'])
                # print(birthday)

                zodiac_sign = zodiac_specifiere(birthday)
                # print(zodiac_sign)
                g_sum = z_m[zodiac_sign]['goal'] + goal

                z_m[zodiac_sign].update({'goal': g_sum})
                # print(z_m)
                # print('......................................................................................................')
        print(z_m)
        sorted_data = sorted(z_m.items(), key=lambda x: x[1]['goal'], reverse=True)
        print(sorted_data)

        max_goals = sorted_data[0][1]['goal']
        scale = 50 / max_goals

        for sign, info in sorted_data:
            # print(f'sign = {sign}, info ={info}')
            total_goals = info['goal']
            bar_length = int(total_goals * scale)
            histogram_bar = '*' * bar_length
            print(f"{sign}:  {' ' * (11 - len(sign))}({total_goals}) {histogram_bar}")
