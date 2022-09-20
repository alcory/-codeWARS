def digitize(n):
    results = list(str(n))
    results.reverse()
    results = [int(number) for number in results.reverse]
    return results




n = 6587921
print(digitize(n))
