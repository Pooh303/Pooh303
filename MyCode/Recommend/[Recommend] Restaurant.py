"""[Recommend] Restaurant"""
def main():
    """calculating"""
    bill = float(input())
    pro = float(input())
    disc = float(input())
    plus = float(input())
    new_price = bill + plus
    if new_price >= pro:
        new_bill = new_price * ((disc/100) * new_price)
    gap = bill - new_bill
    if bill > pro or new_bill == bill:
        print("yes")
    elif bill == pro:
        bill #... Not yet


main()