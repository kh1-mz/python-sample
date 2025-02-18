"""text_file_read-except.py
"""
FILENAME = 'cities.txt'

try:
    f = open(FILENAME, 'r')
    for line in f.readlines():
        print(line.rstrip())  # rstripで改行を削除
except:
    print(f'ERROR: {FILENAME}: open error')
else:
    f.close()
finally:
    print('done')
