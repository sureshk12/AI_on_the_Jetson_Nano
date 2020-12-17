import sys

# print(sys.version)

# #print(sys.version)
# print(sys.executable)

william_test = ["Ankitha", "Suresh", "Vidya", "Ashwin", "Divya", "Alby", "Appa"]

print(william_test)
for a in william_test:
    print(a)

william_test.sort()
print(william_test)

with open('suresh.txt','w+') as file:
    for a in william_test:
        file.write(a + '\n')