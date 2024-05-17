# counties = ["Arapahoe", "Denver", "Jefferson"]
#for loop practice 
# for county in counties:
    # print(county)

#if counties[1] == 'Denver':
  # print(counties[1])

# if counties[3] != 'Jefferson':
#    print(counties[2])

#member operation practice 
# if "Arapahoe" in counties and "El Paso" in counties:
   # print("Arapahoe and El Paso are in the list of counties.")
# else:
    # print("Arapahoe or El Paso is not in the list of counties.")

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
    # print(num)

    #range function simplifying the for loop proccess 
# for num in range(5):
    # print(num)

#for i in range(len(counties)):
 #   print(i)

# counties = ("Arapahoe", "Denver", "Jeffereson")
# for i in range(len(counties)):
    #  print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

#all the ways to find the value of the key items 
for county in counties_dict.values():
    print(county)   

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#to get both the key and the values of the items in the list 
for county, voters in counties_dict.items():
    print(county,voters)
#to get full sentence + key values in output 
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in range(len(voting_data)):
    print(voting_data[county_dict]) 
#prints only the county 
for county in range(len(voting_data)):
      print(voting_data[county]['county'])
#Using nested loop to get the value of each dictionary 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieve just the number of voters 
for county_dict in voting_data:
    print(county_dict['registered_voters'])

print(f{counties_dict}[1])

#new code for opening files in VS2 (main succesful code)
import os 
import csv
 
# Assign a variable for the file to load and the path.
#file_to_load = '/Users/apple/Desktop/Resources/election_results.csv'
file_to_load = os.path.join("/Users/apple/Desktop", "Resources", "election_results.cvs")

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    reader = csv.reader(election_data)
    for row in reader:
     # To do: perform analysis.
     print(row)

#Code for writing in files 
# Add our dependencies.
import csv
import os
# Create a path to Resources folder 
resources_path = "/Users/apple/Desktop/Election_Analysis/Resources"
# Assign a variable to load a file from a path.
file_to_load = os.path.join(resources_path, "election_results.csv")
# Create a path to analysis folder 
desktop_path = "/Users/apple/Desktop"
analysis_path = os.path.join(desktop_path, "analysis")

# Assign a variable to save the file to a path.
file_to_save = os.path.join(analysis_path, "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
      # Print the header row.
     headers = next(file_reader)
     print(headers)

     # Print each row in the CSV file.
     #for row in file_reader:
      # Retriving the first item from the current row 
        #print(row[0])
