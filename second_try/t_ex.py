def es5(set1, k):
    if k == 1:
        return set1
    result = set()
    for i in set1:
        val = es5(set1, k-1)
        for partial in val:
            result.add(i+partial)
    return result

print(es5({'a','bb','c'}, 2))