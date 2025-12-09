with open("data.csv", "r") as file:
    data = file.read()

a=data.strip().split("\n")
total_spent = 0
total_earned = 0
largest_transaction = ""
e=""
for i in a[1:]:
    b=i.split(",")
    Date=b[0].strip()
    Desc=b[1].strip()
    Amount=float(b[2].strip())
    if Amount < 0:
        total_spent += abs(Amount)
    else:
        total_earned += Amount
    
    if abs(Amount) > abs(largest_transaction) if isinstance(largest_transaction, (int, float)) else True:
        largest_transaction = Amount
        e = Desc
print(f"Total Spent: ${total_spent:.2f}")
print(f"Total Earned: ${total_earned:.2f}")
print(f"Largest Transaction: {e} of ${abs(largest_transaction):.2f}")