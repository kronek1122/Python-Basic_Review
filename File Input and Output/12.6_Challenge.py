from pathlib import Path
import csv

score = []
high_score = {}
path = Path.home()/ "scores.csv"

with path.open(mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        score.append(row)

for dic in score:
    name = dic['name']
    score = int(dic['score'])
    if name not in high_score:
        high_score[name] = score
    else:
        if high_score[name] < score:
            high_score[name] = score


print(high_score)
path = Path.home()/ "high_scores.csv"

with path.open(mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'high score'])
    writer.writeheader()
    for name in high_score:
        row_dic = {'name': name, 'high score': high_score[name]}
        writer.writerow(row_dic)
