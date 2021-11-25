import string

class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.__user_name = user_name
        self.__tipe = tipe

    def get_name(self) : 
        return self.__user_name

    def get_tipe(self) : 
        return self.__tipe

    def __str__(self):
        return self.__user_name

class Seller(User) : 
    def __init__(self, user_name):
        """
        Constructor untuk class Seller
        """
        super().__init__(user_name, "SELLER")
        self.__pemasukan = 0
        self.list_barang_jual = []

    def get_pemasukan(self) : 
        return self.__pemasukan

    def set_pemasukan(self, pemasukan) : 
        self.__pemasukan = pemasukan

    def tambah_product(self, nama, harga, stock) :
        if get_product(nama) != None:
            print("Produk sudah pernah terdaftar.")
        else:
            curr_product = Product(nama,harga,stock,self)
            self.list_barang_jual.append(curr_product)
            self.list_barang_jual = sorted(self.list_barang_jual,key=lambda x: str(x))
            list_product.append(curr_product)

    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        for product in self.list_barang_jual : 
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{product.nama:<16}|{product.harga:<11}|{product.stock:<7}")
            pass
        print("-------------------------------------\n")

    def menu(self) : 
        print()
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")        
        while True:
            print()
            print(f"Pemasukan anda {self.get_pemasukan()},")
            menu_select = input("Apa yang ingin anda lakukan? ")
            if menu_select == "1":
                product_info = input("Masukkan data produk : ").split()
                self.tambah_product(product_info[0],product_info[1],product_info[2])
            elif menu_select == "2":
                self.lihat_produk_jualan_saya()
            else:
                break

            

# TODO : implementasikan class Buyer
class Buyer(User) : 
    def __init__(self, user_name, saldo):
        super().__init__(user_name, "BUYER")
        self.__saldo = saldo
        self.list_barang_beli = []
    
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def lihat_semua_produk(self):
        print("\nBerikut merupakan daftar produk di Dekdepedia")
        print("-----------------------------------------------")
        print(" Nama Produk   |   Harga   | Stock |  Penjual  ")
        print("-----------------------------------------------")
        for product in list_product:
            print(f"{product.nama:<15}|{product.harga:<11}|{product.stock:<7}|{str(product.seller):<11}")
        print("-----------------------------------------------")

    def beli_produk(self,nama_produk):
        if nama_produk not in [str(x) for x in list_product]:
            print(f"Barang dengan nama {nama_produk} tidak ditemukan dalam Dekdepedia.")
        else:
            # TODO Implement purchasing product
            pass
        
    def menu(self):
        print()
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA") 
        print("4. LOG_OUT")     
        while True:
            print()
            print(f"Saldo anda {self.get_saldo()},")
            menu_select = input("Apa yang ingin anda lakukan? ").strip()
            if menu_select == "1":
                self.lihat_semua_produk()
            elif menu_select == "2":
                product_info = input("Masukkan barang yang ingin dibeli : ")
                self.beli_produk(product_info)
            elif menu_select == "3":
                self.riwayat_pembelian()
            else:
                break

# TODO : implementasikan class Product
class Product() : 
    def __init__(self, nama, harga, stock, seller):
        self.nama = nama
        self.harga = harga
        self.stock = stock
        self.seller = seller
    
    def __str__(self):
        return self.nama


# method get_user dan get_product tidak perlu diubah, 
# silakan manfaatkan method ini untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

def valid_username(username):
    VALID_CHARACTERS = tuple(string.ascii_letters + string.digits + "_" + "-")
    for character in username:
        if character not in VALID_CHARACTERS:
            return False
    return True

PILIHAN = ("1","2","3")
TIPE_USER = ("SELLER","BUYER")
list_user = []
list_product = []

def main():
    while True:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        if (pilih == "1") : 
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
            
            print("Data akun: ")
            for i in range (banyak_user) : 
                data_user = input(str(i+1)+". ")
                data_user_split = data_user.split(maxsplit=2)
                if data_user_split[0] not in TIPE_USER:
                    print("Akun tidak valid.")
                else:
                    tipe_id = TIPE_USER.index(data_user_split[0])
                    data_user_username = data_user_split[1]
                    if get_user(data_user_username) != None:
                        print("Akun tidak valid.")
                    else:
                        if tipe_id == 0:
                            if len(data_user_split) > 2:
                                print("Akun tidak valid.")
                            elif not valid_username(data_user_username):
                                print("Akun tidak valid.")
                            list_user.append(Seller(data_user_username))
                        else:
                            if not valid_username(data_user_username):
                                print("Akun tidak valid.")
                            elif len(data_user_split) != 3:
                                print("Akun tidak valid.")
                            else:
                                try:
                                    data_user_saldo = int(data_user_split[2])
                                    if data_user_saldo < 0:
                                        raise ValueError
                                except ValueError:
                                    print("Akun tidak valid.")
                                else:
                                    list_user.append(Buyer(data_user_username,data_user_saldo))

        elif (pilih == "2") : 
            user_name_login = input("user_name : ")
            user_logged_in = get_user(user_name_login, list_user)
            if user_logged_in == None:
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan")
            else:
                print(f"Anda telah masuk dalam akun {user_name_login} sebagai {user_logged_in.get_tipe()}")
                user_logged_in.menu()
                print(f"Anda telah keluar dari akun {user_name_login}")
                
        elif (pilih == "3") : 
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()

if __name__ == "__main__":
    main()

# References
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
# https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats