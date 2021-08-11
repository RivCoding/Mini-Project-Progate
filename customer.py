#Berisikan data customer yang didapat dari kartu ATM dibaca oleh mesin atm
#Perintah yang bisa dilakukan mesin atm
import atm_card

class Customer :
    def __init__(self , nama = atm_card.user.nama , rekening = atm_card.user.rekening, custPin = atm_card.user.pin , custBalance = atm_card.user.balance):
        self.rekening = rekening
        self.nama = nama
        self.pin = custPin
        self.balance = custBalance
    
    def namapengguna (self):
        return self.nama

    def checkrekening (self): 
        return self.rekening
    
    def checkPin (self):
        return self.pin
    
    def checkBalance (self):
        return self.balance

    def withdrawBalance (self, nominal):
        self.balance -= nominal
    
    def depositBalance (self, nominal):
        self.balance += nominal

    def transfer (self,nomimal):
        self.balance -= nomimal

historydebet = []
historysimpan = []
historytransfer = []
history = []