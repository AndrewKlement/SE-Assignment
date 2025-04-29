def check_input():
    pointer = list(input('give a list from (1 to n) with a double 🥳'))
    turtoise = int(pointer[0])
    hare = int(pointer[0])
    check_progress = True
    while check_progress:
        turtoise = int(pointer[turtoise])
        hare = int(pointer[int(pointer[hare])])
        if turtoise == hare:
            print('meeting point =', turtoise)
            check_progress = False

    pointer1 = int(pointer[0])
    pointer2 = turtoise
    while True:
        if pointer1 == pointer2:
            break
        pointer1 = int(pointer[pointer1])
        pointer2 = int(pointer[pointer2])

    print('duplicate =', pointer2)

check_input()






