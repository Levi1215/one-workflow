# ipo input  process(处理)  out
# 静态语言,解释型语言

# 两种编程方式
# 交互式 
# 文件式
# import turtle
# turtle.pensize(3)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)
# from turtle import *
# color('blue','red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()
# done()

# temp_str = input('请输入温度值:')
# if temp_str[-1] in ['F','f']:
#     C = (eval(temp_str[0:-1]) - 32) / 1.8
#     print('转换后的温度为{:.2f}C'.format(C))
# elif temp_str[-1] in ['C','c']:
#     F = eval(temp_str[0:-1])*1.8 + 32
#     print('转换后的温度为{:.2f}F'.format(F))
# else:
#     print('格式有问题!')
# 编程语言的多样初心
# C   
#     学习内容    指针 内存  数据类型
#     解决问题    性能问题
#     语言本质    理解计算机系统机构
# java
#     学习内容    对象,跨平台,运行时
#     语言本质    理解主客体关系
#     解决问题    跨平台
# c++
#     学习内容    对象,多态,继承
#     语言本质    理解主客体关系
#     解决问题    大规模程序
# VB
#     学习内容    对象,按钮,文本框
#     语言本质    理解交互逻辑
#     解决问题    桌面应用
# python
#     学习内容    编程逻辑,第三方库
#     语言本质    理解问题求解
#     解决问题    各类问题
# python  通用型语言


# turtle.setup(600,350,200,200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor('red')
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,100)
# turtle.fd(40*2/3)
# turtle.done()
# turtle.seth(45)
# turtle.fd(10)

# 数据库的三范式
# 第一范式1NF:满足列的原子性,列不能再分多列

# 第二范式2NF:满足第一范式1NF,还满足必须有个主键,
# 其他不包含主键的列必须完全依赖于主键

# 第三范式3NF:首先满足2NF,非主键必须完全依赖于主键,
# 不能存在传递的关系
