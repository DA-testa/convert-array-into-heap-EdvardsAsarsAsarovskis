# python3


# python3

def swap(data, swaps, child, parent):
    swaps.append((parent, child))
    data[child], data[parent] = data[parent], data[child]

def HeapUp(data, swaps, m):
    parent = (m-1)//2
    if m == 0:
        return
    if data[m] < data[parent]:
        swap(data, swaps, m, parent)
        HeapUp(data, swaps, parent)

def build_heap(data):
    n = len(data)
    swaps = []

    if n == 0:
        swaps.append(0)
        return swaps

    for i in range(n-1, -1, -1):
        HeapUp(data, swaps, i)

    return swaps


def main():
    input_type = input()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        assert len(swaps) < 4 * n
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif input_type == "F":
        file_name = input().strip()
        file_path = f"tests/{file_name}"
        try:
            with open(file_path, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
                assert len(data) == n
                swaps = build_heap(data)
                assert len(swaps) < 4 * n
                print(len(swaps))
                for i, j in swaps:
                    print(i, j)
        except FileNotFoundError:
            print("File not found error")

if __name__ == "__main__":
    main()