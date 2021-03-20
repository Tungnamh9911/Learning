bài 1
# khai báo class 
class <tên lớp>:
	pass#<hàm giữ chỗ>

#ví dụ

class adu:
	pass

advip = adu()

advip.duma = "adu"

print (advip.duma)

# ví dụ 2

class Sieunhan:
	def __init__(self,par_kiem,par_mau):
		self.kiem = par_kiem
		self.mau = par_mau
	pass

sieunhan1 = Sieunhan("20cm","trắng")

print ("sieunhan1 co kiem dai: ", sieunhan1.kiem)

#ví dụ tự làm  

class nguoidaden:
	def __init__(self,par_mauda,par_canhsat):
		self.mauda = par_mauda
		self.canhsat = par_canhsat
	pass

sieunhan1 = nguoidaden("màu đen","chĩa súng")

print ("anh ta có da", sieunhan1.mauda)
print("cảnh sát",sieunhan1.canhsat)

#ví dụ 

class sieunhan:
	def __init__(self,par_ten,par_kiem,par_mau):
		self.ten = par_ten
		self.kiem = par_kiem
		self.mau = par_mau

	def xinchao(self):
		return "thang lon cut,ta la:"  + self.ten

sieunhan1 = sieunhan("tung","20cm","trắng")
print (sieunhan1.xinchao())
#bài 2

# ví dụ 1
class sieunhan:
	stt = 1
	sothutu = 1
	sucmanh = 50

	def __init__(self,par_ten,par_vukhi):

		self.ten = par_ten
		self.vukhi = par_vukhi

		self.stt = sieunhan.sothutu

		sieunhan.sothutu += 1

sieunhanA = sieunhan("do","kiem")
sieunhanB = sieunhan ("vang","sung")
print (sieunhanA.stt)
print (sieunhanB.stt)
print ("...............")
print (sieunhanA.sothutu)
print (sieunhanB.sothutu)
# classmethod dùng để cập nhật một dữ liệu trong class
@classmethod
#@staticmethod ko cần self khi dùng def....(self) -> def ... ()

#tạo lớp kế thừa

class Sieunhan:
	pass

class Sieunhangao(Sieunhan):
	pass

sieunhan1 = Sieunhangao()
print(sieunhan1)

#kế thừa cả construter