# Buatlah sebuah file python interaktif (.py) berisi sebuah function yang dapat menentukan suatu input dari user tergolong alamat email yang valid 
# atau tidak. Adapun kriteria alamat email yang valid adalah sebagai berikut:

# Memiliki format: namaUser@namaHosting.ekstensi
# namaUser hanya boleh terdiri atas huruf, angka, dot ('.') dan underscore ('_').
# namaHosting hanya boleh terdiri atas huruf dan angka.
# ekstensi hanya boleh terdiri atas huruf, dengan maksimum 5 karakter.
# Contoh:

# ✅ Alamat email valid:

# andre@gmail.com
# joni12_win@purwadhika.com
# andi789@city.id
# steve_roger70@avenger01.space
# ❌ Alamat email tidak valid:

# andre254@gmail
# andre$%^&@gmail.com
# John85_cap@yah$%.com
# andre@@gmail.com
# tony_stark@avengers.wakanda
# Saat file dieksekusi, user diminta memasukkan alamat email, kemudian akan muncul hasil yang menyatakan email user valid atau tidak. 
# Contoh hasil yang diharapkan:

# Input email : hary_963@gmail.com
# Hasil : Alamat Email Yang Anda Masukkan Valid!!
# Untuk Email yang tidak valid, Notifikasi yang keluar sesuai dengan error nya. Contoh :

# Input Email : andre254@gmail
# Hasil : Email Tidak valid!! Format Email Salah!!

# Input Email : andre$%^&@gmail.com
# Hasil : Email Tidak Valid!! Format User Name Salah!!

# Input Email : John85_cap@yah$%.com
# Hasil : Email Tidak Valid!! Format Hosting Salah!!

# Input Email : tony_stark@avengers.wakanda
# Hasil : Email Tidak Valid!! Format Ekstensi Salah!!


import string # untuk meng immport string
def email(namaUser, namaHosting, ekstensi): #function email dengan parameter namaUser,namaHosting,ekstensi
    user = string.ascii_letters + string.digits + string.punctuation # untuk mengimpor karakter yang dibutuhkan
    hosting = string.ascii_letters + string.digits # untuk mengimpor karakter yang dibutuhkan
    ekstend = string.ascii_letters # untuk mengimpor karakter yang dibutuhkan

    for u in namaUser: #membuat variabel baru yaitu u 
        if u in user: # untuk memastikan jika karakter yg diinginkan 
            continue # jika ada maka lanjut
        else:
            return('Hasil : Email Tidak Valid!! Format User Name Salah!!') #jika tidak ada maka akan keluar peringatan seperti ini
            break # untuk memastikan agar tidak tidak melakukan perulangan
    for h in namaHosting: #membuat variabel baru yaitu h 
        if h in hosting: # untuk memastikan jika karakter yg diinginkan
            continue
        else:
            return('Email Tidak Valid!! Format Hosting Salah!!') #jika tidak ada maka akan keluar peringatan seperti ini
            break # untuk memastikan agar tidak melakukan perulangan
    for e in ekstensi:
        if len(ekstensi) <= 5: # jika jumlah kata di ekstensi kurang atau sama dengan 5 maka
            print('Email yang anda masukkan Valid: ') # keluar output yang seperti ini
            return(f'{namaUser}{namaHosting}{ekstensi}') # dan output ini setelah digabung
        else:
            print('Email Tidak Valid!! Format Ekstensi Salah!!') #jika tidak ada maka akan keluar peringatan seperti ini
            break # untuk memastikan agar tidak tidak melakukan perulangan
    
        

print(email('endi99@','gmail','.com'))
print(email('èndi99@','gmail','.com'))
print(email('endi99@','gmail-~`%$','.com'))
print(email('endi99@','gmail','.commmmmmm'))

