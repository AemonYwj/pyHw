# -*- coding: UTF-8 -*-

def testfun(x):
    return x

income = float(input("2022年月税后收入: "))
consumpt = float(input("2021年月消费总额: "))
#deposit = float(input("2021年月储蓄总额"))
profit = float(input("2021年月投资收入: "))
target = float(input("所需房屋首付款: "))

deposit = income+profit-consumpt

time = round(target/deposit) 

month = time % 12
year = int((time-month)/12)

print("需要",year,"年",month,"月")