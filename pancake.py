def flip(s,k,p):
    if len(s) < k+p:
        return none
    else:
        a = list(s)
        for i in range(p,p+k):
            if a[i] == '+':
                a[i] = '-'
            elif a[i] == '-':
                a[i] = '+'
            else:
                return none
        b = ''
        for i in range(0,len(s)):
            b = b + a[i]
        return b

def possible(s,k):
    count = 0
    c = 0
    for i in range(0,len(s)-k+1):
        a = list(s)
        if a[i] == '-':
            s = flip(s,k,i)
            count += 1
    b = list(s)
    for i in range(len(s)-k+1,len(s)):
        if b[i] == '-':
            c = 1
    if c == 1:
        return 'IMPOSSIBLE'
    if c == 0:
        return count

def process(file,output):
    f = open(file)
    target = open(output,'w')
    content = f.readlines()
    for i in range(1,int(float(content[0]))+1):
        c = content[i].split(' ')
        target.write('Case #{0}: {1} \n'.format(i,possible(c[0],int(float(c[1].strip('\n'))))))

process('A-large-practice.txt','resultlarge.txt')
process('A-small-practice.txt','resultsmall.txt')