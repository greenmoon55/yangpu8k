import csv
from collections import defaultdict
import datetime

import pygal

def hms_to_seconds(t):
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s

def get_tuples():
    tuples = []
    with open('result.csv', 'rb') as csvfile:
        r = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in r:
            uid = row[0]
            t = row[1]
            if t == 'None':
                continue
            t = hms_to_seconds(t)
            tuples.append((uid, t))
    return tuples

def draw(values):
    from datetime import datetime, timedelta
    date_chart = pygal.Line(x_label_rotation=20, x_labels_major_every=5, show_minor_x_labels=False)
    date_chart.x_labels = range(90)
    date_chart.add("Count", map(lambda x: x[1], values))
    date_chart.render_to_file('chart.svg')
    

if __name__ == "__main__":
    results = get_tuples()
    d = defaultdict(int)
    for row in results:
        time = row[1]
        minute = time / 60
        d[minute] += 1
    print d
    values = [(k, d.get(k)) for k in range(90)]
    print values
    draw(values)

