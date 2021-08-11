class ATMCard : #Berisi data data dalam kartu ATM

    def __init__ (self, nama, rekening, pin, balance):
        self.nama = nama
        self.rekening = rekening
        self.pin = pin
        self.balance = balance
    
    def namapengguna (self):
        return self.nama

    def cekPinAwal (self):
        return self.defaultPin
    
    def cekSaldoAwal (self):
        return self.defaultBalance

user = ATMCard("Budi", 12345678, 2345, 90000) #Informasi kartu