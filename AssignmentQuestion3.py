import pandas as pd
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
day_info_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))
   


df = pd.DataFrame.from_dict(day_info_dict, orient='index', columns=["Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"])
df.to_excel("days.xlsx", index_label="Name of the Day")
