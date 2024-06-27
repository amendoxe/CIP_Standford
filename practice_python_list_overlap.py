"""practice_python_list_overlap.py
----------------------------------
returns a list that contains only the elements that are common between
 the lists (without duplicates)
"""


def check_common(a_list, b_list):
    """Check if the a list elements are present in b list and
    returns returns a list of them"""
    c_list = []
    for a in a_list:
        if a in b_list:
            c_list.append(a)
    return c_list


def main():
    """main"""
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_elements = check_common(a, b)
    print(common_elements)
    print("now for non repeating")
    print(set(common_elements))
    print("-----------another form--------------")
    print(set([i for i in a if i in b]))
    print("--------sets unordered of non repeating-----------")
    print(set(a + b))


main()
