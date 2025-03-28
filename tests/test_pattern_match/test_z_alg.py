import pytest
from src.pattern_match.z_alg import (
    naive_z_array,
    demonstrate_l_i_r_i,
    naive_pattern_match,
    z_algorithm,
    z_algorithm_pattern_match,
    z_algorithm_ian

)
import random
import string

random.seed(42)

def random_string():
    length = random.randint(2, 100)
    prob = random.random()
    if prob < 0.33:
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    elif prob < 0.66:
        return ''.join(random.choices("ab", k=length))
    else:
        return ''.join(random.choices(string.ascii_lowercase) * length)

@pytest.fixture(scope="module")
def random_strings():
    no_strings = 10000
    return [random_string() for _ in range(no_strings)]


def test_z_algorithm_pattern_match():
    text = "babsdbaubab"
    pattern = "bab"
    target = [False] * len(text)
    target[0] = True
    target[-3] = True
    assert z_algorithm_pattern_match(text, pattern) == target


def test_naive_pattern_match():
    text = "aabcaabxaay"
    pattern = "aab"
    target = [3, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
    assert naive_pattern_match(text, pattern) == target


def test_z_algorithm(random_strings):
    for text in random_strings:
        assert z_algorithm(text)[1:] == naive_z_array(text)[1:], f"Text: {text}"


def test_naive_z_array():
    string = "aabcaabxaay"
    target = [0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
    assert naive_z_array(string) == target

def test_demonstrate_l_i_r_i():
    string = "aabcaabxaay"
    target_r_i = [None, 1, 1, 1, 6, 6, 6, 6, 9, 9, 9]
    target_l_i = [None, 1, 1, 1, 4, 4, 4, 4, 8, 8, 8]
    l_i, r_i = demonstrate_l_i_r_i(string)
    assert  l_i == target_l_i
    assert r_i == target_r_i

def test_z_algorithm_ian(random_strings):
    # text = "aabcaabxaay"
    for text in random_strings:
        assert z_algorithm_ian(text)[1:] == naive_z_array(text)[1:], f"Text: {text}"





