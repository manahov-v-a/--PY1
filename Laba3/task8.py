money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital - spend*(1+increase)**month >= 0:
    if money_capital + salary >= spend*(1+increase)**month:
        money_capital = money_capital + salary - spend*(1+increase)**month
    else:
        break
    month += 1

print(month)
