def hashFunction(key, length):
    return key % length


def insert(table, key):
    table[hashFunction(key, len(table))].append(key)


def get(table, key):
    if table:
        if any(value == key for value in table[hashFunction(key, len(table))]):
        	return key
        else: return None
    else: return None


table = [[] for x in range(10)]

insert(table, 32)
insert(table, 3)
insert(table, 24)
insert(table, 40)
insert(table, 22)
insert(table, 99)
insert(table, 71)
insert(table, 13)
insert(table, 15)
insert(table, 69)
insert(table, 28)
insert(table, 26)
insert(table, 52)

print table
print get(table, 13)
print get(table, 32)
print get(table, 12)
