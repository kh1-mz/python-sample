"""text_file_read-with.py
"""
FILENAME = 'animals.txt'

with open(FILENAME, 'r') as f:
    for line in f.readlines():
        print(line.rstrip())

print('done')
