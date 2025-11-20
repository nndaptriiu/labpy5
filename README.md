## Nama : Ananda Eka Delima Putri
## NIM : 312510210
## Kelas : TI.25.A.2
## Pertemuan : 10
## Mata Kuliah : Pengantar Pemrograman

## Kode Latihan
<img width="967" height="951" alt="Screenshot 2025-11-20 113043" src="https://github.com/user-attachments/assets/2c23b0d8-52c3-4a18-864c-c382710c858b" />

## Output Latihan
<img width="1580" height="591" alt="Screenshot 2025-11-20 113101" src="https://github.com/user-attachments/assets/68a8686b-73d5-4a82-98c4-4d4bfa478424" />

## Kode Praktikum
<img width="1072" height="881" alt="Screenshot 2025-11-20 113523" src="https://github.com/user-attachments/assets/8651ce51-89a9-44f7-94cf-c59b8c9001ee" />

## Output Praktikum
<img width="1451" height="784" alt="Screenshot 2025-11-20 113458" src="https://github.com/user-attachments/assets/7cc0b1f4-84f3-494e-af1e-a27058b943e4" />

## Flowchart
```

                   ┌────────────────────────┐
                   │     MULAI PROGRAM      │
                   └───────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │   TAMPILKAN MENU        │
                   └───────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │   INPUT PILIHAN MENU    │
                   └───────────┬────────────┘
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼

   ┌────────────────┐   ┌────────────────┐   ┌──────────────────────┐
   │ Pilihan = 1 ?   │   │ Pilihan = 2 ?   │   │ Pilihan = 3 ?         │
   └───────┬────────┘   └───────┬────────┘   └───────────┬──────────┘
           │                    │                       │
           ▼                    ▼                       ▼

┌─────────────────────┐  ┌──────────────────────┐ ┌───────────────────────┐
│ INPUT nama, nim,     │  │ INPUT nama yang akan │ │ INPUT nama yang akan   │
│ tugas, uts, uas      │  │ diubah               │ │ dihapus                │
│ HITUNG nilai akhir   │  │ Jika ada → ubah data │ │ Jika ada → hapus data  │
│ SIMPAN ke dictionary │  │ Jika tidak → pesan   │ │ Jika tidak → pesan     │
└─────────┬───────────┘  └───────────┬──────────┘ └────────────┬──────────┘
          │                         │                         │
          └──────────────┬──────────┴───────────────┬─────────┘
                         │                          │
                         ▼                          ▼

              ┌──────────────────────┐     ┌───────────────────────┐
              │   Pilihan = 4 ?       │     │    Pilihan = 5 ?       │
              └───────────┬──────────┘     └───────────┬───────────┘
                          │                            │
                          ▼                            ▼
      ┌────────────────────────────┐   ┌─────────────────────────────┐
      │ TAMPILKAN semua data       │   │ INPUT nama yang dicari       │
      │ Jika kosong → pesan        │   │ Jika ada → tampilkan         │
      └──────────┬─────────────────┘   │ Jika tidak → pesan           │
                 │                     └──────────┬──────────────────┘
                 │                                │
                 └───────────────┬────────────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │   Pilihan = 0 ?        │
                     └────────────┬───────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │    KELUAR PROGRAM   │
                        └────────────────────┘
```
## PENJELASAN PROGRAM
1. Dictionary Data Mahasiswa
   
data_mahasiswa = {}

Semua data mahasiswa akan disimpan dalam dictionary dengan format:
```
data_mahasiswa[nama] = {

    "tugas": nilai,
    
    "uts": nilai,
    
    "uas": nilai,
    
    "akhir": nilai_akhir
    
}
```
2. Fungsi hitung_nilai_akhir()
   ```
   def hitung_nilai_akhir(tugas, uts, uas):
    return (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
   ```
   
   Fungsi ini menghitung nilai akhir berdasarkan bobot:

  *Tugas : 30%

  *UTS : 35%

  *UAS : 35%
  
  3. Menu Utama (Looping while True)

Program menampilkan menu dan meminta pengguna memilih salah satu:
```
1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
0. Keluar
```
Proses berlangsung terus sampai pengguna memilih 0.

4. Tambah Data (Menu 1)

Program meminta input:

*nama

*nim

*nilai tugas

*nilai UTS

*nilai UAS

Lalu menghitung nilai akhir, kemudian menyimpan data ke dictionary.

5. Ubah Data (Menu 2)

Pengguna memasukkan nama mahasiswa yang akan diubah.

Jika ditemukan, data diperbarui dengan input nilai baru.

Jika tidak ditemukan → tampil pesan "Data tidak ditemukan!"

6. Hapus Data (Menu 3)

Pengguna memasukkan nama mahasiswa yang ingin dihapus.

Jika ada → data dihapus.

Jika tidak → muncul pesan.

7. Tampilkan Semua Data (Menu 4)

Menampilkan semua mahasiswa dalam dictionary.

Jika data kosong → tampil "Belum ada data."

8. Cari Data (Menu 5)

Pengguna memasukkan nama.
Jika ada, tampil data mahasiswa.

BUG yang muncul
Pada saat menampilkan NIM, kamu menggunakan nim dari variabel terakhir, karena NIM tidak disimpan.

9. Keluar (Menu 0)

Mengakhiri program.
