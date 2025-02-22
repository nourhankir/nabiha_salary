
def printing(month,salary,saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary,savings_division):
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
        
def calculation(salary,savings_per,rent_per,electricity_per):
        
        saving=(salary*savings_per)/100
        
        rent=(salary*rent_per)/100
        
        electricity=(salary*electricity_per)/100
        
        total_spending=saving+rent+electricity
        
        remainder=salary-total_spending
        
        yearly_rent=rent*12
        
        yearly_electricity=electricity*12
        
        double_salary=salary**2
        return saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary
    
additional_savings=0
#months=['january','february']
months=[]
#budget=[{month_name:'january',salary=1000},{month_name:'february',salary=2000}]
budget=[]

def menu():
    print('1)input your salary')
    print('2)edit your month salary')
    print('3)add an additional amount of money')
    print('4)read your schedule for the month')
    print('5)read all the months')
    print('6)Exit')
    
print('hi Samira this is a program to help you manage your monthly finances ')
savings_per=int(input('enter the percentage for \nsavings: '))
rent_per=int(input('rent:'))
electricity_per=int(input('electricity: '))
menu()
while True:
    action=input('enter the action you would like to take ')
    if action in ['1','2','3','4','5','6']:
        break
while True:
    if action=='1':
        month_name=input('Nabiha input the name of the month you are storing the salary for: ').lower()
        salary=int(input('Nabiha al kabiha please enter your salary: '))
        
        if month_name not in months:
            saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary=calculation(salary,savings_per,rent_per,electricity_per)
            month={"month_name":month_name,'salary':salary,"saving":saving,'rent':rent,'electricity':electricity,'total_spending':total_spending,
                'remainder':remainder,'yearly_rent':yearly_rent,'yearly_electricity':yearly_electricity,'double_salary':double_salary,'additional_savings':additional_savings}
            months.append(month_name)
            budget.append(month)
            
            if saving!=0:
                savings_division = additional_savings / saving 
            else:
                savings_division=0
            menu()
            while True:
                action=input('enter the action you would like to take ')
                if action in ['1','2','3','4','5','6']:
                    break                
        else:
            print('you added this month already!!!!\n')
            menu()
            while True:
                action=input('enter the action you would like to take ')
                if action in ['1','2','3','4','5','6']:
                    break

    elif action=='2':
        month_name=input('Enter the name of the month you would like to edit: ').lower()
        salary=int(input('Enter the new salary'))
        saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary=calculation(salary,savings_per,rent_per,electricity_per)
        for dic in budget:
            if dic['month_name']==month_name:
                dic.update({"month_name":month_name,'salary':salary,"saving":saving,'rent':rent,'electricity':electricity,'total_spending':total_spending,
                    'remainder':remainder,'yearly_rent':yearly_rent,'yearly_electricity':yearly_electricity,'double_salary':double_salary,'additional_savings':additional_savings})
        menu()
        while True:
            action=input('enter the action you would like to take ')
            if action in ['1','2','3','4','5','6']:
                break        
                       
    elif action=='3':
        month_name=input('enter the month where you had an additional saving: ').lower()

        additional_savings=int(input('Enter your additional savings: '))

        salary=salary+additional_savings
        saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary=calculation(salary,savings_per,rent_per,electricity_per)
        if saving!=0:
            savings_division = additional_savings / saving 
        else:
            savings_division=0
        for dic in budget:
            if dic['month_name']==month_name:
                dic.update({"month_name":month_name,'salary':salary,"saving":saving,'rent':rent,'electricity':electricity,'total_spending':total_spending,
                    'remainder':remainder,'yearly_rent':yearly_rent,'yearly_electricity':yearly_electricity,'double_salary':double_salary,'additional_savings':additional_savings})
        menu()
        while True:
            action=input('enter the action you would like to take ')
            if action in ['1','2','3','4','5','6']:
                break 
    elif action=='4':
        month_name=input('enter the name of the month you want to see: ').lower()
        for dic in budget:
            if dic['month_name']==month_name:
                month_name=dic['month_name']
                salary=dic['salary']
                saving=dic['saving']
                rent=dic['rent']
                electricity=dic['electricity']
                total_spending=dic['total_spending']
                remainder=dic['remainder']
                yearly_rent=dic['yearly_rent']
                yearly_electricity=dic['yearly_electricity']
                double_salary=dic['double_salary']
                additional_savings=dic['additional_savings']
                printing(month_name,salary,saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary,savings_division)
                menu()
                while True:
                    action=input('enter the action you would like to take ')
                    if action in ['1','2','3','4','5','6']:
                        break  
    elif action=='5':
        for dic in budget:
                month_name=dic['month_name']
                salary=dic['salary']
                saving=dic['saving']
                rent=dic['rent']
                electricity=dic['electricity']
                total_spending=dic['total_spending']
                remainder=dic['remainder']
                yearly_rent=dic['yearly_rent']
                yearly_electricity=dic['yearly_electricity']
                double_salary=dic['double_salary']
                additional_savings=dic['additional_savings']
                printing(month_name,salary,saving,rent,electricity,total_spending,remainder,yearly_rent,yearly_electricity,double_salary,savings_division)
        while True:
                action=input('enter the action you would like to take ')
                if action in ['1','2','3','4','5','6']:
                    break       
    elif action=='6': 
        break                  

            