# this is super program!

# i = input ('input your money!\n'); #just input
# print (i);
# i = int(i);
# h = i*10;
# print ('real money:', h, ', yeah!\n');

# ----- ex 2.2 ------

## name = input ('Enter your name:\n');
## print ('Hello,', name, '!\n')
       

# ----- ex 2.3 ------

##hours = input ('Enter Hours: ');
##rate = input ('Enter Rate: ');
##hours = float (hours);
##rate = float (hours);
##pay = hours * rate;
##print ('Pay:', pay)

# ----- ex 2.4 Fahrenheit ------

##tC = input ('Enter temetature in Celsius: '); 
##tC = float (tC);
##tF = (9/5) * tC + 32;
##print ('The temerature in Fahrenheit is:', tF)

# ----- ex 3.1, ex 3.2 -------
# ----- ex 4.6 ---------------

##def computepay (h, r):  #this is my function
##    if h > 0 and r > 0:
##            if h < 40:
##                tr = h * r
##            else:
##                tr = (h - 40) * r * 1.5 + 40 * r
##            return tr
##    else: print ('Hours and rate must be positive!') 
##    
##
##h = input ('Enter Hours: ') #this is start
##try:
##    h = float (h)
##    r = input ('Enter Rate: ')
##    try:       
##        r = float (r)
##        totalpay = computepay (h, r) #function call
##        print ('Total pay: ', totalpay)      
##    except:
##        print ('ERROR! Enter numbers!')
##except:
##        print ('ERROR! Enter numbers!')
##

# ----- ex 3.3 -------
# ----- ex 4.7 -------


def computegrade (a):
    a = float (a)
    if a <= 1 and a >= 0:
        if a < 0.6: pr = 'F'
        elif a < 0.7: pr = 'D'
        elif a < 0.8: pr = 'C'
        elif a < 0.9: pr = 'B'
        else: pr = 'A'
    else: pr = 'Bad score'
    return pr

x = input ('Input score: ')
try:
    toprint = computegrade (x)
    print (toprint)
except:
    print ('Bad score')








