
loading_count = "%s"
loading = "loading..."
thongbao = "nhap ten:"
print(thongbao)
#nhập thư viện
import time
import os
#đặt biến nhập từ bàn phím
nhapten = input("")
ten = nhapten
#danh sách tên và mật khẩu gán theo
danh_sach_ten = ["Jotaro","Dio"]
mat_khau_acc = ['1','2']
#if else 1
if ten in danh_sach_ten: #kiểm tra giá trị có trong chuỗi không
	#if else 2	
	if ten == danh_sach_ten[0]:
		note_file = danh_sach_ten[0]
		file_note = open('dadangnhap.txt', mode = 'w')
		data_note = file_note.write("ten dang nhap: " + note_file)
		file_note.close()		
		#mật khẩu đúng gán cho tên Jotaro
		correct_pass = mat_khau_acc[0]
		#gán biến nhập từ bàn phím
		mat_khau = input("nhapmatkhau:")
		mat_khau_nhapdung = [mat_khau,correct_pass]
		#if else 3 #đặt if else đăng nhập
		if mat_khau_nhapdung[0] == mat_khau_nhapdung[1]:
			note_file = mat_khau_nhapdung[1]
			file_note = open('dadangnhap.txt',mode ='a+')
			data_note = file_note.write("\nmat khau dang nhap: "+ note_file)
			file_note.close()		
			time.sleep(2)
			#chuyển đổi thời gian load
			print(loading)
			print (loading_count %("1.kiểm tra đăng nhập"))
			time.sleep(2)
			print (loading_count %("2.kiểm tra dữ liệu"))
			time.sleep(2)
			print (loading_count %("3.trích xuất dữ liệu"))
			time.sleep(2)
			print (loading_count %("4.hoàn thành nốt công đoạn"))
			time.sleep(2)

			time.sleep(5) #delay 5 sec
			print("cho phép truy cập")
			time.sleep(3)
			print("stand: Star platinium")
		else:
			print("từ chối truy cập")
		#end if else 3
	elif ten == danh_sach_ten[1]:
		note_file = danh_sach_ten[1]
		file_note = open('dadangnhap.txt', mode = 'w')
		data_note = file_note.write("ten dang nhap: " + note_file)
		file_note.close()
		#mật khẩu đúng cho tên Dio
		correct_pass = mat_khau_acc[1]
		#gán biến nhập từ bàn phím
		mat_khau = input('nhapmatkhau: ')
		mat_khau_nhapdung = [mat_khau,correct_pass]
		#if else 4 # if else đăng nhập
		if mat_khau_nhapdung[0] == mat_khau_nhapdung[1]:
			note_file1 = mat_khau_nhapdung[1]
			file_note = open('dadangnhap.txt',mode ='a+')
			data_note = file_note.write("\nmat khau dang nhap: "+ note_file1)
			file_note.close()
			time.sleep(2)
			#chuyển đổi thời gian load
			print(loading)
			time.sleep(2)
			print (loading_count %("1.kiểm tra đăng nhập"))
			time.sleep(2)
			print (loading_count %("2.kiểm tra dữ liệu"))
			time.sleep(2)
			print (loading_count %("3.trích xuất dữ liệu"))
			time.sleep(2)
			print (loading_count %("4.hoàn thành nốt công đoạn"))
			time.sleep(5) #delay 5 sec
			print("cho phép truy cập")
			time.sleep(3)
			print("stand: The world")
		else:
			print("từ chối truy cập")
		#end if else 4
	else:
		print(aloalo)
	#end if else2 
else:
	print("không tìm thấy giá trị trong hệ thống")
	#end if else 1
#else if 5