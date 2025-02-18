'''
Nabiha, a software engineering consultant, receives a variable salary every month. She wants to create a Python script that helps her manage her monthly finances by calculating how much money will be allocated to different categories like savings, rent, and electricity, based on percentages of his salary.

Your task is to write a Python script that automates these calculations. The script should:


• Ask Nabiha to input her salary for the month.
• Ask Nabiha to input the name of the month she is storing the salary for.
• Ask Nabiha to input the following percentages for: a) Savings b) Rent c) Electricity

The script should calculate and display:
 

• The amount allocated to savings, rent, and electricity.
• The total amount Nabiha spends on savings, rent, and electricity combined.
• The remainder of Nabiha’s salary after these expenses.
• The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
• Nabiha's total salary for the month raised to the power of 2 (just for fun).
• Assume Nabiha saves an additional random amount (e.g., $50) each month, and you need to calculate how much would be left if this amount is divided by the total amount allocated to savings. 

Finally, the script should output all the results in a readable format.
'''

import random
while True:
    salary=int(input('Nabiha al kabiha please enter your salary: '))
    month=input('Nabiha input the name of the month she is storing the salary for: ')
    savings_per=int(input('enter the percentage for \nsavings: '))
    rent_per=int(input('rent:'))
    electricity_per=int(input('electricity: '))
    saving=(salary*savings_per)/100
    rent=(salary*rent_per)/100
    electricity=(salary*electricity_per)/100
    total_spending=saving+rent+electricity
    remainder=salary-total_spending
    yearly_rent=rent*12
    yearly_electricity=electricity*12
    double_salary=salary**2
    additional_savings=random.randint(10,100)
    if saving!=0:
        savings_division = additional_savings / saving 
    else:
        savings_division=0
    print("\nFinancial Summary for", month)
    print("-" * 40)
    print(f"Total Salary: ${salary}")
    print(f"Allocated to Savings: ${saving}")
    print(f"Allocated to Rent: ${rent}")
    print(f"Allocated to Electricity: ${electricity}")
    print(f"Total Expenses: ${total_spending}")
    print(f"Remaining Salary: ${remainder}")
    print(f"Estimated Yearly Rent: ${yearly_rent}")
    print(f"Estimated Yearly Electricity Cost: ${yearly_electricity}")
    print(f"Salary Squared (for fun): ${double_salary}")
    print(f"you have an extra {savings_division}% on your saving ")
    print("-" * 40)
    cont=input('do you want to continue?')
    if cont=='no':
        break
    


        

    
