import timeit

start = timeit.default_timer()

for i in range(78495):
    for j in range(188):
        internum = len(set([1, 2, 3, 5, 6, 7, 8, 9, 10]).intersection(set([6, 7, 8, 9, 10, 11, 12, 13, 14])))
        unionnum = len(set([1, 2, 3, 5, 6, 7, 8, 9, 10]).union(set([6, 7, 8, 9, 10, 11, 12, 13, 14])))
        result = internum / unionnum
    print(i)
end = timeit.default_timer()
print(str(end - start))
