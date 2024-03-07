"""import time"""
import time
import random
import pandas as pd
from faker import Faker
def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper
@log_execution_time
# Function to generate fake data
def generate_fake_data(num_records):
    """fake data generate"""
    fake = Faker()
    data = []
    for _ in range(num_records):
        emp_id = fake.unique.random_number(digits=5)
        emp_name = fake.name()
        emp_email = fake.email()
        business_unit = fake.random_element(elements=('HR', 'Finance', 'IT', 'Marketing'))
        salary = round(random.uniform(30000, 100000), 2)
        data.append([emp_id, emp_name, emp_email, business_unit, salary])
    return data
fake_data = generate_fake_data(50)
# Save fake data to Excel
df = pd.DataFrame(fake_data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
df.to_excel("Employee_Personal_Details.xlsx", index=False)
@log_execution_time
def get_employee_with_top_salary():
    """top most salary""" 
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    max_salary_row = df[df['Salary'] == df['Salary'].max()]
    return max_salary_row['EMP NAME'].iloc[0]
@log_execution_time
def get_employee_with_less_salary():
    """least salary"""  
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    max_salary_row = df[df['Salary'] == df['Salary'].min()]
    return max_salary_row['EMP NAME'].iloc[0]
@log_execution_time
def get_business_unit_with_top_salary():
    """top salary according to business unit"""
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    top_business_unit = df.groupby('Business Unit')['Salary'].sum().idxmax()
    return top_business_unit
@log_execution_time
def get_employee_with_top_salary_in_each_unit():  #c
    """top most salary in each business unit"""
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    result = {}
    for unit in df['Business Unit'].unique():
        unit_df = df[df['Business Unit'] == unit]
        max_salary_row = unit_df[unit_df['Salary'] == unit_df['Salary'].max()]
        result[unit] = max_salary_row['EMP NAME'].iloc[0]
    return result
@log_execution_time
def delete_employee_with_least_salary():  #d
    """delete employee least salary"""
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    min_salary_row = df[df['Salary'] == df['Salary'].min()]
    df.drop(min_salary_row.index, inplace=True)
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
@log_execution_time
def update_employee_salary(emp_name, new_salary): #e
    """update salary"""
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    df.loc[df['EMP NAME'] == emp_name, 'Salary'] = new_salary
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
# Testing the functions
print("Employee with top most salary:", get_employee_with_top_salary())
print("Employee with less most salary:", get_employee_with_less_salary())
print("Business Unit with top most aggregated salary:", get_business_unit_with_top_salary())
print("Employee:", get_employee_with_top_salary_in_each_unit())
delete_employee_with_least_salary()
update_employee_salary("Kyle Gross", 95000)
