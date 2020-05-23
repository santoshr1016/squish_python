record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(name)
print(email)
print(phone)

records = [
         ('foo', 1, 2),
         ('bar', 'hello'),
         ('bar', 'mr'),
         ('bar', 'white'),
         ('foo', 3, 4),
    ]


def do_foo(*args):
    print("Inside foo")
    print(args)


def do_bar(*args):
    print("Inside bar")
    print(args)


for tag, *args in records:
    if tag == 'foo':
        # print(args)
        do_foo(*args)
    if tag == 'bar':
        # print(args)
        do_bar(*args)
