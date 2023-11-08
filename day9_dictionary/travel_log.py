travel_log = [
  {
      "country" : "France",
      "visits" : 2,
      "cities" : ["abc", "bcd", "efg"]
  },
  {
      "country" : "America",
      "visits" : 7,
      "cities" : ["Selma", "NewYork", "Elbert"]
  },
  {
      "country" : "India",
      "visits" : 5,
      "cities" : ["Amritsar", "Ludhiana", "Jalandhar"]
  }
]

def add_new_country(cou, vis, cit):
  new_con = {}
  new_con["country"] = cou
  new_con["visits"] = vis
  new_con["cities"] = cit

  travel_log.append(new_con)

print(travel_log)
add_new_country("Russia", 20, ["abcd", "bcgd", "ehfg"])
print()
print(travel_log)