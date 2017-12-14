import sys
try:
    a = int(float(sys.argv[1]))
    x = a - 3500
    if x <= -3500:
        print("Parameter Errot")
    elif x > -3500 and x < 1:
        b = 0
    elif x <= 1500:
        b = x * 0.03
    elif x >1500 and x <= 4500:
        b = x * 0.1 - 105
    elif x > 4500 and x <= 9000:
        b = x * 0.2 - 555
    elif x > 9000 and x <= 35000:
        b = x * 0.25 - 1005
    elif x > 35000 and x <= 55000:
        b = x * 0.3 - 2755
    elif x > 55000 and x <= 80000:
        b = x * 0.35 - 5505
    elif x > 80000:
        b = x * 0.45 - 13505

    print(format(b,".2f"))
except:
    print("Parameter Error")
    



