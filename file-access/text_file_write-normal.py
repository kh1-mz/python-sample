""" text_file_write.py
"""
FILENAME = 'cities.txt'
CITIES = ['Tokyo', 'Osaka',
          'Nagoya', 'Yokohama',
          'Fukuoka']

f = open(FILENAME, 'w')
for city in CITIES:
    f.write(city+'\n')
   
f.close()
print('done')
