def greedy_sorting(str_permutation):
    helper = [int(x) for x in str_permutation[1:-1].split()]

    S = []

    for i in range(0, len(helper)):
        if helper[i] == i + 1:
            continue

        idx = i
        while True:
            if helper[idx] == i + 1 or helper[idx] == -1 * (i + 1):
                break
            idx += 1

        mid = [-1 * x for x in helper[i : (idx + 1)]][::-1]
        helper = helper[0:i] + mid + helper[(idx + 1) :]
        S.append(helper.copy())

        if helper[i] < 0:
            helper[i] = abs(helper[i])
            S.append(helper.copy())

    return S


def change(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"
    
def rosalindPrint(permutations):
    strings = []
    for perm in permutations:
        strings.append("(" + " ".join([change(int(x)) for x in perm]) + ")")
    return "\n".join(strings)

with open("rosalind_ba6a (1).txt","r")as f:
    inlines = [x.strip("\n") for x in f.readlines()]
    res = greedy_sorting(inlines[0])
    print(rosalindPrint(res))