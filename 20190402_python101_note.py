
## 0402 note
### 123
- 1.2323
- 2.fdfs
- 3.dsf 

a=5
b='dd'
c=1.3
d=True

print (type(a),type(b),type(c),type(d))

## if elif else statement

a=5
b=8

if a > 8:
    print ("a greater than 4")
elif a < 8:
    print("work")
else :
    print("a is less than 4")

g=''
if g :
    print(a)
elif b:
        print(b)

a ='i am a string'


bool(a)

bool(g)

bool(9)

bool('')

bool(0)

bool(0.01)

bool(bool)

bool('0')

bool('sdfs')

bool(False)

bool(True)

## list

my_list=['a',5,5.5,True]

my_list

type(my_list)

my_list_2=['a',['b','c',7],True,7]

type(my_list_2)

my_questions=['Q1','Q2','Q3','Q4','Q5']

my_questions[0]

my_questions[3]

my_questions[0:2]#python range from head no tail~

my_questions[::2]#list 間隔1

len(my_list)

len(my_questions)#list 有幾個物件

my_questions.append('Q6')#增加list物件於最後

my_questions

my_questions.remove('Q2')#移除物件

my_questions

my_questions[::-1]#將List反向

my_questions[::-2]

my_questions.reverse()

my_questions

my_questions.sort() 

my_questions

## loop

range(10)

for _ in range(10):#for 隨便值 in  list:
    print(_)

###### for _ in my_questions:
    print (_)

for _ in my_questions:
    print (_.lower())#小寫

for _ in my_questions:
    print (_.upper())#大寫

for _ in my_questions:
    print (_.capitalize())#字首大寫

a = [3,6,-1,7,-4,100]

for _ in a:#判斷a中 數值+5
    if (_+5)*3> 10:
        print(_)

# Homework
## folder 中 excel 檔有幾個 檔名有多長 os.listdir()

import os#套件組operation system

for _ in os.listdir():
    if _.endswith('ipynb'):
        lenght = len(_)
        print(_, lenght)

g='actgenomics'

g.capitalize#物件的功能 按tab有所有功能 按shift+tab有功能的作用

g.capitalize

Shift +M 合併
