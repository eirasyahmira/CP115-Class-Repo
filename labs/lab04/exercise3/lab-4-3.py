hours = int(input())
if hours <= 2:
    fee = 0
else:
    if hours <= 5:
        fee = hours - 2 * 2
    else:
        fee = 3 * 2 + hours - 5 * 3
    if fee > 30:
        fee = 30
    else:
        print(parkingFee)
