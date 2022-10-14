# EXERCISE 1
# students = ['Jordin','Josh','Asha']

# print(students[1])
# print(students[-1])

# EXERCISE 2
# foods = ('soup', 'chicken', 'apple')

# for food in foods:
  # print(f"{food} is a good food")

# EXERCISE 3
# for food in foods[-2:]:
  # print(food)

# EXERCISE 4

# home_town = {
#   'city': 'Detroit',
#   'state': 'Michigan',
#   'population': '672,351'
# }
# print( f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

#EXERCISE 5
# for key, val in home_town.items():
#   print(f"{key} = {val}")

#EXERCISE 6
# cohort = []
# for idx, student in enumerate(students):
#   cohort.append({'student': student,'fav_food': foods[idx]})
# print(cohort)


# EXERCISE 7

# awesome_students = [f'{student} is awesome' for student in students]
# for student in awesome_students:
  # print(student)

#EXCERCISE 8

# a_foods =[food for food in foods if 'a' in food]
# print(a_foods)