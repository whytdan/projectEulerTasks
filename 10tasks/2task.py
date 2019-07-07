
def make_fibo_list(n):
    f0, f1 = 1, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1

fibo_nums = list(make_fibo_list(33))
even_fibo_nums = [i for i in fibo_nums if i%2==0]
print(sum(even_fibo_nums))