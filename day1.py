def read_number_pairs(filename):
    first_numbers = []
    second_numbers = []
    
    with open(filename, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.strip().split())
            first_numbers.append(num1)
            second_numbers.append(num2)
    
    return first_numbers, second_numbers

if __name__ == "__main__":
    first_list, second_list = read_number_pairs('day1input.txt')
    print("First numbers:", first_list[0:10])
    print("Second numbers:", second_list[0:10])

    order_first_list = sorted(first_list)
    order_second_list = sorted(second_list)
    
    print(order_first_list)
    print(order_second_list)

    total_distance = 0

    for i in range(len(order_first_list)):
        total_distance += abs(order_first_list[i] - order_second_list[i])

    print(f"Answer part1: {total_distance}")

    #part 2:
    similarity_score = 0
    for element in first_list:
        els_in_second = [x for x in second_list if x == element]
        similarity_score += element * len(els_in_second)
    print(f"Answer part2: {similarity_score}")