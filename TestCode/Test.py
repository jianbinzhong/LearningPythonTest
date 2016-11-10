def power(x,n):
    #对输入做判断
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        print 'input type error'
    s = 1
    while n>0:
        s=s*x
        n = n-1
    return s
