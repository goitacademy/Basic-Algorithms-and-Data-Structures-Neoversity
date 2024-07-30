def knapsack(values, weights, capacity, i=0):
    if len(values) == i:
        return 0
    elif capacity < 0:
        return float("-inf")
    else:
        return max(values[i]+knapsack(values, weights, capacity-weights[i], i+1),
                   knapsack(values, weights, capacity, i+1))

def find_knapsack_top(values,weights, capacity, i=0, lookup= None):
    lookup = {} if lookup is None else lookup
    if (i,capacity) in lookup:
        return lookup[(i,capacity)]

    if len(values) == i or capacity < 0:
        return 0
    elif (weights[i] > capacity):
        return find_knapsack_top(values, weights, capacity, i+1, lookup)
    else:
        lookup[(i,capacity)] = max(values[i]+ find_knapsack_top(values,weights,capacity-weights[i],i+1,lookup),
                            find_knapsack_top(values, weights,capacity,i+1, lookup))
        return lookup[(i,capacity)]