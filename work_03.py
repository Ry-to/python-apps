meisan = {'ジンギスカン': '北海道', 'せんべい汁': '青森', 
          '冷麺': '岩手', '牛タン': '宮崎', '稲庭うどん': '秋田', 
          '芋煮': '山形', 'ソースカツ丼': '福島', 'あんこう鍋': '茨城', 
          '餃子': '栃木', '焼きまんじゅう': '群馬', 'わらじかつ': '埼玉', 
          '勝浦担々麺': '千葉', 'もんじゃ焼き': '東京', 'サンマーメン': '神奈川', 
          'タレカツ丼': '新潟', '白えび': '富山', 'ハントンライス': '石川', 
          'おろしそば': '福井', 'ほうとう': '山梨', 'おやき': '長野', 
          '鶏ちゃん': '岐阜', '静岡おでん': '静岡', 'ひつまぶし': '愛知', 
          '伊勢うどん': '三重', '近江牛': '滋賀', '湯豆腐': '京都', 'たこ焼き': '大阪', 
          '明石焼き': '兵庫', '柿の葉すし': '奈良', '和歌山ラーメン': '和歌山', 
          '牛骨ラーメン': '鳥取', '出雲そば': '島根', 'エビめし': '岡山', 'お好み焼き': '広島', 
          '瓦そば': '山口', '徳島ラーメン': '徳島', 'うどん': '香川', '鯛めし': '愛媛', 
          'カツオのたたき': '高知', 'ラーメン': '福岡', 'シシリアンライス': '佐賀', 
          'ちゃんぽん': '長崎', '馬刺し': '熊本', 'とり天': '大分', 'チキン南蛮': '宮崎', 
          '黒豚料理': '鹿児島', '沖縄そば': '沖縄'}
import random
mondai = random.randint(0,46)
meisan_key = list(meisan.keys())
meisan_value = list(meisan.values())
soumondai = 0
seikai = 0
M = 1
li = []
print("!全国名産品都道府県当てクイズ!")
print("明産物を表示するのでどの都道府県のものかを当ててね")
print("ルール 県などは書かなくてOK(東京都→東京)exitでやめれます")
while True:
    if 0 == len(meisan_key):
        seikairitu = (seikai / soumondai * 100)
        seikairitu_round = round(seikairitu,2)
        print(f"正解率は{seikairitu_round}%でした")
        print("間違えた問題")
        for item,val in li:
            print(f"{M}問目:{item} → 正解:{val}")
            M += 1
        print("問題をすべて解きました！")
        print("ありがとうございました")
        break
    else:
        mondai = random.randint(0, len(meisan_key) - 1)
        ans = input(f"{meisan_key[mondai]}はどこの名産品でしょう？")
        if ans == "exit":
            if soumondai == 0:
                print("ありがとうございました！")
                break
            else:
                seikairitu = (seikai / soumondai * 100)
                seikairitu_round = round(seikairitu,2)
                print("【結果】")
                print(f"正解率は{seikairitu_round}%でした")
                print("間違えた問題")
                for item,val in li:
                    print(f"{M}問目:{item} → 正解:{val}")
                    M += 1
                print("ありがとうございました")
                break
        else:
            soumondai += 1
            if ans == meisan_value[mondai]:
                print("!正解!")
                seikai += 1
            else:
                print("不正解")
                li.append((meisan_key[mondai],meisan_value[mondai]))
            del meisan_key[mondai]
            del meisan_value[mondai]