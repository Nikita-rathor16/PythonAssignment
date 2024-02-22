from tabulate import tabulate
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
day_info_dict = {}
for i, day in enumerate(days_of_week, start=1):
    day_info_dict[day] = (i, day[:3], day.lower(), day.upper(), len(day))
print("+------------+------------+------------+------------+------------------------+")
print("| Day        | Occurrence | Short      | Lowercase  | Uppercase  | Length    |")
print("+------------+------------+------------+------------+------------------------+")
for day, info in day_info_dict.items():
    print("| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}|".format(day, *info))
print("+------------+------------+------------+------------+------------------------+")

# headers = ["Name of the Day", "Occurrences", "Short Form", "Name in lower", "Name in upper", "Length"]
 
# table = []
# for day, info in day_info_dict.items():
#     sublist = [day]
#     #print(sublist)
#     for header in headers[1:]:
#         sublist.append(info[header])
#         #print(sublist)
#     table.append(sublist)
# #print(table)
# print(tabulate(table, headers=headers,tablefmt='grid'))

# print("{:<15} {:<12} {:<10} {:<15} {:<15} {:<7}".format(
#     "Name of the Day", "Occurences", "Short Form", "Name in Lower", "Name in Upper", "Length"
# ))
# for day, info in day_info_dict.items():
#     print("{:<15} {:<12} {:<10} {:<15} {:<15} {:<7}".format(
#         day, *info
#     ))