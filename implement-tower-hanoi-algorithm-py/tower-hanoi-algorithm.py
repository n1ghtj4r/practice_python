def hanoi_solver(n):
    rods = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
        'B': [],
        'C': []
    }
    
    moves = []
    
    def state_str():
        return f"{rods['A']} {rods['B']} {rods['C']}"
    
    moves.append(state_str())
    
    def move(source, target):
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(state_str())
    
    def hanoi(num_disks, source, auxiliary, target):
        if num_disks == 1:
            move(source, target)
        else:
            hanoi(num_disks - 1, source, target, auxiliary)
            move(source, target)
            hanoi(num_disks - 1, auxiliary, source, target)
    
    hanoi(n, 'A', 'B', 'C')
    
    return "\n".join(moves)

# --- Test the function ---
print(hanoi_solver(3))
print("-" * 40)
print(hanoi_solver(2))