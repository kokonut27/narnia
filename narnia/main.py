import random
import os
import json

class Assets:
  first_names = [
    "Joe", "Billy", "Bob", "Harry", "Gary", "Liam", "Ella", "Olivia", "Ava", "Noah", "James", "Jake", "William", "Eli", "Aidan", "Jeff", "Isabella", "Violet", "Luna", "Hazel", "Aurora", "Oliver", "Theodore", "Jasper", "Quinn", "Owen", "Ethan", "Luca", "Logan", "Leo", "Eric", "Alexander", "Levi", "Iris", "Nora", "Riley", "Harper", "Artemis", "Juliet", "Jade", "Julian", "John", "Luke", "Lucas"
  ]
  
  last_names = [
    "Smith", "Williams", "Davis", "Jones", "Miller", "Brown", "Lopez", "Wilson", "Martinez", "Lee", "Jackson", "Thomas", "Tayler", "Anderson", "Moore", "White", "Harrison", "Clark", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Torres", "Scott", "Hill", "Green", "Hall", "Nelson", "Baker", "Flores", "Roberts", "Mitchell", "Carter", "Campbell" 
  ]

  def parse_json(tjson):
    return json.dumps(tjson, sort_keys=False, indent=2)

class data:
  def name(num=1):
    all_names = {}
    a = 0
    for _ in range(num):
      a += 1
      all_names[f"name_{str(a)}"] = random.choice(Assets.first_names) + " " + random.choice(Assets.last_names)
      
    return Assets.parse_json(all_names)
  
  def firstName(num=1):
    all_first_names = {}
    a = 0
    for _ in range(num):
      a += 1
      all_first_names[f"firstName_{str(a)}"] = random.choice(Assets.first_names)
  
    return Assets.parse_json(all_first_names)

  def lastName(num=1):
    all_last_names = {}
    a = 0
    for _ in range(num):
      a += 1
      all_last_names[f"lastName_{str(a)}"] = random.choice(Assets.last_names)
      
    return Assets.parse_json(all_last_names)

class experiments:
  def __init__(self, num=1):
    pass

# print(data.lastName(2))