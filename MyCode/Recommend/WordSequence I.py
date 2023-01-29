"""WordSequence I"""
def main():
    """main"""
    word, word_list, count = input(), [], -1
    for i in word:
        word_list.append(i)
        count += 1
        text = (word_list[0:count+1])
        for i in text:
            print(i, end="")
        print("")
main()
