deposit_rubles = 997530
deposit_pennies = 4041
deposit_pennies = deposit_pennies / 100
money_before = deposit_rubles + deposit_pennies
money_after = (money_before*(100+percent)/100)
result = int(money_after)
print(result)