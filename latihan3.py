# Januar Haykal Firdaus
# 2508627
# 1A

# latihan3.py
def hitung_selisih_waktu():
    print("input waktu mulai:")
    jam_mulai = int(input("jam: "))
    menit_mulai = int(input("menit: "))
    detik_mulai = int(input("detik: "))

    print("\ninput waktu selesai:")
    jam_selesai = int(input("jam: "))
    menit_selesai = int(input("menit: "))
    detik_selesai = int(input("detik: "))

    total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    selisih = total_selesai - total_mulai

    jam = selisih // 3600
    selisih %= 3600
    menit = selisih // 60
    detik = selisih % 60

    print(f"\nselisih waktunya adalah: {jam} jam - {menit} menit - {detik} detik")

hitung_selisih_waktu()