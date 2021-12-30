def fifo():
    count_page_faults = 0

    no_of_frames = int(input("Enter number of frames: "))
    frame = [-1 for i in range(no_of_frames)]
    no_of_pages = int(input("Enter number of pages: "))
    ref_string = list(map(str, input("Enter reference string: ").split()))

    j = 0

    for i in range(0, no_of_pages):
        free = 0
        for k in range(0, no_of_frames):
            if frame[k] == ref_string[i]:
                free = 1

        if free == 0:
            frame[j] = ref_string[i]
            j = (j + 1) % no_of_frames
            count_page_faults = count_page_faults + 1

    print("String after")
    for n in range(0, no_of_frames):
        print(frame[n])

    print("Page faults = " + str(count_page_faults))


def LRU():
    count_page_faults = 0

    no_of_frames = int(input("Enter number of frames: "))
    frame = [-1 for i in range(no_of_frames)]
    fcount = [0 for i in range(no_of_frames)]
    no_of_pages = int(input("Enter number of pages: "))
    ref_string = list(map(str, input("Enter reference string: ").split()))

    count = 0
    while count < no_of_pages:
        j = 0
        flag = 0

        while j < no_of_frames:
            if ref_string[count] == frame[j]:
                flag = 1
                fcount[j] = count + 1
            j = j + 1
        j = 0

        if flag == 0:
            min = 0
            k = 0
            while k < no_of_frames - 1:
                if fcount[min] > fcount[k + 1]:
                    min = k + 1
                k = k + 1
            frame[min] = ref_string[count]
            fcount[min] = count + 1
            count_page_faults = count_page_faults + 1
        count = count + 1

    print("String after")
    for n in range(0, no_of_frames):
        print(frame[n])

    print("Page faults = " + str(count_page_faults))


def optimal():
    count_page_faults = 0
    temp = []
    temp = [0 for i in range(10)]
    no_of_frames = int(input("Enter number of frames: "))
    frame = [-1 for i in range(no_of_frames)]
    no_of_pages = int(input("Enter number of pages: "))
    ref_string = list(map(str, input("Enter reference string: ").split()))

    for i in range(0, no_of_pages):
        flag1 = flag2 = 0
        for j in range(0, no_of_frames):
            if frame[j] == ref_string[i]:
                flag1 = 1
                flag2 = 1
                break

        if flag1 == 0:
            for j in range(0, no_of_frames):
                if frame[j] == -1:
                    count_page_faults = count_page_faults + 1
                    frame[j] = ref_string[i]
                    flag2 = 1
                    break

        if flag2 == 0:
            flag3 = 0
            for j in range(0, no_of_frames):
                temp[j] = -1
                for k in range(i + 1, no_of_pages):
                    if frame[j] == ref_string[k]:
                        temp[j] = k
                        break

            for j in range(0, no_of_frames):
                if temp[j] == -1:
                    position = j
                    flag3 = 1
                    break

            if flag3 == 0:
                max = temp[0]
                position = 0

                for j in range(1, no_of_frames):
                    if temp[j] > max:
                        max = temp[j]
                        position = j

            frame[position] = ref_string[i]
            count_page_faults = count_page_faults + 1

    print("String after")
    for n in range(0, no_of_frames):
        print(frame[n])

    print("Page faults = " + str(count_page_faults))


# main
if __name__ == "__main__":
    case = "Y"
    while case == 'Y' or case == 'y':

        c = str(input("Enter 'f' for FIFO , 'l' for LRU, and 'o' for optimal: "))
        if c == 'f' or c == 'F':
            fifo()
        if c == 'l' or c == 'L':
            LRU()
        if c == 'o' or c == 'O':
            optimal()

        case = str(input("Would you like another algorithm ? type 'Y'... and 'N' to End: "))
