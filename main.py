def recursion_sum(x):
    if len(x) == 0:
        return 0
    else:
        p = x[len(x)-1]
        x.pop(len(x)-1)
        return p + recursion_sum(x)


lst = [int(i) for i in input('Введите, пожалуйста, список чисел через пробел:').split()]
print('Сумма чисел из списка =', recursion_sum(lst))