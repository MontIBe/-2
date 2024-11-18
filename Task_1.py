money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

num_of_months = 0 # Кол. месяцев
balance_1 = money_capital + salary - spend # Остаток бюджета 1-ого месяца

while balance_1 >= 0: # Создание цикла при условии, что бюджет >= 0
    spend += spend * increase # Рост цен на 5%
    balance_1 += salary - spend
    num_of_months +=1

print("Количество месяцев, которое можно протянуть без долгов:", num_of_months)

