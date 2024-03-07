"""import"""
import time
from tabulate import tabulate
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
day_names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
dict_1 = {}
@log_execution_time
def tables():
    """print in table format"""
    for i, day in enumerate(day_names, start=1):
        dict_1[day] = {
            "Occurrences": i,
            "Short Form": day[:3],
            "Name in lower": day.lower(),
            "Name in upper": day.upper(),
            "Length": len(day)
        }
    headers = ["Name of the Day", "Occurrences", "Short Form",
               "Name in lower", "Name in upper", "Length"]
    table = []
    for day, info in dict_1.items():
        list_1 = [day]
        for header in headers[1:]:
            list_1.append(info[header])
        table.append(list_1)
    print(tabulate(table, headers=headers, tablefmt='grid'))
tables()
