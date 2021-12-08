list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list3 = []

for i in list1:
    if i % 2 != 0:
        list1.remove(i)
        list2 = list1
print('hazf adad fard:', list2)

for i in list2:
    l1 = i * i
    list3.append(l1)

print('baghi mande be tavaan 2:', list3)
