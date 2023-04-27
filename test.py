# class Mahasiswa:
#     def init(self, no, nim, nama, tempat_lahir, tanggal_lahir, program_studi, tahun_masuk):
#         self.no = no
#         self.nim = nim
#         self.nama = nama
#         self.tempat_lahir = tempat_lahir
#         self.tanggal_lahir = tanggal_lahir
#         self.program_studi = program_studi
#         self.tahun_masuk = tahun_masuk

#     def display(self):
#         print("No: ", self.no)
#         print("NIM: ", self.nim)
#         print("Nama: ", self.nama)
#         print("Tempat Lahir: ", self.tempat_lahir)
#         print("Tanggal Lahir: ", self.tanggal_lahir)
#         print("Program Studi: ", self.program_studi)
#         print("Tahun Masuk: ", self.tahun_masuk)
#         print("\n")


# def tambah_data_mahasiswa(mahasiswa_list):
#     no = len(mahasiswa_list) + 1
#     nim = input("Masukkan NIM: ")
#     nama = input("Masukkan Nama: ")
#     tempat_lahir = input("Masukkan Tempat Lahir: ")
#     tanggal_lahir = input("Masukkan Tanggal Lahir (DD/MM/YYYY): ")
#     program_studi = input("Masukkan Program Studi: ")
#     tahun_masuk = input("Masukkan Tahun Masuk: ")

#     mahasiswa = Mahasiswa(no, nim, nama, tempat_lahir, tanggal_lahir, program_studi, tahun_masuk)
#     mahasiswa_list.append(mahasiswa)
#     print("Data Mahasiswa berhasil ditambahkan!")


# def tampilkan_data_mahasiswa(mahasiswa_list):
#     print("\nDaftar Data Mahasiswa:")
#     for mahasiswa in mahasiswa_list:
#         mahasiswa.display()


# def ubah_data_mahasiswa(mahasiswa_list):
#     nim = input("Masukkan NIM Mahasiswa yang akan diubah: ")
#     for mahasiswa in mahasiswa_list:
#         if mahasiswa.nim == nim:
#             nama = input("Masukkan Nama: ")
#             tempat_lahir = input("Masukkan Tempat Lahir: ")
#             tanggal_lahir = input("Masukkan Tanggal Lahir (DD/MM/YYYY): ")
#             program_studi = input("Masukkan Program Studi: ")
#             tahun_masuk = input("Masukkan Tahun Masuk: ")

#             mahasiswa.nama = nama
#             mahasiswa.tempat_lahir = tempat_lahir
#             mahasiswa.tanggal_lahir = tanggal_lahir
#             mahasiswa.program_studi = program_studi
#             mahasiswa.tahun_masuk = tahun_masuk

#             print("Data Mahasiswa berhasil diubah!")
#             return

#     print("NIM Mahasiswa tidak ditemukan.")


# def bubble_sort_by_nim(mahasiswa_list):
#     n = len(mahasiswa_list)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if mahasiswa_list[j].nim > mahasiswa_list[j + 1].nim:
#                 mahasiswa_list[j], mahasiswa_list[j + 1] = mahasiswa_list[j + 1], mahasiswa_list[j]

# def bubble_sort_by_nim(mahasiswa_list):
#     n = len(mahasiswa_list)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if mahasiswa_list[j].nim > mahasiswa_list[j + 1].nim:
#                 mahasiswa_list[j], mahasiswa_list[j + 1] = mahasiswa_list[j + 1], mahasiswa_list[j]


# def bubble_sort_by_nama(mahasiswa_list):
#     n = len(mahasiswa_list)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if mahasiswa_list[j].nama > mahasiswa_list[j + 1].nama:
#                 mahasiswa_list[j], mahasiswa_list[j + 1] = mahasiswa_list[j + 1], mahasiswa_list[j]


# def urutkan_data_mahasiswa(mahasiswa_list):
#     if not mahasiswa_list:
#         print("Data Mahasiswa kosong.")
#         return

#     print("Pilih metode pengurutan:")
#     print("1. Berdasarkan NIM")
#     print("2. Berdasarkan Nama")
#     choice = input("Masukkan pilihan (1/2): ")

#     if choice == "1":
#         bubble_sort_by_nim(mahasiswa_list)
#         print("Data Mahasiswa berhasil diurutkan berdasarkan NIM!")
#     elif choice == "2":
#         bubble_sort_by_nama(mahasiswa_list)
#         print("Data Mahasiswa berhasil diurutkan berdasarkan Nama!")
#     else:
#         print("Pilihan tidak valid.")


# def linear_search_by_nim(mahasiswa_list, nim):
#     for mahasiswa in mahasiswa_list:
#         if mahasiswa.nim == nim:
#             return mahasiswa
#     return None


# def linear_search_by_nama(mahasiswa_list, nama):
#     for mahasiswa in mahasiswa_list:
#         if mahasiswa.nama.lower() == nama.lower():
#             return mahasiswa
#     return None


# def cari_data_mahasiswa(mahasiswa_list):
#     if not mahasiswa_list:
#         print("Data Mahasiswa kosong.")
#         return

#     print("Pilih metode pencarian:")
#     print("1. Berdasarkan NIM")
#     print("2. Berdasarkan Nama")
#     choice = input("Masukkan pilihan (1/2): ")

#     if choice == "1":
#         nim = input("Masukkan NIM Mahasiswa yang dicari: ")
#         mahasiswa = linear_search_by_nim(mahasiswa_list, nim)
#         if mahasiswa:
#             print("Data Mahasiswa ditemukan:")
#             mahasiswa.display()
#         else:
#             print("NIM Mahasiswa tidak ditemukan.")
#     elif choice == "2":
#         nama = input("Masukkan Nama Mahasiswa yang dicari: ")
#         mahasiswa = linear_search_by_nama(mahasiswa_list, nama)
#         if mahasiswa:
#             print("Data Mahasiswa ditemukan:")
#             mahasiswa.display()
#         else:
#             print("Nama Mahasiswa tidak ditemukan.")
#     else:
#         print("Pilihan tidak valid.")

# def main():
#     mahasiswa_list = []

#     while True:
#         print("\nMenu:")
#         print("1. Tambah Data Mahasiswa")
#         print("2. Tampilkan Data Mahasiswa")
#         print("3. Ubah Data Mahasiswa")
#         print("4. Urutkan Data Mahasiswa")
#         print("5. Cari Data Mahasiswa")
#         print("6. Keluar")
#         choice = input("Masukkan pilihan (1/2/3/4/5/6): ")

#         if choice == "1":
#             tambah_data_mahasiswa(mahasiswa_list)
#         elif choice == "2":
#             tampilkan_data_mahasiswa(mahasiswa_list)
#         elif choice == "3":
#             ubah_data_mahasiswa(mahasiswa_list)
#         elif choice == "4":
#             urutkan_data_mahasiswa(mahasiswa_list)
#         elif choice == "5":
#             cari_data_mahasiswa(mahasiswa_list)
#         elif choice == "6":
#             print("Terima kasih telah menggunakan program ini!")
#             break
#         else:
#             print("Pilihan tidak valid.")


# main()

