"""[Recommend] Diginity"""

def main():
    """Digits"""
    while True:
        num = int(input())

        if num == 0:
            break
        if len(str(num)) == 1:
            print(num)
        elif len(str(num)) > 1:
            while True:
                count = 0
                for i in str(num):
                    count += int(i)
                if len(str(count)) == 1:
                    break
                num = count
            print(count)

main()