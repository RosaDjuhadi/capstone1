import pyinputplus as pyip
import re
from datetime import date
list_mobil = [
    {
       'merk':'Hyundai Stargazer',
       'penumpang':7,
       'plat':'A 1345 C',
       'tahun':2023,
       'harga_sewa':700000,
       'kesediaan':'Tersedia',
       'ron_bensin':'92',
       'transmisi':'Matic'
    }
]


def TunjukkanListMobil():
    print('===========Semua List Mobil Rental Jaya==========\n')
    print('index\t|merk\t\t\t|penumpang\t|plat\t\t|tahun\t|harga_sewa\t|kesediaan\t|ron_bensin\t|transmisi')
    for i in range(len(list_mobil)) :
        print('{}\t|{}\t|{}\t\t|{}\t|{}\t|{}\t\t|{}\t|{}\t\t|{}'.format(i,list_mobil[i]['merk'],list_mobil[i]['penumpang'],list_mobil[i]['plat'],list_mobil[i]['tahun'],list_mobil[i]['harga_sewa'],list_mobil[i]['kesediaan'],list_mobil[i]['ron_bensin'],list_mobil[i]['transmisi']))
            

    
def MasukkanMobilBaruDalamList():
    while True:
        print("\t\t=====Tambahkan Mobil Baru=====")
        print("""
              1.Buat List Mobil Baru
              2.Kembali ke Menu
              """)
        user_input=input("Masukkan Angka Menu Pilihan Anda:")
        if user_input=="1":
            print("======Masukkan Detail Mobil Baru======")

                
                
            merk=pyip.inputStr("Masukkan Merk mobil:").title()
            penumpang=pyip.inputInt("Masukkan Jumlah Orang:")
            
            
            while True:
                plat=pyip.inputStr("Masukkan nomor plat dengan format 'X 1234 X':").upper()
                plat_valid=re.findall('[A-Z]{1,2}\s[0-9]{1,4}',plat)
                if plat_valid:
                    break
                else:
                    print("Masukan kembali dengan format KAPITAL-SPASI-ANGKA-SPASI-KAPITAL")
        


            while True:
                tahun=pyip.inputStr("Masukkan tahun pembuatan mobil sesuai STNK(dalam format angka):")
                tahun_valid=re.findall('[1-2][0-9][0-9][0-9]',tahun)
                if tahun_valid:
                    break
                else:
                    print("Masukkan kembali tahun pembuatan (hanya dri tahun 1000-2999)")
        
            
            harga_sewa=pyip.inputFloat('Masukkan harga mobil per hari (dalam format angka):')
            harga_sewa="Rp{:.2f}".format(harga_sewa)
                    

            while True:
                kesediaan=pyip.inputStr("Masukkan Kesediaan (Tersedia/Kosong):").lower()
                if kesediaan=="tersedia":
                    kesediaan="tersedia"
                    break
                elif kesediaan=="kosong":
                    kesediaan="kosong"
                    break
                else:
                    print("mohon hanya masukkan tersedia/kosong")

            while True:
                ron_bensin=pyip.inputStr("Masukkan Ron Bensin:")
                ron_bensin_valid=re.findall('9[0258]',ron_bensin)
                if ron_bensin_valid:
                    break
                else:
                    print("Masukkan kembali ron bensin (90/92/95/98)")

            while True:
                transmisi=pyip.inputStr("Masukkan Jenis Transmisi (Automatic/Manual):").lower()
                if transmisi=="automatic":
                    transmisi="Automatic"
                    break
                elif transmisi=="manual":
                    transmisi="Manual"
                    break
                else:
                    print("mohon hanya masukkan automatic/manual")
            


            mobil_baru={
                "merk":merk,
                "penumpang":penumpang,
                "plat":plat,
                "tahun":tahun,
                "harga_sewa":harga_sewa,
                "kesediaan":kesediaan,
                "ron_bensin":ron_bensin,
                "transmisi":transmisi
            }

            while True:
                print("Data Sudah Tersimpan")
                list_mobil.append(mobil_baru)
                TunjukkanListMobil()
                break
            break
        elif user_input=="2":
            return

def UpdateListMobil():
    while True:
        print("\t\t=====UPDATE LIST MOBIL=====")
        print("""
              1.Update List Mobil
              2.Kembali ke Menu
              """
        )
        user_input=input("Masukkan Angka Menu Pilihan Anda:")
        if user_input=="1":
            update_mobil_id=pyip.inputInt("Masukkan index mobil yang ingin di update:")
                
            print("=====Detail yang Ingin Diubah=====")
            print(
                """Pilih Nomor dari Detail yang diubah
                1. Merk 
                2. Penumpang
                3. Plat
                4. Tahun
                5. Harga Sewa
                6. Kesediaan
                7. Ron Bensin
                8. Transmisi
                """
            )
            user_input=pyip.inputStr("Masukkan angka 1-10:")
            if user_input=="1":
                list_mobil[update_mobil_id]['merk']=pyip.inputStr("Update Merk Mobil Menjadi:").title()
                TunjukkanListMobil
            elif user_input=="2":
                list_mobil[update_mobil_id]['penumpang']=pyip.inputInt("Update Jumlah Orang Menjadi:")
            elif user_input=="3":
                while True:
                        x=pyip.inputStr("Update nomor plat dengan format 'X 1234 X':")
                        x_valid=re.findall('[A-Z]{1,2}\s[0-9]{1,4}',x)
                        if x_valid:
                            list_mobil[update_mobil_id]['plat']=x
                            break
                        else:
                            print("Masukan kembali dengan format KAPITAL-SPASI-ANGKA-SPASI-KAPITAL")

            elif user_input=="4":
                y=pyip.inputInt("Update Tahun Menjadi:")
                y_valid=re.findall('[1-2][0-9][0-9][0-9]',list_mobil[update_mobil_id]['tahun'])
                if y_valid:
                    list_mobil[update_mobil_id]['tahun']
                    break
                else:
                    print("Masukkan kembali tahun pembuatan (hanya boleh memasukan antara tahun 1000-2999)")

            elif user_input=="5":
                list_mobil[update_mobil_id]['harga_sewa']=pyip.inputFloat("Update Harga Sewa Menjadi:")
                list_mobil[update_mobil_id]['harga_sewa']="Rp{:.2f}".format(list_mobil[update_mobil_id]['harga_sewa'])
            elif user_input=="6":
                while True:
                    a=pyip.inputStr("Update Kesediaan (Tersedia/Kosong):").title()
                    a_valid=re.findall('[Tersedia][Kosong]',a)
                    if a_valid:
                        list_mobil[update_mobil_id]['kesediaan']=a
                        break
                    else:
                        print("mohon hanya masukkan Tersedia/Kosong")

            elif user_input=="7":
                u=list_mobil[update_mobil_id]['ron_bensin']=pyip.inputStr("Update Ron Bensin Menjadi:").title()
                u_valid=re.findall('[90][92][95][98]',list_mobil[update_mobil_id]['ron_bensin'])
                if y_valid:
                    list_mobil[update_mobil_id]['ron_bensin']
                    break
                else:
                    print("Masukkan kembali tahun pembuatan (hanya boleh memasukan antara tahun 1000-2999)")

            elif user_input=="8":
                while True:
                    list_mobil[update_mobil_id]['transmisi']=pyip.inputStr("Masukkan Jenis Transmisi (Automatic/Manual):").title()
                    if jenis_transmisi=="automatic":
                        jenis_transmisi="automatic"
                        break
                    elif jenis_transmisi=="manual":
                        jenis_transmisi="manual"
                        break
                    else:
                        print("mohon hanya masukkan automatic/manual")

            else:
                print("Mohon hanya masukkan angka 1-10")
        elif user_input=="2":
            return

        else:
            print("Mohon pilih angka 1 atau 2 saja")

def HapusMobilDariDalamList():
    while True:
        print("======Hapus dari List Rental=====")
        print("""
              1. Hapus Mobil
              2. Kembali ke Menu Utama"""
            )
        user_input=pyip.inputStr("Masukkan Pilihan Anda:")
        if user_input=="1":
            if len(list_mobil)!=0:
                TunjukkanListMobil()
                hapus_mobil_id=pyip.inputInt("Masukkan ID yang ingin dihapus:")
                del list_mobil[hapus_mobil_id]
                TunjukkanListMobil()
                break
                    
            else:
                print("tidak ada list mobil untuk saat ini")
                break
            
        elif user_input=="2":
            return
        else:
            print("Mohon hanya pilih 1 atau 2")
                            
while True:
        print("\n\t======Selamat Datang di Rental Mobil Jaya======")
        print("""List Menu:
            1. Tunjukkan List Mobil
            2. Masukkan Mobil Baru Dalam List
            3. Update List Mobil
            4. Hapus Mobil Dari Dalam List
            5. Keluar
            """
        )
        user_input=pyip.inputStr("Masukkan Angka Dari Pilihan Menu Anda:")
        if(user_input=="1"):
            TunjukkanListMobil()
        elif(user_input=="2"):
            MasukkanMobilBaruDalamList()
        elif(user_input=="3"):
            UpdateListMobil()
        elif(user_input=="4"):
            HapusMobilDariDalamList()
        elif(user_input=="5"):
            break
        else:
            print("Ketik Angka 1-5:")