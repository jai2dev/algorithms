def count_ways_to_color(n, edges, num_colors):
    dp = [[[-1 for _ in range(num_colors)] for _ in range(2)] for _ in range(n)]

    def dfs(node, parent, is_parent_colored, color_used):
        if dp[node][is_parent_colored][color_used] != -1:
            return dp[node][is_parent_colored][color_used]

        total_ways = 0
        start_color = 0 if is_parent_colored else 1

        for color in range(start_color, num_colors):
            if color != color_used:
                ways_subtree = 1
                for child in edges[node]:
                    if child != parent:
                        ways_subtree *= dfs(child, node, True, color)
                        ways_subtree %= 1000000007  # Modulo to avoid overflow

                total_ways += ways_subtree
                total_ways %= 1000000007  # Modulo to avoid overflow

        dp[node][is_parent_colored][color_used] = total_ways
        return total_ways

    total_ways = dfs(0, -1, False, -1)
    return total_ways

# Example usage
if __name__ == '__main__':
    n = 5
    edges = {
        0: [],
        1: [0, 2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }
    num_colors = 3

    ways = count_ways_to_color(n, edges, num_colors)
    print(ways)
