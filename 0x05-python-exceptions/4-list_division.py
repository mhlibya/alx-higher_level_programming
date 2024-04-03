#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            try:
                num1 = float(my_list_1[i])
                num2 = float(my_list_2[i])
            except (ValueError, TypeError):
                print("wrong type")
                result.append(0)
                continue

            try:
                result.append(num1 / num2)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
        except IndexError:
            print("out of range")
            break
        finally:
            pass
    return result
