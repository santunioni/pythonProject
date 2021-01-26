"""
Writing in CSV files

Use the analogous to the method you chose to read:
 - reader() -> writer(), writerow()
 - DictReader() -> DictWriter()
"""

from csv import writer, DictWriter

# with open('filmes.csv', 'w') as file:
#     csv_writer = writer(file)
#     movie = None
#     csv_writer.writerow(['Title', 'Genre', 'Duration'])
#     while movie != 'quit':
#         movie = input('Inform the movie name: ')
#         if movie != 'quit':
#             genre = input('Inform the genre: ')
#             duration = input('Inform the duration (minutes): ')
#             csv_writer.writerow([movie, genre, duration])


# Using DIctWriter
with open('filmes.csv', 'w') as file:
    head = ['Title', 'Genre', 'Duration']
    csv_writer = DictWriter(file, fieldnames=head)
    csv_writer.writeheader()
    movie = None
    while movie != 'quit':
        movie = input('Inform the movie name: ')
        if movie != 'quit':
            genre = input('Inform the genre: ')
            duration = input('Inform the duration (minutes): ')
            csv_writer.writerow({head[0]: movie, head[1]: genre, head[2]: duration})


