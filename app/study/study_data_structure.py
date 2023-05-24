# stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]

# queue
from collections import deque
queue = deque(['1', '2', '3'])
queue.append("4")
queue.append('5')
queue.popleft()
queue.popleft()
queue

# 5.1.3 included list
s = []
for x in range(10):
   s.append(x**2)

s

s2 = list(map(lambda x: x**2, range(10)))
s3 = [x**2 for x in range(10)]

## 分かりにくいでしょ
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs

# tuple
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]

[x for x in vec if x >= 0]
[abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# weapon?
[weapon.strip() for weapon in freshfruit]

[(x, x**2) for x in range(6)]

# ネストループ
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# 円周率を1桁から6桁まで出す
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#5.1.4. ネストしたリストの内包表記
matrix = [
    [1,2,3,4,],
    [5,6,7,8,],
    [9,10,11,12,],
]

# matrix の行と列を入替える
[[row[i] for row in matrix] for i in range(4)]
# 以下と同じ
trans = []
for i in range(4):
    trans.append([row[i] for row in matrix])

# 更に直す (これを1行に出来るのがpython だが・・・)
trans = []
for i in range(4):
    trans_row = []
    for row in matrix:
        trans_row.append(row[i])

    trans.append(trans_row)

# 実際には組込関数を使うべき以下で行ける
# zip = 平行反復処理 タプル生成
# listを付けることで、obj->arrayに変換される
# これはマスターしたい
list(zip(*matrix))

# 5.2. del 文¶
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]

# 5.3. タプルとシーケンス
tp = 12345, 54321, 'hello'
up = tp, (1,2,3,4,5)

# 内側のリストは変更可能
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 'a'# 可能

# 5.4. 集合型
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

a = set('abracadabra')
b = set('alacazam')

a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}

# 5.5. 辞書型 (dictionary)
tel = {'jack': 4098, 'sape': 4139}
tel['add'] = 2020
del tel['sape']
tel['irv'] = 4127
'guido' in tel
True
'jack' not in tel
False

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

# 5.6. ループのテクニック
ks = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in ks.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

q = ['name', 'quest', 'f color']
ans = ['lance', 'holly', 'blue']
for q, a in zip(q, ans): # zip 関数で要素をひとまとめにする
    print('what is your {0}? it is {1}.' . format(q, a))

# シーケンス逆ループ
for i in reversed(range(1, 10, 2)):
    print(i)

# シーケンス order sorted()
# 重複は認める
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# 重複をカットする為に、setを使用する
for i in sorted(set(basket)):
    print(i)

# 新しいリストを作成する
import math
r_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
f_data = []
for val in r_data:
    if not math.isnan(val):
        f_data.append(val)

f_data

# 5.7. 条件についてもう少し
# bool 式の結果を変数に代入する
s1, s2, s3 = '', 'test', 'scroll'
non_null = s1 or s2 or s3 # bool ではなく、真の文字列が返却する
non_null

ttest = s1 and s2 and s3

# 5.8. シーケンスとその他の型の比較
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)