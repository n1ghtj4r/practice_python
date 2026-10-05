def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if square_target == 0:
        print(f"The square root of {square_target} is 0")
        return 0
    if square_target == 1:
        print(f"The square root of {square_target} is 1")
        return 1

    # Special low/high for numbers between 0 and 1
    low = square_target if square_target < 1 else 1
    high = 1 if square_target < 1 else square_target
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid ** 2

        if high - low <= tolerance:          # ← key difference
            root = mid
            break

        if square_mid < square_target:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {max_iterations} iterations")
        return None
    else:
        print(f"The square root of {square_target} is approximately {root}")
        return root

# --- Test the function ---

print("--- 0 ---")
print(square_root_bisection(0))

print("\n--- 1 ---")
print(square_root_bisection(1))

print("\n--- 0.001 ---")
print(square_root_bisection(0.001, 1e-7, 50))

print("\n--- 0.25 ---")
print(square_root_bisection(0.25, 1e-7, 50))

print("\n--- 81 ---")
print(square_root_bisection(81, 1e-3, 50))

print("\n--- 225 (should fail) ---")
print(square_root_bisection(225, 1e-7, 10))