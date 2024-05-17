counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} 

for county, population in counties_dict.items():
    print(f"{county} county has {population} registerd voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}] 

for entry in voting_data:
    county = entry["county"]
    registered_voters = entry["registered_voters"]
    print(f"{county} county has {registered_voters} registered voters.")