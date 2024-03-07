"""import time"""
import time
import pandas as pd
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
#days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
@log_execution_time
def create_excel(days_of_week):
    """create excel file"""
    day_info_dict = {}
    for i, day in enumerate(days_of_week, start=1):
        day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))
    df = pd.DataFrame.from_dict(day_info_dict, orient='index', columns=["Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
    df.to_excel("days.xlsx", index_label="Name of the Day")
create_excel(('Mondaay','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
