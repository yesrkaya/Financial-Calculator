class FinancialCalculator:
    def __init__(self):
        pass
    
    def calculate_loan_installments(self, principal_amount, interest_rate, installment_count):
        interest_rate = interest_rate / 100
        monthly_interest_rate = interest_rate / 12
        installment_amount = (principal_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -installment_count)
        total_payment = installment_amount * installment_count
        return installment_amount, total_payment

    def calculate_interest(self, principal_amount, interest_rate, years):
        interest_rate = interest_rate / 100
        interest_amount = principal_amount * interest_rate * years
        total_amount = principal_amount + interest_amount
        return interest_amount, total_amount

    def calculate_savings(self, monthly_investment_amount, annual_interest_rate, years):
        monthly_interest_rate = annual_interest_rate / 12 / 100
        total_amount = 0
        for month in range(years * 12):
            total_amount = (total_amount + monthly_investment_amount) * (1 + monthly_interest_rate)
        return total_amount

calculator = FinancialCalculator()

principal_amount = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
installment_count = int(input("Enter the number of installments: "))

installment_amount, total_payment = calculator.calculate_loan_installments(principal_amount, interest_rate, installment_count)
print("Monthly installment amount:", round(installment_amount, 2))
print("Total payment amount:", round(total_payment, 2))

principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years for interest calculation: "))

interest_amount, total_amount = calculator.calculate_interest(principal_amount, interest_rate, years)
print("Total interest amount:", round(interest_amount, 2))
print("Total amount (including interest):", round(total_amount, 2))

monthly_investment_amount = float(input("Enter the monthly investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years for savings calculation: "))

total_amount = calculator.calculate_savings(monthly_investment_amount, annual_interest_rate, years)
print("Total savings amount:", round(total_amount, 2))
