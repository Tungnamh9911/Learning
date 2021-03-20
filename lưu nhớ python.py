#đây là chương trình đầu tiên tôi tiến vào môi trường cntt

#gán cho biến một giá trị
a = 2
b = 2
c = "nana" 

#in ra màn hình chuỗi
print ("ha")
#câu lệnh điều kiện if else
if a < 2:
	print ("a be")
elif a > 2:
	print ("a lon")
else:
	print ("ok")
# câu lệnh lặp while,for


while a <= 100: 
	 print (a)
     a += 1 


#lệnh kiểm tra giá trị biến (in ra màn hình)
print (type(a))

#lấy, nhập nội dung của một thư viện:

import #nhập thư viện
# lấy toàn bộ thư viện demical

from decimal import*

getcontext().prec = 30 # lấy tối đa 30 chữ số
#dùng thư viện Decimal
print (Decimal(10)/Decimal(3))
#kiem tra bien A co trong bien  B khong
strA = "zawarudo"
strB = "z"
strC =  strA in strB
print (strC)

#cắt chuỗi
strB = strA[3]
#lấy ra độ dài của chuỗi
strB = len(strA)
#cắt chuỗi theo độ dài nhất định
strB = strA[so nguyen:so nguyen]
#none (trống, lấy từ đầu)
#cắt chuỗi có bước nhảy(cách):
strB = strA[số nguyên:số nguyên:số nguyên]
           #cắt từ      tới     bước nhảy
#ép kiểu chuỗi - số
int("69") + số nguyên # chuỗi có thể cộng với số nguyên
#sửa giá trị/dữ liệu trong chuỗi
strA = "helloboy"
strB = strA [none:1] + "0" + strA[2:none]
                 #kí tự cần thay
# chuỗi là một hàm hash(không thay đổi khi chạy chương trình). Vậy nên khi chạy một chương trình python, ta chỉ có thể thay đổi giá trị chuỗi bằng lệnh 

#thay thế %s trong chuỗi bằng đánh dấu % bên ngoài
a = 'my team is %s' %('Kteam')
print (a)
#thay nhiều đơn vị
a = 'my %s team is %s' %('Kteam','kteam two')
print (a)

#thay bằng print 
a = 'my team is %s'
print (a %('1'))
#or
a = 'my team is %s'
thay = a %('1')
print (thay)

# chữ f để xóa ngoặc nhọn chứa biến bên trong
Kteam = Kteam
a = f'{Kteam} - bu cac'
print (a)

#phương pháp format
r = '1: {} , 2:{}'.format(111,222)
#căn lề trái phải giữa
r = '{:^10}'.format('kteam')
       # > <
print (r)
#thêm dấu trang trí
r = '{:@^10}'.format('kteam')
print (r)
#thêm chữ
r = 'dafuq{:^10}ditme'.format('kteam')
print (r)
#viết hoa đầu câu
a = 'howkteam'
b = a.capitalize()
print (b)
#viết hoa cả câu
a = 'howkteam'
b = a.upper()
print (b)
#viết thường hết
a = 'howkteam'
b = a.lower()
print (b)
#viết thường thành hoa và hoa thành thường
a = 'howkteam'
b = a.swapcase()
print (b)
#viết hoa chữ đầu từng từ
a = 'howkteam'
b = a.title()
print (b)
#căn giữa
a = 'howkteam'
b = a.center(30,'-')
print (b)
#mã hóa
a = 'howkteam'
b = a.encode(encoding ='utf-8', errors ='strict')
print (b)
#đánh dấu từng từ trong chuỗi bằng số chuỗi + số
a = 'howkteam'
b = a.join(['1','2','3'])
print (b)
#thay thế kí tự hoặc chuỗi 
a = 'howkteamh'
b = a.replace("h","k","1")
print (b)             #thay chữ h đầu tiên
#cắt chữ ở 2 đầu
a = 'howkteamh'
b = a.strip('h') #r/lstrip
print (b)
#cắt từng khoảng trắng trong chuỗi
a = 'howkteamh'
b = a.split('h')
print (b)
#cắt có số lần
a = 'howkteamh'
b = a.split('',2 )
print (b)     #căt bao nhiêu lần
#trả về giá trị chuỗi trước k, chuỗi k và chuỗi sau k
a = 'howkteamh'
b = a.partition('k')
print (b)
#đếm ký tự trong chuỗi
a = 'howkteamh'
b = a.count('h',0,5)
print (b)
#kiểm tra xem chuỗi có bắt đầu bằng chữ " " không
a = 'howkteamh'
b = a.startwith('h',0,9)
print (b)
#tìm một chuỗi trong 1 chuỗi
a = 'howkteamh'
b = a.find('h') #trả về số nguyên vị trí đầu tiên tìm thấy chuỗi
print (b)
#giống cái trên nhưng báo lỗi
a = 'howkteamh'
b = a.index('h')
print (b)
#có viết thường toàn chuỗi không
a = 'howkteamh'
b = a.islower()
print (b)

#viết hoa toàn chuỗi không 
a = 'howkteamh'
b = a.isupper()
print (b)

#kiểm tra chuỗi all số hay không
a = 'howkteamh'
b = a.isdigit()
print (b)
#check chuỗi có phải khoảng trắng không
a = 'howkteamh'
b = a.isspace()
print (b)
#biến nhiều giá trị
a = [['2','3']'2','3']
print (a)
# tạo ra list gán vào biến a từ 0 - 30
a = [i for i in range(30)]
print (a)
#nhân từ 2 đến 4 với 1
a = [[n*1]for n in range(1,4)]
print (a)
#tách từng ký tự trong chuỗi
a = list("kteam")
print(a)
#cộng tập hợp với chuỗi
a = [1,2]
a = a + ['3','4']
print (a)
#nhân nhiều lần chuỗi
a = [1,2]
a += 2 
print (a)
#kiểm tra chuỗi trong biến bằng in
#số lần xuất hiện của  1 số 
a = [1,1,1,2,3,4]
c = a.count(1)
print (c)
#trả về vị trí đầu tiên của chuỗi nằm trong list
a = [1,1,1,4,8,9,8]
c = a.index(1)
print (c)
#tạo ra một bản sao
a = [1,2,3]
c = a.copy()
print (c)
#xóa đi các phần từ trong list
a = [1]
c = [1]
print (a)
print (c)

c.clear()

print (a)
print (c)

#thêm vào list một phần tử
a = [1,2,3]
a.append([2,4])
print (a)

# thêm vào từng phần tử
a = [1,2,3]
a.extend([2,4])
print (a)
# thêm phần tử x vào vị trí y
a = [1,2,3]
a.insert(2,4)
print (a)
#bỏ đi phần tử y của x và trả về giá trị đó
a = [1,2,3]
c = a.pop(2)
print (a)
#xóa bỏ phần tử trong list
a = [1,2,3]
a.remove(2)
print (a)
#ra một list đảo ngược lại
a = [1,2,3]
a.reverse()
print (a)
#sắp xếp list lại theo thứ tự
a = [1,2,3]
a.sort(reverse=true) #or  a.sort()
print (a)

#biến tup
# 
tup = (1,(2,3))
print (tup)
#
tup = (i for i in range(10))
a = tuple (tup)
print (a)
#
tup = (1,2,3)
a = tup[2]
print (tup)
#check độ dài tup
tup = (1,2,3)
a = len(tup)
print (tup)
#kết quả trẳ về int hoặc longint
a = id(5)
print (a)
#add thêm một đơn vị
n = 3
print (n.__add__(1))
#sub trừ 1 đơn vị
n = 3
print (n.__sub__(1))
#mul nhân n = 3
n = 3
print (n.__mul__(1))
#neg thêm dấu âm
n = 3
print (n.__neg__(1))
#set không trùng phần tử và ko thể chứa set trong set
set = {69,95}
print (set)
#set = {in for in range()} có thể dùng đc\
set_2 = set("zawarudo")
print set_2
#trừ
print ({2,3} - {1,2,3})
#Láy hết cả 2 bên
print ({1,2} | {3,4})
#tìm giá trị chung của hai ngoặc nhọn
print ({1,2,4} & {3,4})
#set4.clear xóa toàn bộ
set4.clear()
#set9.pop lấy rồi in ra cái lấy
set9.pop(1)
#set2.remove lấy rồi in ra cái còn lại
set2.remove(1)
#set3.discard giống remove nhưng không lỗi
set3.discard()
#set1.copy nhân bản
#set3.add (4) thêm phần tử

#dic

dic = {key: value for key,value in [("name","kteam"),("member",69)]}
print (dic)

#4 cách khởi tạo dic
dic = dict ()
print (dic)
#
iter_ = ('name','number',69.True)
dic = dict.fromkeys(iter_,'Howkteam')
print (dic)
#lấy key
iter_ = ('name','number',69.True)
dic = dict.fromkeys(iter_,'Howkteam')
print (dic[name])
#gán giá trị cho key
iter_ = ('name','number',69.True)
dic = dict.fromkeys(iter_,'Howkteam')
dic['name'] = 'free education'
print ("dic") #tự thêm key nếu gán cho key ko tồn tại trong list

#
dic = dict(k = 69, H ='s')
print (dic)

dic["k"] = dic['k'] + 1 #or + chuỗi
print (dic)

#get key trả value của key
d = {'Team':"teamK",(1,2):69}
print(d)
value = d.get ("team")
print value
# thay thế nếu giá tị ko có
d = {'Team':"teamK",(1,2):69}
print(d)
value = d.get ("dsd","default")
print value
#Trả ra key và value
value = d.items()
#chỉ lấy ra danh sach key
value = d.keys()
#lấy danh sách values
value = d.values()
#pop xóa luôn key và value lấy ra
value = d.pop("team")
# trả về giá trị value có key
value = d.popitem()
#thêm một thằng value mới và set key
value = d.setdefault("teamFF","yaro..")
#update key mới(chưa tồn tại thì thêm,tồn tại lấy mới)
value = d.update(Team = "fReE")
# hàm mở file
o_file = open('file.text')
#đọc file 
o_file = open('file.text')
data = o_file.read()
#đóng file
o_file = open('file.text')
o_file.close()
#đọc từng dòng bằng .readline()
#ghi vào file text và đọc số ký tự vừa ghi trong file
data = o_file.write("")
#os.rename (nguồn file + ten file,nguồn di chuyen + ten moi)
          #(ten file,ten moi) 2 muc dich  1 chuyen vi tri 2 thay ten

          
# iterable
itera = (x for x in range(3))
print (itera)
print (next(itera))
print (next(itera))
print (next(itera)) 
#trả về tổng các giá trị
sum(itera,0)
#tìm giá trị lớn nhất
max(itera)
#tìm giá trị nhỏ nhất min()
                          #hàm sắp sết sorted #reverse = true

#bài hàm nhập xuất trong python

#sep = "" tạo kí tự khoảng cách
print ("Kteam","solo",sep ="===")
#end ko xuống dòng
print ("khong xuong dong", end ="")

'''hàm đợi:
import time 
time.sleep = (3)'''

#một cách mở file(ghi vào file)(đóng luôn sau khi sử dụng)

with open("ghivaofile.txt", 'w' ) as ten:
  print ("ghi vao file", file = ten)


# in ra giá trị khi không có newline(khi dùng hàm end = "")
from time import sleep

print ("start...",end = "",flush = True)
sleep (3)
print ("end...")

#tạo chương tình đánh từng chữ
import time

a = "za"
b = "warudo!"
for c in a + b:
  print (c , end = "", flush  = True)
  time.sleep(0.1)

# hàm evel có khả năng thực thi một expression (khá là phức tạp nên sẽ tìm hiểu sau)
    #ví dụ đối với hàm input khi kết hợp có thể thực thi lệnh ngay trên dòng nhập input: eval(input(""))

#kiểm tra giá trị ACSII bằng hàm ord("")

#break :kết thúc vòng lặp while
#continue tiếp tục vòng lặp while

#Hàm try() được sử dụng trong việc xử lý lỗi và ngoại lệ trong Python
            #Cú pháp cơ bản:

try:
  // Code
except:
  // Code

#items

aduvjp = {"name":"team","wow":69}
print (aduvjp.items())
#làm gọn dễ nhìn
aduvjp = {"name":"team","wow":69}
value = list(aduvjp.items())
print (value)

#for else( kết thúc vòng lặp sẽ dùng câu lệnh ở else)
for k in (1,2,3):
  print (k)

else:
  print("done")
#ví dụ khác
for k in (1,2,3):
  print (k)
  if k % 2 == 0:
    break
else:
  print("done")

#ví dụ khác
for k in (1,2,3):
  print (k)
  if k % 2 == 0:
    continue
else:
  print("done")

#hàm range tạo danh sách theo số đặt bên trong
k = range(6)
print (list(k)) # range từ 0,6 (0 đến 6)
#
k = range(6,9)
print (list(k))
#range ngược
k = range(4 , 1 , -1)
print (list(k))
#vd khác
lst = [5,(1,2,3), {"abc","xyz"}]
for i in range(len(lst)):
  print (1st[i])
#cập nhật list phải dùng range
lst = [5,(1,2,3), {"abc","xyz"}]
for i in range(len(lst)):
  lst[i] += 1
  print (lst[i])
#hàm enumerate
student_list = ["alo","buh bub","lmao lmao"]

gen = enumerate(student_list)
print (list(gen))
#  ví dụ khác
db = ["alo","buh bub","lmao lmao"]
for idx, student in enumerate(db,9):
  print (idx, "=", student)

# lưu chữ một khối lệnh để có thể tái sử dụng
'''Trong Python, pass là một lệnh trống.
 Nói nôm na thì lệnh pass không làm gì cả, nó chỉ 
 giữ chỗ cho các hàm, vòng lặp mà bạn đã thêm vào, nhưng
  chưa dùng đến trong hiện tại mà để "dành cho con cháu"
   mở rộng trong tương lai.'''
def Kteam():
  print ("aduvjp")
Kteam()

#truyền parameter
def Kteam(text):
  print (text)
Kteam()


#set default cho param
def Kteam(age,text = "sasuke"):
  print (text)
  print (age)
Kteam(28)
#ví dụ 
def f (kteam=[]):
  kteam.append("F")
  print (kteam)
f()
#ví dụ keyword
def kteam(a,b):
  pass

kteam(3,'Free')
kteam(b = 3,a ='Free')

#dùng * vào phần keyword def ... (a,*,b) để đánh dấu ngăn cách pos và keyword

#unpack
def team(a,b,c,d):
  print (k,t,e,r)
lst = ['za','wa','ru','do']
kteam(*lst)
#truyền thêm thì đưa thêm kteam(*lst, "bla bla")
#vd khác 
def team(*muda):
  print (muda)
  print(type(muda))

team(*(x for x in range(10)))
#ví dụ khác
def kteam(a,b):
  print (a)
  print (b)


dic = {'name':'duma','fuck':'muda'}
kteam(**dic)
#ví dụ nữa
def team(**kdu):
  print(kdu)

team(name='kteam',member=69)

#vd nữa
def team(**kdu):
  for key,value in kdu.items(): 
    print(kdu)

team(name='kteam',member=69)
#ví dụ tiếp
kteam = "howk"
def say():
  kteam_ = "howkteam"
  print ("weare",kteam)
say()

#tạo ra các biến toàn cục để tái sử dụng lại bằng gobal
def a():
  global kteam
  kteam = "howkteam"

a()
print (kteam)

#ví dụ
def make_global():
  global x
  x = 1

def local():
  x = 5
  print ("x in local", x)

make_global()
print (x)

local()
print (x)

#dùng return để ngắt hàm
def _return ():
  print ("haha")
  return
  print ("không được gọi tới")

goi_ham = _return()
print (type(goi_ham))
#gọi ra nhiều thành phần trong hàm cùng return
def a(a,b):
  c = (int(a) + (b))
  d = int(a) - int(b)
  return a,b 
a_ = 3
b_ = 2
tong_tru = a(a = a_, b = b_)
print (tong_tru)
# hàm yield sẽ trả về một generator mà ko chạy ngay
def adu(lst):
  for num in lst:
    yield num**2

kteam = adu([1,2,3])
for value in kteam:
  print(value)

#return sau khi đưa ra giá trị sẽ ngắt luôn hàm còn yield sẽ tiếp tục hàm

#ví dụ về send và next
def gk():
  while True:
    x = yield 
    yield x ** 2

g = gk()
next(g)
print (g.send(2))
next(g)
print (g.send(10))

#cách sử dụng lambda khá giống def
ave = lambda a,b,c: (a + b + c)/3

print (ave(1,2,3))
#ví dụ khác
x_a = lambda x, a=2: x ** a

print (x_a(2))

# ví dụ khác

kteam_lst = [lambda x: x**2 , lambda x: x**3]
print (kteam_list[1](3))
 #mở rộng ví dụ trên
for fuc in kteam_list:
  print(fuc(3))

#ví dụ khác
key1 = "a ne"

print({"b ne": lambda:"cung voi b",
  "c ne":lambda:"cung voi c",
  "a ne":lambda:"cung voi a"}[key1]())

#vi du
adu = lambda x,y: x if x > y else y
print (adu(1,2))
#ví dụ
def kteam(first_string):
  return lambda second_string: first_string + second_string # trả về một hàm, và lưu biến first_string
a = kteam("how team k")
print (a("dcm thang cho nay m chan song a"))

#hàm map thêm 1 đơn vị cho tất cả các thứ trong 1 list 

def adu(x): return x + 1

kteam = [1,2,3,4]

print(list(map(adu, kteam)))
#or 
inc = lambda x: x + 1
kteam = [1,2,3,4]
print([inc(x) for x in kteam])

#ví dụ

func = lambda x,y: x + y
k1 = [1,2]
k2 = [3,4]
kteam = map(func,k1,k2)
print (kteam)

#filter lọc
func = lambda x: x>0
kteam = [1,-3,5,-2]
print(filter(func,kteam))
#or
print([x for x in kteam if x > 0])

#reduce tính tất các số trong list hoặc cộng lần lượt bằng cách gom
from functools import*
kteam_add = lambda x,y: x + y
kteam = ["dit","me","dang","gom"]
#đệ quy python (khó hiểu)

def cal(l):
  return 0 if not L[0] + cal_sum(L[1:])

print (cal([1,2,3]))


#ví dụ hàm đệ quy
def giaithua(n):
    """Đây là hàm tính giai thừa của
    một số nguyên by Quantrimang.com"""
    if n == 1: 
       return 1 
    else: 
        return (n * giaithua(n-1))
num = 5
num1 = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", num, "là", giaithua(num)) 
print("Giai thừa của", num1, "là", giaithua(num1)) 
