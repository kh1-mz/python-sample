def greeting(**kwargs):
    print(kwargs)

greeting(en='Hello', fr='Bonjour', de='Guten Tag')

greeting_dict = {'en': 'Hello', 'fr': 'Bonjour', 'de': 'Guten Tag'}
greeting(**greeting_dict)
