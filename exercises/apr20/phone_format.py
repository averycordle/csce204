# (803)-123-4567   we will change this

def update_phone(phone):
    answer = ""

    for char in phone:
        if char == "(" or char ==")":
            continue
        elif char == "-":
            answer+= "."
        else:
            answer+=char
    return answer


phone_number=update_phone("(803)-123-4567")
print(phone_number)

