def count_word_count(contents):

    contents_as_list =  contents.strip().split()
    return len(contents_as_list)


def count_char_occurances(contents):

    result = {}

    for char in contents:
        if char.lower() in result:
            result[char.lower()] += 1
        else:
            result[char.lower()] = 1

    return result

def sort_on(item):
    return item["num"]

def sort_char_occurances(char_count_dict):

    result = []

    for char in char_count_dict:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = char_count_dict[char]
        result.append(char_dict)

    result.sort(reverse=True, key=sort_on)

    return result
