
coupons = {
    "DISC10": 10,
    "DISC20": 20,
    "DISC50": 50
}

def show_coupons():
    if not coupons:
        print("Tidak ada kupon yang tersedia.")
    else:
        print("\nKupon yang tersedia:")
        print("Kode Kupon\tDiskon (%)")
        print("-" * 25)
        for code, discount in coupons.items():
            print(f"{code}\t\t{discount}")
    print("-" * 25)


def process_transaction():
    try:
        total = float(input("Masukkan total belanja: "))
        if total < 0:
            print("Total belanja tidak boleh negatif.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    code = input("Masukkan kode kupon: ").upper()  
    if code in coupons:
        discount = coupons[code]
        total_after_discount = total * (1 - discount / 100)
        print(f"Kupon valid! Diskon {discount}% diterapkan.")
        print(f"Total yang harus dibayar: Rp {total_after_discount:.2f}")
        
        del coupons[code]
        print("Kupon sudah digunakan dan dihapus dari daftar kupon.")
    else:
        print("Kupon tidak valid atau sudah dipakai.")
    print("-" * 25)

def main():
    while True:
        print("\n=== Sistem Kasir dengan Kupon Diskon ===")
        print("1. Tampilkan semua kupon yang tersedia")
        print("2. Proses transaksi dengan kupon")
        print("3. Keluar")
        choice = input("Pilih menu (1-3): ")

        if choice == "1":
            show_coupons()
        elif choice == "2":
            process_transaction()
        elif choice == "3":
            print("Terima kasih telah menggunakan sistem kasir!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            print("-" * 25)

if __name__ == "__main__":
    main()
