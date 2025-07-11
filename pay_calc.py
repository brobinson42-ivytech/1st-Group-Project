def calculate_pay(employee):
    name = employee['name']
    rate = employee['rate']

    while True:
        try:
            hours_worked = float(input(f"How many hours did {name} work this week? "))
            if hours_worked < 0:
                print("Hours worked cannot be negative. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Why you putting letters? You crazy. Numbers only, son.")

    if hours_worked <= 40:
        gross = hours_worked * rate
        print(f"{name} made ${gross:.2f} this week.")
    else:
        gross = 40 * rate
        over = hours_worked - 40
        overtime = over * (rate * 1.5)
        gross += overtime
        print(f"{name} made ${gross:.2f} this week.")
    print("Now let's factor in taxes.")
    input("Press enter to continue.")

    state = 0.056
    federal = 0.079
    stateTax = gross * state
    fedTax = gross * federal
    netPay = gross - stateTax - fedTax

    print(f"The state is taking ${stateTax:.2f}")
    print(f"Federal is taking ${fedTax:.2f}")
    print(f"{name} is bringing home ${netPay:.2f}")

    employee["Hours worked"] = hours_worked
    employee["Gross pay"] = gross
    employee["State Tax"] = stateTax
    employee["Federal Tax"] = fedTax
    employee["Net Pay"] = netPay
    input("Press enter to continue.")
#This section is here just to test the module
if __name__ == "__main__":
    sample = {"name": "Demo Man", "rate": 10.0}
    calculate_pay(sample)