# python3

def parse_input_user():
    n = int(input())
    # print(n)
    data = list(map(int, input().strip().split(' ')))
    # print(data)
    return n, data

def parse_input_file(file_name):
    file = open(file_name, "r", -1, "utf-8")
    n = int(file.readline().strip())
    # print(n)
    data = list(map(int, file.readline().strip().split(' ')))
    # print(data)
    return n, data

def create_heap(data, n, i, swaps, swap_amount):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        swap_amount = swap_amount + 1
        swaps.append([data[i], data[largest]])

        data[i], data[largest] = data[largest], data[i]
        create_heap(data, n, largest, swaps, swap_amount)

    return swaps, swap_amount

def build_heap(data, swaps, swap_amount):
    n = len(data)

    for i in range(n//2, -1, -1):
        swaps, swap_amount = create_heap(data, n, i, swaps, swap_amount)
  
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        swaps, swap_amount = create_heap(data, i, 0, swaps, swap_amount)

    return swaps, swap_amount

def main():
    n, swap_amount = 0, 0
    input_data, data, swaps = [], [], []

    try:
        key = input().strip()
        # print(key)
        if (key.upper() == "I"):
            n, input_data = parse_input_user()
        elif (key.upper() == "F"):
            file_name = input().strip()
            if (file_name.lower() == "a"):
                pass
            n, input_data = parse_input_file("tests/" + file_name)
    except:
        pass

    # checks if lenght of data is the same as the said lenght
    data = input_data.copy()
    assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps, swap_amount = build_heap(data, swaps, swap_amount)
    if input_data == data:
        print(0)
        return

    if swaps:
        swaps.pop()
    else:
        print(swap_amount)
        return

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(swap_amount)
    if swap_amount != 0 and swap_amount < 1000:
        # output all swaps
        for i in swaps:
            print(i[0], i[1])


if __name__ == "__main__":
    main()
