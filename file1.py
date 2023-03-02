# #login
akun={"username" : ["admin"],
      "password" : ["admin"]
      }

while True:
  username = input("masukkan username :")
  password = input("masukkan password :")

  #panjang data
  pdata = len(akun.get("username"))

  try:
    cariin = akun.get("username").index(username)
    if username == akun.get("username")[cariin] and password == akun.get("password")[cariin]:
      print("login berhasil")
      def menu():
          print("""
 ===== SELAMAT DATANG DI KONVERSI MATA UANG =====
DAFTAR PILIHAN KONVERSI MATA UANG
Contoh : A1 untuk konversi Kurs Jual USD ke GBP
  X. Kurs Jual
     a. USD to IDR
     b. GBP to IDR

  Y. Kurs Beli
     a. USD to IDR
     b. GBP to IDR
 
  Z. Keluar
          """)
      menu()
      while True :
        opr = input("masukan pilihan anda :")
        if opr == "Xa":
           print("USD to IDR")
           n = int(input("Masukkan Nominal USD Anda : US$ "))
           h = n * 19000
           print(h)
        elif opr == "Xb":
           print("USD to IDR")
           n = int(input("Masukkan Nominal USD Anda : US$ "))
           h = n * 14000
           print(h)
        elif opr == "Ya":
           print("GBP to IDR")
           n = int(input("Masukkan Nominal USD Anda : US$ "))
           h = n * 19500
           print(h)
        elif opr == "Yb":
           print("GBP to IDR")
           n = int(input("Masukkan Nominal USD Anda : US$ "))
           h = n * 14300
           print(h)
        elif opr == "Z" :
            print ("""
            PROGRAM SELESAI
            TERIMA KASIH
            """)
        else :
            break
      else : 
            print("login gagal, password anda salah")
  except ValueError:
    print("maaf username tidak tersedia")
    