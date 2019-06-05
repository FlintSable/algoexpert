import string


def reverse_a_list(my_list):
    """
    :param
        my_list:
            list of values
    :return:
        reverse the order of my_list
    """
    print(len(my_list))
    length = len(my_list)
    if(length == 1):
        return my_list
    else:
        return reverse_a_list(my_list[1:]) + list(my_list[0])


def main():
    alphabet = list(string.ascii_lowercase)
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()