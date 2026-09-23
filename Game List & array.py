import time

bahan_utama = ["gula", "tepung", "telur", "susu", "garam", "mentega"] # list data yang sudah disiapkan
skor = 0 # skor awal pemain

print("Selamat datang di game tebak bahan, kamu diberi kesempatan 3 kali, Jawab dengan benar!!")
time.sleep(2)

bahan_1 = input("\napa bahan pertama?? ").lower()
if bahan_1 in bahan_utama: # memastikan apakah data yang diinput sesuai dengan list
    skor += 1
    print("betul sekali!!", bahan_1, "ada di dalam list" )
    time.sleep(1)
    print("kamu mendapat 1 score")
    time.sleep(1)
else: # jika data yang diinput tidak sesuai dengan list
    print("salah, sayang sekali:(") 
    time.sleep(2)
    
bahan_2 = input("\napa bahan kedua?? ").lower()
if bahan_2 == bahan_1: # memastikan apakah data diinput ulang dengan data sebelumnya
    print("bahan itu sudah kamu tebak sebelumnya")
    time.sleep(0.5)
    print("skor belum nambah deh")
    time.sleep(1)
elif bahan_2 in bahan_utama: # memastikan apakah data diinput sesuai dengan list dan tidak diulang
    skor += 1
    print("betul sekali!!", bahan_2, "ada di dalam list" )
    time.sleep(1)
    print("kamu mendapat tambahan 1 score")
    time.sleep(1)
else: # jika data yang diinput tidak sesuai dengan lis
    print("salah, sayang sekali:(") 
    time.sleep(2)

bahan_3 = input("\napa bahan ketiga?? ").lower()
if bahan_3 == bahan_1 or bahan_3 == bahan_2: # memastikan apakah data diinput ulang dengan data sebelumnya
    print("bahan itu sudah kamu tebak sebelumnya")
    time.sleep(0.5)
    print("skor belum nambah deh")
    time.sleep(1)
elif bahan_3 in bahan_utama: # memastikan apakah data diinput sesuai dengan list dan tidak diulang
    skor += 1
    print("betul sekali!!", bahan_3, "ada di dalam list" )
    time.sleep(1)
    print("kamu mendapat tambahan 1 score")
    time.sleep(1)
else: # jika data yang diinput tidak sesuai dengan list
    print("salah, sayang sekali:(") 
    time.sleep(2)

print("\ngame over, skor akhir kamu adalah ", skor) # menampilkan jumlah skor pemain
print("\nbahan yang ada di list adalah ",bahan_utama) # menampilkan list data di awal