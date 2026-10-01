def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]
    else:
        return [start_num] + range_of_numbers(start_num + 1, end_num)

print(range_of_numbers(1, 9))