# PARAMETER
def my_function(nama):
    print(nama)

# DEFAULT PARAMETER


def my_negara(negara="indonesia"):
    print(negara)


# MULTIPLE PARAMETER
def data_diri(nama, umur):
    print(nama, umur)


# RETURN VALUE
'''
return menyimpan hasil agar tidak langsung di gunakan
'''


def tambah(angka1, angka2):
    return angka1 + angka2


# PANGGIL FUNGSI
my_function('ucup')

print()
my_negara()
my_negara('jerman')

print()
data_diri()
data_diri('ucup', 19)

hasil = tambah(10, 2)
print(hasil)
