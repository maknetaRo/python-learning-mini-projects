# The fourth out of hundred pro/g/ramming challenge
print("This small program calculate your age in seconds.")

from datetime import date
year = int(input("What year were you born in?: "))
month = int(input("What month were you born in? (give the number): "))
day = int(input("What day were you born in? "))
your_birthday = date(year, month, day)
print(your_birthday)
today = date.today()
print(today)
age_days = today - your_birthday
age_days = age_days.days
print("You are  {} days old.".format(age_days))
age_seconds = int(age_days) * 86400


print("You are  about {} seconds old.".format(age_seconds))