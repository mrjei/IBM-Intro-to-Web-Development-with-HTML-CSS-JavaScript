first_name = "John"
last_name = "Dough"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
print(type(full_name))

age = 25
age += 1
print("Your age is: "+str(age))
print(type(age))

human = True
print("Are you a human: "+str(human))
print(type(human))

first = input("First: ")
second = input("Second: ")
print(sum)

first = input("First: ")
second = input("Second: ")
sum = first  + second
print("Sum: " + str(sum))

#course = 'Python for Beginners'
#print(course.upper())
#print(course.find('y'))
#print(course.replace('for', '4'))
#print('Python' in course)

#print(10 / 3)
#print(10 // 3)

#x=10
#x = x + 3
#x += 3

#x = 10 + 3 * 2
#print(x)

#x2 = (10 + 3) * 2
#print(x2)

#x = 3 > 2
#print(x)

#x = 3 == 2
#print(x)

#x = 3 != 2
#print(x)

#price = 25
#print(price > 10 and price < 30)

#and (both)
#or (at least one)
#not

temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30)
    print("It's a nice day")
print("Done")

temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30)
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

Weight = int(input("Weight: "))
unit = input ("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = Weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = Weight * 0.45
    print("Weight in Kgs: " + str(converted))
