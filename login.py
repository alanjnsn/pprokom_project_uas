# import mysql.connector

# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Satbang1__',
#     database = 'database_toko'
# )

# if db.is_connected():
#     print('terhubung')
# cursor = db.cursor()

class user ():
    global username
    username = []
    global password
    password = []
    user = 0
    def __init__(self,store,sandi) -> None:
        self.store = store
        self.sandi = sandi
        user.user += 1
        username.append(self.store)
        password.append(self.sandi)

toko_A = user('toko_A','tokoAjaya123')
toko_B = user('toko_B','tokoBjaya123')
toko_C = user('toko_C','tokoCjaya123')

class product ():
    global list_merk
    list_merk = []
    global list_seri
    list_seri = []
    global list_stok
    list_stok = []
    def __init__(self,merk,seri,stok) -> None:
        self.merk = merk
        self.seri = seri
        self.stok = stok
        if merk not in list_merk:
            list_merk.append(self.merk)
            list_seri.append(self.seri)
            list_stok.append(self.stok)
        else:
            if seri in list_seri:
                indeks = list_seri.index(self.seri)
                list_stok[indeks] += self.stok
            else:
                list_merk.append(self.merk)
                list_seri.append(self.seri)
                list_stok.append(self.stok)
#sign up page
def sign_up ():
    print('sign up'.center(36,"="))
    nama_toko = input('username (tanpa spasi): ')
    sandi = input('password (minimal 8 karakter disertai kombinasi angka dan huruf): ')
    print()
    print('sign up berhasil'.center(36," "))
    toko = user(nama_toko,sandi)
    print()
    landing_page()

#login page
def login ():
    print('login'.center(36,"="))
    nama_toko = input('username: ')
    sandi = input('password: ')
    if nama_toko in username and sandi in password:
        print('login berhasil'.center(36," "))
        show_menu()
        
    else:
        for i in range (3):
            print('username atau password salah')
            nama_toko = input('username: ')
            sandi = input('password: ')
            if nama_toko in username and sandi in password:
                print('login berhasil'.center(36," "))
                break
        else:
            print('mohon maaf anda telah salah memasukkan username atau password sebanyak 3 kali')
            exit ()

#landing page
def landing_page ():
    print("="*36)
    print('|','manajemen gudang kompor listrik'.center(32," "),'|')
    print('|','silahkan login atau sign up'.center(32," "),'|')
    print("="*36)
    print('[1] login\n[2] sign up')
    pilihan = input('pilih menu: ')
    if pilihan == '1' or pilihan == 'login':
        print()
        login()
    elif pilihan == '2' or pilihan == 'sign in':
        print()
        sign_up()
    else:
        print()
        print('menu tidak tersedia')
        landing_page()

#add product
def add_product ():
    print('add product'.center(36,"="))
    print("tuntaskan satu jenis merk terlebih dahulu".center(36," "))
    merk = input('merk: ')
    seri = input('seri: ')
    stok = int(input('stok: '))
    produk = product(merk,seri,stok)
    print()
    desicion = input('apakah anda ingin menambah produk lagi? (y/n):')
    if desicion.lower() == 'y':
        add_product()
    else:
        show_menu()


def edit():
    print('hapus'.center(36,"="))
    print("pilih produk yang ingin diedit".center(36," "))
    merk= input('merk: ')
    seri= input('seri: ')
    if merk in list_merk and seri in list_seri:
        merk_baru= input('merk baru: ')
        seri_baru= input('seri baru: ')
        stok_baru= int(input('stok baru: '))
        list_merk[list_merk.index(merk)]= merk_baru
        list_stok[list_seri.index(seri)]= stok_baru
        list_seri[list_seri.index(seri)]= seri_baru
    else:
        print('tidak ditemukan merk yang sesuai')
        print()
        show_menu()


def hapus():
    print('hapus'.center(36,"="))
    print("pilih produk yang ingin dihapus".center(36," "))
    merk = input('merk: ')
    seri = input('seri: ')
    stok = int(input('stok: '))
    if merk in list_merk and seri in list_seri:
        list_merk.remove(merk)
        list_seri.remove(seri)
        list_stok.remove(stok)
    else:
        print('tidak ditemukan produk yang sesuai')
        print()
        show_menu()


def list_produk():
    print()
    print('produk berhasil ditambahkan')
    print()
    print('list produk'.center(36,"="))
    print('merk'.ljust(10," "),'seri'.ljust(10," "),'stok'.ljust(10," "))
    all_product = []
    for i in range (len(list_merk)):
        x = f'{list_merk[i].ljust(10," ")} {list_seri[i].ljust(10," ")} {list_stok[i]}'
        print(x)
        all_product.append(x)
    print()
    print("1. A-Z\n2. Z-A\n3. back")
    urutan = input('urutkan berdasarkan(pilih nomer):')
    if urutan == '1':
        print('merk'.ljust(10," "),'seri'.ljust(10," "),'stok'.ljust(10," "))
        all_product.sort()
        for i in all_product:
            print(i)
    elif urutan == '2':
        print('merk'.ljust(10," "),'seri'.ljust(10," "),'stok'.ljust(10," "))
        all_product.sort(reverse=True)
        for i in all_product:
            print(i)
    else:
        show_menu()
    show_menu()

def show_menu ():
    print("="*36)
    print ('|',"PILIHAN".center(32," "),"|")
    print("="*36)
    for i in range (1,6):
        if i == 1:
            print(f"|[{i}] add product".ljust(34," "),'|')
        elif i == 2:
            print(f'|[{i}] edit'.ljust(34," "),'|')
        elif i == 3:
            print(f'|[{i}] hapus'.ljust(34," "), '|')
        elif i == 4:
            print(f'|[{i}] list produk'.ljust(34," "), '|')
        else:
            print(f'|[{i}] exit'.ljust(34," "), '|')
    print("="*36)
    choice = int(input('pilih nomer opsi:'))
    print()
    if choice == 1: 
        add_product()
    elif choice == 2:
        edit()
    elif choice == 3:
        hapus()
    elif choice == 4:
        list_produk()
    elif choice == 5:
        exit()
    else:
        print('menu tidak tersedia')
        show_menu()
    if __name__ == '__main__':
        show_menu()

landing_page()