'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items') # Orderという型の宣言
Item = namedtuple('Item', 'type, description, amount, quantity') # Itemという型の宣言

def validorder(order: Order):
    net = Decimal("0.00")
    total = Decimal("0")

    for item in order.items:
        if item.type == 'payment': # 支払だったら？
            net = net + Decimal(str(item.amount))
        elif item.type == 'product': # 製品だったら？
            if not isinstance(item.quantity, int): # quantityが整数ではなかったら？
                return "Order ID: %s - invalid order" % order.id
            net = net - Decimal(str(item.amount)) * Decimal(str(item.quantity))
            total = total + Decimal(str(item.amount)) * Decimal(str(item.quantity))
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net) # 請求額に対し支払った額が一致していない
    else:
        if total > 100000:
            return "Total amount payable for an order exceeded"
        else:
            return "Order ID: %s - Full payment received!" % order.id # 問題なし！