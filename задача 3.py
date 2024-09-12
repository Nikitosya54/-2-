a = int(input("введите первое число: "))
b = int(input("введите вторе число: "))
c = int(input("введите ретье число: "))
if a+b>c and a+c>b and c+b>a:
    print("yes")
else:
    print("no")