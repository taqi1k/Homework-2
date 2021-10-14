# Taqi Syed
# 1863528

def main():
  input_val = int(input())
  if input_val <= 0:
    print('no change')
  else:
    num_dollars = input_val // 100
    input_val %= 100
    num_quarters = input_val // 25
    input_val %= 25
    num_dimes = input_val // 10
    input_val %= 10
    num_nickels = input_val // 5
    input_val %= 5
    num_pennies = input_val

    if num_dollars > 1:
        print('%d dollars' % num_dollars)
    elif num_dollars == 1:
        print('%d dollar' % num_dollars)
    if num_quarters > 1:
        print('%d quarters' % num_quarters)
    elif num_quarters == 1:
        print('%d quarter' % num_quarters)
    if num_dimes > 1:
        print('%d dimes' % num_dimes)
    elif num_dimes == 1:
        print('%d dime' % num_dimes)
    if num_nickels > 1:
        print('%d nickels' % num_nickels)
    elif num_nickels == 1:
        print('%d nickel' % num_nickels)
    if num_pennies > 1:
        print('%d pennies' % num_pennies)
    elif num_pennies == 1:
        print('%d penny' % num_pennies)
main()