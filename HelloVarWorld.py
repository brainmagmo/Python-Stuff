# make name var
name = ""
#assign it
name = "Chris O'dowd"

#nmake country
country = "United States"

# make age int
age = "69"

#make hourly_wage var (int)
hourly_wage = 11.25

daily_wage = hourly_wage * 8

satisfied = 100 < daily_wage

print(f"Hello {name}!")
print(f"You live in {country}.")
print(f"You are {age} years old.")
print("You make " + str(daily_wage) + " per day")
print(f"are you satisfied with your current wage? {satisfied}")