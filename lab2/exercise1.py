def main():
    c = True
    while c is True:
        data = int(input('please enter a number with 5 digits(enter 0 to exit):'))
        if 10000 < data < 99999:
            for i in str(data):
                print(i)
        else:
            print('you entered the wrong amount of digits')
        c = data



main()
