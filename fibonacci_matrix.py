#coding:utf-8#
'''
运用矩阵计算出雯波那契数列

'''
import numpy   #安装numpy包，并导入numpy模块
def fib_matrix(n):
    '''定义矩阵函数，
       输出雯波那契数列
    '''
    for i in range(n):
        res = pow((numpy.matrix([[1, 1], [1, 0]], dtype='int64')), i)\
              * numpy.matrix([[1], [0]])    #创建矩阵，运用pow函数返回前面矩阵的i次方和后面的矩阵相乘
        print(int(res[0][0]))

if __name__ == '__main__':    
    nterms = input("你要输出几项数列？")    #获取用户输入
    if not nterms.isdigit():    #判断这个字符串是否为数值
        print('提示：请输入的数字为整数！')
    else:       
        print('雯波那契数列为：')
        fib_num = fib_matrix(int(nterms))
        print(fib_num)
