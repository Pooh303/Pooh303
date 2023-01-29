"""[Recommend] Ball"""
def main():
    """fall"""
    height = float(input())
    count = 0
    while True:
        height = height*(3/5)
        if height < 0.01:
            break
        count += 1
    print(count)

main()