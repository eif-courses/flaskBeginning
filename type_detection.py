import csv
import numpy as np

if __name__ == '__main__':

    temp = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        columns = len(header)
        rows = 0
        for row in reader:
            rows += 1
            for j in range(columns):
                try:
                    if isinstance(int(row[j]), int):
                        # if type(int(row[j])) is int:
                        temp.append('integer')
                except ValueError:
                    temp.append('string')

    l = np.array(temp)
    ilist = l.reshape(rows, columns)

   # int_count = [0, 0, 0, 0]

    int_count = [0] * columns
    str_count = [0] * columns

    # [print(i, end=' ') for i in range(10)]

    for j in range(columns):
        for i in range(rows):
            if ilist[i][j] == 'integer':
                int_count[j] += 1
            elif ilist[i][j] == 'string':
                str_count[j] += 1

    for j in range(columns):
        print(f"{j + 1}: {int_count[j]} integers, {str_count[j]} strings")
