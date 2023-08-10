import random
import pandas as pd

def generate_dataset(rows, columns):
    dataset = []
    for _ in range(rows):
        row = [random.uniform(-0.2, 0.2) for _ in range(columns)]
        row.sort()
        dataset.append(row)
    return dataset

def print_dataset(dataset):
    for row in dataset:
        print('\t'.join(f'{value:.3f}' for value in row))

rows = 200  # Number of rows in the dataset
columns = 4  # Number of columns in the dataset

dataset = generate_dataset(rows, columns)
# print_dataset(dataset)

df = pd.DataFrame(dataset)

df.to_csv('file1.csv')
