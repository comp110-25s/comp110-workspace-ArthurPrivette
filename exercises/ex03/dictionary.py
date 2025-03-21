_author_: "730768516"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of given dictionary"""
    result_dict: dict[str, str] = {}
    for key in input_dict:
        value: str = input_dict[key]

        if value in result_dict:
            raise KeyError("Duplicate value found in dictionary")

        result_dict[value] = key
    return result_dict


def count(count_list: list[str]) -> dict[str, int]:
    "Will count how many times a string appeared in the input list"
    result_dict: dict[str, int] = {}

    for item in count_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that appears the most often."""
    """If there is a tie it returns the first color encountered"""
    color_count: dict[str, int] = {}
    # Creates a list to store the values of the colors
    for name in color_dict:
        color: str = color_dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_color: str = ""
    max_count: int = 0

    for name in color_dict:
        color: str = color_dict[name]
        if color_count[color] > max_count:
            max_count = color_count[color]
            max_color = color
    # This returns the color that shows up the most and if tie it returns the first one
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Groups the words together by their length into dictionary of sets"""
    result_dict: dict[int, list[str]] = {}

    for word in words:
        length: int = len(word)
        # If this length is already a key, it adds the word only if not already in list
        if length in result_dict:
            if word not in result_dict[length]:
                result_dict[length].append(word)
        else:
            result_dict[length] = [word]

    length_bins: dict[int, set[str]] = {}
    # Converts all the lists of words to sets to remove the duplicates
    for length in result_dict:
        length_bins[length] = set(result_dict[length])
    # Return the dictionary with word lengths as keys and sets of words as values
    return length_bins
