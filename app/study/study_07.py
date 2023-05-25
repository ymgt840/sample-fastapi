#7. 入力と出力

#7.1. 出力を見やすくフォーマットする

y = 2016
event = 'Referendum'
f'results of the {y} {event}'

y_v = 42_572_654
n_v = 43_132_495
percent = y_v / (y_v + n_v)
'{:-9} yes votes {:2.2%}'.format(y_v, percent)

s = 'Hello, world.'
str(s)
repr(s)
str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

hello = 'hello, world\n'
hellos = repr(hello)

repr((x, y, ('spam', 'eggs')))

import math
print(f'{math.pi:.6f}')