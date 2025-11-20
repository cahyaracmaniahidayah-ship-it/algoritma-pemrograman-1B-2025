
contacts = {
    "Caca": ["085785008669", "cahyaracmaniahidayah@gmail.com"],
    "Nia": ["085704774782", "cahyarachmaniah@gmail.com"]
}

def show_contacts():
    if not contacts:
        print("Belum ada kontak tersimpan.")
    else:
        print("\nDaftar Kontak:")
        for name, info in contacts.items():
            print(f"Nama: {name}, Telepon: {info[0]}, Email: {info[1]}")
    print("-" * 30)

def search_contact():
    name = input("Masukkan nama kontak yang dicari: ")
    if name in contacts:
        print(f"Nama: {name}, Telepon: {contacts[name][0]}, Email: {contacts[name][1]}")
    else:
        print("Kontak tidak ditemukan.")
    print("-" * 30)

def add_contact():
    name = input("Masukkan nama kontak baru: ")
    if name in contacts:
        print("Kontak sudah ada.")
    else:
        phone = input("Masukkan nomor telepon: ")
        email = input("Masukkan email: ")
        contacts[name] = [phone, email]
        print("Kontak berhasil ditambahkan.")
    print("-" * 30)

def update_email():
    name = input("Masukkan nama kontak yang ingin diperbarui: ")
    if name in contacts:
        new_email = input("Masukkan email baru: ")
        contacts[name][1] = new_email
        print("Email berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")
    print("-" * 30)

def delete_contact():
    name = input("Masukkan nama kontak yang ingin dihapus: ")
    if name in contacts:
        del contacts[name]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")
    print("-" * 30)

def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak berdasarkan nama")
        print("3. Tambah kontak baru")
        print("4. Perbarui email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            update_email()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Terima kasih telah menggunakan Contact Book!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            print("-" * 30)

if __name__ == "__main__":
    main()
