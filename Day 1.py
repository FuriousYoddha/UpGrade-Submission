x = input('Enter the values: ')
y = x.split()
print(y)

val = []

for i in y:
  val.append(int(i))

print( sum (val))