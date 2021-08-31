import csv

dict_top_1 = {}
dict_top_5 = {}
dict_out_top_5 = {}

path = "/Users/tomasmamede/Documents/Investigação/Paper Lepilens/lepilens_model_res.csv"

print("SPECIES,TOTAL_IMAGES,TOP_1,TOP_5,TOP_1(%),TOP_5(%)")

with open(path, 'r') as csv_file:
    lines = csv.reader(csv_file)
    next(lines)

    for line in lines:
        if line[1] == line[2]:
            if line[1] in dict_top_1:
                dict_top_1[line[1]] = dict_top_1[line[1]] + 1
            else:
                dict_top_1[line[1]] = 1
                dict_top_5[line[1]] = 0
                dict_out_top_5[line[1]] = 0
        elif line[1] == line[4] or line[1] == line[6] or line[1] == line[8] or line[1] == line[10]:
            if line[1] in dict_top_5:
                dict_top_5[line[1]] = dict_top_5[line[1]] + 1
            else:
                dict_top_1[line[1]] = 0
                dict_top_5[line[1]] = 1
                dict_out_top_5[line[1]] = 0
        else:
            if line[1] in dict_out_top_5:
                dict_out_top_5[line[1]] = dict_out_top_5[line[1]] + 1
            else:
                dict_top_1[line[1]] = 0
                dict_top_5[line[1]] = 0
                dict_out_top_5[line[1]] = 1

    total_top_1 = 0
    total_top_5 = 0

    for key in sorted(dict_top_1):
        total = dict_top_1[key] + dict_top_5[key] + dict_out_top_5[key]
        top_1 = dict_top_1[key]
        top_5 = dict_top_1[key] + dict_top_5[key]
        percent_top_1 = top_1 / total
        percent_top_5 = top_5 / total

        total_top_1 += top_1
        total_top_5 += top_5

        print('{},{},{},{},{:.2f},{:.2f}'.format(key, total, top_1, top_5, percent_top_1, percent_top_5))

    print('{},{},{},{},{:.2f},{:.2f}'.format("Total", " ", total_top_1, total_top_5, total_top_1 / total, total_top_5 / total))









