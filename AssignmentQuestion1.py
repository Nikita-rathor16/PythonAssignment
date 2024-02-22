from collections import Counter
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

consecutive_days = [(days_of_week[i], days_of_week[i+1]) for i in range(len(days_of_week)-1)]


day_info_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))


char_occurrences = tuple((day, Counter(day)) for day in days_of_week)


print("list of tuples which has the two consequtive days grouped together")
print(consecutive_days)
print("\nDictionary with day information")
print(day_info_dict)
print("\ntuple with all the characters and their number of occurences in each name of the day.")
print(char_occurrences)