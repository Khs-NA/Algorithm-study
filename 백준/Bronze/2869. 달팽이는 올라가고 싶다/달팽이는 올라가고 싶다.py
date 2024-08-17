def calculate_days(A, B, V):
    # Edge case: If A is greater than or equal to V, you need only one day
    if A >= V:
        return 1
    
    # Net gain per day after a full cycle
    net_gain = A - B
    
    # Remaining height to reach (excluding the last day)
    remaining_height = V - A
    
    # Calculate number of full cycles required
    full_cycles = (remaining_height + net_gain - 1) // net_gain
    
    # Total days is the number of full cycles plus the last day
    return full_cycles + 1

# Reading input
A, B, V = map(int, input().split())

# Calculate and print the result
print(calculate_days(A, B, V))
