# Write script that will print all books and their titles like “Alice in Wonderland” ­ Lewis
# Carroll.
import xml.dom.minidom

doc = xml.dom.minidom.parse("books.xml")
books = doc.getElementsByTagName("book")

for book in books:
    title = book.getElementsByTagName("title")
    author = book.getElementsByTagName("author")
    print(title[0].firstChild.nodeValue, '-', author[0].firstChild.nodeValue)
