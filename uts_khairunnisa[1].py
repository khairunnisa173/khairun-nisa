class Absen:
    def __init__(self, nama, npm, prodi, kelas, presensi,pertemuan):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        self.kelas = kelas
        self.presensi = presensi
        self.pertemuan = pertemuan

    def keterangan(self):
        ket =""
        if presensi == "H" or presensi == "h":
            ket = "hadir"
        elif presensi == "I" or presensi == "i":
            ket = "Izin"
        elif presensi == "A" or presensi == "a":
            ket = "Alpha"

        print("Mahasiswa dengan\n nama : {}\n npm : {}\n prodi : {}\n Kelas : {}\n".format(self.nama,self.npm,self.prodi,self.kelas))
        print (" Telah {} pada pertemuan ke-{}".format(ket,self.pertemuan))


# Program Absensi Kuliah
nama = input("masukkan nama:")

# jika kita ingin mengambil int, maka
npm = int(input("masukkan NPM:"))

# menentukan kelas
prodi = input("masukkan prodi : ")

kelas = input("pilih kelas:")

pertemuan = int(input("pertemuan ke- : "))

# H = Hadir
# I = Izin
# A = Alpha

presensi = input("pilih presensi [H/I/A]: ")

absensi = Absen(nama, npm, prodi, kelas, presensi,pertemuan)
absensi.keterangan()