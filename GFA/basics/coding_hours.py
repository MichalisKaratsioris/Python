# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

hours_daily = 6
semester_weeks = 17
days = 5
avrg_working_weekly_hours = 52

total_hours_per_attendee = days * semester_weeks * hours_daily
print("total hours: " + str(total_hours_per_attendee) + " hours")
print("percentage coding hours: " + str(hours_daily * days / 52 * 100) + " %")
print("percentage coding hours (rounded): " + str(int((hours_daily * days + 0.5) * 100 // 52)) + " %")
