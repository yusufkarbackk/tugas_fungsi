def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas


def hitung_keliling(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling


def tampilan_luas(panjang, lebar):
    hasil_luas = hitung_luas(panjang, lebar)
    print("luasnya adalah ", str(hasil_luas))


def tampilan_keliling(panjang, lebar):
    hasil_keliling = hitung_keliling(panjang, lebar)
    print("keliling adalah ", str(hasil_keliling))


panjang = int(input('masukan panjang: '))
lebar = int(input('masukan lebar: '))

tampilan_luas(panjang, lebar)
tampilan_keliling(panjang, lebar)
