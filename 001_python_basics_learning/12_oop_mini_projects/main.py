# main.py
from taxi_service import Taxi

def main():
    taxi1 = Taxi("Ahmed", "AP01AB1234")

    taxi1.pick_customer("Mr. Ali")
    taxi1.drop_customer(5)

    taxi1.pick_customer("Ms. Sana")
    taxi1.drop_customer(7)

    taxi1.change_driver("Imran")

    taxi1.pick_customer("Mr. Farooq")
    taxi1.drop_customer(3)

    taxi1.change_driver("Rahim")
   
    taxi1.pick_customer("Ms. Zara")
    taxi1.drop_customer(6)

    taxi1.pick_customer("Mr. Bilal")
    taxi1.drop_customer(4)  

    taxi1.pick_customer("Ms. Aisha")
    taxi1.drop_customer(2)

    taxi1.summary()
    taxi1.save_summary_to_file()

if __name__ == "__main__":
    main()
