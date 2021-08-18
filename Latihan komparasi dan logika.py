# ++++3------10++++++
user = float(input("Masukan nilai kurang dari 3\natau\nlebih dari 10: "))

# Gabungan dari 
# ++++3------10++++++

# +++++3------
kurang_dari = user < 3
print("status angka: ",kurang_dari)

# ------10+++++++
lebih_dari = user > 10
print("status angka: ",lebih_dari)

# Gabungan nya
gabungan = kurang_dari or lebih_dari
print("status angka yang anda masukan adalah: ",gabungan)

# Irisan
# --------3+++++++++++10--------

user = float(input("Masukan nilai lebih dari 3\natau\nkurang dari 10: "))

#---------3+++++++++
lebih_dari = user > 3
print("status angka: ",lebih_dari)

# +++++++10---------
kurang_dari = user < 10
print("status angka: ",kurang_dari)

# Irisan nya
irisan = kurang_dari and lebih_dari
print("status angka yang anda masukan adalah: ",irisan)



print("\nTUGAS KELAS TERBUKA NOMOR 1")

x = float(input("Masukan angka: "))

hasil = 0 < x < 5 or 8 < x < 11
print(0,'<',x,'<',5,'OR',8,'<',x,'<',11,'\nstatus angka: ',hasil)




print("\nTUGAS KELAS TERBUKA NOMOR 2")

x = float(input("Masukan angka: "))

hasil = 0 > x and 5 < x and x > 8 and x < 11
print(0,'>',x,'AND',5,'<',x,'AND',x,'>',8,'AND',x,'<',11,'\nstatus angka: ',hasil)

