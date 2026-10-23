from colorama import Fore, Style, init
import os, time
init(autoreset=True)

ROWS = 10
COLS = 10

table = {f"row_{i}": [0] * COLS for i in range(ROWS)}
last_move = "up"
pasos = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class bot:
    class position:
        x = 5
        y = 5

        @classmethod
        def get_position(cls):
            return f"row_{cls.y}", cls.x

    class move:
        @staticmethod
        def up():
            global last_move
            bot.position.y -= 1
            last_move = "up"

        @staticmethod
        def right():
            global last_move
            bot.position.x += 1
            last_move = "right"

        @staticmethod
        def down():
            global last_move
            bot.position.y += 1
            last_move = "down"

        @staticmethod
        def left():
            global last_move
            bot.position.x -= 1
            last_move = "left"

    @staticmethod
    def getBotPosition():
        return bot.position.get_position()

def table_print():
    bot_row, bot_x = bot.getBotPosition()

    for i in range(ROWS):
        r_key = f"row_{i}"
        line = []
        for col, val in enumerate(table[r_key]):
            if r_key == bot_row and col == bot_x:
                line.append(f"{Fore.GREEN}{Style.BRIGHT}{val}{Style.RESET_ALL}")
            elif val == 1:
                line.append(f"{Fore.BLUE}{Style.BRIGHT}{val}{Style.RESET_ALL}")
            else:
                line.append(str(val))
        print(" ".join(line))

def conditions():
    global last_move
    row_key, x = bot.getBotPosition()

    if row_key in table and 0 <= x < COLS:
        current_val = table[row_key][x]

        turn_right = {"up": "right", "right": "down", "down": "left", "left": "up"}
        turn_left  = {"up": "left", "left": "down", "down": "right", "right": "up"}

        if current_val == 0:
            table[row_key][x] = 1
            last_move = turn_right.get(last_move, "right")
        else:
            table[row_key][x] = 0
            last_move = turn_left.get(last_move, "left")

        if last_move == "up":
            bot.move.up()
        elif last_move == "down":
            bot.move.down()
        elif last_move == "right": 
            bot.move.right()
        elif last_move == "left":
            bot.move.left()

def main():
    global pasos
    clear()
    table_print()
    conditions()
    pasos += 1
    clear()
    table_print()
    time.sleep(1)

if __name__ == "__main__":
    while True:
        main()
        row_key, x = bot.getBotPosition()
        y = bot.position.y

        if x < 0:
            print("El bot ha salido por la izquierda. Deteniendo el programa...")
            print(pasos)
            break
        elif x >= COLS:
            print("El bot ha salido por la derecha. Deteniendo el programa...")
            print(pasos)
            break
        elif y < 0:
            print("El bot ha salido por arriba. Deteniendo el programa...")
            print(pasos)
            break
        elif y >= ROWS:
            print("El bot ha salido por abajo. Deteniendo el programa...")
            print(pasos)
            break