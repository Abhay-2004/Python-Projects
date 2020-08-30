import datetime

age = int(input("Enter your Birth Year: "))

today = datetime.datetime.today().year

def age_calc(age):
    age1_s = age*365*24*60*60
    age2_m = age*365*24*60
    age3_d = age*365
    age4_y = today - age
    return f"Your age is{age1_s} in seconds \nYour age is{age2_m} in minutes \n Your age is{age3_d} in days \nYour age in Years is {age4_y}"

print(age_calc(age))
