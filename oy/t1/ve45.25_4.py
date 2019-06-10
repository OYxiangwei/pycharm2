class weierror(ValueError):
    def da(self):
        print("wei er")


try:
    l = int(input("please input number:"))
    rst = 100/l
    #raise weierror
    print(rst)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except AttributeError as e:
    print(e)
except weierror as e:
    print(e)
except Exception as e:
    print(e)

else:
    print("没有错误")
finally:
    print("wo must print")