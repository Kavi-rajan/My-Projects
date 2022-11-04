import datetime
class CycleRental:
    count=5
    return_id=100
    cycle_directory={}
    def __init__(self):
        self.no_of_cycles=0
        self.rental_basis=0
        self.rental_time=0
        self.bill=0
    
    def display_count(self):
        print(f'we have currently {self.count} bikes available.')

    def rent_cycle_by_hours(self,n):
        if n<1:
            print("Please enter a positive number")
        elif n>self.count:
            print(f"Sorry.. We have only {self.count} cycles available now.")
        else:
            now=datetime.datetime.now()
            print(f"You have rented {n} bikes on hourly basis on {now.date()} at {now.hour} {now.strftime('%p')}")
            print("You will be charged Rs.10 per hour per cycle")
            print("Enjoy your ride. Thank you")
            print("Your return ID is",self.return_id)
            rented_time=now
            rent_basis=1
            no_of_cycles=n
            self.cycle_directory[self.return_id]=[rented_time,rent_basis,no_of_cycles]
            self.return_id+=1
            self.count-=n

    def rent_cycle_by_days(self,n):
        if n<1:
            print("Please enter a positive number")
        elif n>self.count:
            print(f"Sorry.. We have only {self.count} cycles available now.")
        else:
            now=datetime.datetime.now()
            print(f"You have rented {n} bikes on day basis on {now.date()} at {now.hour} {now.strftime('%p')}")
            print("You will be charged Rs.100 per day per cycle")
            print("Enjoy your ride. Thank you")
            print("Your return ID is",self.return_id)
            self.return_id+=1
            self.count-=n

    def rent_cycle_by_week(self,n):
        if n<1:
            print("Please enter a positive number")
        elif n>self.count:
            print(f"Sorry.. We have only {self.count} cycles available now.")
        else:
            now=datetime.datetime.now()
            print(f"You have rented {n} bikes on weekly basis on {now.date()} at {now.hour} {now.strftime('%p')}")
            print("You will be charged Rs.600 per hour per cycle")
            print("Enjoy your ride. Thank you")
            print("Your return ID is",self.return_id)
            self.return_id+=1
            self.count-=n

    def return_cycle(self,rented_time, rent_basis, no_of_cycles):
        bill=0

        if rented_time and rent_basis and no_of_cycles:
            self.count+=no_of_cycles
            return_time=datetime.datetime.now()
            rent_period=return_time-rented_time
            if rent_basis==1:#hourly_basis
                bill=round((rent_period.seconds/3600)*10*no_of_cycles)
            if rent_basis==2:#day_basis
                bill=round((rent_period.days)*100*no_of_cycles)
            if rent_basis==3:#weekly_basis
                bill=round(((rent_period.days)/7)*600*no_of_cycles)
            if no_of_cycles>5 and (rent_basis==2 or rent_basis==3): #discount for bulk rentals
                bill=bill*0.75
            
            print("Hope you enjoyed our service")
            print(f"your bill would be Rs.{bill}")
        else:
            print("enter valid details")
    
    def request_cycle(self):
        self.no_of_cycles=int(input("Enter How many cycles you want :"))
        print("\n1-hourly basis\n2-day basis\n3-weeklybasis\n")
        self.rental_basis=int(input("choose your rental basis :"))
        if self.rental_basis==1:
            self.rent_cycle_by_hours(self,self.no_of_cycles)
        if self.rental_basis==2:
            self.rent_cycle_by_days(self,self.no_of_cycles)
        if self.rental_basis==3:
            self.rent_cycle_by_week(self,self.no_of_cycles)
        


    