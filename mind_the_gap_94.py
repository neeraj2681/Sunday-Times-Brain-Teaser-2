#generating the average and calculating the closest difference


def get_all_numbers(start='1023456789'):
    from itertools import permutations

    digits = list(start)
    all_numbers = set()
    for length in range(2, len(digits) + 1):
        for perm in permutations(digits, length):
            if perm[0] != '0':  # avoid leading zeros
                num = int(''.join(perm))
                if len(str(num)) == 10:
                    all_numbers.add(num)
    return sorted(all_numbers)



def get_min_difference(numbers):
    min_diff = float('inf')
    closest_num = None
    avg = 0

    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        avg+=(diff / (len(numbers) - 1))

    for i in range(len(numbers) - 1):
        diff = abs((numbers[i+1] - numbers[i]) - avg)
        if diff < min_diff:
            min_diff = diff
            closest_num = numbers[i+1] - numbers[i]
    return closest_num, min_diff

if __name__ == "__main__":    
    nums = get_all_numbers()
    # avg = get_average(nums)
    closest, difference = get_min_difference(nums)
    print(f"Closest difference to average: {closest}")
