# Program Daftar Nilai Mahasiswa menggunakan Dictionary

data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    # Tambah Data
    if pilihan == "1":
        nama = input("Nama Mahasiswa : ")
        nim = input ("Nim Mahasiswa : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))
        akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil ditambahkan!")

    # Ubah Data
    elif pilihan == "2":
        nama = input("Masukkan nama yang akan diubah: ")
        if nama in data_mahasiswa:
            tugas = float(input("Nilai Tugas baru : "))
            uts = float(input("Nilai UTS baru   : "))
            uas = float(input("Nilai UAS baru   : "))
            akhir = hitung_nilai_akhir(tugas, uts, uas)

            data_mahasiswa[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    # Hapus Data
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        if nama in data_mahasiswa:
            del data_mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    # Tampilkan Semua Data
    elif pilihan == "4":
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        if len(data_mahasiswa) == 0:
            print("Belum ada data.")
        else:
            for nama, nilai in data_mahasiswa.items():
                print(f"- {nama} | Tugas: {nilai['tugas']} | UTS: {nilai['uts']} | UAS: {nilai['uas']} | Akhir: {nilai['akhir']:.2f}")

    # Cari Data
    elif pilihan == "5":
        nama = input("Masukkan nama yang dicari: ")
        if nama in data_mahasiswa:
            nilai = data_mahasiswa[nama]
            print("\n=== DATA MAHASISWA ===")
            print(f"Nama  : {nama}")
            print(f"Nim   : {nim}")
            print(f"Tugas : {nilai['tugas']}")
            print(f"UTS   : {nilai['uts']}")
            print(f"UAS   : {nilai['uas']}")
            print(f"Akhir : {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # Keluar
    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid, coba lagi.")