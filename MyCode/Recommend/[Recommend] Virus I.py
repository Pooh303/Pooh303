"""[Recommend] Virus I"""
# def main():
#     """Ooo"""
#     virus = input()
#     print(virus.count("o"))
# main()


def virus():
    """ban count"""
    body = 0
    virus = input()
    for i in virus:
        if i == "o":
            body += 1
    print(body)


virus()
