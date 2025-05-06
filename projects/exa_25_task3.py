def find_first_odd_position(number_list: list[int]) -> int:
    i = 0
    while i < len(number_list):
        if number_list[i] % 2 == 1:
            return i

        i += 1

    return -1