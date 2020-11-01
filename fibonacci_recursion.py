#coding:utf-8#
'''
运用递归法运算出雯波那契数列

'''
def fib_recur(n):
    """ 递归函数
    输出雯波那契数列"""
    if n <= 1:
        return n
    else:
        return(fib_recur(n-1)+fib_recur(n-2))

#if _name_ == '_main_':
nterms = input("你要输出几项数列？")    #获取用户输入
if not nterms.isdigit():    #判断这个字符串是否为数值
    print('提示：请输入的数字为整数！')
else:       
    print('雯波那契数列为：')
    for i in range(int(nterms)):
        print(fib_recur(i),end=" ")
