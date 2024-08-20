# Author Ricky Birnbaum
# python3 version used -- Python 3.4.2

# to run this file, cd to the directory called gold_bars. 
#  Then run `python3 test_solution.py` 

# Must have python installed as well. 
#  run if you do not have already. `brew install python`
# verify with `python3 --version`

import unittest

from solution import GoldBar, find_name_for_smallest_bar_of_three_bars, sum_weight_of_bars

class TestGoldBarHelpers(unittest.TestCase):

  def test_sum_same_weight_bars(self):
      """Test for 'three same weight bars sum test'"""
      bar_one = GoldBar("bar 1", 2)
      bar_two = GoldBar("bar 2", 2)
      bar_three = GoldBar("bar 3", 2)
      first_third_of_bars = [bar_one, bar_two, bar_three]
      self.assertEqual(sum_weight_of_bars(first_third_of_bars), 6)

  def test_sum_weight_bars_with_one_lighter_size(self):
      """Test for '3 bar sum test with one lighter weight bar with two same weight bars'"""
      bar_seven = GoldBar("bar 7", 2)
      bar_eight = GoldBar("bar 8", 2)
      bar_nine = GoldBar("bar 9", 1)
      final_third_of_bars = [bar_seven, bar_eight, bar_nine]
      self.assertEqual(sum_weight_of_bars(final_third_of_bars), 5)

  def test_sum_single_bar(self):
      """Test for 'one bar sum test'"""
      bar_nine = GoldBar("bar 9", 1)
      self.assertEqual(sum_weight_of_bars([bar_nine]), 1)

  def test_sum_zero_bar(self):
      """Test for 'no bars sum test'"""
      self.assertEqual(sum_weight_of_bars([]), 0)

  def test_find_smallest_bar_first_is_smallest(self):
      """Test that first bar is lightest of three bars"""
      bar_one = GoldBar("bar 1", 1)
      bar_two = GoldBar("bar 2", 2)
      bar_three = GoldBar("bar 3", 2)
      self.assertEqual(find_name_for_smallest_bar_of_three_bars([bar_one, bar_two, bar_three]), "bar 1")

  def test_find_smallest_bar_middle_is_smallest(self):
      """Test that second bar is lightest of three bars'"""
      bar_one = GoldBar("bar 1", 2)
      bar_two = GoldBar("bar 2", 1)
      bar_three = GoldBar("bar 3", 2)
      self.assertEqual(find_name_for_smallest_bar_of_three_bars([bar_one, bar_two, bar_three]), "bar 2")

  def test_find_smallest_bar_last_is_smallest(self):
      """Test that third bar is lightest of three bars"""
      bar_one = GoldBar("bar 1", 2)
      bar_two = GoldBar("bar 2", 2)
      bar_three = GoldBar("bar 3", 1)
      self.assertEqual(find_name_for_smallest_bar_of_three_bars([bar_one, bar_two, bar_three]), "bar 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)