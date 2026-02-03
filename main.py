import json
import urllib.request
from datetime import date
from Board import Board
from Solver import Solver

def getCurrentDayLevelInfo():
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    url = f"http://enclose.horse/api/daily/{date_str}"

    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.load(resp)

    return data["map"], data["budget"]

def main():
    boardStr, wallBudget = getCurrentDayLevelInfo()
    print(boardStr, wallBudget)
    board = Board(boardStr)
    solver = Solver(board, wallBudget)
    solver.solve()

if __name__ == "__main__":
    main()