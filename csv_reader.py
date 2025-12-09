with open("data.csv", "r") as file1:
    data = file1.read()
with open("data1.csv", "r") as file2:
    data1 = file2.read()

b = data.strip() + "\n" + data1.strip()
a = b.strip().split("\n")
a = [row for row in a if not row.startswith('"Date"')]
total_spent = 0
total_earned = 0
largest_transaction = ""
e=""
for i in a[1:]:
    b=i.split(",")
    Date=b[0].strip()
    Desc=b[1].strip()
    Amount = float(b[2].strip().replace('"', ''))
    if Amount < 0:
        total_spent += abs(Amount)
    else:
        total_earned += Amount
    
    if abs(Amount) > abs(largest_transaction) if isinstance(largest_transaction, (int, float)) else True:
        largest_transaction = Amount
        e = Desc
print(f"Total Spent: Rs {total_spent:.2f}")
print(f"Total Earned: Rs {total_earned:.2f}")
print(f"Largest Transaction: {e} of Rs {abs(largest_transaction):.2f}")