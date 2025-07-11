employees = {
    "01": {"name": "Ben Robinson", "rate": 29.28, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "02": {"name": "Cosmo Kumo", "rate": 22.25, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "03": {"name": "Sleve McDichael", "rate": 16.72, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "04": {"name": "Preston Garvey", "rate": 21.25, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "05": {"name": "Tonald Drump", "rate": 20.24, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "06": {"name": "Hervert Franscois", "rate": 14.14, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "07": {"name": "Money Bags", "rate": 55.55, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "08": {"name": "Hercules Strawberry", "rate": 17.32, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "09": {"name": "Lunafred Broomhilda", "rate": 21.25, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
    "10": {"name": "Chibert Mewmew", "rate": 19.86, "Hours worked": 0, "Gross pay": 0, "State Tax": 0, "Federal Tax": 0, "Net Pay": 0},
}
for emp_id, info in employees.items():
    print(f"ID: {emp_id} | Name: {info['name']} | Rate: ${info['rate']:.2f} | Hours: {info['Hours worked']:.2f} | Gross: {info['Gross pay']:.2f} | State: {info['State Tax']:.2f} | Federal: {info['Federal Tax']:.2f} | Net: {info['Net Pay']:.2f} ")
def select_employee(employee_list):
    while True:
     selected_id = input("Select employee ID: ").strip()

     if selected_id in employee_list:
        print(f"You selected {employees[selected_id]['name']}. Correct? (Y or N)")
        confirmation = input().strip().lower()

        if confirmation == "y":
            print("Let's calculate this employee's pay")
            return selected_id
        elif confirmation == "n":
            print("Okay, let's try again.")

        else:
            print("Invalid response. Please enter Y or N.")

     else:
        print("Employee ID not found")

from pay_calc import calculate_pay
while True:
    emp_id = select_employee(employees)
    if emp_id:
        calculate_pay(employees[emp_id])
    print("\n--- updated Employee List ---\n")
    for emp_id, info in employees.items():
        print(f"ID: {emp_id} | Name: {info['name']} | Rate: ${info['rate']:.2f} | Hours: {info['Hours worked']:.2f} | Gross: ${info['Gross pay']:.2f} | State: ${info['State Tax']:.2f} | Federal: ${info['Federal Tax']:.2f} | Net: ${info['Net Pay']:.2f} ")
    again = input("\nReady to calculate another employee? (Y or N)")
    if again == "n":
        input("Thanks for playing! Press enter to exit.")
        break
