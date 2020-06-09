#Write script that will change amount of available books for id=2 from 14 to 1
import xml.etree.ElementTree as ET
tree = ET.parse('books.xml')
value = tree.getroot()
root = value[0]

for book in root.findall('book'):
    if book.get('id') == '2':
        book.set('available', '10')

tree.write('books.xml')
