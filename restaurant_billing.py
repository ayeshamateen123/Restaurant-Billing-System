# ==============================
# Restaurant Billing System
# Developed by: Ayesha Mateen
# Language: Python
# ==============================

print("===== Welcome To Restaurant =====")

# Get customer details
Customer_name = input("Enter Customer Name: ")
Table_no = input("Enter Table Number: ")

# Variable to store total bill
total = 0

# Repeat until user chooses Exit
while True:

    # Display Menu
    print("\n===== Restaurant Menu =====")
    print("1. Pizza - ₹199")
    print("2. Burger - ₹120")
    print("3. Sandwich - ₹100")
    print("4. Coffee - ₹80")
    print("5. Generate Bill & Exit")

    # Take customer choice
    enter_choice = input("Enter your choice: ")

    # Pizza
    if enter_choice == "1":
        quantity = int(input("Enter Quantity: "))
        Bill = 199 * quantity
        total += Bill
        print("Pizza added successfully!")

    # Burger
    elif enter_choice == "2":
        quantity = int(input("Enter Quantity: "))
        Bill = 120 * quantity
        total += Bill
        print("Burger added successfully!")

    # Sandwich
    elif enter_choice == "3":
        quantity = int(input("Enter Quantity: "))
        Bill = 100 * quantity
        total += Bill
        print("Sandwich added successfully!")

    # Coffee
    elif enter_choice == "4":
        quantity = int(input("Enter Quantity: "))
        Bill = 80 * quantity
        total += Bill
        print("Coffee added successfully!")

    # Generate Bill
    elif enter_choice == "5":
        gst = total * 0.05
        grand_total = total + gst

        print("\n======= BILL =======")
        print("Customer Name :", Customer_name)
        print("Table Number  :", Table_no)
        print("-------------------------")
        print("Subtotal      : ₹", total)
        print("GST (5%)      : ₹", gst)
        print("-------------------------")
        print("Grand Total   : ₹", grand_total)
        print("=========================")
        print("Thank You! Visit Again.")
        break

    # Invalid Choice
    else:
        print("Invalid Choice! Please Try Again.")