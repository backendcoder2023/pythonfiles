A = input()
count = 0
max_count = 0

for i in A:
    if i == '1':
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print(max_count)