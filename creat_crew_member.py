import json

with open('static/img/joseph_joestar.webp', 'rb') as f:
    img1 = f.read()

with open('static/img/caesar_zeppeli.jpeg', 'rb') as f:
    img2 = f.read()

with open('static/img/giorno_govvano.jpg', 'rb') as f:
    img3 = f.read()
crew = [
    {'name': 'Kirill',
     'surname': 'Belous',
     'image': 'joseph_joestar.webp',
     'profession': 'IT developer, planet saver'},
    {'name': 'Mihail',
     'surname': 'Chekardov',
     'image': 'caesar_zeppeli.jpeg',
     'profession': 'IT developer, planet saver'},
    {'name': 'Rinal',
     'surname': 'Akhmetzhanov',
     'image': 'giorno_govvano.jpg',
     'profession': 'it developer, planer saver'}
]

with open('crew.json', 'w') as js:
    json.dump(crew, js, ensure_ascii=False)
