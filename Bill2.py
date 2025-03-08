import time
import datetime
import random

idli_price = 30
dosa_price = 50
upma_price = 20
vada_price = 40
rate=0

gstin = "203B1A0513"


def add_item(name, rate):
    qty = int(input(f"\nEnter Quantity for {name}: "))
    total = qty * rate
    return name, qty, rate, total


order = []
total_amount = 0

print("\n====  SHIVARA THINDI ====")
print("\n==== Menu ====")
print(" 1. IDLI\n 2. DOSA\n 3. UPMA\n 4. VADA\n 5. FINISH ORDER")

while True:
    option = int(input("\nSelect Your Item (or 5 to Finish Order): "))
    
    if option == 1:
        item = add_item("IDLI", idli_price)
        order.append(item)
        total_amount += item[3]
        
    elif option == 2:
        item = add_item("DOSA", dosa_price)
        order.append(item)
        total_amount += item[3]
        
    elif option == 3:
        item = add_item("UPMA", upma_price)
        order.append(item)
        total_amount += item[3]
        
    elif option == 4:
        item = add_item("VADA", vada_price)
        order.append(item)
        total_amount += item[3]
        
    elif option == 5:
        if not order:
            print("No items ordered.")
            break
        con = input("\nDo you want to Place the Order? (yes/no): ")
        if con.lower() == "yes":
            print("\n\t\t    SHIVARA THINDI \n\t\tGSTIN:", gstin, "\n\t\t      CASH BILL\n--------------------------------------------------")
            bill_no = random.randint(1, 10000)
            print("Bill No:", bill_no, "\t\t\tBill DT:", end=" ")
            bill_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(bill_date)
            print("------------------------------------------------------")
            print("Item Name\tQTY\tRate\t\tAmount")
            
            for item in order:
                print(f"{item[0]}\t\t{item[1]}\t{item[2]}\t\t{item[3]}")
                
            print("------------------------------------------------------")
            cgst = total_amount * 0.06
            sgst = total_amount * 0.06
            print("CGST 6%\t\t\t\t\t", cgst)
            print("SGST 6%\t\t\t\t\t", sgst)
            print("------------------------------------------------------")
            grand_total = total_amount + cgst + sgst
            grand_total = round(grand_total, 2)
            print("Grand Total\t\t\t\t", grand_total)
            print("\n--- Please Visit Again ---")
            print("----- Thank You ------")
        else:
            print("Order cancelled.")
        break
    else:
        print("This option is not available.")
