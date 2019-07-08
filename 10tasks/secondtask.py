
def make_fibo_list(n):
    f0, f1 = 1, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1


def sum_of_fibo_list(n):

    if type(n) != int:
        return 'Number can not be float! Int is required!'
    elif n<0:
        return 'Number must be positive!'
    else:
        fibo_nums = list(make_fibo_list(n))
        even_fibo_nums = [i for i in fibo_nums if i%2==0]
        return sum(even_fibo_nums)

