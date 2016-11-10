#add
def add(num1,num2):
    if isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        print 'you have input two int or float number:'
    elif isinstance(num1,(str)) and isinstance(num2,(str)):
        print 'you have input two strings:'
    else:
        print 'input error,please try again'
    return num1 + num2

def abs(num1):
    if isinstance(num1,(int,float)):
        if num1>0:
            return num1
        else:
            return -num1
    else:
        print 'input error'

def pas():
    pass

#n*n
def square(num1,num2=2):
    sum = 1
    while num2 > 0:
        sum = num1 *sum
        num2 = num2-1
    return sum

