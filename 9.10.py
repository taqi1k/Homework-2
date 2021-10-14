# Taqi Syed
# 1863528

import csv

input1 = input()

with open(input1, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        list_of_words = row

no_duplicates_in_list = list(dict.fromkeys(list_of_words))
listlength = len(no_duplicates_in_list)

for i in range(listlength):
    print(no_duplicates_in_list[i], list_of_words.count(no_duplicates_in_list[i]))
