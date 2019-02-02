import csv

star_wars = csv.DictReader(open("star-wars.csv", "r"))
print("-"*90)
print("MAIN CHARACTERS")
print("Star Wars: Episode VII: The Force Awakens (2015)")
print("-"*90)
for entry in star_wars:
    print(entry["name"]," "*(30 - len(entry["name"])), entry["character"]," "* (30 - len(entry["character"])), entry["birthday"])
    
