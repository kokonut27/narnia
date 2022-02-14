import random
import os

class Assets:
  first_names = [
    "Joe", "Billy", "Bob", "Harry", "Gary", "Liam", "Ella", "Olivia", "Ava", "Noah", "James", "Jake", "William", "Eli", "Aidan", "Jeff", "Isabella", "Violet", "Luna", "Hazel", "Aurora", "Oliver", "Theodore", "Jasper", "Quinn", "Owen", "Ethan", "Luca", "Logan", "Leo", "Eric", "Alexander", "Levi", "Iris", "Nora", "Riley", "Harper", "Artemis", "Juliet", "Jade", "Julian", "John", "Luke", "Lucas"
  ]
  
  last_names = [
    "Smith", "Williams", "Davis", "Jones", "Miller", "Brown", "Lopez", "Wilson", "Martinez", "Lee", "Jackson", "Thomas", "Tayler", "Anderson", "Moore", "White", "Harrison", "Clark", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Torres", "Scott", "Hill", "Green", "Hall", "Nelson", "Baker", "Flores", "Roberts", "Mitchell", "Carter", "Campbell" 
  ]

class data:
  def name(num=1):
    all_names = []
    for _ in range(num):
      all_names.append(random.choice(Assets.first_names) + " " + random.choice(Assets.last_names))
      
    return "\n".join(all_names)
  
  def firstName(num=1):
    all_first_names = []
    for _ in range(num):
      all_first_names.append(random.choice(Assets.first_names))
  
    return "\n".join(all_first_names)

  def lastName(num=1):
    all_last_names = []
    for _ in range(num):
      all_last_names.append(random.choice(Assets.last_names))
    return "\n".join(all_last_names)

class experiments:
  def __init__(self, num=1):
    pass

print(data.lastName(2))