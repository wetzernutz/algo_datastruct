"""
Pytest module for testing selection sort.
"""

import pytest
from tests.test_sorting.testcases.inout.sort_num import (
    inout_pos_integers,
    inout_neg_integers,
    inout_pos_floats,
    inout_neg_floats
)
from tests.test_sorting.testcases.check_inout import check_inout

from src.sorting.selectionsort import s_sort

sort_func = s_sort


@pytest.mark.parametrize("input_list, expected_output", inout_pos_integers)
def test_sort_pos_integers(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)


@pytest.mark.parametrize("input_list, expected_output", inout_neg_integers)
def test_sort_neg_integers(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)


@pytest.mark.parametrize("input_list, expected_output", inout_pos_floats)
def test_sort_pos_floats(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)


@pytest.mark.parametrize("input_list, expected_output", inout_neg_floats)
def test_sort_neg_floats(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)


@pytest.mark.parametrize("input_list, expected_output", inout_pos_integers)
def test_sort_pos_integers_reversed(input_list, expected_output):
    check_inout([(input_list, expected_output[::-1])], sort_func, reverse=True)


@pytest.mark.parametrize("input_list, expected_output", inout_neg_integers)
def test_sort_neg_integers_reversed(input_list, expected_output):
    check_inout([(input_list, expected_output[::-1])], sort_func, reverse=True)
