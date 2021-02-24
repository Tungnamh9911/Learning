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
