#перевод из 10 в 8 
def my_to_oct(s):
    if s.count('.') != 0:
        s1, s2 = s.split('.')
    else:
        s1 = s

    s1 = int(s1)

    s1end = ''
    
    
    while(s1 > 0):
        s1end = str(s1%8) + s1end
        s1//=8
    
    if s.count('.') != 0:
        s2end = ''
        s2 = float('0.'+s2)
        while s2-int(s2)>0:
            s2*=8
            s2end+=str(int(s2))
            s2-=int(s2)
        return float(s1end+'.'+s2end)
    else:
        return float(s1end)


#перевод из 8 в 10 
def my_to_des(s):

    if s.count('.') != 0:
        s1, s2 = s.split('.')
    else:
        s1 = s

    s1end = 0

    mult = 1

    for x in reversed(s1):
        if x != ' ': 
            s1end += (mult * int(x))
        mult*=8
    
    if s.count('.') != 0:

        mult = 1/8

        s2end = 0
        for x in s2:
            if x != ' ':
                s2end += (mult * int(x))
            mult /= 8
            
            
        s2end = str(s2end)

        s1end = s1end + float(s2end)
        return float(s1end)
    else:
        return float(s1end)

