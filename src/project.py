import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from typing import List


class Game1:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("game1-012345")
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 1
        self.computer_choices = []

        # 라운드 정보 출력
        self.round_label = tk.Label(self.root, text="라운드 1", font=("Arial", 24, "bold"))
        self.round_label.pack(pady=20)

        # 플레이어 선택 옵션 메뉴
        self.player_choice_var = tk.IntVar(self.root, 0)
        self.player_choice_label = tk.Label(self.root, text="플레이어 선택:", font=("Arial", 16))
        self.player_choice_label.pack()

        # 숫자 선택 버튼
        self.number_buttons = []
        for i in range(6):
            button = tk.Button(self.root, text=str(i), command=lambda num=i: self.make_choice(num), font=("Arial", 16))
            button.pack(side=tk.LEFT, padx=10, pady=10)
            self.number_buttons.append(button)

        # 결과 텍스트 라벨
        self.result_label = tk.Label(self.root, text="", font=("Arial", 18, "bold"))
        self.result_label.pack(pady=20)

        # 이전 라운드 결과 창
        self.result_window = None

        # 이전 라운드 점수 표시
        self.prev_score_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.prev_score_label.pack()
        self.total_score_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.total_score_label.pack()

        # 컴퓨터가 냈던 카드를 출력
        self.computer_choices_label = tk.Label(self.root, text="컴퓨터가 냈던 카드:", font=("Arial", 16))
        self.computer_choices_label.pack()

    def make_choice(self, player_choice):
        # 이미 선택한 숫자인 경우 return
        if self.player_choice_var.get() != 0:
            messagebox.showwarning("경고", "다른 숫자를 선택해주세요.")
            return

        # 컴퓨터의 선택 무작위로 결정
        computer_choice = random.choice([i for i in range(6) if i not in self.computer_choices])
        self.computer_choices.append(computer_choice)

        # 컴퓨터가 냈던 카드 업데이트
        self.computer_choices_label.configure(text=f"컴퓨터가 냈던 카드: {', '.join(map(str, self.computer_choices))}")

        # 이전 라운드 결과 창 닫기
        if self.result_window:
            self.result_window.destroy()

        # 선택한 숫자를 표시할 두 번째 창 생성
        self.result_window = tk.Toplevel(self.root)
        self.result_window.title("결과")

        # 선택한 숫자 출력
        player_label = tk.Label(self.result_window, text=f"플레이어: {player_choice}", font=("Arial", 16))
        player_label.pack(pady=10)
        computer_label = tk.Label(self.result_window, text=f"컴퓨터: {computer_choice}", font=("Arial", 16))
        computer_label.pack(pady=10)

        # 승패 결정
        if player_choice == computer_choice:
            self.result_label.configure(text="무승부!", fg="blue")
        elif (player_choice, computer_choice) in ((0, 2), (2, 5), (5, 0)):
            self.result_label.configure(text="가위바위보에서 이겼습니다!", fg="green")
            self.player_score += (player_choice + computer_choice)
        elif (player_choice, computer_choice) in ((2, 0), (5, 2), (0, 5)):
            self.result_label.configure(text="가위바위보에서 졌습니다!", fg="red")
            self.computer_score += (player_choice + computer_choice)
        elif player_choice > computer_choice:
            self.result_label.configure(text="이겼습니다!", fg="green")
            self.player_score += (player_choice + computer_choice)
        else:
            self.result_label.configure(text="졌습니다!", fg="red")
            self.computer_score += (player_choice + computer_choice)

        # 선택한 숫자 비활성화
        self.number_buttons[player_choice].configure(state=tk.DISABLED)

        # 이전 라운드 점수 표시
        self.prev_score_label.configure(text=f"이전 라운드 점수: 플레이어 {player_choice + computer_choice} - 컴퓨터 {player_choice + computer_choice}")

        # 누적 점수 표시
        self.total_score_label.configure(text=f"누적 점수: 플레이어 {self.player_score} - 컴퓨터 {self.computer_score}")

        # 라운드 종료 후 다음 라운드로 진행
        self.rounds += 1
        if self.rounds <= 6:
            self.round_label.configure(text=f"라운드 {self.rounds}")
            self.player_choice_var.set(0)
        else:
            # 최종 결과 출력
            self.result_label.configure(text=f"\n\n게임이 종료되었습니다.\n최종 점수: 플레이어 {self.player_score} - 컴퓨터 {self.computer_score}", font=("Arial", 18, "bold"))
            if self.player_score > self.computer_score:
                messagebox.showinfo("게임 종료", "축하합니다! 플레이어가 이겼습니다.")
            elif self.player_score == self.computer_score:
                messagebox.showinfo("게임 종료", "무승부입니다.")
            else:
                messagebox.showinfo("게임 종료", "아쉽게도 컴퓨터가 이겼습니다.")
            self.root.destroy()


class Game2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("쓰리카드택틱")
        self.root.geometry("900x450")

        self.cards = ["하트J", "하트Q", "하트K", "스페이드J", "스페이드Q", "스페이드K", "다이아몬드J", "다이아몬드Q", "다이아몬드K"]
        self.player1_cards = []
        self.player2_cards = []
        self.turn = None
        self.card_count = 0
        self.timer_label = None
        self.timer = None
        self.selected_cards = set()
        self.start_count = -1
        
        self.create_widgets()
    
    def create_widgets(self): # 게임 GUI생성 및 변수 레이블을 생성함
        self.label = tk.Label(self.root, text="선공 플레이어를 결정합니다. 버튼을 클릭하세요.")
        self.label.place(x=10, y=10)

        self.start_button = tk.Button(self.root, text="시작", command=self.start_game)
        self.start_button.place(x=380, y=50)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.place(x=10, y=200)

        self.player1_label = tk.Label(self.root, text="Player 1의 카드:")
        self.player1_label.place(x=10, y=250)

        self.player1_cards_label = tk.Label(self.root, text="")
        self.player1_cards_label.place(x=120, y=250)

        self.player2_label = tk.Label(self.root, text="Player 2의 카드:")
        self.player2_label.place(x=10, y=280)

        self.player2_cards_label = tk.Label(self.root, text="")
        self.player2_cards_label.place(x=120, y=280)
        
        self.timer_label = tk.Label(self.root, text="")
        self.timer_label.place(x=450, y=300)

        # 카드 버튼 위치를 플레이스로 설정
        button_width = 80
        button_height = 30
        button_spacing = 10
        start_x = 10
        start_y = 100
        self.card_buttons = []  # 카드 버튼 리스트 생성


        for i, card in enumerate(self.cards):
            self.card_buttons.append(tk.Button(self.root, text=card, command=lambda c=card: self.choose_card(c)))
            x = start_x + (button_width + button_spacing) * i
            y = start_y
            self.card_buttons[i].place(x=x, y=y, width=button_width, height=button_height)
            self.card_buttons[i].config(state='disabled')
        self.disable_card_buttons()
              # 생성된 버튼을 리스트에 추가

        
    def start_game(self):
        # 게임 시작 시 초기 설정
        self.turn = random.choice(["player1", "player2"])
        self.label.config(text=f"{self.turn}가 선공입니다. 카드를 선택하세요.")
        self.start_button.config(state=tk.DISABLED)
        self.start_count += 1
        self.start_timer()
        self.selected_cards = set()

        for button in self.card_buttons:
            button.config(state=tk.NORMAL)
        
        self.timer_label.place(x=450, y=300)
    
    def start_timer(self):
        # 타이머 시작
        self.timer = 30 - 5*self.start_count
        if self.timer < 1:
            self.timer = 2
        if self.timer_switch == 0 :
            self.timer_switch = 1
            self.timer_()
            self.update_timer()
    
    timer_switch = 0

    def timer_(self) :
        self.timer -= 1
        self.root.after(1000, self.timer_)
        
    def update_timer(self):
        # 타이머 갱신
        self.timer_label.config(text=f"남은 시간: {self.timer}초")
        if self.timer > 0:
            pass
        else:
            self.disable_card_buttons()
            self.switch_turn()
            self.label.config(text=f"시간이 초과되었습니다. {self.turn}의 차례입니다.")
            print()
        
        self.root.after(1000, self.update_timer)
    
    def choose_card(self, card):
        # 카드 선택
        if card in self.selected_cards:
            return
        
        self.disable_card_buttons()
        self.selected_cards.add(card)
        
        if self.turn == "player1":
            self.player1_cards.append(card)
            self.label.config(text="player2가 카드를 선택하세요.")
        else:
            self.player2_cards.append(card)
            self.label.config(text="player1이 카드를 선택하세요.")
        
        self.card_count += 1
        self.disable_selected_card(card)
        self.check_winner()
        self.switch_turn()
    
    def disable_card_buttons(self):
        # 카드 버튼 비활성화
        for button in self.card_buttons:
            button.config(state=tk.DISABLED)
    
    def disable_selected_card(self, card):
        # 선택한 카드 버튼 비활성화
        for button in self.card_buttons:
            if button.cget("text") == card:
                button.config(state=tk.DISABLED)
                break
    
    def check_winner(self):
        # 승자 확인
        if self.card_count >= len(self.cards):
            player1_win = self.check_condition(self.player1_cards)
            player2_win = self.check_condition(self.player2_cards)
            
            if player1_win and player2_win:
                self.result_label.config(text="무승부입니다.")
                self.reset_game()
            elif player1_win:
                self.result_label.config(text="player1이 승리했습니다!")
            elif player2_win:
                self.result_label.config(text="player2가 승리했습니다!")
            else:
                self.result_label.config(text="승자가 나타나지 않았습니다.")
                self.reset_game()
            self.timer = 9999999999
            self.timer_label.place_forget()

            self.disable_card_buttons()

        
        # 각 플레이어의 카드 표시
        self.player1_cards_label.config(text=", ".join(self.player1_cards))
        self.player2_cards_label.config(text=", ".join(self.player2_cards))
    
    def reset_game(self):
        # 게임 초기화
        self.card_count = 0
        self.player1_cards = []
        self.player2_cards = []
        self.turn = None
        self.label.config(text="선공 플레이어를 결정합니다. 버튼을 클릭하세요.")
        self.start_button.config(state=tk.NORMAL)
        self.disable_card_buttons()
            
    
    def check_condition(self, cards):
        # 승리 조건 확인
        if len(cards) < 3:
            return False
        
        counts = {}
        for card in cards:
            suit = card[0]
            rank = card[1:]
            if suit not in counts:
                counts[suit] = set()
            counts[suit].add(rank)
        
        for suit, ranks in counts.items():
            if len(ranks) >= 3:
                return True
        
        for rank in ranks:
            count = 0
            for suit in counts:
                if rank in counts[suit]:
                    count += 1
            if count >= 3:
                return True
        
        return False
    
    def switch_turn(self):
        # 턴 전환
        if self.turn == "player1":
            self.turn = "player2"
        else:
            self.turn = "player1"
        
        self.enable_card_buttons()
        self.start_timer()
    
    def enable_card_buttons(self):
        # 선택 가능한 카드 버튼 활성화
        for button in self.card_buttons:
            if button.cget("text") not in self.selected_cards:
                button.config(state=tk.NORMAL)
    
    def run(self):
        self.root.mainloop()


def start_game(game):
    game_window = tk.Tk()
    game(game_window)
    game_window.mainloop()

# 초기화면 생성
def main_screen():
    root = tk.Tk()
    root.title("종합 두뇌 게임")
    root.geometry('600x450')
    root.resizable(False,False)
    background_image = tk.PhotoImage(file="wallpaper.png")
    background_image = background_image.subsample(2,2)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 게임 선택 버튼
    game1_image = Image.open("game1.png")
    game1_photo = ImageTk.PhotoImage(game1_image)
    game1_button = tk.Button(root, image=game1_photo, command=Game1)
    game1_button.image = game1_photo
    game1_button.pack(pady=20)

    game2_image = Image.open("game2.png")
    game2_photo = ImageTk.PhotoImage(game2_image)
    game2_button = tk.Button(root, image=game2_photo, command=Game2)
    game2_button.image = game2_photo
    game2_button.pack(pady=20)

    game3_image = Image.open("game3.png")
    game3_photo = ImageTk.PhotoImage(game3_image)
    game3_button = tk.Button(root, image=game3_photo, command=placeholder)
    game3_button.image = game3_photo
    game3_button.pack(pady=20)



    root.mainloop()

# 임시로 사용되는 함수 (placeholder)
def placeholder():
    messagebox.showinfo("알림", "게임 준비 중입니다.")

# 초기화면 실행
main_screen()
