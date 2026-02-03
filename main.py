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
    return data["id"], data["map"], data["budget"]

""" To submit the level
await fetch("https://enclose.horse/api/levels/ECT9f-/submit", {
    "credentials": "omit",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "x-player-id": "4f54aa18-1e1d-4f",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0"
    },
    "referrer": "https://enclose.horse/play/2026-02-02",
    "body": "{\"walls\":[60,81,97,113,135,145,161,165,175,213]}",
    "method": "POST",
    "mode": "cors"
});
"""
def main():
    levelId, boardStr, wallBudget = getCurrentDayLevelInfo()
    print(boardStr, wallBudget)
    board = Board(boardStr)
    print(board)
    solver = Solver(board, wallBudget)
    solver.solve()

if __name__ == "__main__":
    main()