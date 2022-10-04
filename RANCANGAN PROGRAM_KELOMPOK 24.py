#Input = Nama Pengirim, Nama Penerima, Alamat Tujuan Paket, Kota Asal, Kota Tujuan, Berat Paket
#Output = Detail Pengiriman, Total Tagihan Yang Harus Dibayar, Nomor Resi, Total Kembalian (Bila ada)

from random import randint
import pandas as pd

Jawa = [{"Jakarta Pusat" : '001'}, {"Jakarta Timur" : '002'}, 
        {"Jakarta Barat" : '003'}, {'Jakarta Utara' : '004'}, 
        {'Jakarta Selatan' : '005'}, {'Bandung' : '006'}, 
        {'Yogyakarta' : '007'}, {'Semarang' : '008'}, 
        {'Solo': '009'}, {"Surabaya":'010'},{"Malang":"011"}]
Bali = [{'Denpasar':'012'}]
Sumatera = [{'Medan' : '013'}, {'Palembang' : '014'}, 
            {'Bandar Lampung' : '015'},{'Padang' : '016'}]
Kalimantan = [{'Samarinda' : '017'} ,{'Balikpapan' : '018'},
              {'Banjarmasin' : '019'},{'Pontianak' : '020'}]
Sulawesi = [{'Makassar' : "021"},{'Manado' : '022'},{'Palu' : '023'}]
Papua = [{'Jayapura' : '024'},{'Sorong' : '025'}]

Pulau = [Jawa , Bali, Sumatera, Kalimantan, Sulawesi, Papua]

Jenis_pengiriman = [
           {
               "Jenis":"Kilat",
               "Kode":"11",
               "Harga Sama Pulau" : 15000,
               "Harga Beda Pulau": 20000,
               "Deskripsi" : "1 Hari pengiriman"
           },
           {
               "Jenis" : "Reguler",
               "Kode": "12",
               "Harga Sama Pulau" : 9000,
               "Harga Beda Pulau": 12000,
               "Deskripsi" : "3-5 Hari pengiriman"
           },
           {
               "Jenis" : "Murah Meriah",
               "Kode" : "13",
               "Harga Sama Pulau" : 6000,
               "Harga Beda Pulau": 9000,
               "Deskripsi" : "7 Hari pengiriman"
           }]
Detailkirim = {}

# Login
print(50*"=")
coba_login = 3
while coba_login >= 1:
    userpass = {'a':'1'}
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if username in userpass and password == userpass[username]:
        print('Login Diterima')
        break
    else:
        coba_login -= 1
        print("Login Ditolak")
        if coba_login == 0:
            print("Mohon maaf anda sudah melakukan percobaan login 3 kali")
            quit() 

#Halaman Awal
print(50*"=")
print("Selamat datang",username.upper(),"pada ICL EXPRESS")

#Tampilkan Daftar Pulau
print(50*"=")
print("Berikut Pulau Jangkauan ICL Express",'\n1. Pulau Jawa\n2. Pulau Bali\n3. Pulau Sumatera\n4. Pulau Kalimantan\n5. Pulau Sulawesi\n6. Pulau Papua')
cek1 = True
while cek1 == True :
    try:
        pulauasal = int(input("Pilih Pulau Asal: "))
        pulautujuan = int(input("Pilih Pulau Tujuan: "))
    except:
        print ("Pilihan tidak tersedia")
        continue
    if pulauasal not in range (1, len(Pulau)+1) or pulautujuan not in range (1, len(Pulau)+1):
        print ("Pilihan tidak tersedia")
    else:
        cek1 = False
print(50*"=")
pulau_asal = Pulau[pulauasal-1] 
pulau_tujuan = Pulau[pulautujuan-1] 
kotaasal = []
kotatujuan = []

if pulau_asal == pulau_tujuan:
    print("Menampilkan List Kota")
    for n, item in enumerate (pulau_asal, start=1): 
        for key, value in item.items():
            kotaasal.append(key)
    tabel1 = pd.DataFrame({"Nama Kota":kotaasal})
    tabel1.index+=1
    pd.set_option('display.colheader_justify','center')
    print (tabel1)
else:
    print("Menampilkan List Kota di Pulau Asal")
    for n, item in enumerate (pulau_asal, start=1): 
        for key, value in item.items():
            kotaasal.append(key)
    tabel2 = pd.DataFrame({"Nama Kota":kotaasal})
    pd.set_option('display.colheader_justify','center')
    tabel2.index+=1
    print (tabel2) 
    print("\nMenampilkan List Kota di Pulau Tujuan")
    for n,item in enumerate (pulau_tujuan, start=1):
        for key, value in item.items():
            kotatujuan.append(key)
    tabel3 = pd.DataFrame({"Nama Kota":kotatujuan})
    pd.set_option('display.colheader_justify','center')
    tabel3.index+=1
    print (tabel3)

#Masukkan Detail Pengirim
print(50*"=")
cek = 0 
while cek == 0:
    nama_pengirim = input('Masukkan nama pengirim: ')
    cek2 = True
    while cek2 == True :
        try:
            origin = int(input("Masukkan Kode Kota Asal: "))
        except:
            print ("Pilihan tidak tersedia")
            continue
        if origin not in range (1, len(pulau_asal)+1) :
            print ("Pilihan tidak tersedia")
        else:
            cek2 = False
    cek3 = True
    while cek3 == True:
        try:
            berat = float(input("Masukkan Berat Paket: "))
        except:
            print ("Input yang dimasukkan salah")
            continue
        if berat == 0 :
            print ("Input yang dimasukkan salah")
        else:
            cek3 = False
    nama_penerima = input('Masukkan nama penerima: ')
   
    cek4 = True
    while cek4 == True :
        try:
            to = int(input("Masukkan Kode Kota Tujuan: "))
        except:
            print ("Pilihan tidak tersedia")
            continue
        if to not in range (1, len(pulau_tujuan)+1) :
            print ("Pilihan tidak tersedia")
        else:
            cek4 = False
    alamat = input("Masukkan alamat lengkap penerima paket: ")
    Detailkirim.update(pulau_tujuan[to-1])
    Detailkirim.update(pulau_asal[origin-1])

#Menampilkan Pilihan Jenis Pengiriman
    print(50*"=")
    tabel4 = []
    tabel5 = []
    tabel6 = []
    if pulau_asal == pulau_tujuan:
        print("Silahkan memilih jenis pengiriman dalam pulau\n")
    else:
        print("Silahkan memilih jenis pengiriman antar pulau\n")
    for n in range(len(Jenis_pengiriman)):
        pengiriman = Jenis_pengiriman[n]['Jenis']
        if pulau_asal == pulau_tujuan:
            harga = Jenis_pengiriman[n]['Harga Sama Pulau']
        else:
            harga = Jenis_pengiriman[n]['Harga Beda Pulau'] 
        keterangan = Jenis_pengiriman[n]['Deskripsi']
        tabel4.append(pengiriman)
        tabel5.append(harga)
        tabel6.append(keterangan)
        pd.set_option('display.colheader_justify','center')
    print (pd.DataFrame({"Jenis pengiriman" : tabel4, "Harga" : tabel5, "Keterangan" : tabel6}, ["1","2","3"]))
#Memilih Pilihan Jenis Pengiriman
    cek5 = True
    while cek5 == True:
        try:
            pilihan = int(input('Masukkan kode jenis pengiriman yang dipilih : ')) 
        except:
            print ("Pilihan tidak tersedia")
            continue
        if pilihan >3 or pilihan <1:
            print ("Pilihan tidak tersedia")
        else:
            cek5 = False
    jenisterpilih = Jenis_pengiriman[pilihan-1]['Jenis']
    keterangan = Jenis_pengiriman[pilihan-1]['Deskripsi']
    Detailkirim.update({"Kode" : Jenis_pengiriman[pilihan-1]['Kode']})
    if pulau_asal == pulau_tujuan:
        harga = Jenis_pengiriman[pilihan-1]['Harga Sama Pulau']
    else:
        harga = Jenis_pengiriman[pilihan-1]['Harga Beda Pulau']
    print('Anda akan memilih jenis pengiriman', jenisterpilih, "dengan harga sebesar", harga, "per kg"
        "\nPerkiraan waktu pengiriman:",keterangan,"\n")

#Memproses Detail Pengiriman
    biaya = harga * berat
    def detailkirim(): 
        print ("Nama Pengirim\t:", nama_pengirim, 
            "\nNama Penerima\t:", nama_penerima)  
        for key,value in pulau_asal[origin-1].items():
                print('Kota Asal\t:', key)
        for key,value in pulau_tujuan[to-1].items():
                print('Kota Tujuan\t:', key)
        print('Alamat Tujuan\t:',alamat,
            '\nBerat Paket\t:', berat,"kg", 
            "\nBiaya Total\t:", "Rp.",int(biaya))
        return
    print(50*"=")
    detailkirim()
    print(50*"=")
    cek6 = True
    while cek6 == True:
        try:
            cek = input("Apakah detail pengiriman sudah benar?(ya/tidak):").lower()
        except:
            print ("input tidak tersedia")
        if cek == 'ya':
            cek6 = False
            cek = 1
            break
        elif cek == "tidak":
            cek6 = False
            cek = 0
        else:
            print ("Input tidak tersedia")
            cek = 0

#Memproses Pembayaran
dibayar = 0
while dibayar == 0:
    cek7 = True
    while cek7 == True:
        try:
            dibayar = int(input('Masukkan nominal uang yang dibayar:'))
        except:
            print ("Pembayaran tidak sesuai")
        else:
            cek7 = False
    if dibayar == biaya:
        total_kembalian = 0
    elif dibayar > biaya:
        total_kembalian = dibayar - int(biaya)
    else:
        dibayar = 0 
print(50*"=")


#Memproses Nomor Resi
res = []
for key,value in Detailkirim.items():
    res.append(str(value))
if len(res) == 2:
    urut = res[1],res[0],res[0]
else:
    urut = res[2],res[0],res[1]
Resi = ("".join(urut),str(randint(1000,9999)))

#Menampilkan Struk Pengiriman
print("\n")
print(50*"=")
print('STRUK DETAIL PENGIRIMAN ICL EXPRESS\n')
print ("Nomor Resi\t:","".join(Resi))
detailkirim()
print("Total Kembalian\t:","Rp.",total_kembalian)
print(50*"=")

#Quit
print("Terima Kasih Telah Mempercayai ICL EXPRESS")
quit()