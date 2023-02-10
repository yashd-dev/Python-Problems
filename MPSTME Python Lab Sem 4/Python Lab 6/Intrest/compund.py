def compound_intrest(p,r,n,t):
    return (p * (((1 + ((r/100.0)/n)) ** (n*t))))
    # starting principle  is p
    # n is number of compounding periods
    # r is annual interest rate
    # t is amount of years