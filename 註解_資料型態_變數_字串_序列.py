# 「#」表示註解
#用「"""..."""」也可以表示註解(...的位置放要註解的東西。)

"""
程式中的註解，是寫給人看的，電腦執行時不會執行註解裡的東西
註解的功用：做紀錄、說明
"""

print("Hello world!")
print(1)

# 資料：程式的基本單位
# 以下介紹各種資料型態

# 數字
1      #整數int
1.2    #浮點數float(小數)

# 字串 String
"apple"
"蘋果"
"Hello world!"

# 布林值
True
False

# 有順序、可變的列表 List
[1,2,3]
["蘋果","香蕉"]

# 有順序、不可變的列表 Tuple
(1,2,3)
("蘋果","香蕉")

# 集合 Set
{1,2,3}
{"蘋果","香蕉"}

# 字典 Dictionary
{"apple":"蘋果","banana":"香蕉"}

# 變數：用來儲存資料的自訂名稱
# 變數名稱=資料
# 變數名稱須為英文，開頭不可以是數字
# 變數名稱可以照個人喜好命名，除了保留字元，例如：if、for、import、def...
# 放入變數(整數int)
a = 1

# 放入變數(浮點數float)
a = 1.2

# print(資料) => 把資料顯示出來
print(1)

print(True)

print([1,2,3])

print(a)

# 覆蓋問題
a = 1.2
a = True # 舊的資料會被取代

print(a)

a = [1,2,3]

print(a)

a = "apple"

print(a)

a = {1,2,3} # 集合 Set

print(a)

# 四則運算
a = 10
b = 2

a+b #加
a-b #減
a*b #乘
a/b #除
a%b #取餘數
a//b #取商數
a**b #立方

# 畢氏定理
d=7
e=24
f=(d**2+e**2)**0.5
print(f)

