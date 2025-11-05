#Januar Haykal Firdaus
#2508627
#1A

# latihan1.py
def fibonacci(n):
    a, b = 0, 1
    hasil = []
    for i in range(n):
        hasil.append(a)
        a, b = b, a + b
    return hasil

jumlah = int(input("masukkan jumlah bilangan fibonacci: "))
print("deret fibonacci:", fibonacci(jumlah))

def volume_tabung(jari_jari, tinggi):
    phi = 3.14
    return phi * jari_jari ** 2 * tinggi

r = float(input("\nmasukkan jari-jari tabung: "))
t = float(input("masukkan tinggi tabung: "))

volume = volume_tabung(r, t)
print("volume tabung: {:.2f}".format(volume))

def hitung_total_rata(*angka):
    total = sum(angka)
    rata = total / len(angka)
    return total, rata

input_angka = input("\nmasukkan angka yg dipisah koma: ")
angka_list = [int(x.strip()) for x in input_angka.split(",")]
total, rata = hitung_total_rata(*angka_list)
print("total:", total)
print(f"rata-rata: {rata:.2f}")