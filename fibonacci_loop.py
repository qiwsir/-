#coding:utf-8#
'''
运用循环语句运算出雯波那契数列

'''
List = [1,1]    #定义初始列表
def function(n):
    ''' 循环函数
    输出雯波那契数列'''
    for i in range(1,n+1):
        if i==1 or i == 2:    #定义数列前两项
            pass
        else:
            List.append(List[i-2]+List[i-3])    #在初始列表后面添加

nterms = input("你要输出几项数列？")    #获取用户输入
if not nterms.isdigit():    #判断这个字符串是否为数值
    print('提示：请输入的数字为整数！')
else:       
    print('雯波那契数列为：')
function(int(nterms))
print(List)
