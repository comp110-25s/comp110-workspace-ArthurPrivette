import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


_author_: "730768516"


def test_invert_normal():
    """Test a case of inverting."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_one_pair():
    """Test invert with only one key-value pair."""
    assert invert({"apple": "fruit"}) == {"fruit": "apple"}


def test_invert_duplicate_values():
    """Test invert when duplicate values exist."""
    with pytest.raises(KeyError):
        invert({"one": "1", "two": "1"})


def test_count_basic():
    """Test counting simple list of words."""
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_count_all_unique():
    """Test count when all words are unique."""
    assert count(["dog", "cat", "fish"]) == {"dog": 1, "cat": 1, "fish": 1}


def test_count_empty():
    """Test count with an empty list."""
    assert count([]) == {}


def test_favorite_color_simple():
    """Test when one color is clearly the favorite."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "red"}) == "blue"


def test_favorite_color_tie():
    """Test when there's a tie, should return the first color encountered."""
    assert (
        favorite_color(
            {"Alice": "red", "Bob": "blue", "Charlie": "red", "David": "blue"}
        )
        == "red"
    )


def test_favorite_color_only_one_person():
    """Test when there is only one person in the dictionary."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_bin_len_basic():
    """Test simple case where words are binned by length."""
    assert bin_len(["hi", "hello", "bye"]) == {2: {"hi"}, 5: {"hello"}, 3: {"bye"}}


def test_bin_len_repeats():
    """Test bin_len where words have repeats (should remove duplicates)."""
    assert bin_len(["cat", "dog", "cat", "bat"]) == {3: {"cat", "dog", "bat"}}


def test_bin_len_empty():
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}
