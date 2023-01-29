"""GCD_v1"""
def main():
    """main"""
    anum, bnum = int(input()), int(input())
    listnum = []
    checknum = max(anum, bnum)
    for i in range(1, checknum+1):
        if anum % i == 0 and bnum % i == 0:
            listnum.append(i)
    print(max(listnum))
main()
