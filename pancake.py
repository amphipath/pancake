def flip(s,k,p)
    if len(s) < k+p:
        return none
    else:
        var a = list(s)
        for i in range(p,p+k-1):
            if a[i] = '+':
                a[i] = '-'
            elif a[i] = '-':
                a[i] = '+'
            else:
            return none
        var b = ''
        for i in range(0,len(s)-1):
            b = b + a[i]
        return b

flip('+--++',3,2)