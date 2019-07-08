def multiplesOf3and5(num):
    if type(num) != int:
        return 'Number can not be float! Int is required!'
    elif num<=3:
        return 'Number must be greater than 3!'
    else:
        multiples = [i for i in range(num) if i%3==0 or i%5==0]
        return sum(multiples)
