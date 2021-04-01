#.price of the house is $1m.  if buyer has good credit they need to put down 10% other wise they need to
#  print 20%.   print the down payment.


price=100000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down payment : ${down_payment}")






