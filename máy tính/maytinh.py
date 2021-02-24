#biến căn lề       
can_le1 = '                        + {:-<6} + {:-^15} + {:->10} +'.format('', '', '')#dòng đầu bảng
can_le2 = '                        |{:>25}              |'.format('chon phep tinh')#chữ chọn phép tính
can_le3 = '                        + {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
can_le4 = '                        |      | {:<3} | {:^3} | {:>3} | {:>3} |     |'.format('cong', 'tru', 'nhan','chia') #dấu phép tính
can_le5 = '                        | {:^36}  |'.format('')  #gạch 2 bên
can_le6 = '                        | {:^36}  |'.format('')#gạch 2 bên
can_le7 = '                        + {:-<6} + {:-^15} + {:->10} +'.format('', '', '')#dòng cuối bảng
can_le1 = '                        + {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
#in biến căn lề
print (can_le1)
print (can_le2)
print (can_le3)
print (can_le4)
print (can_le5)
print (can_le6)
print (can_le7)

#end căn lề 
lua_chon = input("lua chon:")
chon_lua = lua_chon
if chon_lua == "1":
	a = input("so a:")
	b = input("so b:")
	print (int(a)+int(b))
elif chon_lua == "2":
	a = input("so a:")
	b = input("so b:")
	print (int(a)-int(b))
elif chon_lua == "3":
	a = input("so a:")
	b = input("so b:")
	print (int(a)*int(b))
elif chon_lua == "4":
	a = input("so a:")
	b = input("so b:")
	print (int(a)/int(b))
else:
	loi = "nhap loi"
	print (loi)
		