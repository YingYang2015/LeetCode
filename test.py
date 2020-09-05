order = "hlabcdefgijkmnopqrstuvwxyz"

order ='0' + order

letter_ord = {order[i]: i for i in range(len(order))}

print(letter_ord['0'])
