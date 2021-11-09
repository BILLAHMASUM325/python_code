fh = open('mbox-short.txt')
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

fh = open('mbox-short.txt')
for lx in ly:
    ly = lx.rstrip()
    print(ly.upper())

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# searching through a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    if line.startswith('From: '):
        print(line)
# remove newline
fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

fruit = "banana"
x = fruit[1]
print(x)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year; ', friend)

friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year: ', friend)

