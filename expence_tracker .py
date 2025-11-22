from datetime import datetime

def get_valid_date():
    while True:
        date_str=input("Enter date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print("Invalid date! Please use DD-MM-YYYY.\n")

def  ask_yes_no(question):
    while True:
        more=input(question+"(Yes or No): ").lower()

        if more=="yes":
            return True
        elif more=="no":
            return False
        else:
            print("Invalid input! Please only yes or no.")

def add_expense():
    print("\n----- Add Expence -----")
    date=get_valid_date()

    while True:
        try:
            amount=int(input("Enter amount: "))
        except ValueError:
            print("Enter a vlid amount for amount!\n")
            continue

        cateogary=input("Enter cateogary: ")

        with open("expence.txt","a") as f:
            f.write(f"\n{date}\n{amount}\n{cateogary}")

        print("Expence added successfully!\n")

        if not ask_yes_no("Do you have another item to add?"):
            break


def view_expence():
    print("\n----- All Expence -----")
    try:
        with open("expence.txt","r") as f:
            data=[line.strip() for line in f.readlines() if line.strip()]

            if not data:
                print("No expence found.\n")
                return
            
            current_date = None
            i = 0

            while i < len(data):
                date = data[i]
                amount = data[i+1]
                category = data[i+2]
                i += 3

                if date != current_date:

                    if current_date is not None:
                        print("------------------------------")

                    print(f"\n{date}")   # print date ONCE
                    current_date = date

                print(f" {category} -- ₹{amount}")
            print("------------------------------")



    except FileNotFoundError:
        print("No expence file found. Add expence file first.\n")

def main():
    while True:
        print("\n====== DAILY EXPENCE TRACKER =======")
        print("1. Add Expence")
        print("2. View Expence")
        print("3. Exit")

        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Enter a number between (1-3).")
            continue

        match choice:
            case 1:
                add_expense()
            case 2:
                view_expence()
            case 3:
                print("Exiting... Goodbye!\n")
                break
            case _:
                print("Invalid choice! Enter a number (1-3).\n")

main()