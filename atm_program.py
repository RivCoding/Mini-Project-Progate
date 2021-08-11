import customer
import utils
import time

atm = customer.Customer() #Kartu dimasukkan ke mesin ATM
while True :
    print("SELAMAT DATANG DI ATM PROGATE")
    print("Silahkan masukkan kartu Anda.")
    time.sleep(1)
    id = int(input("Masukkan PIN Anda : "))
    trial = 0
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin Anda salah. Silahkan masukkan lagi : "))
        trial +=1 
        if trial == 3 :
            print("Error. Silahkan ambil kartu dan coba lagi.")
            exit()

    while True :
        print("\nSelamat datang Bapak/Ibu", atm.nama, "di ATM Progate.")
        print("\n[1] Cek Saldo \t[2] Debet \t[3] Setor \t[4] Transfer")
        print("[5] Ganti Pin \t[6] Riwayat \t[7] Keluar")
        selectmenu = int(input("\nSilahkan pilih menu: "))
        if selectmenu == 1 :
            print("Mohon Tunggu Sebentar...")
            time.sleep(2) #Memberikan jeda
            atm.checkBalance()
            utils.border()
            print("Saldo Anda sekarang adalah Rp", atm.checkBalance())
            print("Nomor rekening Anda adalah", atm.checkrekening())
            utils.border()

        elif selectmenu == 2 :
            nominal = float(input("Masukkan nominal saldo untuk didebet: ")) 
            print("Saldo Anda saat ini adalah Rp", atm.checkBalance())
            print("\nKonfirmasi Anda akan melakukan debet dengan nominal Rp " + str(nominal) + " ? (Y/N): ")
            verifikasi_debet = input("")
            print("Sedang Memproses Transaksi...")
            time.sleep(3)   #Memberikan jeda 
            if verifikasi_debet.upper() == "Y" :
                if nominal <= atm.checkBalance() :
                    atm.withdrawBalance(nominal)
                    histdebet = "DEBET " +time.asctime() + " Telah melakukan penarikan sebesar Rp " + str(nominal)
                    customer.historydebet.append(histdebet)
                    customer.history.append(histdebet)
                    utils.skripheader()
                    print("Transaksi Berhasil")
                    print(histdebet)
                    print("Sisa saldo Anda Rp", atm.checkBalance())
                    utils.skripfooter()
                    print("Silahkan Ambil Uang Anda")

                else :
                    print("Mohon maaf, saldo Anda tidak mencukupi")
                    continue
            else :
                continue

        elif selectmenu == 3 :
            nominal = float(input("Masukkan nominal saldo untuk distor: ")) 
            print("\nKonfirmasi Anda akan melakukan stor dengan nominal Rp " + str(nominal) + " ? (Y/N): ")
            verifikasi_simpan = input("")
            print("Sedang Memproses Transaksi...")
            time.sleep(3)   #Memberikan jeda
            if verifikasi_simpan.upper() == "Y":
                atm.depositBalance(nominal)
                histsimpan = "DEPOSIT " + time.asctime() + " Telah melakukan stor tunai sebesar Rp " + str(nominal)
                customer.historysimpan.append(histsimpan)
                customer.history.append(histsimpan)
                utils.skripheader()
                print("Transaksi Berhasil")
                print(histsimpan)
                print("Sisa saldo Anda Rp", atm.checkBalance())
                utils.skripfooter()
            else:
                continue

        elif selectmenu == 4:
            print("Saldo Anda saat ini adalah Rp", atm.checkBalance())
            nominal = float(input("Masukkan nominal saldo untuk ditransfer: ")) 
            tujuan = input("Masukkan rekening tujuan: ")
            if tujuan != str(atm.checkrekening()):
                print("\nAnda akan melakukan transfer dengan nominal Rp " + str(nominal) + " ke " + tujuan)
                print("\nKonfirmasi Anda akan melakukan transfer dengan nominal Rp " + str(nominal) + " ke " + tujuan + " ? (Y/N): ")
                verifikasi_simpan = input("")
                print("Sedang Memproses Transaksi...")
                time.sleep(3)   #Memberikan jeda
                if verifikasi_simpan.upper() == "Y":
                    atm.transfer(nominal)
                    histtransfer = "TRANSFER " + time.asctime() + " Telah melakukan transfer sebesar Rp " + str(nominal) + " ke " +tujuan
                    customer.historytransfer.append(histtransfer)
                    customer.history.append(histtransfer)
                    utils.skripheader()
                    print("Transaksi Berhasil")
                    print(histtransfer)
                    print("Sisa saldo Anda Rp", atm.checkBalance())
                    utils.skripfooter()
                else:
                    continue
            else :
                print("\nAnda tidak bisa melakukan transfer ke rekening Anda sendiri.")

        elif selectmenu == 5 :
            verify_pin = int(input("Silahkan masukkan PIN Anda saat ini : "))
            if verify_pin == atm.pin :
                new_pin = int(input("Masukkan PIN baru Anda (minimal 4 digit): "))
                if len(str(new_pin)) >= 4 :
                    new_pin_check = int(input("Masukkan ulang PIN baru Anda : "))
                    if new_pin == new_pin_check and new_pin != atm.pin: 
                        print("\nYakin ingin merubah PIN ? (Y/N): ")
                        verifikasi_ganti = input("")
                        print("Sedang Memproses...")
                        time.sleep(3)   #Memberikan jeda
                        if verifikasi_ganti.upper() == "Y":
                            atm.pin = new_pin
                            histganti = "CHANGE PIN " + time.asctime() + " Telah mengganti PIN"
                            customer.history.append(histganti)
                            print("\nPIN berhasil diganti")
                            print("Silahkan login ulang dengan PIN Baru Anda\n")
                            break
                        else: 
                            continue
                    else:
                        print("\nTerjadi kesalahan. \nPIN baru tidak boleh sama dengan PIN lama. \nPastikan telah memasukan PIN dengan benar")
                        continue
                else :
                    print("PIN harus memiliki setidaknya 4 digit")
            else:
                print("PIN Anda salah. Silahkan coba lagi\n")

        elif selectmenu == 6 :
            print("[1] Riwayat Debet \t[2] Riwayat Stor \t[3] Riwayat Transfer \t[4] Riwayat Lengkap \t[5] Kembali")
            select = int(input("Masukkan jenis riwayat yang ingin dilihat: "))
            if select == 1:
                utils.border()
                for i in customer.historydebet:
                    print(i)
                utils.border()
            elif select == 2:
                utils.border()
                for i in customer.historysimpan:
                    print(i)
                utils.border()
            elif select == 3:
                utils.border()
                for i in customer.historytransfer:
                    print(i)
                utils.border()
            elif select == 4:
                utils.border()
                for i in customer.history:
                    print(i)
                utils.border()
            else:
                continue

        elif selectmenu == 7:
            print("\nTerima kasih telah menggunakan ATM Progate. \nSilahkan ambil kembali kartu Anda\n")
            utils.border()
            break

        else: 
            print("\nMenu tidak tersedia. Silahkan ambil kembali kartu Anda")
            break
    continue