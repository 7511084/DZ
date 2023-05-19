money = input('Введите сумму вклада: ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent['ТКБ'] * int(money)
b = per_cent['СКБ'] * int(money)
c = per_cent['ВТБ'] * int(money)
d = per_cent['СБЕР'] * int(money)
dep = [round(a),round(b),round(c), round(d)]
max_dep=max(dep)

print (dep)
print ("Максимальная сумма, которую вы можете заработат:", max_dep)

