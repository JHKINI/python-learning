import random
import flet as ft

playerWins = 0
computerWins = 0
resetBtn = None
pageMain = None
result = None
def playerSelect(e, select, arrRSP, result):
    global playerWins
    global computerWins
    global resetBtn
    global pageMain
    if playerWins >= 3 or computerWins >= 3:
        return
    
    comSelect = random.choice(arrRSP)
    if select == comSelect:
        result.value = "비겼습니다! (컴퓨터: " + comSelect + ") 현재 {}승 {}패".format(playerWins, computerWins)
    elif (select == "가위" and comSelect == "보") or \
         (select == "바위" and comSelect == "가위") or \
         (select == "보" and comSelect == "바위"):
        playerWins += 1
        result.value = "이겼습니다! (컴퓨터: " + comSelect + ") 현재 {}승 {}패".format(playerWins, computerWins)   
    else:
        computerWins += 1
        result.value = "졌습니다! (컴퓨터: " + comSelect + ") 현재 {}승 {}패".format(playerWins, computerWins) 

    if playerWins >= 3 or computerWins >= 3:
        if playerWins > computerWins:
            result.value += " 최종 승리!"
        else:
            result.value += " 최종 패배!"
    
        if resetBtn != None:
            resetBtn.visible = True
        if pageMain != None:
            pageMain.update()

def resetGame(e):
    global playerWins
    global computerWins
    global resetBtn
    global pageMain
    
    playerWins = 0
    computerWins = 0
    if result != None:
        result.value = ""
    if resetBtn != None:
        resetBtn.visible = False
    if pageMain != None:
        pageMain.update()

def main(page: ft.Page):
    global resetBtn
    global pageMain
    global result

    pageMain = page
    pageMain.title = "가위바위보 게임"

    arrRSP = ["가위", "바위", "보"]

    title = ft.Text("가위바위보 게임", size=30)
    result = ft.Text("")

    resetBtn = ft.ElevatedButton("게임 리셋", on_click=resetGame)

    pageMain.add(
        title,
        ft.ElevatedButton("가위", on_click=lambda e: playerSelect(e, arrRSP[0], arrRSP, result)),
        ft.ElevatedButton("바위", on_click=lambda e: playerSelect(e, arrRSP[1], arrRSP, result)),
        ft.ElevatedButton("보", on_click=lambda e: playerSelect(e, arrRSP[2], arrRSP, result)),
        resetBtn,
        result,
    )
    resetBtn.visible = False
    pageMain.update()


ft.run(main, view=ft.AppView.WEB_BROWSER)