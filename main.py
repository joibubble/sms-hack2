import time
print('приветствую!')
print('введите номер жертвы: ')
i=input()
print('OK.')
print('Введите ник отправителя: ')
x=input()
print('OK.')
print('Введите циферный пароль: ')
p1=int(input())
p2=446653184
print('Подождите...')
time.sleep(5)
if p1==p2:
	print('АХАХАХАХА')
	time.sleep(1)
	print('МАКСИМ ГЕЙ!!!')
	time.sleep(1)
	print('ПОВЁЛСЯ АХХААХАХ')
elif p1!=p2:
	print('неверный пароль.')
