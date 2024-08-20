# Author Ricky Birnbaum
# python3 version used -- Python 3.4.2

# to run this file, cd to the directory called gold_bars. 
#  Then run `python3 solution.py` 

# Must have python installed as well. 
#  run if you do not have already. `brew install python`
# verify with `python3 --version`

class GoldBar:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

def sum_weight_of_bars(goldBars):
  sum = 0
  for bar in goldBars:
    sum += bar.weight
  return sum
  	
def find_name_for_smallest_bar_of_three_bars(threeBars):
  if threeBars[0].weight > threeBars[1].weight:
    return threeBars[1].name
  elif threeBars[0].weight < threeBars[1].weight:
    return threeBars[0].name
  else:
    return threeBars[2].name

def main():
  bar_one = GoldBar("bar 1", 2)
  bar_two = GoldBar("bar 2", 2)
  bar_three = GoldBar("bar 3", 2)
  bar_four = GoldBar("bar 4", 2)
  bar_five = GoldBar("bar 5", 2)
  bar_six = GoldBar("bar 6", 2)
  bar_seven = GoldBar("bar 7", 2)
  bar_eight = GoldBar("bar 8", 2)
  bar_nine = GoldBar("bar 9", 1)

  first_third_of_bars = [bar_one, bar_two, bar_three]
  middle_third_of_bars = [bar_four, bar_five, bar_six]

  sum_first_three_bars = sum_weight_of_bars(first_third_of_bars)
  sum_middle_three_bars = sum_weight_of_bars(middle_third_of_bars)
  

  # scale use 1 is check the weight of bars 1,2,3 against the weight of bars 4,5,6
  # scale use 2 is to compare the weight of a single bar vs a single bar, taken from the three remaining bars that we know has to contain the lightest bar. See logic below for how to know which three bars are used.

  if sum_first_three_bars > sum_middle_three_bars:
    print(find_name_for_smallest_bar_of_three_bars(middle_third_of_bars) + " is the smallest bar")
  elif sum_first_three_bars < sum_middle_three_bars:
    print(find_name_for_smallest_bar_of_three_bars(first_third_of_bars) + " is the smallest bar")
  else: 
    final_third_of_bars = [bar_seven, bar_eight, bar_nine]
    print(find_name_for_smallest_bar_of_three_bars(final_third_of_bars) + " is the smallest bar")


if __name__ == "__main__":
    main()