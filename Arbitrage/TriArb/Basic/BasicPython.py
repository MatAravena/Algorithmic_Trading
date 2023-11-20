import time

"""
General comments
"""
# Linear comments


# General Variables
car_something = 50
car_value = 321.321
total_value = car_value * car_something
# print(total_value)
# print(type(car_value ))


# Objects Variables
# A Dictionary in Python is an Object in JS
cars_names = ["bmw","audi","mercedes","porche"]
# print(cars_names[0])
carA = { 
    "name":"bmw",
     "value" : 123
     }
carB = { 
    "name":"bmw2",
     "value" : 234
     }
# print(carA["name"])

cars_list = [carA, carB]
print(cars_list[0])
print(cars_list[0]["name"])


# If statement
if cars_list[0]["name"] != "bmw" :
    print("true 1")
elif  cars_list[1]["name"] == "bmw"  :
    print("true 2")
else: 
    print("true 3")

# Conditions    && == and     || == or 


# Turnary if statement 
will_purchase = "yes" if cars_list[0]["name"] == "bmw" else "no"
print(will_purchase)

# For Looppps !
# Position with 1 tab indicate if the next line code is part of the loop or condition
for car in cars_list:
    if car["value"] > 1:
        print(car)
        break

# While Loop
count = 0
# while count < 10:
#     count += 1
#     print(count)
    
while True:
    time.sleep(1)
    print(count)
    count += 1
    if count == 10:
        break


## Getting Data