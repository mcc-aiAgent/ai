import jsonpath
import json

book_json = """
{
  "store": {
      "book": [
        { "category": "reference",
          "author": "Nigel Rees",
          "title": "Sayings of the Century",
          "price": 8.95
        },
        { "category": "fiction",
          "author": "J. R. R. Tolkien",
          "title": "The Lord of the Rings",
          "isbn": "0-394-19394-8",
          "price": 22.99}
        ],
      "bicycle": {
        "color": "red",
        "price": 19.95}
  }
}
"""
books = json.loads(book_json)
print(type(books))  # <class 'dict'>
json_expression = "$.store.bicycle.color"
result = jsonpath.jsonpath(books, json_expression)
print(result)

json_expression = "$.store.book[*]"
result = jsonpath.jsonpath(books, json_expression)
print(result)
