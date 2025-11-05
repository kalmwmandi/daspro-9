# Januar Haykal Firdaus
# 2508627
# 1A

# latihan2.py
def login():
    password_sistem = "Latihan"  
    kesempatan = 3

    username = input("masukkan username: ")

    if username == "Daspro2023":
        while kesempatan > 0:
            password = input("masukkan password: ")
            if password == password_sistem:
                print("login berhasil, selamat datang!!")
                return
            else:
                kesempatan -= 1
                print("password salah, sisa kesempatan:", kesempatan)
        print("anda telah 3 kali salah, akses ditolak")
    else:
        print("maaf, username tidak terdaftar")

login()