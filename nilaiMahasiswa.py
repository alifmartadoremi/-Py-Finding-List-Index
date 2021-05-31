__author__="kvda"

class myClass():

    def myFunc(self):
        offsetRerata = 0
        print("Aplikasi Nilai Mahasiswa")
        print("-----")
        jumlahMahasiswa = input("Masukkan Jumlah Mahasiswa : ")
        offset=0
        myNim = []
        myNama = []
        myNilaiTugas = []
        myNilaiUTS = []
        myNilaiUAS = []
        myTotalNilai = []
        while offset<int(jumlahMahasiswa):
            print("Mahasiswa ke-",offset+1)
            print("---")
            nim     =   input("NIM : ")
            if(nim in myNim):
                print("NIM Sudah ada, silahkan masukkan ulang.")
                continue
            else:
                myNim.append(nim)
                nama    =   input("Nama : ") 
                myNama.append(nama)
                nilaiTugas  =   input("Nilai Tugas : ")
                myNilaiTugas.append(nilaiTugas)
                nilaiUTS    =   input("Nilai UTS : ")
                myNilaiUTS.append(nilaiUTS)
                nilaiUAS    =   input("Nilai UAS : ")
                myNilaiUAS.append(nilaiUAS)
                totalNilai = (int(nilaiTugas)+int(nilaiUTS)+int(nilaiUAS))/3
                myTotalNilai.append(totalNilai)
                offsetRerata+=int(totalNilai)
                print("Total Nilai : ",totalNilai)
                offset+=1
        myJumlahMahasiswa = int(len(myNim))
        rerata = int(offsetRerata)/int(myJumlahMahasiswa)
        print("Rata-rata total nilai : ",rerata)

        menuUtama = 1
        while menuUtama==1:
            print(" ")
            print("---")
            print("Cari Nilai Mahasiswa")
            print("---")
            searchNim = input("Masukkan NIM Mahasiswa : ")
            if(searchNim not in myNim):
                print("NIM yang anda cari tidak tersedia.")
                continue
            elif(searchNim in myNim):
                getIndex = myNim.index(searchNim)
                print("Nama mahasiswa : {0} ".format(myNama[getIndex]))
                print("Nilai Tugas : {0}".format(myNilaiTugas[getIndex]))
                print("Nilai UTS : {0} ".format(myNilaiUTS[getIndex]))
                print("Nilai UAS : {0}".format(myNilaiUAS[getIndex]))
                print("Total Nilai : {0}".format(myTotalNilai[getIndex]))
                print("---")
                enableLoop = input("Ingin cari lagi? (Y/N) : ")
                if(enableLoop == "Y"):
                    continue
                elif(enableLoop == "N"):
                    break
        print("---")
        print("Copyright 2021 kvda-creator")
if __name__ == '__main__':
    myClass().myFunc()