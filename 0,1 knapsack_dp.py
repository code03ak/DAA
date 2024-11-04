def knapsack_dp(weights, values, capacity):
    #finds the maximum achievable value for the knapsack by constructing a DP table.
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp, dp[n][capacity]

def get_selected_items(dp, weights, capacity):
    selected_items, w = [], capacity
    for i in range(len(weights), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    return selected_items[::-1]

def main():
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter weights (space-separated): ").split()))
    values = list(map(int, input("Enter values (space-separated): ").split()))
    capacity = int(input("Enter capacity of knapsack: "))

    dp, max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in Knapsack: {max_value}")
    print("Selected item indices:", get_selected_items(dp, weights, capacity))

if __name__ == "__main__":
    main()
