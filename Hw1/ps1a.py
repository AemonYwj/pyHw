# -*- coding: UTF-8 -*-

total_cost = float(input("请输入你希望购买房屋的价格: "))

portion_down_payment = float(input("请输入你希望购买房屋的首付比例: "))

# your salary per year
annual_salary = float(input("请输入你的年收入: "))
# the saving percentage
portion_saved = float(input("请输入你每月从收入中存入银行的占比（小数形式）: "))

# the deposit you kept, starting at 0
current_savings = 0
# the annual return rate of your saving
r = float(input("请输入你的储蓄的投资收入利率（年化）（小数形式）: "))

down_payment = total_cost*portion_down_payment
counter = 0
monthly_salary = annual_salary/12


while current_savings<down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    counter += 1

years = counter//12
months = counter-(years*12)

print("攒到首付所需要的时间",years,"年",months,"月。")
    