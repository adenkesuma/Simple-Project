# buat data siswa secara random
data = [
    [1, 221151892, 'John Mariano', '7-14-2009','Medan', 'Akutansi', 2015],
    [2, 211112345, 'Jane Maharani', '3-4-2004','Surabaya','Manajemen', 2017],
    [3, 201113433, 'Bob Ferdinand', '2-12-2002','Jakarta','Teknik Informatika', 2019],
    [4, 201181892, 'Puan Putri Tjiaksana', '7-14-2009','Bandung', 'Akutansi', 2015],
    [5, 211161234, 'Riski Kalkulus', '3-4-2004','Makasar','Ilmu Komputer', 2017],
    [6, 221413433, 'Bernard Sinaga', '2-12-2002','Lamongan','Teknologi Informasi', 2019],
    [7, 171156892, 'Dino Maharudi', '7-14-2009','Madiun', 'Akutansi', 2015],
    [8, 191111234, 'Mesa Hibriji', '3-4-2004','Bali','Manajemen', 2017],
    [9, 181113433, 'Ilham Prasmanan', '2-12-2002','Aceh','Sistem Informasi', 2019],
    [10, 221111805, 'Aden Kesuma', '14-08-2004', 'Medan', 'Teknik Informatika', 2022]
]

# fungsi printData adalah fungsi yang bertugas untuk menampilkan data siswa
def PrintData(data):
    # kompleksitas waktu: O(n)
    # karena perulangan sebanyak N kali untuk menampilkan setiap baris, dan untuk setiap baris perlu melihat setiap kolom.
    column_names = ['No', 'Nim', 'Nama', 'Tanggal Lahir', 'Tempat Lahir', 'Program Studi', 'Tahun Masuk']
    max_widths = [max(len(str(row[i])) for row in data) for i in range(len(column_names))]
    separator = '+-' + '-+-'.join('-' * w for w in max_widths[:3] + [max(max_widths[3], 14), max(max_widths[4], 12), max(max_widths[5], 15), max(max_widths[6], 11)]) + '-+'

    print(separator)
    print('| ' + ' | '.join('{:<{}}'.format(name, max_widths[i]) for i, name in enumerate(column_names[:3])) + ' | ' + '{:<{}}'.format(column_names[3], max(max_widths[3], 14)) + ' | ' + '{:<{}}'.format(column_names[4], max(max_widths[4], 12)) + ' | ' + '{:<{}}'.format(column_names[5], max(max_widths[5], 15)) + ' | ' + '{:<{}}'.format(column_names[6], max(max_widths[6], 11)) + ' |')
    print(separator)

    for row in data:
        print('| ' + ' | '.join('{:<{}}'.format(str(val), max_widths[i]) for i, val in enumerate(row[:3])) + ' | ' + '{:<{}}'.format(str(row[3]), max(max_widths[3], 14)).replace(",", ",\n") + ' | ' + '{:<{}}'.format(str(row[4]), max(max_widths[4], 12)).replace(",", ",\n") + ' | ' + '{:<{}}'.format(str(row[5]), max(max_widths[5], 15)).replace(",", ",\n") + ' | ' + '{:<{}}'.format(str(row[6]), max(max_widths[6], 11)).replace(",", ",\n") + ' |')
    print(separator)

    enter = input()

# fungsi addData adalah fungsi yang bertugas untuk menambah data baru 
def AddData(data):
    # kompleksitas waktu: O(1)
    # karena hanya menambahkan satu baris data pada akhir list, yang tidak tergantung pada ukuran data yang sudah ada.
    print("Tambah Data")
    print("="*30)
    nim = int(input("Nim\t\t: "))
    nama = input("Nama\t\t: ")
    tanggalLahir = input("Tanggal Lahir\t: ")
    tempatLahir = input("Tempat Lahir \t: ")
    programStudi = input("Program Studi\t: ")
    tahunMasuk = int(input("Tahun Masuk\t: "))
    data.append([len(data)+1, nim, nama, tanggalLahir, tempatLahir, programStudi, tahunMasuk])

    print("Data berhasil di tambahkan\n")
    if True:
        Main()

# fungsi changeData adalah fungsi yang bertugas untuk mengubah data yang sebelumnya menjadi data baru
def ChangeData(data):
    # kompleksitas waktu: O(n)
    # karena mencari baris yang sesuai dengan NIM membutuhkan perulangan sebanyak N kali
    findNim = int(input("Masukan Nim : "))
    print("="*30)

    for i in range(len(data)):
        if findNim == data[i][1]:
            del data[i]
            nim = int(input("Nim: "))
            nama = input("Nama: ")
            tanggalLahir = input("Tanggal Lahir: ")
            tempatLahir = input("Tempat Lahir: ")
            programStudi = input("Program Studi: ")
            tahunMasuk = int(input("Tahun Masuk: "))

            data.insert(i, [i+1, nim, nama, tanggalLahir, tempatLahir, programStudi, tahunMasuk])

            print("Data berhasil di ubah")
            enter = input()
            if True:
                Main()
    else:
        print(f'Mahasiswa dengan nim {findNim} tidak di temukan, tolong masukan nim yang sesuai')
        ChangeData(data)    
        
# fungsi sortData adalah fungsi yang hanya bertugas untuk menyortir data atau mengurutkan data
def SortData(data):
    # kompleksitas waktu: O(n^2)
    # dikarenakan terdapat dua buah perulangan for bersarang yang menjalankan operasi perbandingan dan penukaran elemen pada array sebanyak n-1 kali pada setiap iterasi.
    def SortByNim(data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j][1] > data[j + 1][1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        PrintData(data)
        print("Data Mahasiswa berhasil diurutkan berdasarkan NIM!\n")
        if True:
            SortMetode()

    def SortByName(data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j][2] > data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        PrintData(data)
        print("Data Mahasiswa berhasil diurutkan berdasarkan Nama!\n")
        if True:
            SortMetode()

    def SortBySubject(data):
        n = len(data)
        for i in range(n-1):
            for j in range(n-i-1):
                if data[j][5] > data[j+1][5]:
                    data[j], data[j+1] = data[j+1], data[j]
        PrintData(data)
        print("Data Mahasiswa berhasil diurutkan berdasarkan Program Studi!\n")
        if True:
            SortMetode()

    def SortByYear(data):
        n = len(data)
        for i in range(n-1):
            for j in range(n-i-1):
                if data[j][6] > data[j+1][6]:
                    data[j], data[j+1] = data[j+1], data[j]
        PrintData(data)
        print("Data Mahasiswa berhasil diurutkan berdasarkan Tahun Masuk!\n")
        if True:
            SortMetode()

    if not data:
        print("Data Mahasiswa kosong.")

    def SortMetode():
        print("Pilih metode pengurutan:")
        print("1. Berdasarkan NIM\n2. Berdasarkan Nama\n3. Berdasarkan Program Studi\n4. Berdasarkan Tahun Masuk\n5. Keluar")
        choice = int(input("Masukkan pilihan: "))

        if choice == 1:
            SortByNim(data)
        elif choice == 2:
            SortByName(data)
        elif choice == 3:
            SortBySubject(data)
        elif choice == 4:
            SortByYear(data)
        elif choice == 5:
            Main()
        else:
            print("Pilihan tidak valid.")

    SortMetode()

# fungsi searchData adalah fungsi yang bertugas khusus mencari sebuah data
def SearchData(data):
    # kompleksitas waktu: O(n)
    # karena hanya menjalankan satu perulangan for dengan operasi perbandingan sebanyak n kali
    def SearchByName(name):
        result = []
        for mahasiswa in data:
            if name in mahasiswa[2]:
                result.append(mahasiswa)
        
        if result:
            PrintData(result)
            if True:
                Main()
        else:
            print("Mahasiswa tidak di temukan")
            Main()

    def SearchByNim(nim):
        result = []
        for mahasiswa in data:
            if str(nim) in str(mahasiswa[1]):
                result.append(mahasiswa)
        if result:
            PrintData(result)
            if True:
                Main()
        else:
            print("Mahasiswa tidak di temukan")
            Main()
        


    if not data:
        print("Data Mahasiswa kosong.")

    print("Pilih metode pencarian:")
    print("1. Berdasarkan NIM\n2. Berdasarkan Nama")
    choice = int(input("Masukkan pilihan (1/2): "))

    if choice == 1:
        nim = int(input("Masukkan NIM Mahasiswa yang dicari: "))
        mahasiswa = SearchByNim(nim)
    elif choice == 2:
        nama = input("Masukkan Nama Mahasiswa yang dicari: ")
        mahasiswa = SearchByName(nama)
    else:
        print("Pilihan tidak valid.")

# function main adalah fungsi yang pertama kali muncul ketika kode di jalankan
def Main():
    '''
        Kompleksitas waktu dari fungsi ini tergantung pada urutan pemanggilan fungsi dan logika program yang terkait.
    '''
    print("Database Mahasiswa")
    print("="*18)
    print("1. Tambah \n2. Tampilkan \n3. Ubah \n4. Urutkan \n5. Cari \n0. Keluar")
    print("="*18)
    choice = int(input("Masukan pilihan: "))

    if choice == 1:
        print("\n")
        AddData(data)
    elif choice == 2:
        print("\n")
        PrintData(data)
        if True:
            Main()
    elif choice == 3:
        print("\n")
        ChangeData(data)
    elif choice == 4:
        print("\n")
        SortData(data)
    elif choice == 5:
        print("\n")
        SearchData(data)
    elif choice == 0:
        print("\nTerimakasih sudah menggunakan program kami")
        quit()
    
Main()


'''
    Dalam hal ini, kompleksitas terbesar terdapat pada bagian O(N*M) 
    dengan kompleksitas waktu O(N*M) karena memiliki perulangan sebanyak N kali
    untuk menampilkan setiap baris, dan untuk setiap baris perlu melihat setiap kolom.
    Jadi, kompleksitas keseluruhan dari algoritma ini adalah O(N*M).
'''