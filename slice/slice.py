class Cat:
    def __getitem__(self, key):
        a = []
        for i in key:
            a.append(i * 2)
        return a

cat = Cat()
x = cat[1,2,3,4,5,6,7,8,9,0]

print(x)

