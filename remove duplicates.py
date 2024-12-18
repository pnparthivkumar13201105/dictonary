data = {'id1':
        {'name': ['ayush'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id2':
        {'name': ['vasant'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id3':
        {'name': ['parthiv'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id4':
        {'name': ['abdul'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id5':
        {'name': ['parthiv'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id6':
        {'name': ['pranita'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id7':
        {'name': ['mahi'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         'id8':
        {'name': ['shasmeen'],
         'class': ['8b'],
         'sub': ['english,math,science']
         },
         }
result = {}

for key , value in data.items():
    if value not in result.values():
        result[key] = value
print(result)        
