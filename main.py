data = [
    [1, 221151892, 'John Mariano', '7-14-2009','Medan', 'Akutansi', 2015],
    [2, 211112345, 'Jane Maharani', '3-4-2004','Surabaya','Manajemen', 2017],
    [3, 201113433, 'Bob Ferdinand', '2-12-2002','Jakarta','Teknik Informatika', 2019],
    [4, 201181892, 'Puan Putri Tjiaksana', '7-14-2009','Bandung', 'Akutansi', 2015],
    [5, 211161234, 'Riski Kalkulus', '3-4-2004','Makasar','Ilmu Komputer', 2017],
    [6, 221413433, 'Bernard Sinaga', '2-12-2002','Lamongan','Teknologi Informasi', 2019],
    [7, 171156892, 'Dino Maharudi', '7-14-2009','Madiun', 'Akutansi', 2015],
    [8, 191111234, 'Mesa Hibriji', '3-4-2004','Bali','Manajemen', 2017],
    [9, 181113433, 'Ilham Prasmanan', '2-12-2002','Aceh','Sistem Informasi', 2019]
]

def PrintData():
    column_names = ['No', 'Nim', 'Nama', 'Tanggal Lahir', 'Tempat Lahir', 'Program Studi', 'Tahun Masuk']
    max_widths = [max(len(str(row[i])) for row in data) for i in range(len(column_names))]
    separator = '+-' + '-+-'.join('-' * w for w in max_widths) + '-+'

    print(separator)
    print('| ' + ' | '.join('{:<{}}'.format(name, max_widths[i]) for i, name in enumerate(column_names)) + ' |')
    print(separator)

    for row in data:
        print('| ' + ' | '.join('{:<{}}'.format(str(val), max_widths[i]) for i, val in enumerate(row)) + ' |')
    print(separator)

    enter = input()
    if True:
        Main()

def AddData():
    print("Tambah Data")
    print("="*30)
    nim = int(input("Nim\t\t: "))
    nama = input("Nama\t\t: ")
    tanggalLahir = input("Tanggal Lahir\t: ")
    tempatLahir = input("Tempat Lahir \t: ")
    programStudi = input("Program Studi\t: ")
    tahunMasuk = int(input("Tahun Masuk\t: "))
    data.append([len(data)+1, nim, nama, tanggalLahir, tempatLahir, programStudi, tahunMasuk])

    print("Data berhasil di tambahkan")
    enter = input()
    if True:
        Main()

def ChangeData():
    findNim = int(input("Masukan Nim : "))
    print("="*30)

    for i in range(len(data)):
        if findNim == data[i][1]:
            print(data[i][1])
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

def Main():
    print("Database Mahasiswa")
    print("ahah")
    print("="*18)
    print("1. Tambah \n2. Tampilkan \n3. Ubah \n4. Urutkan \n5. Cari \n0. Keluar")
    print("="*18)
    choice = int(input("Masukan pilihan: "))

    if choice == 1:
        print("\n")
        AddData()
    elif choice == 2:
        print("\n")
        PrintData()
    elif choice == 3:
        print("\n")
        ChangeData()
    elif choice == 0:
        print("\nTerimakasih sudah menggunakan program kami")
        quit()
    

Main()

