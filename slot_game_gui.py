import tkinter as tk
import random


class SlotGame:
    def __init__(self, master):
        self.master = master
        self.master.title("スロットゲーム🎰")
        self.master.geometry("400x400")
        self.master.configure(bg="white")

        self.coins = 100
        self.animating = False  # アニメーション中フラグ

        tk.Label(
            master, text="🎰 スロットゲーム 🎰", font=("Arial", 20), bg="white"
        ).pack(pady=10)

        self.slot_display = tk.Label(
            master, text="- - -", font=("Courier", 36), bg="white"
        )
        self.slot_display.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 14), bg="white")
        self.result_label.pack()

        self.coin_label = tk.Label(
            master, text=f"所持コイン: {self.coins}", font=("Arial", 14), bg="white"
        )
        self.coin_label.pack(pady=10)

        self.bet_frame = tk.Frame(master, bg="white")
        self.bet_frame.pack()

        tk.Label(
            self.bet_frame, text="BET枚数（1〜100）:", font=("Arial", 12), bg="white"
        ).pack(side=tk.LEFT)
        self.bet_entry = tk.Entry(self.bet_frame, width=5, font=("Arial", 12))
        self.bet_entry.insert(0, "10")
        self.bet_entry.pack(side=tk.LEFT)

        self.spin_button = tk.Button(
            master, text="🎰 スピン", command=self.start_spin, font=("Arial", 14)
        )
        self.spin_button.pack(pady=20)

        self.symbols = ["🍒", "🍋", "🍊", "💎", "⭐"]

    def start_spin(self):
        if self.animating:
            return

        try:
            self.bet = int(self.bet_entry.get())
            if self.bet < 1 or self.bet > 100:
                self.result_label.config(text="BETは1〜100の範囲で！")
                return
        except ValueError:
            self.result_label.config(text="BETは数値で入力してね")
            return

        if self.coins < self.bet:
            self.result_label.config(text="コインが足りません")
            return

        self.coins -= self.bet
        self.update_coins()

        self.result_label.config(text="")
        self.animating = True
        self.spin_animation_count = 0
        self.animate_spin()

    def animate_spin(self):
        if self.spin_animation_count < 10:
            # 回転中のランダム表示
            temp_result = [random.choice(self.symbols) for _ in range(3)]
            self.slot_display.config(text=" ".join(temp_result))
            self.spin_animation_count += 1
            self.master.after(100, self.animate_spin)  # 100ミリ秒ごとに更新
        else:
            self.animating = False
            self.finish_spin()

    def finish_spin(self):
        result = [random.choice(self.symbols) for _ in range(3)]
        self.slot_display.config(text=" ".join(result))

        payout = 0
        message = "はずれ…"

        if result.count(result[0]) == 3:
            if random.random() < 0.1:
                payout = self.bet * 10
                message = "🎉🎉 大当たり！ x10 🎉🎉"
                self.flash_bg("yellow")
            else:
                payout = self.bet * 2
                message = "3つ揃った！ x2"
                self.flash_bg("lightgreen")
        elif result.count(result[0]) == 2 or result.count(result[1]) == 2:
            payout = int(self.bet * 1.2)
            message = "2つ揃った！ x1.2"
            self.flash_bg("lightblue")

        self.coins += payout
        self.result_label.config(text=message)
        self.update_coins()

    def flash_bg(self, color):
        original_color = self.master.cget("bg")
        self.master.configure(bg=color)
        self.master.after(300, lambda: self.master.configure(bg=original_color))

    def update_coins(self):
        self.coin_label.config(text=f"所持コイン: {self.coins}")


# 起動
root = tk.Tk()
game = SlotGame(root)
root.mainloop()
