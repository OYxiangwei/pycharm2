s = input("请输入一到一百之间的整数:")
if s.isdigit():
    s = int(s)
    if s <1  :
        print("小了")
    elif s >100 :
        print("大了")
    else:
        print("输入的是：{}".format(s))
else:
    print("请输入数字")

