import csv

path = "/Users/tomasmamede/Documents/Investigação/Paper Lepilens/lepilens_model_res.csv"

species_dict = {}

with open(path, 'r') as csv_file:
    lines = csv.reader(csv_file)
    next(lines)

    ################# Preparação matrix #################
    for line in lines:
        species_dict[line[1]] = {}
    for species_line in species_dict:
        for species_column in species_dict:
            species_dict[species_line][species_column] = 0

    #################

    csv_file.seek(0)
    next(lines)

    for line in lines:
        species_dict[line[1]][line[2]] += 1

    ################# Print matrix #################

    count = 0 # Não deixa ficar com mais uma coluna
    print(" ,", end="")
    for species in sorted(species_dict):
        if count < len(species_dict) - 1:
            print(species, ",", end="")
        else:
            print(species, end="")
        count += 1
    print()

    for species_line in sorted(species_dict):
        print(species_line, ",", end="")
        count = 0
        for species_column in sorted(species_dict[species_line]):
            if count < len(species_dict) - 1:
                print(species_dict[species_line][species_column], ",", end="")
            else:
                print(species_dict[species_line][species_column], end="")
            count += 1
        print()

    #################


