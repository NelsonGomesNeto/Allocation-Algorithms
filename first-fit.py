def readQuery():
    line = input().split()
    return(line[0], line[1], int(line[2]))

memorySize = int(input())
print("memory size:", memorySize, end="\n\n")
allocated = set()

queries = int(input())
while (queries):
    query = readQuery()
    if (query[0] == 'A'):
        id, allocationSize = query[1:]
        now = [0, memorySize - 1, id]

        if (len(allocated)):
            for s, e, i in allocated:
                now[1] = s
                break
        for s, e, i in sorted(allocated):
            if (s - now[0] >= allocationSize):
                now[1] = now[0] + allocationSize
                break
            now[0] = e + 1

        else:
            now[1] = memorySize - 1
        now[1] = now[0] + allocationSize
        if (now[1] < memorySize and now[1] - now[0] >= allocationSize):
            # now[1] = now[0] + allocationSize
            allocated.add(tuple(now))
            print("\tFitted at", now[0], now[1])
        else:
            print("\tDoesn't fit")
    if (query[0] == 'F'):
        p, id = False, query[1]
        for s, e, i in allocated:
            if (i == id):
                p = (s, e, i)
        if (p):
            print("\tRemoved", id)
            allocated.remove(p)
    print("memory:", sorted(allocated))
    queries -= 1
