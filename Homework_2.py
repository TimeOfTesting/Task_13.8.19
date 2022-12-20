number_of_tickets = int(input("Введите количество билетов: "))

total_amount = 0
for i in range(1, number_of_tickets + 1):
    age_visitor = int(input("Введите возраст: "))
    if age_visitor < 18:
        total_amount += 0
    elif 18 <= age_visitor < 25:
        total_amount += 990
    else:
        total_amount += 1390
if number_of_tickets > 3:
    total_amount_discount = total_amount - total_amount * 0.1
    print("Сумма к оплате с учетом скидки - 10%: ", total_amount_discount, "руб")
else:
    print("Сумма к оплате: ", total_amount, "руб")