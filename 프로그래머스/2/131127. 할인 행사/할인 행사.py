def solution(want, number, discount):
    to_be_register_date = 0

    want_dict = {w: n for w, n in zip(want, number)}

    for i in range(len(discount) - 9):  
        current_discount = {}

        for item in discount[i:i+10]:
            current_discount[item] = current_discount.get(item, 0) + 1

        if all(current_discount.get(item, 0) >= want_dict[item] for item in want_dict):
            to_be_register_date += 1

    return to_be_register_date