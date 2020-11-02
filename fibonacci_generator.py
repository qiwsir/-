#coding:utf-8#
'''
运用生成器运算出雯波那契数列

'''
def fib_yield(max):
    '''定义生成器函数
       输出雯波那契数列
    '''
    a, b = 0,1    #定义a,b初始值
    while max > 0:
        a, b = b,a+b
        max -= 1
        yield a    #返回a值

def fib_yield_for(n):  # 能去掉n或者上面的max吗？
    a, b = 0,1
    for _ in range(n):
        a, b = b,a+b
        yield a

if __name__ == '__main__':    
    nterms = input("你要输出几项数列？")    #获取用户输入
    if not nterms.isdigit():    #判断这个字符串是否为数值
        print('提示：请输入的数字为整数！')
    else:       
        print('雯波那契数列为：')
    for i in fib_yield_for(int(nterms)):
        print(i,end=" ")
