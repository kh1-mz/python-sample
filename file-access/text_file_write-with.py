"""text_file_write-with.py
"""
FILENAME = 'animals.txt'
ANIMALS = ['dog', 'cat',
           'monkey', 'elephant',
           'zebra']

with open(FILENAME, 'w') as f:
    for animal in ANIMALS:
        f.write(animal+'\n')
   
print('done')
