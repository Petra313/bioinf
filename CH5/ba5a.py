with open('rosalind_ba5a (5).txt', 'r') as f:
    money = int(f.readline().strip())
    coins = list(map(int, f.readline().strip().split(',')))

def min_coins(money, coins):
    min_count = [float('inf')] * (money + 1)
    min_count[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                min_count[m] = min(min_count[m], min_count[m - coin] + 1)
    
    return min_count[money]

result = min_coins(money, coins)
print(result)
