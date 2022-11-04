from rentalfunctions import CycleRental
class User():
    def __init__(self):
        None
    def execute(self,choice):
        if choice==1:
            CycleRental.display_count(CycleRental)
        if choice==2:
            CycleRental.request_cycle(CycleRental)
        if choice==3:
            num=int(input("Enter your return ID :"))
            CycleRental.return_cycle(CycleRental,*CycleRental.cycle_directory[num])
    
if __name__ =='__main__':
    user=User()
    while True:
        print("""WELCOME TO THAMIZH RENTAL CYCLES
         1.view count
         2.request cycle
         3.return cycle and pay bill
         4.Exit""")
        choice=int(input("Enter your choice :"))
        if choice==4:
            print("Thank you for visiting. Hope you enjoyed our services")
            break
        else:
            user.execute(choice)

