#! /usr/bin/env python3
row = ["10/25/13", "08:24:00 AM", "29", "", "01:15:00 PM","27"]

print(row)
target_position = row.index('')
print(target_position)
row.pop(target_position)
print(row)