def histogram():
    user_input = input()
    values = [int(x) for x in user_input.split()]

    for value in values:
        line = ''
        for i in range(value):
            line += '*'  
        print(line)  

histogram()
