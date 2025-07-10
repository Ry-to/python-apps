import tkinter as tk
import random


class HorseRaceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("競馬ゲーム🏇")
        self.master.geometry("850x400")
        self.master.configure(bg="white")

        self.coins = 100
        self.selected_horse = None
        self.running = False

        self.canvas = tk.Canvas(master, width=800, height=280, bg="lightgreen")
        self.canvas.pack(pady=10)

        self.horse_emojis = ["🐎", "🫏", "🦓", "🦄", "🐐"]
        self.horses = []
        self.positions = [0] * 5
        self.odds = [round(random.uniform(1.5, 5.0), 2) for _ in range(5)]

        self.canvas.create_text(30, 10, text="🏁 START", anchor="w", font=("Arial", 12))
        self.goal_x = 700
        self.canvas.create_line(self.goal_x, 0, self.goal_x, 280, fill="red", width=2)
        self.canvas.create_text(
            self.goal_x + 10, 10, text="GOAL 🏁", anchor="w", font=("Arial", 12, "bold")
        )

        for i in range(5):
            emoji = self.horse_emojis[i]
            y = 40 + i * 45
            horse = self.canvas.create_text(
                60, y, text=f"{emoji} 馬{i+1}", anchor="w", font=("Arial", 18)
            )
            self.horses.append(horse)

        self.bet_frame = tk.Frame(master, bg="white")
        self.bet_frame.pack()

        tk.Label(
            self.bet_frame,
            text="賭ける馬を選んでください：",
            font=("Arial", 12),
            bg="white",
        ).pack(side=tk.LEFT)

        for i in range(5):
            b = tk.Button(
                self.bet_frame,
                text=f"{self.horse_emojis[i]}\n馬{i+1}\n({self.odds[i]}倍)",
                command=lambda i=i: self.select_horse(i),
            )
            b.pack(side=tk.LEFT, padx=5)

        self.bet_amount_label = tk.Label(
            master, text="BET金額（1〜100）:", font=("Arial", 12), bg="white"
        )
        self.bet_amount_label.pack()

        self.bet_amount_entry = tk.Entry(master, font=("Arial", 12))
        self.bet_amount_entry.insert(0, "10")
        self.bet_amount_entry.pack()

        self.start_button = tk.Button(
            master, text="レーススタート！", font=("Arial", 14), command=self.start_race
        )
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Arial", 14), bg="white")
        self.status_label.pack()

        self.coin_label = tk.Label(
            master, text=f"所持コイン：{self.coins}", font=("Arial", 14), bg="white"
        )
        self.coin_label.pack()

    def select_horse(self, i):
        self.selected_horse = i
        self.status_label.config(text=f"{self.horse_emojis[i]} 馬{i+1} にBETします！")

    def start_race(self):
        if self.running:
            return

        if self.selected_horse is None:
            self.status_label.config(text="まず賭ける馬を選んでください！")
            return

        try:
            bet = int(self.bet_amount_entry.get())
            if bet < 1 or bet > 100:
                self.status_label.config(text="BETは1〜100の範囲で！")
                return
            if bet > self.coins:
                self.status_label.config(text="コインが足りません！")
                return
        except ValueError:
            self.status_label.config(text="BET金額は数値で入力してください")
            return

        self.bet = bet
        self.coins -= bet
        self.update_coins()

        self.positions = [0] * 5
        for i, horse in enumerate(self.horses):
            y = 40 + i * 45
            self.canvas.coords(horse, 60, y)

        self.running = True
        self.status_label.config(text="レース中…")
        self.animate_race()

    def animate_race(self):
        if not self.running:
            return

        winner = None
        for i in range(5):
            base_speed = random.randint(1, 6)
            odds_penalty = int(self.odds[i] * 0.6)
            move = max(1, base_speed - odds_penalty)
            self.positions[i] += move
            self.canvas.move(self.horses[i], move * 5, 0)
            x, _ = self.canvas.coords(self.horses[i])
            if x >= self.goal_x:
                winner = i
                break

        if winner is not None:
            self.running = False
            self.finish_race(winner)
        else:
            self.master.after(100, self.animate_race)

    def finish_race(self, winner):
        if self.selected_horse == winner:
            reward = int(self.bet * self.odds[winner])
            self.status_label.config(
                text=f"🎉 {self.horse_emojis[winner]} 馬{winner+1}が勝ち！ {reward}コイン獲得 🎊"
            )
            self.coins += reward
        else:
            self.status_label.config(
                text=f"🏁 {self.horse_emojis[winner]} 馬{winner+1}が勝ちました！残念…"
            )

        self.update_coins()
        self.selected_horse = None

    def update_coins(self):
        self.coin_label.config(text=f"所持コイン：{self.coins}")


# 起動
root = tk.Tk()
game = HorseRaceGame(root)
root.mainloop()
