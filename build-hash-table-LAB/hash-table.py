class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
            # Optional: clean up empty bucket
            if not self.collection[hashed]:
                del self.collection[hashed]

    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]
        return None

# --- Test the HashTable ---
ht = HashTable()

print("Hash of 'golf':", ht.hash('golf'))          # should be 424

ht.add('golf', 'sport')
print("After adding golf:", ht.collection)

ht.add('dear', 'friend')
ht.add('read', 'book')
print("After adding dear and read:", ht.collection)

print("Lookup 'golf':", ht.lookup('golf'))         # sport
print("Lookup 'read':", ht.lookup('read'))         # book
print("Lookup missing key:", ht.lookup('xyz'))     # None

ht.remove('golf')
print("After removing golf:", ht.collection)
print("Lookup 'golf' after remove:", ht.lookup('golf'))  # None