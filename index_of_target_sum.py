def get_aspected_index(two_pair_values, target_value):
    # write your code here
    list2=[]
    for i in range(len(two_pair_values)):
        list = two_pair_values[i]
        if sum(list) == target_value:
            list2.append(i)
    return list2

two_pair_values = [
[1, 5],
[9, -7],
[0, 8],
[6, 4],
[4, 11],
[14, 0],
[8, 1],
[4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)