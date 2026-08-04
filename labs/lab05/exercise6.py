minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Original Minutes:", minutes)
print("Converted Time:", hours, "hours and", remaining_minutes, "minutes")