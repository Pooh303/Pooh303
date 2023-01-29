"""[Recommend] RockPaperScissor"""
def check(text_a, text_b):
    """check score"""
    ans = ""
    if text_a == text_b:
        return "Draw"
    elif text_a == "P" and text_b == "R":
        ans = "A"
    elif text_a == "S" and text_b == "P":
        ans = "A"
    elif text_a == "R" and text_b == "S":
        ans = "A"
    else:
        ans = "B"
    return ans


def main():
    """main"""
    result = ""
    text = input()
    for i in range(len(text)):
        if i % 2 == 0:
            result += check(text[i], text[i+1])
    score_a = result.count("A")
    score_b = result.count("B")
    draw_count = result.count("Draw")
    if score_a == score_b:
        print("DRAW", score_a)
    elif score_a > score_b:
        print("A win", score_a, "-", score_b)
    elif score_b > score_a:
        print("B win", score_b, "-", score_a)


main()
