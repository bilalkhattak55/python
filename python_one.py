# print("hello world", 23, end='\n')

# name = input('Name: ')
# print(name)

# name = input('Name: ')
# age = input('age: ')

# print('Hello', name, 'you are', age, 'years old')

# print(ord('a'))
# print(ord('abb'))

# x = input('Name: ')

# if x == 'bilal': 
#     print('you are greate') 
#     y=input('Name: ')
#     if y== 'ali': print('ali ali')
#     else: print('not ali')
# elif x=='joe': print('good boy')
# elif x=='faraz':print('you will become an engineer')
# else:
#      print('please be like bilal')

# x= [4, True, 'hi']

# x.append('bilal')
# x.extend([4,5,6,8])
# print(x.pop(1))
# x[0]=5
# x[1]= False

# y=x[:]
# x[1]= False
# print(x, y)



#Tuple
# x= (0,2,4,6,8)
# x[2] = 5
# print(x)

# for i in range(-5, 12, 2):
#     print(i)

# for i in [4, 4, 45, 45, 6, 74, 77]: print(i)


# x= [3, 4, 5, 6,7, 8, 10]

# for t in range(len(x)): print((x[t]))

# for i, elem in enumerate(x): print(i, elem)
# i=0

# while i < 10:
#     print('rin', i)
#     i+=1
    
# while True:
#     print('start')
#     i+= 1
#     if i == 10:
#         break

# while True:
#     print('start')
#     print("1", i)
#     i+=1
#     while True:
#         if i == 10:
#             print("2",i)
#             break



#slice

# x= [3, 4, 5, 6,7, 8, 10, 12, 14, 16, 18, 20]
# y= ['hi', 'bye', 'hello', 'cya']

# sliced = x[start:stop:step]
# sliced = x[1:8:2]
# sliced = x[:8]
# sliced = x[3:]
# sliced=x[::-1]
# sliced=x[::2]
# sliced=(1,2,3,4,5,6,7,8,9)[::-2]
# print(sliced)

# x= set(range(1000000))
# x.add(2)
# x.add(3)
# x.add(4)
# x.add(2)
# x.add(2)
# print(x)



# s={3,4,5,6,7,8}
# s2={2,5,6,14,33}
# # print(s.union(s2))
# # print(s.intersection(s2))
# print(s.difference_update(s2))


#Dictionaries;

# x= {'key': 5, 'key2': 6}

# y={'key': [3,4,5]}

# print(x['key'])
# print(y['key'])
# for key, value in x.items(): print(key, value)
# for i in x: print(i, x['key'])





#Comprehensions

# x= [x for x in range(5)]
# x= [x%5 for x in range(5)]
# x= [[0 for x in range(10)] for x in range(2)]
# x= [i for i in range(100) if i % 10 == 0]
# x= {i:i for i in range(100) if i % 10 == 0}
# x= (i for i in range(100) if i % 10 == 0)
# x= tuple(i for i in range(100) if i % 10 == 0)

# print(x)




#functions

# def func(num):
#     print(num)
#     def func(num):
#         print(num) 
#     func(num + 1) 
 
  
# num =1
# func(num)     

# def func(x, y):
#     print('run', x + y)
#     return x+y, x*y, x/y

# print(fun(4, 5))
# val1, val2, val3 = func(4, 8)
# print(val1, val2, val3)




############################# unpack operator / *ARGS And ** kwargs
# def func(x):
#     def func2():
#         print(x)
#     return func2


# func(3)()

# def func(*args, **kwargs):
#     pass

# x= [1, 2, 3, 4, 55]
# print(*x)

# def func(x, y):
#     print(x, y)

# pairs = [(1,2,3), (4,5,6,7)]

# for pair in pairs:
#     print('pair', pair)
#     print('pair0', pair[0])
#     # func(pair[0], pair[1])
#     func(*pair)

# func(**{'y': 5, 'x': 2})

# def func(*args, **kwargs):
#     print(args, kwargs)
#     print(*args)


# func(1, 2,3,4,5,6, x=0, two=5)


# x= 'bilal'


# def func(name):
#     # x= name
#     global x
#     x= name
#     print(x)

# print(x)
# func('changed')
# print(x)


# raise Exception('Bad')
# raise FileExistsError('badd')

# try:
#     x=7/0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

# x= lambda x, y: x+y

# print(x(2, 3))


# x= [1, 3,4,5,6,7,7,8]

# # mp = map(lambda i: i*2, x)
# def func(i):
#     return i % 2 == 0
# # mp = filter(lambda i: i%2 == 0, x)
# mp = filter(func, x)
# print(list(mp))


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} is starting")


my_car = Car('Toyota', 'Corolla', 2020)
my_car.start()
    
