'''15, 11, 27, 8, 12
0: -
1: 15
2: -
3: -
4: 11
5: -
6: 27


'''

class HashTable:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for _ in range(b)]

    def hashFunction(self, x):
        return x % self.BUCKET

    def insertItem(self, key):
        index = self.hashFunction(key)
        self.table[index].append(key)

    def deleteItem(self, key):
        index = self.hashFunction(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def displayHash(self):
        for i in range(self.BUCKET):
            print(i, end="")
            for x in self.table[i]:
                print(" -->", x, end="")
            print()

if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]

    h = HashTable(7)
    for key in a:
        h.insertItem(key)

    x = int(input())
    h.deleteItem(x)
    h.displayHash()