

annualInterestRate = float(input("Enter annual interest rate, e.g., 8.25: "))
monthlyInterestRate = annualInterestRate / 1200

numberOfYears = int(input("Enter number of years as an integer, e.g., 5: "))
    
loanAmount = float(input("Enter loan amount, e.g., 120000.95: "))
    
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

print("The monthly payment is", int(monthlyPayment * 100) / 100)
print("The total payment is", int(totalPayment * 100) /100)