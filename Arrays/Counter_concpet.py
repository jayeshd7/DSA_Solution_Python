from collections import Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
counter = Counter(my_list)

print(counter)
most_common = counter.most_common(3)
print(most_common)
