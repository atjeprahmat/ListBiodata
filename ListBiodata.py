import datetime

# Contribution by : Evenus
# Datetime : Thursday 05 September 2019 , 15:05.p.m.
'''  
	ADD :
		- import datetime
		- retrieve data from (data_diri)
'''


print("Biodata Guru oleh @atjeprahmat")
print("*"*40)

data_diri=[]
nama = input("Nama : ")
tempat_lahir = (input("Tempat Lahir : "))
tahun_lahir = int(input("Tahun Lahir : "))
kota_asal = input("Kota Asal : ")
sekolah_ngajar = input("Sekolah Tempat Mengajar : ")
jumlah_siswa = int(input("Jumlah Siswa : "))

print("*"*40)
data_diri.extend([nama, tempat_lahir, tahun_lahir, kota_asal, sekolah_ngajar, jumlah_siswa])
print("List Awal : ", data_diri)

year = datetime.date.today().year
umur = year-tahun_lahir
umur_thn_depan = umur + 1
siswa_thn_depan = jumlah_siswa * 2
print("*"*40)
print("Nama saya", data_diri[0],"."
	,"Saya Lahir di ", data_diri[1]
	,".","Saya tinggal di ",data_diri[2]
	,".","dan Mengajar di", data_diri[3]
	,".","Saya memiliki siswa ", data_diri[4]
	,"orang.", "Tahun depan, saya akan berusia", umur_thn_depan
	, "tahun", "dan akan memiliki siswa sebanyak", siswa_thn_depan, "orang")
print("*"*40)