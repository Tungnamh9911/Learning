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