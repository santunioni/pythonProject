"""
Reading CSV files

CSV - Comma Separated Values

We can collect data from dados.gov.br

Python language possess two different ways to read data in CSV:
  - reader -> allow us to iterate over CSV lines as lists
  - DictReader -> allow us to iterate over CSV lines as OrderedDicts
"""

with open('lutadores.csv') as data_file:
    # Cleaning the data. This is possible but not ideal
    data = data_file.read()
    print(type(data))
    data = data.split('\n')
    print(data)


# Working with Reader
from csv import reader, DictReader

with open('lutadores.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for line in csv_reader:
        print(f'{line[0]} was born in {line[1]} and is {int(line[2])/100} meters high.')
    print(csv_reader)
    print(type(csv_reader))

print("\n\n")

# Working with DictReader
with open('lutadores.csv') as file:
    csv_reader = DictReader(file, delimiter=',')
    for line in csv_reader:
        print(f"{line.get('Nome')} was born in {line.get('País')} and is {int(line.get('Altura (em cm)'))/100} \
        meters high.")

    print("\n")
    print(csv_reader)
    print(type(csv_reader))
    print(dir(csv_reader))
    print(csv_reader.line_num)

