"""text_file_read.py
"""
FILENAME = 'cities.txt'

f = open(FILENAME, 'r')
for line in f.readlines():
    print(line)  # 何が表示されるか？

f.close()
print('done')
