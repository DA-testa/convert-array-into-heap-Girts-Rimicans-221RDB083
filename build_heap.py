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

def create_heap(swaps, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and swaps[left] > swaps[largest]:
        largest = left

    if right < n and swaps[right] > swaps[largest]:
        largest = right

    if largest != i:
        swaps[i], swaps[largest] = swaps[largest], swaps[i]

        create_heap(swaps, n, largest)

def build_heap(data):
    swaps = data
    n = len(swaps)
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
        create_heap(swaps, n, i)

    return swaps

def main():
    n = 0
    data = []

    try:
        key = input().strip()
        # print(key)
        if (key.upper() == "I"):
            n, data = parse_input_user()
        elif (key.upper() == "F"):
            file_name = input().strip()
            if (file_name.lower() == "a"):
                pass
            n, data = parse_input_file("test/" + file_name)
    except:
        pass

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
