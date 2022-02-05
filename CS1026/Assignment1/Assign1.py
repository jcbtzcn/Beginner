''' Yakup Tezcan

                       #GOOD MORNING CANADA
        MENU

        Egg               : $0.99   (each)
        Bacon             : $0.49   (per strip)
        Sausage           : $1.49   (each)
        Hash brown        : $1.19   (each)
        Toast             : $0.79   (per slice)
        Small Breakfast   : $6.23
        Regular breakfast : $9.69
        Big breakfast     : $15.92
        Coffee            : $1.49   (per cup)
        Tea               : $1.09   (per tea bag)

        Tax : %13

        Please enter q to quit and finish your selection.

'''
food_first_price = 0.99
food_second_price = 0.49
food_third_price = 1.49
food_fourth_price = 1.19
food_fifth_price = 0.79
beverage_first_price = 1.49
beverage_second_price = 1.09
small_breakfast_fee = food_first_price + food_fourth_price + 2*food_fifth_price + 2*food_second_price + food_third_price
regular_breakfast_fee = 2*food_first_price + food_fourth_price + 2*food_fifth_price + 4*food_second_price + 2*food_third_price
big_breakfast_fee = 3*food_first_price + 2*food_fourth_price + 4*food_fifth_price + 6*food_second_price + 3*food_third_price
customer_input = 0
customer_quantity_input = 0
cost = 0
tax = 0
total = 0
while customer_input != 'q':
      customer_input = input('Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg,'
                             '\nbacon, sausage, hash brown, toast, coffee, tea: ',) #Takes input from customer.
      customer_input = customer_input.lower().strip()
      wordList = customer_input.split()
      customer_input = ' '.join(wordList)
      if customer_input in ('egg', 'bacon', 'sausage', 'hash brown', 'toast', 'coffee', 'tea', 'small breakfast',
                            'regular breakfast', 'big breakfast', 'q'):  #Provides Invalid Input if customer enters something that is not on menu.
          if customer_input != 'q':  # Does not keep asking for quantity when customer enters q.
              customer_quantity_input = input('Enter quantity: ')
              while not str(customer_quantity_input).isnumeric():  #Make sures that entered value is a number.
                  customer_quantity_input = input('Enter a valid number: ')
          if 'egg' in customer_input:
              cost += food_first_price * int(customer_quantity_input)
          if 'bacon' in customer_input:
              cost += food_second_price * int(customer_quantity_input)
          if 'sausage' in customer_input:
              cost += food_third_price * int(customer_quantity_input)
          if 'hash brown' in customer_input:
              cost += food_fourth_price * int(customer_quantity_input)
          if 'toast' in customer_input:
              cost += food_fifth_price * int(customer_quantity_input)
          if 'small breakfast' in customer_input:
              cost += small_breakfast_fee * int(customer_quantity_input)
          if 'regular breakfast' in customer_input:
              cost += regular_breakfast_fee * int(customer_quantity_input)
          if 'big breakfast' in customer_input:
              cost += big_breakfast_fee * int(customer_quantity_input)
          if 'coffee' in customer_input:
              cost += beverage_first_price * int(customer_quantity_input)
          if 'tea' in customer_input:
              cost += beverage_second_price * int(customer_quantity_input)
      else:
          print('The item is not on the menu. Please enter again.')

print('\nCost : ${:.2f}'.format(cost))
print('Tax : ${:.2f}'.format(cost * 0.13))
print('Total : ${:.2f}'.format(cost * 1.13))




















