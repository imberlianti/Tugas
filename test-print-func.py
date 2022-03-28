def Dompet(JML_MAHASISWA , UANGDOMPET):
    return JML_MAHASISWA * UANGDOMPET

Jml_Mahasiswa = int(input("Jumlah Mahasiswa: "))
UangInDompet = int(input("Jumlah Uang: Rp. "))

print("Total Uang: Rp. " + str(Dompet(Jml_Mahasiswa, UangInDompet)))
