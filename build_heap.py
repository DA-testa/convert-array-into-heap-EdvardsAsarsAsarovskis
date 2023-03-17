# python3


def build_heap(data):
    swaps = []
    n = len(data)
    
    # loop through the elements in reverse order from the middle
    # (the middle index of a heap is n/2 - 1)
    for i in range(n//2 - 1, -1, -1):
        sift_down(data, i, swaps)
        
    # heap sort
    for i in range(n-1, 0, -1):
        # move the root of the heap (which is the maximum element) to the end
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        
        # maintain the heap property by sifting down the new root
        sift_down(data, 0, swaps, i)
        
    return swaps

def sift_down(data, i, swaps, n=None):
    if n is None:
        n = len(data)
    while i < n//2:
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        # choose the child with the larger value
        if right_child < n and data[right_child] > data[left_child]:
            j = right_child
        else:
            j = left_child
        
        # if the parent has a larger value than the larger child, stop sifting down
        if data[i] >= data[j]:
            break
        
        # otherwise, swap the parent and child and continue sifting down
        swaps.append((i, j))
        data[i], data[j] = data[j], data[i]
        i = j


def main():
    
    # TODO: Add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_type = input("Enter input type (K for keyboard input, F for file input): ")

    if input_type == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        # checks if length of data is the same as the said length
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

    elif input_type == "F":
        # input from file
        filename = input("Enter filename: ")
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

            # checks if length of data is the same as the said length
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

    else:
        print("Invalid input type")


if __name__ == "__main__":
    main()
