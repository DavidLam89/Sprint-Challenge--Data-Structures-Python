import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

with open('names_1.txt', 'r') as f1, open('names_2.txt', 'r') as f2:
    duplicates = []
    myset = set()
    for line in f1:
        myset.add(line)
    for line in f2:
        if line in myset:
            duplicates.append(line.strip())

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

