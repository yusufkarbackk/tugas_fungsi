def kuadrat(x):
    hasil = x * x
    return hasil

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil


angka = input('masukan angka yabng ingin di kuadratkan: ')

hasil_kuadrat = kuadrat(int(angka))
print(hasil_kuadrat)

angka1 = input('masukan angka pertama: ')
angka2 = input('masukan angka pertama: ')

hasil_tambah = tambah(int(angka1), int(angka2))
print(hasil_tambah)
