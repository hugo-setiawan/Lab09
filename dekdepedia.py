import string

class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User. Menerima 2 argumen yakni user_name, dan tipe yang bernilai "SELLER" atau "BUYER"
        """
        self.__user_name = user_name
        self.__tipe = tipe

    def get_name(self) : 
        """
        Method yang mengembalikan username dari user.
        """
        return self.__user_name

    def get_tipe(self) : 
        """
        Method yang mengembalikan tipe dari user.
        """
        return self.__tipe

    def __str__(self):
        """
        Mengembalikan nama user jika object dari User dicast ke str.
        """
        return self.__user_name

class Seller(User) : 
    def __init__(self, user_name):
        """
        Constructor untuk class Seller. Menerima 1 argumen yakni username.
        """
        super().__init__(user_name, "SELLER")
        self.__pemasukan = 0
        self.list_barang_jual = []

    def get_pemasukan(self) : 
        """
        Method yang mengembalikan pemasukan total dari seller.
        """
        return self.__pemasukan

    def set_pemasukan(self, pemasukan) : 
        """
        Method yang mengeset pemasukan total dari seller ke suatu nilai tertentu yang ada di parameter pemasukan.
        """
        self.__pemasukan = pemasukan

    def tambah_product(self, nama, harga, stock) :
        """
        Method yang menambah produk yang dijual oleh seller. Menerima 3 parameter yakni nama produk (unik), harga produk, dan stok produk.
        """
        # Cek apakah produk dengan nama tsb sudah terdaftar
        if get_product(nama, list_product) != None:
            print("Produk sudah pernah terdaftar.")

        else:
            # Buatlah object produk dengan parameter yang sesuai, kemudian masukkan ke list punya Seller dan list_product global
            curr_product = Product(nama,harga,stock,self)
            self.list_barang_jual.append(curr_product)
            # Pastikan list_barang_jual Seller selalu dalam keadaan tersortir
            self.list_barang_jual = sorted(self.list_barang_jual,key=lambda x: str(x))
            list_product.append(curr_product)

    def lihat_produk_jualan_saya(self) : 
        """
        Method yang mencetak seluruh barang yang dijual oleh seller.
        """
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Produk   |   Harga   | Stock ")
        print("-------------------------------------")
        for product in self.list_barang_jual : 
            # dengan format : nama product 16 spaces + "|" + harga product 11 spaces + "|" + stok 7 spaces
            print(f"{product.get_name():<16}|{product.harga:<11}|{product.stock:<7}")
        print("-------------------------------------\n")

    def menu(self) : 
        """
        Method yang befungsi menjadi menu operasi utama untuk seller.
        """
        print()
        print(f"Selamat datang {self.get_name()},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")        
        while True:
            print()
            print(f"Pemasukan anda {self.get_pemasukan()},")
            menu_select = input("Apa yang ingin Anda lakukan? ")
            if menu_select == "1":
                product_info = input("Masukkan data produk : ").split()
                self.tambah_product(product_info[0],product_info[1],product_info[2])

            elif menu_select == "2":
                self.lihat_produk_jualan_saya()
                
            else:
                break

class Buyer(User) : 
    def __init__(self, user_name, saldo):
        """
        Constructor untuk kelas Buyer. Menerima 2 argumen yakni username dan saldo awal.
        """
        super().__init__(user_name, "BUYER")
        self.__saldo = saldo
        self.list_barang_beli = []
    
    def get_saldo(self):
        """
        Method yang mengembalikan saldo yang dimiliki buyer saat ini.
        """
        return self.__saldo

    def set_saldo(self, saldo):
        """
        Method yang mengeset saldo dari buyer ke suatu nilai tertentu yang ada di parameter saldo.
        """
        self.__saldo = saldo

    def lihat_semua_produk(self):
        """
        Method yang mencetak seluruh barang yang dijual di Dekdepedia.
        """
        print("\nBerikut merupakan daftar produk di Dekdepedia")
        print("------------------------------------------------")
        print("  Nama Produk   |   Harga   | Stock |  Penjual  ")
        print("------------------------------------------------")
        # Sortir list_product global sebelum ditampilkan ke user
        sorted_list_product = sorted(list_product,key=lambda x: str(x))
        for product in sorted_list_product:
            print(f"{product.get_name():<16}|{product.harga:<11}|{product.stock:<7}|{str(product.seller):<11}")
        print("------------------------------------------------")

    def beli_produk(self,nama_produk):
        """
        Method yang menambah produk yang dibeli oleh buyer. Menerima 1 parameter yakni nama produk yang hendak dibeli.
        """
        # Carilah object Product yang hendak dibeli
        produk_beli = get_product(nama_produk, list_product)
        if produk_beli == None:
            print(f"Barang dengan nama {nama_produk} tidak ditemukan dalam Dekdepedia.")

        elif produk_beli.stock <= 0:
            print("Maaf, stok produk telah habis.")

        elif produk_beli.harga > self.get_saldo():
            print(f"Maaf, saldo Anda tidak cukup untuk membeli {nama_produk}")

        else:
            # Jika produk bisa dibeli, lakukan transaksi dengan mengurangi saldo, memanggil method buy() pada object Product
            self.__saldo -= produk_beli.harga
            produk_beli.buy()
            # Tambahkan produk yang telah dibeli ke list barang barang dibeli milik Buyer, kemudian sortir list tsb
            self.list_barang_beli.append(produk_beli)
            self.list_barang_beli = sorted(self.list_barang_beli,key=lambda x: str(x))
            print(f"Berhasil membeli {str(produk_beli)} dari {str(produk_beli.seller)}")

    def riwayat_pembelian(self):
        """
        Method yang mencetak seluruh barang yang telah dibeli oleh buyer.
        """
        print("\nBerikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print("  Nama Produk  |   Harga   | Penjual ")
        print("-------------------------------------")
        for product in self.list_barang_beli:
            print(f"{product.get_name():<15}|{product.harga:<11}|{str(product.seller):<11}")
        print("-------------------------------------")
    
    def menu(self):
        """
        Method yang befungsi menjadi menu operasi utama untuk buyer.
        """
        print()
        print(f"Selamat datang {self.get_name()},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA") 
        print("4. LOG_OUT")     
        while True:
            print()
            print(f"Saldo anda {self.get_saldo()},")
            menu_select = input("Apa yang ingin Anda lakukan? ").strip()
            if menu_select == "1":
                self.lihat_semua_produk()

            elif menu_select == "2":
                product_info = input("Masukkan barang yang ingin dibeli : ")
                self.beli_produk(product_info)

            elif menu_select == "3":
                self.riwayat_pembelian()

            else:
                break

class Product() : 
    def __init__(self, nama, harga, stock, seller):
        """
        Constructor untuk kelas Product. Menerima 4 argumen yakni nama produk, harga, jumlah stock, dan object Seller yang menjual.
        """        
        self.__nama = nama
        self.harga = int(harga)
        self.stock = int(stock)
        self.seller = seller
    
    def buy(self):
        """
        Method yang melakukan transaksi pembelian sekali pada Product ini.
        """        
        # Lakukan transaksi dengan mengurangi stock Product dan menambah pemasukan dari Seller yang menjual Product ini.
        self.stock -= 1
        self.seller.set_pemasukan(self.seller.get_pemasukan() + self.harga)

    def get_name(self):
        """
        Method yang mengembalikan nama dari Product.
        """        
        return self.__nama

    def __str__(self):
        """
        Mengembalikan nama dari Product jika object dicast ke str.
        """
        return self.__nama

def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter.
    Mengembalikan None jika user dengan nama tersebut tidak ditemukan.
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name, list_product):
    """
    Method untuk mengembalikan product dengan name sesuai parameter.
    Mengembalikan None jika produk dengan nama tersebut tidak ditemukan.
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

def valid_username(username):
    """
    Method yang melakukan validasi karakter pada username yang dimasukkan.
    Method ini mengembalikan True jika username terdiri dari karakter valid, False jika ada karakter yang tidak valid.
    """
    # Karakter valid berisi A-Z, a-z, 0-9, -, dan _
    VALID_CHARACTERS = tuple(string.ascii_letters + string.digits + "_" + "-")
    for character in username:
        if character not in VALID_CHARACTERS:
            return False
    return True

TIPE_USER = ("SELLER","BUYER")
list_user = []
list_product = []

def main():
    while True:
        print()
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        # Sign Up
        if (pilih == "1") : 
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
            
            print("Data akun: ")
            for i in range (banyak_user) : 
                data_user = input(str(i+1)+". ")
                # Split input user ke maksimal 3 elemen dgn maxsplit (karena input valid paling banyak yakni input utk Buyer ada 3 elemen)
                data_user_split = data_user.split(maxsplit=2)
                # Validasi tipe user
                if data_user_split[0] not in TIPE_USER:
                    print("Akun tidak valid.")

                else:
                    # tipe_id 1 untuk Seller, 2 untuk Buyer
                    tipe_id = TIPE_USER.index(data_user_split[0])
                    # Sign up seller account
                    if tipe_id == 0:
                        # Validasi: tidak ada argumen lain di input selain tipe_user dan username
                        if len(data_user_split) != 2:
                            print("Akun tidak valid.")

                        # Validasi: cek apakah terdapat karakter di luar yang diperbolehkan
                        elif not valid_username(data_user_split[1]):
                            print("Akun tidak valid.")

                        # Validasi: apakah nama username sudah terdaftar pada user lain
                        elif get_user(data_user_split[1], list_user) != None:
                            print("Username sudah terdaftar.")

                        # Jika input valid, tambahkan Seller dengan nama tsb ke list_user
                        else:
                            list_user.append(Seller(data_user_split[1]))
                    # Sign up buyer account
                    else:
                        # Validasi: jumlah argumen sesuai yang diminta (tipe_user username saldo)
                        if len(data_user_split) != 3:
                            print("Akun tidak valid.")

                        # Validasi: cek apakah terdapat karakter di luar yang diperbolehkan
                        elif not valid_username(data_user_split[1]):
                            print("Akun tidak valid.")

                        else:
                            # Validasi: saldo valid (berupa integer yang tidak negatif)
                            try:
                                data_user_saldo = int(data_user_split[2])
                                if data_user_saldo < 0:
                                    raise ValueError
                            except ValueError:
                                print("Akun tidak valid.")
                            else:                    
                                # Validasi: apakah nama username sudah terdaftar pada user lain
                                if get_user(data_user_split[1], list_user) != None:
                                    print("Username sudah terdaftar.")

                                # Jika input valid, tambahkan Seller dengan nama dan saldo ke list_user
                                else:
                                    list_user.append(Buyer(data_user_split[1],data_user_saldo))
        # Log In
        elif (pilih == "2") : 
            user_name_login = input("user_name : ")
            # Cek ada user di list_user dengan username yang dimasukkan
            user_logged_in = get_user(user_name_login, list_user)
            if user_logged_in == None:
                # Jika tidak ada user dengan username yang dimasukkan
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan")

            else:
                # Login dengan user tersebut, dan akses menu dari user tersebut.
                print(f"Anda telah masuk dalam akun {user_name_login} sebagai {user_logged_in.get_tipe()}")
                user_logged_in.menu()
                # Tampilkan prompt logout jika user selesai dari menu. 
                print(f"Anda telah keluar dari akun {user_name_login}")
        
        # Exit dari program
        elif (pilih == "3") : 
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()

if __name__ == "__main__":
    main()

# References
# Slides DDP-1 B
# https://docs.python.org/3.9/library/stdtypes.html
# https://docs.python.org/3.9/tutorial/datastructures.html
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
#
#  /$$$$$$$            /$$             /$$                                     /$$ /$$          
# | $$__  $$          | $$            | $$                                    | $$|__/          
# | $$  \ $$  /$$$$$$ | $$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$ 
# | $$  | $$ /$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ |____  $$
# | $$  | $$| $$$$$$$$| $$$$$$/ | $$  | $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  | $$| $$  /$$$$$$$
# | $$  | $$| $$_____/| $$_  $$ | $$  | $$| $$_____/| $$  | $$| $$_____/| $$  | $$| $$ /$$__  $$
# | $$$$$$$/|  $$$$$$$| $$ \  $$|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$
# |_______/  \_______/|__/  \__/ \_______/ \_______/| $$____/  \_______/ \_______/|__/ \_______/
#                                                   | $$                                        
#                                                   | $$                                        
#                                                   |__/                                        