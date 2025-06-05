import random
atari = random.randint(1,100)
print("1から100までの数字を当ててください")
print("挑戦は5回までです")
while True:
    import random
    atari = random.randint(1,100)
    for i in range(5):
        input_line = input(f"{i + 1}回目:")
        print("入力された文字列:",input_line)
        if atari == int(input_line):
            print(f"当たりました{i + 1}回目で勝ちました！")
            break
        else:
            print("不正解です")
            if atari + 30 < int(input_line):
                print("当たりよりかなり大きいです")
            elif atari + 20 < int(input_line):
                print("当たりより少し大きです")
            elif atari + 10 > int(input_line) > atari -10:
                print("当たりに近いです")
            elif atari - 20 > int(input_line):
                print("当たりより少し小さいです")
            elif atari - 30 > int(input_line):
                print("当たりよりかなり小さいです")
            else:
                print("当たりに近いかも？")
    
    print(f"正解は{atari}でした")
    ans = input("やめますか？(yesでやめる/enterKeyで続ける):")
    if ans == "yes":
        print("お疲れ様でした")
        break

