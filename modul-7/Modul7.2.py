
inventory = {
    "001": ["Pensil", 2000, 50],
    "002": ["Buku Tulis", 5000, 30]
}

def show_items():
    if not inventory:
        print("Belum ada barang di inventaris.")
    else:
        print("\nDaftar Barang:")
        print("ID\tNama\tHarga\tStok")
        print("-" * 40)
        for item_id, info in inventory.items(): 
         print(f"{item_id:<5} {info[0]:<15} {info[1]:<10} {info[2]:<5}")

    print("-" * 40)

def search_item():
    item_id = input("Masukkan ID barang yang dicari: ")
    if item_id in inventory:
        info = inventory[item_id]
        print(f"ID: {item_id}, Nama: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")
    else:
        print("Barang tidak ditemukan.")
    print("-" * 40)

def add_item():
    item_id = input("Masukkan ID barang baru: ")
    if item_id in inventory:
        print("ID barang sudah ada.")
    else:
        name = input("Masukkan nama barang: ")
        try:
            price = int(input("Masukkan harga barang: "))
            stock = int(input("Masukkan jumlah stok: "))
            if stock < 0 or price < 0:
                print("Harga dan stok tidak boleh negatif.")
                return
            inventory[item_id] = [name, price, stock]
            print("Barang berhasil ditambahkan.")
        except ValueError:
            print("Harga dan stok harus berupa angka.")
    print("-" * 40)

def update_stock():
    item_id = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if item_id in inventory:
        try:
            change = int(input("Masukkan jumlah stok (positif untuk tambah, negatif untuk kurangi): "))
            if inventory[item_id][2] + change < 0:
                print("Stok tidak boleh negatif!")
            else:
                inventory[item_id][2] += change
                print(f"Stok barang '{inventory[item_id][0]}' berhasil diperbarui. Stok sekarang: {inventory[item_id][2]}")
        except ValueError:
            print("Jumlah stok harus berupa angka.")
    else:
        print("Barang tidak ditemukan.")
    print("-" * 40)

def delete_item():
    item_id = input("Masukkan ID barang yang ingin dihapus: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")
    print("-" * 40)

def main():
    while True:
        print("\n=== Manajemen Inventaris Gudang ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan ID")
        print("3. Tambah barang baru")
        print("4. Perbarui stok barang")
        print("5. Hapus barang")
        print("6. Keluar")
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            show_items()
        elif choice == "2":
            search_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            print("Terima kasih telah menggunakan sistem inventaris!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            print("-" * 40)

if __name__ == "__main__":
    main()
