print("Simple Company Payroll System")
print("--------------------------------------------------------")


def get_non_blank_string(prompt, error_msg):
    while True:
        value = input(prompt).strip()
        if value == "":
            print(error_msg)
        else:
            return value


def get_valid_float(prompt, invalid_msg, too_low_msg=None, min_value=None, allow_zero=True):
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
        if not allow_zero and value == 0:
            print(too_low_msg)
            continue
        return value


def main():
    # Validate number of workers
    while True:
        total_workers = input("How many workers does your company have: ").strip()
        if not total_workers.isdigit():
            print("Please type a valid whole number of workers")
            continue
        total_workers = int(total_workers)
        if total_workers == 0:
            print("You don't have any workers in your company")
            return
        break
    
    print("--------------------------------------------------------")
    total_salary_paid = 0
    
    for i in range(1, total_workers + 1):
        print(f"\nEnter details for worker #{i}:")
        name = get_non_blank_string(f"Employee number {i} name: ", "We can't have a blank name")
        hourly_rate = get_valid_float(f"What is the hourly rate of {name}: ", "Invalid hourly rate, please try again",
            min_value=1)
        hours_worked = float(input(f"How many hour did {name} work: "))
        overtime_hours = float(input("Total hours of Overtime: "))
        late_hours = float(input("Total hours of late: "))
        
        overtime_payment = (hourly_rate / 8) * overtime_hours
        deduction_for_late = late_hours * hourly_rate
        total_salary = (hourly_rate * hours_worked) + overtime_payment - deduction_for_late
        
        total_salary_paid += total_salary
        
        print(f"\nPayroll Summary of Employee No. {i}-{name}:")
        print(f"Employee number {i}: ")
        print(f"Employee Name: {name}")
        print(f"Hourly Rate: PHP {hourly_rate:.2f}")
        print(f"Total hours worked: {hours_worked} hours")
        print(f"Total hours of overtime: {overtime_hours} hours")
        print(f"Total hours of late: {late_hours} hours")
        print(f"Overtime Payment of {name} is: PHP {overtime_payment:.2f}")
        print(f"Deduction for Late: PHP {deduction_for_late:.2f}")
        print(f"Total Salary of {name} is: PHP{total_salary:.2f}")

    print("--------------------------------------------------------")
    print(f"\nTotal salary paid to {i} Worker is: PHP{total_salary_paid:.2f}")

if __name__ == "__main__":
    main()
