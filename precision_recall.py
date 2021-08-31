import csv

true_positives = {}
false_positives = {}
false_negatives = {}

precision = {}
recall = {}

path = "/Users/tomasmamede/Documents/Investigação/Paper Lepilens/lepilens_model_res.csv"

conf_matrix = {}

with open(path, 'r') as csv_file:
    lines = csv.reader(csv_file)
    next(lines)

    ################# Preparação matriz #################
    for line in lines:
        conf_matrix[line[1]] = {}

        true_positives[line[1]] = 0
        false_negatives[line[1]] = 0
        false_positives[line[1]] = 0

    for species_line in conf_matrix:
        for species_column in conf_matrix:
            conf_matrix[species_line][species_column] = 0

    #################

    csv_file.seek(0)
    next(lines)

    for line in lines:
        conf_matrix[line[1]][line[2]] += 1


    for species in conf_matrix:
        true_positives[species] = conf_matrix[species][species]
        precision[species] = 0.0
        recall[species] = 0.0

    for species_line in conf_matrix:
        for species_column in conf_matrix:

            if species_line == species_column:
                continue

            false_positives[species_line] += conf_matrix[species_line][species_column]
            false_negatives[species_line] += conf_matrix[species_column][species_line]

        # print(species_line, true_positives[species_line], false_positives[species_line], false_negatives[species_line])

    total_true_positives = 0
    total_false_positives = 0
    total_false_negatives = 0

    division_by_zero = False
    for species in conf_matrix:

        if (true_positives[species] + false_positives[species]) == 0:
            division_by_zero = True
            precision[species] = 0.0

        if (true_positives[species] + false_negatives[species]) == 0:
            division_by_zero = True
            recall[species] = 0.0

        if division_by_zero:
            division_by_zero = False
            continue

        precision[species] = true_positives[species] / (true_positives[species] + false_positives[species])
        recall[species] = true_positives[species] / (true_positives[species] + false_negatives[species])

        total_true_positives += true_positives[species]
        total_false_positives += false_positives[species]
        total_false_negatives += false_negatives[species]

    print("SPECIES,PRECISION,RECALL")
    for key in sorted(conf_matrix):
         print('{},{:.3f},{:.3f}'.format(key, precision[key], recall[key]))

    total_precision = total_true_positives / (total_true_positives + total_false_positives)
    total_recall = total_true_positives / (total_true_positives + total_false_negatives)

    print('{},{:.3f},{:.3f}'.format("Total", total_precision, total_recall))