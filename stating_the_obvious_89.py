#pick numbers from 100 to 999999, and try to check 
# if perfect square and if 2 * the number = two, and
#  do all the necessary checks as well



def check_perfect_square(num):
    root = int(num**0.5)
    return root * root == num


def find_numbers():
    results = {}
    for num in range(100, 1000000):
        if check_perfect_square(num):
            twice = 2 * num
            if len(str(twice)) <= 6 and (str(twice)[-2:] == str(num)[:2] or str(twice)[-1:] == str(num)[:1]):
                results[num] = 2 * num  
    return results

if __name__ == "__main__":
    numbers = find_numbers()
    for num, double in numbers.items():
        print(f"Number: {num}, Double: {double}")
            