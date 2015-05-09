# ---- 5.1 iterations ----


##s = 0
##c = 0
##
##while True:
##    n = input ('Enter a number: ')
##    if n == 'done':
##        break
##    else:
##        try:
##            n = float (n)
##            print (n)
##            s = s + n
##            c = c + 1
##            a = s/c
##        except: print ('Bad number, try again')
##print ('total: ', s)
##print ('count: ', c)
##print ('average: ', a)
##        


# ---- 5.2 iterations ----

smal = None
larg = None
s = 0
c = 0

while True:
    n = input ('Enter a number: ')
    if n == 'done':
        break
    else:
        try:
            n = float (n)
            print (n)
            s = s + n
            c = c + 1
            if smal==None or smal>n:
                smal = n
            if larg==None or larg<n:
                larg = n
        except: print ('Bad number, try again')
print ('Total:', s)
print ('Count:', c)
print ('Smallest:', smal)
print ('Largest:', larg)


