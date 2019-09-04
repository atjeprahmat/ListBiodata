#ATJEP RAHMAT

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

umur = 2019-tahun_lahir
umur_thn_depan = umur + 1
siswa_thn_depan = jumlah_siswa * 2
print("*"*40)
print("Nama saya", nama,".","Saya Lahir di ", tempat_lahir,".","Saya tinggal di ",kota_asal,".","dan Mengajar di", sekolah_ngajar,".","Saya memiliki siswa ", jumlah_siswa,"orang.", "Tahun depan, saya akan berusia", umur_thn_depan, "tahun", "dan akan memiliki siswa sebanyak", siswa_thn_depan, "orang")
print("*"*40)
