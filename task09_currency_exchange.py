amount_usd=float(input("Enter Amount in USD: "))

exchange_rate=float(input("Enter Exchage Rate: "))
amount_etb=exchange_rate*amount_usd
print("\n")
print("==========================")
print("   CURRENCY EXCHANGE  ")
print("==========================")
print(f"USD Amount: {amount_usd}")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB")
print(f"ETB Amount: {amount_etb}")
print("==========================")