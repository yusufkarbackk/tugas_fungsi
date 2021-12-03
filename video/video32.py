x = 10 #variabel global

def ambil_global():
    return x #mengambil variabel global

def x_local():
    x = 5 #variabel local scopenya x_local()
    return x

print(f"1. variabel global: {x}")
print(f"2. variabel ambil_global: {ambil_global()}")
print(f"3. variabel x_local: {x_local()}")


