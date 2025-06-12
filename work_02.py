li = []
while True:
    import random
    aizu = random.randint(5,15)
    import time
    print("反射神経テストをします")
    print("合図が出たらenterkeyを押してね")
    time.sleep(aizu)
    start_time = time.time()
    input_line = input("【！！！！！】")
    end_time = time.time()
    sokudo = (end_time - start_time)
    rounded_num = round(sokudo,4)
    li.append(rounded_num)
    if sokudo < 0.1:
        print("あなたは不正してます")
    else:
        print(f"反応時間{rounded_num}秒でした！")
    ans = input("もう１回しますか？(するyes/しないno)")
    if ans == "no":
        saikou = min(li)
        print(f"最高記録は{saikou}でした！")
        print("お疲れ様でした")
        break