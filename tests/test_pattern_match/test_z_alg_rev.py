import pytest
from src.pattern_match.z_alg import (
    naive_z_array,
    demonstrate_l_i_r_i,
    naive_pattern_match,
    z_algorithm,
    z_algorithm_pattern_match,
    z_algorithm_ian,
    _z_explicit_match
)

from src.pattern_match.z_alg_rev import (
    _z_explicit_match_reverse,
    z_algorithm_reverse_ian
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

def reverse_string(string):
    return string[::-1]

def reverse_list(lst):
    return list(reversed(lst))

def reversed_idx(n, idx):
    return n - (idx + 1)

def test_z_explicit_match_reverse(random_strings):
    for string in random_strings:
        n = len(string)
        l_finger_start = random.randint(0, n - 2)
        r_finger_start = random.randint(l_finger_start+1, n - 1)
        q = _z_explicit_match(string, r_finger_start, l_finger_start)

        reversed_string = reverse_string(string)
        q_rev = _z_explicit_match_reverse(reversed_string, reversed_idx(n,r_finger_start), reversed_idx(n, l_finger_start))
        assert q == reversed_idx(n,q_rev)


def test_z_algorithm_reverse_ian(random_strings):
    for string in random_strings:
        reversed_string = reverse_string(string)
        target_z_array = reverse_list(z_algorithm_ian(reversed_string))
        z_array = z_algorithm_reverse_ian(string)
        assert target_z_array == z_array



