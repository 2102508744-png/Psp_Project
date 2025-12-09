data = """Date,Desc,Amount
2023-01-01,Salary,5000
2023-01-02,Rent,-1200
2023-01-03,Groceries,-150
2023-01-04,Freelance,300"""

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