def calculation(num,numm):
    operations = ['-','*','/','+']
    for x in operations:
        print(x)

    ask = input("Whats operation you want to do::")
    result = 0
    if ask == '-':
        result =  num - numm
        print (result)
    elif ask == '+':
        result = num + numm
    elif ask == '*':
        result = num * numm
    elif ask == '/':
        result = int(num / numm)
    else:
        print('Please enter correct operation.')
    
    return result


def futher_calc():
    other_num = int(input("Enter other number::"))
    new_result = calculation(glob_var,other_num)
    return new_result

num1 = int(input("What's the First number::"))
num2 = int(input("What's the Second number::"))
# calculation(num1,num2)
the_result = calculation(num1,num2)
glob_var = the_result
print(f'The result is {the_result}.')


repeat = True
while repeat == True:
    con = input("Do you want to continue further operations? 'y' or 'n' ::")
    if con == 'y':
        your_result = futher_calc()
        print(f'The result is {your_result}')
        glob_var = your_result
    else:
        repeat = False

    

    


