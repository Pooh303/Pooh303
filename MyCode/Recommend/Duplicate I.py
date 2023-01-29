"""Duplicate I"""
def main():
    """main"""
    group_m, group_n, set_m, set_n = int(input()), int(input()), [], []
    for _ in range(group_m):
        set_m.append(int(input()))
    for _ in range(group_n):
        set_n.append(int(input()))
    get = sorted(set(set_m).intersection(set(set_n)), reverse=True)
    if get == []:
        print("Nope")
    else:
        print(*get, sep="\n")
main()
