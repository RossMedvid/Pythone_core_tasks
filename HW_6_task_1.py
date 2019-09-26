def count_positives_sum_negatives(arr):
    p=[]
    n=[]
    if len(arr)==0:
        return []
    else:
        for i in arr:
            if i > 0:
                p.append(i)
            else:
                n.append(i)

    return [len(p),sum(n)]



print(count_positives_sum_negatives([]))