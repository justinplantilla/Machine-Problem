print("Simple Loan Calculator")
print("--------------------------------------------------------")


def get_valid_float(prompt, invalid_msg, too_low_msg=None, min_value=None):
    """Validate float input with conditions."""
    while True:
        value = input(prompt).strip()
        try:
            value = float(value)
        except ValueError:
            print(invalid_msg)
            continue
        if min_value is not None and value < min_value:
            print(too_low_msg)
            continue
        return value


def get_valid_int(prompt, invalid_msg, too_low_msg=None, min_value=None):
    """Validate integer input with conditions."""
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print(invalid_msg)
            continue
        value = int(value)
        if min_value is not None and value < min_value:
            print(too_low_msg)
            continue
        return value


def loan_calcu():
    principal_amount = get_valid_float(f"Enter amount to be borrowed: PHP ",
        "Invalid input. Please enter a valid number.",
        "Principal amount must be greater than 0. Please try again.",
        min_value=0.01)
    interest_rate = get_valid_float(f"Enter annual interest rate (%): ",
        "Invalid input. Please enter a valid number.",
        "Interest rate cannot be negative. Please try again.",
        min_value=0)
    loan_duration = get_valid_int(f"Hoy many months would you like to pay your debt: ", "Invalid input. Please enter a whole number.", min_value=1)
    
    monthly_principal_payment = principal_amount / loan_duration
    remaining_balance = principal_amount
    total_interest_paid = 0
    
    print("\n========== Loan Summary ==========")
    print(f"Total Amount Borrowed: {principal_amount:.2f}")
    print(f"Loan Duration: {loan_duration} months\n")

    # Monthly breakdown (not in table form)
    for month in range(1, loan_duration + 1):
        monthly_interest = remaining_balance* (interest_rate / 100)
        monthly_due = monthly_principal_payment + monthly_interest
        remaining_balance -= monthly_principal_payment
        total_interest_paid += monthly_interest

        print(f"Month {month}:")
        print(f"  Monthly Principal Payment: {monthly_principal_payment:.2f}")
        print(f"  Interest Rate: {interest_rate:.2f}%")
        print(f"  Monthly Interest: {monthly_interest:.2f}")
        print(f"  Monthly Due: {monthly_due:.2f}")
        print(f"  Remaining Balance: {remaining_balance:.2f}\n")

    total_amount_to_pay = principal_amount + total_interest_paid

    # Totals
    print("========== Totals ==========")
    print(f"Total Gain Interest: {total_interest_paid:.2f}")
    print(f"Total Amount to Pay: {total_amount_to_pay:.2f}")
    print("====================================================\n")


def main():
    while True:
        loan_calcu()
        # Ask if the user wants to process another loan
        while True:
            choice = input("Would you like to calculate another loan? (Y/N): ").strip().upper()
            if choice == "Y":
                break
            elif choice == "N":
                print("Exiting program. Thank you!")
                return
            else:
                print("Invalid input, please type Y or N.")


if __name__ == "__main__":
    main()