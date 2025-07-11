from random import randint

class Train :
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def get_status(self) :
        print(f"Train no {self.trainNo} is running on time.")

    def book_ticket(self, fro, to) :
       print(f"Booked a ticket in train no : {self.trainNo} for {fro} to {to}.") 

    def get_fare(self, fro, to) :
       print(f"Fare in train no : {self.trainNo} for {fro} to {to} is {randint(500, 2999)}.") 
    
t = Train(12315)

t.get_fare('Sealdah', 'DDU')
t.book_ticket('Sealdah', 'DDU')
t.get_status()