import csv
import sys
import tfmodel

model_file = "/Users/tomasmamede/Documents/Investigação/Paper Lepilens/Model Files/model.tflite"
dict_file = "/Users/tomasmamede/Documents/Investigação/Paper Lepilens/Model Files/dict.txt"

model = tfmodel.Model(model_file, dict_file)
files = ["image_classification_1.csv", "image_classification_2.csv"]

print("IMAGE NAME, CORRECT LABEL, CLASS_1, CONF_1, CLASS_2, CONF_2, CLASS_3, CONF_3, CLASS_4, CONF_4, CLASS_5, CONF_5")

for file in files:
    path = "../Model Data/" + file
    with open(path, 'r') as csv_file:
        lines = csv.reader(csv_file)
        next(lines)

        for line in lines:

            if line[0] == "TEST":

                image_name = line[1].split("/")[5]
                correct_label = line[2]

                image_path = "../Model Data/files/" + image_name
                results = model.classify(image_path, 5, 0.0)

                print('{},{},{},{:.2f},{},{:.2f},{},{:.2f},{},{:.2f},{},{:.2f}'.format(image_name, correct_label, results[0][0], results[0][1], results[1][0], results[1][1], results[2][0], results[2][1], results[3][0], results[3][1], results[4][0], results[4][1]))





