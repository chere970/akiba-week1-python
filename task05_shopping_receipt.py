customer_name=input("Enter customer name: ")
product_name1=input("Enter product name: ")
price1=float(input("Enter price: "))
quantity1=int(input("Enter quantity: "))

product_name2=input("Enter product name: ")
price2=float(input("Enter price: "))
quantity2=int(input("Enter quantity: "))

total_price1=price1*quantity1
total_price2=price2*quantity2

total_price=total_price1 + total_price2

print("==========================")
print("          RECEIPT")
print("==========================")
print(f"Customer: {customer_name}\n")
print(f"{'Product':<15}{'Price':<10}{'Qty':<10}")
print("-"*40)
print(f"{product_name1:<15}{price1:>10.2f}{quantity1:>10}")
print(f"{product_name2:<15}{price2:>10.2f}{quantity2:>10}")
print(f"\nTotal:         {total_price:.2f} ETB\n")
print("Thank you for shopping!")
print("==========================")
