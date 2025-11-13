data_kunjungan = []  
id_counter = 1       

def tambah_data():
    global id_counter
    nama_pengunjung = input("Nama pengunjung: ")
    nama_santri = input("Nama santri yang dijenguk: ")
    
    while True:
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        print("Daerah tidak valid! Pilih antara Sumatra, Kalimantan, atau Jawa.")
    
    data = (id_counter, nama_pengunjung, nama_santri, daerah)
    data_kunjungan.append(data)
    print(f"Data berhasil ditambahkan! ID Antrian: {id_counter}")
    id_counter += 1

def tampilkan_data():
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return
    
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for d in urutan_daerah:
        print(f"\n=== Daerah {d} ===")
        for data in data_kunjungan:
            if data[3] == d:
                print(f"ID {data[0]} - {data[1]} menjenguk {data[2]}")

def hapus_data():
    global data_kunjungan
    if not data_kunjungan:
        print("Belum ada data untuk dihapus.")
        return
    
    try:
        id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
    except ValueError:
        print("Input ID harus berupa angka!")
        return
    
    data_baru = [data for data in data_kunjungan if data[0] != id_hapus]
    
    if len(data_baru) < len(data_kunjungan):
        data_kunjungan = data_baru
        print("Data berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")

while True:
    print("\n=== Sistem Kunjungan Santri ===")
    print("1. Tambah data kunjungan")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")


