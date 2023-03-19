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

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        top = i
        while True:
            left = 2 * top + 1
            right = 2 * top + 2
            if left < n and data[left] < data[top]:
                top = left
            if right < n and data[right] < data[top]:
                top = right
            if i != top:
                data[i], data[top] = data[top], data[i]
                swaps.append((i, top))
                i = top
            else:
                break

    return swaps

def main():
    n = 0
    input_data = []

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
    assert len(input_data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(input_data)

    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
