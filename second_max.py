#! /usr/bin/env python3

list  = []
n = int(input("Enter the number of participants : "))

for i in range(1, n+1):
	k = float(input("Enter the score for each participant : "))
	list.append(k)

print(list)
list.sort()
print(list)
#list.reverse()
#print(list)

