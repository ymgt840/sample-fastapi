# https://docs.python.org/ja/3/tutorial/controlflow.html#more-control-flow-tools

# measure some strings
words = ['cat', 'window', 'def']
for w in words:
    print(w, len(w))


# collection
users = {'hans': 'active', 'Éléonore': 'inactive', '太郎': 'active',}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
 if status == 'active':
    active_users[user] = status

# range()
for i in range(5):
   print(i)

# list
list(range(5,10))

list(range(0,10,3)) # 第三引数はステップ

list(range(-10,-100,-30)) # 第三引数はステップ

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
   print(i, a[i])

range(10)

sum(range(4))

# break / continue / else
for n in range(2, 10):
   for x in range(2, n):
      if n % x == 0:
         print(n, 'equals', x, '*', n//x)
         break
      else:
         print(n, 'is a prime number')

for num in range(2, 10):
   if num % 2 == 0:
      print("even", num)
      continue
   print('odd', num)

# pass
while True:
   pass

class MyEmptyClass:
   pass

def initlog(*args):
   pass

# match
def http_error(status):
   match status:
      case 400:
         return 'bad'
      case 404:
         return 'not'
      case 418:
         return 'teapot'
      case _: # default
         return 'something wrong'

def match_point(point):
   match point:
      case (0, 0):
         print('origin')
      case (0, y):
         print(f"Y={y}")
      case (x, 0):
         print(f"X={x}")
      case (x, y):
         print(f"X={x}, Y={y}")
      case _:
         raise ValueError('No!!')

#  function with default args
def ask_ak(prompt, retries=4, reminder='please try again!'):
   while True:
      ok = input(prompt)
      if ok in ('y', 'ye', 'yes'):
         return True
      if ok in ('n', 'no', 'nop', 'nope'):
         return False
      retries = retries - 1
      if retries < 0:
         raise ValueError('invalid!!')
      print(reminder)

# warning1
i = 5
def f(arg=i):
   print(arg)

i = 6
f() # output is 5!!

# warning2
def f(a, L=[]): # 破壊的にLに干渉する
   L.append(a)
   return L

def f2(a, L=None): # L には干渉しない
   if L is None:
      L = []
   L.append(a)
   return L

# keyword args
def parrot(voltage, state='a stiff', action='voom', type='Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

# *name **name
# *name = 'tuple', **name=> dict
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop("test", "1","2","3","4","5",akan="test1",iyan="test2",bakan="twsss3", oioi="iyada")

# special params
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

def foo(name, /, **kwds):
    return 'name' in kwds

# unpack list
list(range(3,6))
args = [3,6]
list(range(*args))

# lambda no name function
def make_incrementor(n):
   return lambda x: x+n

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) # アルファベット順で並ぶ
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# annotation of function
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
