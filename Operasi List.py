## ---- OPERASI LIST ---- ##
# index: fungsi ini digunakan untuk mengembalikan indeks kemunculan pertama yang nilainya disebutkan
# append: digunakan untuk menambahkan nilai di akhir daftar.
# prepend: digunakan untuk menambahkan nilai di awal daftar.
# insert: digunakan untuk menyisipkan suatu nilai pada posisi tertentu
# remove: fungsi ini digunakan untuk menghapus nilai tertentu dari array.
# pop: fungsi ini digunakan untuk menghapus item pada posisi tertentu dalam daftar, dan mengembalikannya.
# count: digunakan untuk mengembalikan jumlah item dari nilai yang ditentukan
# sort: fungsi ini digunakan untuk mengurutkan item dari daftar secara Ascending
# reverse: fungsi ini digunakan untuk mengurutkan item dari daftar secara Descending
# Extend: fungsi ini digunakan untuk memperpanjang daftar dengan menambahkan semua item dalam daftar yang berbeda ke dalam array
# len: digunakan untuk mengembalikan nilai berupa jumlah item dalam daftar.

ganjil = [1,3,5,7,3,1,9,13]

print(ganjil)
print(ganjil.index(9))
ganjil.append(17)
print(ganjil)
ganjil.pop(8)
print(ganjil)
del ganjil[1]
print(ganjil)
print(f"Jumlah angka 1 dalam list adalah {ganjil.count(1)}")
ganjil.sort()
print(ganjil)
ganjil.reverse()
print(ganjil)
print(f"panjang list ini adalah {len(ganjil)}")

prima = [11, 13, 23]
ganjil.extend(prima)
print(ganjil)