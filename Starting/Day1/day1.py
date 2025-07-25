hello = "Hello, World!"
print(hello)
print("This is a new Python file.")

list = [1,2,3,4,5]
list.append(6)
print(list)

books = ["1984", "To Kill a Mockingbird", "The Great Gatsby"]
for book in books:
    print(f"Book title {book}")

list.pop(4)
print(list)

list.remove(4)
print(len(list))

print(list)

#list comperehension
[ print (x) for x in list]

new_list = ['book', 'pen', 'ruler','pencil']
i = 0
while i < len(new_list):
    print(new_list[i])
    i += 1

