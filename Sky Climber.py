# Libary imports
from tkinter import *
import os
import pickle
from SkyClimberAssets import *

# Random variables
whichStage = 0
greyColour = "#585858"
leftControl = "a"
rightControl = "d"
jumpControl = "space"
buttonState = "normal"
topLevelOpen = False
menuOpen = False
playingGame = False
pauseOpen = False
loseOpen = False
gameActive = False
levelQuit = True

# 1D Array of the colours that correspond to
# each circle and button in the level select map
levelSelectColours = ["red", "black", "black", "black", "black", "black",
                      "black", "black", "black", "black", "black"]

# 1D Array to track if a button on
# the level select map can be pressed or not
buttonDisabled = ["normal", "disabled", "disabled", "disabled", "disabled",
                  "disabled", "disabled", "disabled", "disabled", "disabled", "disabled"]

# 1D Array of the colours that are iterated through for the title
titleColourList = ["#ebebff", "#dbd8ff", "#d8d8ff", "#c9c4ff", "#c4c4ff", "#b1b1ff",
                   "#b8b1ff", "#9d9dff", "#a59dff", "#8989ff", "#9389ff", "#7676ff",
                   "#8176ff", "#6262ff", "#6f62ff", "#4e4eff", "#5d4eff", "#3b3bff",
                   "#4b3bff", "#2727ff", "#3927ff", "#1414ff", "#2814ff"]

titleColour = "#ebebff"

# 2D Array of the directories for each LevelTime text file,
# and their coresponding level number
leaderboardIndexArray = [["LevelTimes/LevelOneTimes.txt", "Level 1"],["LevelTimes/LevelTwoTimes.txt", "Level 2"],
                         ["LevelTimes/LevelThreeTimes.txt", "Level 3"],["LevelTimes/LevelFourTimes.txt", "Level 4"],
                         ["LevelTimes/LevelFiveTimes.txt", "Level 5"],["LevelTimes/LevelSixTimes.txt", "Level 6"],
                         ["LevelTimes/LevelSevenTimes.txt", "Level 7"],["LevelTimes/LevelEightTimes.txt", "Level 8"],
                         ["LevelTimes/LevelNineTimes.txt", "Level 9"],["LevelTimes/LevelTenTimes.txt", "Level 10"],
                         ["LevelTimes/FinalLevelTimes.txt", "Final Level"]]

window = Tk() # Creates an instance of Tk to be used of the window

# Makes the window fullscreen
window.attributes("-fullscreen", True)

window.config(bg = greyColour, cursor = "tcross")
window.title("Sky Climber")

# Gets the directory path of "Sky Climber.py"
# Adds the file names to the directory path so a true path
# is made for the PhotoImage method
dirPath = "C:\Sky Climber" + "\Textures"
dirPathMenuBackground = dirPath + "\MenuBackground.gif"
dirPathCharacterRight = dirPath + "\CharacterRight.gif"
dirPathCharacterLeft = dirPath + "\CharacterLeft.gif"

# Defines the tkinter variables are able to
# be dynamically changed by the widgets
coinChangeSpeed = IntVar()
coinChangeSpeed.set(150)
menuChangeSpeed = IntVar()
menuChangeSpeed.set(55)
gameUpdateSpeed = IntVar()
gameUpdateSpeed.set(16)
enemySpeed = IntVar()
enemySpeed.set(8)
scrollSpeed = DoubleVar()
scrollSpeed.set(1.49)
gameAnimations = BooleanVar()
gameAnimations.set(True)
menuArrows = BooleanVar()
menuArrows.set(False)
menuColourChange = BooleanVar()
menuColourChange.set(True)
textWobble = StringVar()
textWobble.set("sunken")
statSelection = StringVar()
statSelection.set("")

# Gets the images for the game
menuBackground = PhotoImage(file = dirPathMenuBackground)
grassCentre = PhotoImage(file = dirPath + "\Grass_Centre.gif")
grassEdgeRight = PhotoImage(file = dirPath + "\Grass_Edge_Right.gif")
dirtCentre = PhotoImage(file = dirPath + "\Dirt_Centre.gif")
dirtEdgeRight = PhotoImage(file = dirPath + "\Dirt_Edge_Right.gif")
tree1 = PhotoImage(file = dirPath + "\Tree_1.gif")
gameBackgroundGrass = PhotoImage(file = dirPath + "\Game_Background_Grass.gif")
dirtEdgeLeft = PhotoImage(file = dirPath + "\Dirt_Edge_Left.gif")
grassEdgeLeft = PhotoImage(file = dirPath + "\Grass_Edge_Left.gif")
stoneCentre = PhotoImage(file = dirPath + "\Stone_Centre.gif")
stoneTop = PhotoImage(file = dirPath + "\Stone_Top.gif")
sawBlade = PhotoImage(file = dirPath + "\Saw_Blade.gif")
sawBlade2 = PhotoImage(file = dirPath + "\Saw_Blade_2.gif")
sawBlade3 = PhotoImage(file = dirPath + "\Saw_Blade_3.gif")
sawBlade4 = PhotoImage(file = dirPath + "\Saw_Blade_4.gif")
sawBlade5 = PhotoImage(file = dirPath + "\Saw_Blade_5.gif")
sawBlade6 = PhotoImage(file = dirPath + "\Saw_Blade_6.gif")
sawBlade7 = PhotoImage(file = dirPath + "\Saw_Blade_7.gif")
sawBlade8 = PhotoImage(file = dirPath + "\Saw_Blade_8.gif")

# Loads the "world1Assets" array from "LevelSelectionAssets"
world1Assets = levelSelection.world1AssetsArray(menuBackground, greyColour)

# If there is something inside of GameStats.dat
# then it will load the serialised data from it
# If there is nothing in the file, a new dictionary will be made
#if os.path.getsize( dirPath + "\GameStats.dat") > 0:
#    with open(dirPath + "GameStats.dat", "rb") as statsFile:
#        gameStats = pickle.load(statsFile)
#else:
#    gameStats = {"TotalJumps" : 0, "TotalDeaths" : 0, "TotalWins" : 0, "TotalCoins" : 0}

class windowManipulation:
    """Class for the main menu generation and anything that handles the root window"""

    def mainMenu():
        """Sets up the main menu in a canvas"""

        global menuCanvas, window, quitMenuButton, startMenuButton, menuBackground, menuOpen, titleColour, menuTitle, arrowLine, arrowObjects, buttonState
        global acheivementMenuButton, optionsMenuButton

        # Creates the menu canvas
        # Draws the box that includes the main buttons
        menuOpen = True
        buttonState = "normal"
        statSelection.set("")
        menuCanvas = Canvas(window, bg = "white", highlightthickness = 0)
        menuCanvas.create_image("0 0", image = menuBackground, anchor = "nw")

        arrowLine = menuCanvas.create_rectangle("0 -100 1920 -100", width = 0, tags = "ArrowLine")
        menuCanvas.create_line("300 1160 300 1080", fill = titleColour, width = 15, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("100 1280 100 1220", fill = titleColour, width = 12, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("400 1390 400 1310", fill = titleColour, width = 15, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("225 1500 225 1440", fill = titleColour, width = 9, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("1620 1160 1620 1080", fill = titleColour, width = 15, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("1820 1280 1820 1220", fill = titleColour, width = 12, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("1520 1390 1520 1310", fill = titleColour, width = 15, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        menuCanvas.create_line("1695 1500 1695 1440", fill = titleColour, width = 9, arrow = "last", tags = ("ColourChange", "MenuArrow"))
        arrowObjects = menuCanvas.find_withtag("MenuArrow")

        menuCanvas.create_line("1414 75 514 75", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_line("1414 280 514 280", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_line("511 74 511 280", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_line("1416 74 1416 280", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_rectangle("514 75 1414 280", fill = greyColour, outline = greyColour)
        menuCanvas.create_text("965 175", text = "Sky Climber", fill = titleColour, font = "Times 110 bold", tags = "ColourChange")

        menuCanvas.create_line("1414 355 514 355", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_line("1414 1005 514 1005", fill = greyColour, width = 10, capstyle = "round", dash = 255) # Y = 960, diffrence = 45
        menuCanvas.create_line("511 354 511 1005", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_line("1416 354 1416 1005", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        menuCanvas.create_rectangle("514 355 1414 1005", fill = greyColour, outline = greyColour)

        # Draws the buttons for the main menu
        startMenuButton = Button(menuCanvas, text = "Start!", bg = greyColour, overrelief = textWobble.get(), fg = "white", font = "Arial 90 bold", state = buttonState, relief = "ridge", border = 0, activebackground = greyColour, activeforeground = greyColour, command = levelGeneration.levelSelectionGeneration, compound = "center")
        startMenuButton.place(relx = 0.4131, rely = 0.35, relheight = 0.1, relwidth = 0.18)
        acheivementMenuButton = Button(menuCanvas, text = "Statistics", bg = greyColour, overrelief = textWobble.get(), fg = "white", font = "Arial 90 bold", state = buttonState, relief = "ridge", border = 0, activebackground = greyColour, activeforeground = greyColour, command = Statistics.statisticsMenu, compound = "center")
        acheivementMenuButton.place(relx = 0.354, rely = 0.46, relheight = 0.1, relwidth = 0.3)
        optionsMenuButton = Button(menuCanvas, text = "Options", bg = greyColour, overrelief = textWobble.get(), fg = "white", font = "Arial 90 bold", state = buttonState, relief = "ridge", border = 0, activebackground = greyColour, activeforeground = greyColour, command = Options.optionsMenu, compound = "center")
        optionsMenuButton.place(relx = 0.374, rely = 0.555, relheight = 0.13, relwidth = 0.257)
        quitMenuButton = Button(menuCanvas, text = "Quit", bg = greyColour, overrelief = textWobble.get(), fg = "white", font = "Arial 90 bold", state = buttonState, relief = "ridge", border = 0, activebackground = greyColour, activeforeground = greyColour, command = windowManipulation.quitCheck, compound = "center")
        quitMenuButton.place(relx = 0.431, rely = 0.8, relheight = 0.1, relwidth = 0.14)

        menuCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # Bindings for the buttons on the main menu
        # If the mouse hovers over any of the menu buttons the text gets turned to yellow
        # When the mouse leaves the text it gets retrurned back to white
        # This only happens if the TopLevel window "quitCheck" is not open
        startMenuButton.bind("<Enter>", lambda startEnter: startMenuButton.config(fg = "yellow") if topLevelOpen == False else ())
        startMenuButton.bind("<Leave>", lambda startLeave: startMenuButton.config(fg = "white") if topLevelOpen == False else ())
        acheivementMenuButton.bind("<Enter>", lambda acheiveEnter: acheivementMenuButton.config(fg = "yellow") if topLevelOpen == False else ())
        acheivementMenuButton.bind("<Leave>", lambda acheiveLeave: acheivementMenuButton.config(fg = "white") if topLevelOpen == False else ())
        optionsMenuButton.bind("<Enter>", lambda optionsEnter: optionsMenuButton.config(fg = "yellow") if topLevelOpen == False else ())
        optionsMenuButton.bind("<Leave>", lambda optionsLeave: optionsMenuButton.config(fg = "white") if topLevelOpen == False else ())
        quitMenuButton.bind("<Enter>", lambda quitEnter: quitMenuButton.config(fg = "red") if topLevelOpen == False else ())
        quitMenuButton.bind("<Leave>", lambda quitLeave: quitMenuButton.config(fg = "white") if topLevelOpen == False else ())

        # All threads that need to called once the main menu has been drawn
        menuCanvas.after(250, windowManipulation.titleColourChanger)
        windowManipulation.arrowCollision()
        windowManipulation.arrowMover()

        window.mainloop() # The main event thread for the Tk instance

    def arrowCollision():
        global menuCanvas, arrowLine, arrowObjects

        # Checks if the menu arrows have been turned on in settigns
        if menuArrows.get():
            arrowLineCoords = menuCanvas.coords(arrowLine)
            arrowLineOverlapping = menuCanvas.find_overlapping(*arrowLineCoords)

            for i in arrowObjects:
                if i in arrowLineOverlapping:
                    # If an arrow overlaps the arrowLine
                    # then it moved to the bottom of the screen
                    menuCanvas.move(i, 0, 1350)

            menuCanvas.after(15, windowManipulation.arrowCollision)

    def titleColourChanger():
        """Changes the colour of the main menu title"""

        global titleColourList, titleColour, menuTitle, menuCanvas

        if menuColourChange.get():
            for i in range(len(titleColourList)):
                try:
                    if titleColour == titleColourList[i]:
                        titleColour = titleColourList[i + 1]
                        break
                except IndexError:
                    # If the thread iterates past the size of the colours
                    # list then it returns titleColour to the first item
                    titleColour = titleColourList[0]

            menuCanvas.itemconfig("ColourChange", fill = titleColour)
            menuCanvas.after(menuChangeSpeed.get(), windowManipulation.titleColourChanger)

    def arrowMover():
        """Moves the arrows"""

        global menuCanvas

        if menuArrows.get():
            # Moves all the arrows up by 6 pixels
            menuCanvas.move("MenuArrow", 0, -6)
            menuCanvas.after(menuChangeSpeed.get(), windowManipulation.arrowMover)

    def quitCheck():
        """When the user presses a button to quit the game this TopLevel window appears
            to ask if they are sure they want to quit allowing them to cancel or quit"""

        global menuCanvas, window, greyColour, topLevelOpen, quitCheckWidget, menuOpen, quitMenuButton, startMenuButton, buttonState
        global acheivementMenuButton, optionsMenuButton

        topLevelOpen = True
        buttonState = "disabled"
        quitCheckWidget = Toplevel(window)
        quitCheckWidget.resizable(False, False) # Makes so the TopLevel is not able to be resized
        quitCheckWidget.overrideredirect(1) # Removes all window borders
        quitCheckWidget.attributes("-alpha", 0.9)
        quitCheckWidget.config(bg = "#585858", cursor = "tcross")

        # If the menu is open when the quitCheck is ran
        # the menu button are returned to their orginal state
        if menuOpen == True:
            acheivementMenuButton.config(state = buttonState)
            optionsMenuButton.config(state = buttonState)
            quitMenuButton.config(image = "", fg = "white", border = 0, state = buttonState)
            startMenuButton.config(image = "", fg = "white", border = 0, state = buttonState)

        # Gets the width and height of the screen and window
        # To make sure the TopLevel window is drawn in the centre of the screen
        windowWidth = quitCheckWidget.winfo_reqwidth()
        windowHeight = quitCheckWidget.winfo_reqheight()
        positionRight = int(quitCheckWidget.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(quitCheckWidget.winfo_screenheight()/2 - windowHeight/2)
        quitCheckWidget.geometry("190x100+{}+{}".format(positionRight, positionDown))

        Label(quitCheckWidget, bg = greyColour, borderwidth = 4, relief = "solid").place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        Label(quitCheckWidget, text = "Are You Sure?", bg = "#585858", font = "Arial 14 bold").place(relx = 0.14, rely = 0.1)
        topLevelQuit = Button(quitCheckWidget, text = "Quit!", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 12 italic", activebackground = greyColour, activeforeground = greyColour, command = windowManipulation.quitGame)
        topLevelQuit.place(relx = 0.55, rely = 0.66, relwidth = 0.25, relheight = 0.3)
        topLevelCancel = Button(quitCheckWidget, text = "Cancel", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 12 italic", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("TopLevelDestroy"))
        topLevelCancel.place(relx = 0.2, rely = 0.66, relwidth = 0.28, relheight = 0.3)

        # Makes the buttons yellow when they are hovered over
        topLevelQuit.bind("<Enter>", lambda topQuitEnter: topLevelQuit.config(fg = "red"))
        topLevelQuit.bind("<Leave>", lambda topQuitLeave: topLevelQuit.config(fg = "white"))
        topLevelCancel.bind("<Enter>", lambda topCancelEnter: topLevelCancel.config(fg = "yellow"))
        topLevelCancel.bind("<Leave>", lambda topCancelLeave: topLevelCancel.config(fg = "white"))

    def pauseMenu():
        """The pause menu that is drawn when Esc is pressed in game,
           allows the restart, resume and exiting of the level"""

        global pauseMenuWidget, pauseOpen, playingGame, stageCanvas, gameActive, greyColour, headsUp

        pauseOpen = True
        gameActive = False
        headsUp.destroy()
        stageCanvas.config(cursor = "tcross")
        pauseMenuWidget = Toplevel(window)
        pauseMenuWidget.config(bg = "#585858", cursor = "tcross")

        # Makes so the TopLevel is fullscreen and the whole window becomes
        # transparent so the screen is darkened when the menu is drawn
        pauseMenuWidget.attributes("-fullscreen", True)
        pauseMenuWidget.attributes("-alpha", 0.65)

        # Gets the width and height of the screen and window
        # To make sure the TopLevel window is drawn in the centre of the screen
        windowWidth = pauseMenuWidget.winfo_reqwidth()
        windowHeight = pauseMenuWidget.winfo_reqheight()
        positionRight = int(pauseMenuWidget.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(pauseMenuWidget.winfo_screenheight()/2 - windowHeight/2)
        pauseMenuWidget.geometry("+{}+{}".format(positionRight, positionDown))

        Label(pauseMenuWidget, bg = greyColour, borderwidth = 4, relief = "solid").place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        Label(pauseMenuWidget, text = "Paused", bg = "#585858", fg = "light blue", font = "Arial 150 bold").place(relx = 0.315, rely = 0.065)
        pauseQuit = Button(pauseMenuWidget, text = "Back To Map", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("BackToMap"))
        pauseQuit.place(relx = 0.377, rely = 0.37)
        pauseCancel = Button(pauseMenuWidget, text = "Resume", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("PauseMenuDestroy"))
        pauseCancel.place(relx = 0.415, rely = 0.46)
        pauseRestart = Button(pauseMenuWidget, text = "Restart", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("PauseMenuRestart"))
        pauseRestart.place(relx = 0.42, rely = 0.55)

        # Makes the buttons yellow when they are hovered over
        pauseQuit.bind("<Enter>", lambda menuEnter: pauseQuit.config(fg = "yellow"))
        pauseQuit.bind("<Leave>", lambda menuLeave: pauseQuit.config(fg = "white"))
        pauseCancel.bind("<Enter>", lambda quitLevelEnter: pauseCancel.config(fg = "yellow"))
        pauseCancel.bind("<Leave>", lambda quitLevelLeave: pauseCancel.config(fg = "white"))
        pauseRestart.bind("<Enter>", lambda quitLevelEnter: pauseRestart.config(fg = "yellow"))
        pauseRestart.bind("<Leave>", lambda quitLevelLeave: pauseRestart.config(fg = "white"))

    def loseScreen():
        global loseWidget, loseOpen, playingGame, stageCanvas, headsUp, gameStats

        loseOpen = True
        headsUp.destroy()
        gameStats["TotalDeaths"] += 1

        # Draws the cursor on the stage canvas
        stageCanvas.config(cursor = "tcross")
        loseWidget = Toplevel(window)
        loseWidget.config(bg = "red", cursor = "tcross")

        # Makes so the TopLevel is fullscreen and the whole window becomes
        # transparent so the screen is darkened when the menu is drawn
        loseWidget.attributes("-fullscreen", True)
        loseWidget.attributes("-alpha", 0.65)

        # Gets the width and height of the screen and window
        # To make sure the TopLevel window is drawn in the centre of the screen
        windowWidth = loseWidget.winfo_reqwidth()
        windowHeight = loseWidget.winfo_reqheight()
        positionRight = int(loseWidget.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(loseWidget.winfo_screenheight()/2 - windowHeight/2)
        loseWidget.geometry("+{}+{}".format(positionRight, positionDown))

        Label(loseWidget, bg = greyColour, borderwidth = 4, relief = "solid", highlightbackground = "red").place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        Label(loseWidget, text = "You Died!", bg = "#585858", fg = "red", font = "Arial 200 bold").place(relx = 0.18, rely = 0.065)
        loseQuit = Button(loseWidget, text = "Back To Map", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("BackToMapLose"))
        loseQuit.place(relx = 0.37, rely = 0.45)
        loseRetry = Button(loseWidget, text = "Retry", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("LoseMenuDestroy"))
        loseRetry.place(relx = 0.43, rely = 0.54)

        # Makes the buttons yellow when they are hovered over
        loseQuit.bind("<Enter>", lambda menuEnter: loseQuit.config(fg = "yellow"))
        loseQuit.bind("<Leave>", lambda menuLeave: loseQuit.config(fg = "white"))
        loseRetry.bind("<Enter>", lambda quitLevelEnter: loseRetry.config(fg = "yellow"))
        loseRetry.bind("<Leave>", lambda quitLevelLeave: loseRetry.config(fg = "white"))

    def completeScreen():
        global completeWidget, playingGame, stageCanvas, headsUp, seconds, minutes, gameStats

        headsUp.destroy()
        gameStats["TotalWins"] += 1
        stageCanvas.config(cursor = "tcross")
        completeWidget = Toplevel(window)
        completeWidget.config(bg = "red", cursor = "tcross")

        # Makes so the TopLevel is fullscreen and the whole window becomes
        # transparent so the screen is darkened when the menu is drawn
        completeWidget.attributes("-fullscreen", True)
        completeWidget.attributes("-alpha", 0.65)

        # Gets the width and height of the screen and window
        # To make sure the TopLevel window is drawn in the centre of the screen
        windowWidth = completeWidget.winfo_reqwidth()
        windowHeight = completeWidget.winfo_reqheight()
        positionRight = int(completeWidget.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(completeWidget.winfo_screenheight()/2 - windowHeight/2)
        completeWidget.geometry("+{}+{}".format(positionRight, positionDown))

        Label(completeWidget, bg = greyColour, borderwidth = 4, relief = "solid", highlightbackground = "red").place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        Label(completeWidget, text = "Level Complete!", bg = "#585858", fg = "light blue", font = "Arial 180 bold").place(relx = 0.02, rely = 0.065)
        completeQuit = Button(completeWidget, text = "Back To Map", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("BackToMapComplete"))
        completeQuit.place(relx = 0.37, rely = 0.45)
        completeRetry = Button(completeWidget, text = "Retry", bg = greyColour, overrelief = textWobble.get(), fg = "white", relief = "ridge", border = 0, font = "Arial 50 bold", activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("CompleteMenuDestroy"))
        completeRetry.place(relx = 0.43, rely = 0.54)

        # Checks if minute(s) or second(s) needs to be pluralised
        if minutes == 1:
            minutesString = "minute"
        else:
            minutesString = "minutes"
        if seconds == 1:
            secondsString = "second"
        else:
            secondsString = "seconds"
        Label(completeWidget, text = ("Level Completed In: " + str(minutes) + " " + minutesString + " and " + str(seconds) + " " + secondsString), bg = greyColour, fg = "dark blue", font = "Arial 40 bold").place(relx = 0.2, rely = 0.75)

        # Makes the buttons yellow when they are hovered over
        completeQuit.bind("<Enter>", lambda menuEnter: completeQuit.config(fg = "yellow"))
        completeQuit.bind("<Leave>", lambda menuLeave: completeQuit.config(fg = "white"))
        completeRetry.bind("<Enter>", lambda quitLevelEnter: completeRetry.config(fg = "yellow"))
        completeRetry.bind("<Leave>", lambda quitLevelLeave: completeRetry.config(fg = "white"))

    def headsUpDisplay():
        global headsUp, headsUpCanvas, greyColour, headsUpCoinCounter

        headsUp = Toplevel(window)

        # Stops from window decoration from being drawn, such as border and shadow
        headsUp.overrideredirect(1)
        headsUp.geometry("1920x200")
        headsUp.attributes("-alpha", 0.65)
        headsUp.config(cursor = "none")

        headsUpCanvas = Canvas(headsUp, bg = "#585858", highlightthickness = 0)
        headsUpCanvas.pack(side = "left", expand = True, fill = "both")

        headsUpCanvas.create_line("0 200 1920 200", fill = "white", width = 10, capstyle = "round", dash = 255)
        headsUpCanvas.create_line("1650 65 1650 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1850 65 1850 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1650 135 1850 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1650 65 1700 65", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1850 65 1800 65", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_text("1750 62", text = "time", fill = "dark blue", font = "Arial 20 bold")

        headsUpCanvas.create_line("1350 65 1350 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1550 65 1550 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1350 135 1550 135", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1350 65 1400 65", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_line("1550 65 1500 65", fill = "dark blue", width = 3, capstyle = "round")
        headsUpCanvas.create_text("1450 62", text = "coins", fill = "dark blue", font = "Arial 20 bold")
        headsUpCoinCounter = Entry(headsUp, bg = greyColour, fg = "dark blue", justify = "center", border = 0, font = "Arial 50 bold")
        headsUpCoinCounter.place(relx = 0.705, rely = 0.359, relwidth = 0.1, relheight = 0.29)


    def quitGame():
        """Does what it says :)"""

        with open("GameStats.dat", "wb") as statsFile:
            pickle.dump(gameStats, statsFile)

        window.destroy()

    def closeMediator(arguement):
        """When a "object.destroy()" needs to happen, it happens here to allow for variables
           to be changed before going into the desired function"""

        # A whole lot of globalisation
        global levelSelectionCanvas, quitCheckWidget, topLevelOpen, pauseMenuWidget, pauseOpen, stageCanvas, loseWidget, gameActive, loseOpen, whichStage, headsUpCoinCounter, coinCount, optionsCanvas
        global statsisticsCanvas, statisticsSelect, buttonState
        global startMenuButton, acheivementMenuButton, optionsMenuButton, quitMenuButton, levelQuit

        if arguement == "BackToMenu":
            levelSelectionCanvas.destroy()
            windowManipulation.mainMenu()
        elif arguement == "TopLevelDestroy":
            topLevelOpen = False
            buttonState = "normal"
            acheivementMenuButton.config(state = buttonState)
            optionsMenuButton.config(state = buttonState)
            quitMenuButton.config(state = buttonState)
            startMenuButton.config(state = buttonState)
            quitCheckWidget.destroy()
        elif arguement == "BackToMap":
            stageCanvas.destroy()
            pauseMenuWidget.destroy()
            levelGeneration.levelSelectionGeneration()
        elif arguement == "PauseMenuDestroy":
            pauseOpen = False
            stageCanvas.after(350)
            gameActive = True
            stageCanvas.config(cursor = "none")
            windowManipulation.headsUpDisplay()
            headsUpCoinCounter.insert(0, coinCount)
            pauseMenuWidget.destroy()
        elif arguement == "LoseMenuDestroy":
            loseOpen = False
            loseWidget.destroy()
            stageCanvas.destroy()
            levelGeneration.stageGeneration(whichStage)
        elif arguement == "BackToMapLose":
            loseWidget.destroy()
            stageCanvas.destroy()
            levelGeneration.levelSelectionGeneration()
        elif arguement == "PauseMenuRestart":
            pauseMenuWidget.destroy()
            stageCanvas.destroy()
            levelGeneration.stageGeneration(whichStage)
        elif arguement == "BackToMapComplete":
            levelQuit = True
            completeWidget.destroy()
            stageCanvas.destroy()
            levelGeneration.levelSelectionGeneration()
        elif arguement == "CompleteMenuDestroy":
            levelQuit = True
            completeWidget.destroy()
            stageCanvas.destroy()
            levelGeneration.stageGeneration(whichStage)
        elif arguement == "OptionsQuit":
            optionsCanvas.destroy()
            windowManipulation.mainMenu()
        elif arguement == "StatsQuit":
            statisticsCanvas.destroy()
            statisticsSelect.destroy()
            windowManipulation.mainMenu()


class Options:
    """Class for everything that has to do with
       the options portion of the menu"""


    def optionsMenu():
        """Draws all of the widgets and canvas for the options menu"""

        global menuCanvas, leftControlLabel, rightControlLabel, jumpControlLabel, optionsCanvas, coinChangeSpeed
        global optionsBackToMenuButton, leftRebindButton, rightRebindButton, jumpRebindButton, controlDefaultsButton

        menuCanvas.destroy()
        # Draws the canvas, with the background and dashed rectangle
        optionsCanvas = Canvas(window, bg = "#585858")
        optionsCanvas.pack(side = "left", expand = True, fill = "both")
        optionsCanvas.create_image("0 0", image = menuBackground, anchor = "nw")
        optionsCanvas.create_line("50 1030 1890 1030", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        optionsCanvas.create_line("50 50 1890 50", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        optionsCanvas.create_line("50 50 50 1030", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        optionsCanvas.create_line("1870 50 1870 1030", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        optionsCanvas.create_rectangle("50 50 1870 1030", fill = greyColour, outline = greyColour)
        optionsCanvas.focus_set()

        optionsBackToMenuButton = Button(optionsCanvas, text = "Back To Menu", bg = "#585858", fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 23 bold", activebackground = "#585858", activeforeground = "#585858", command = lambda: windowManipulation.closeMediator("OptionsQuit"))
        optionsBackToMenuButton.place(relx = 0.04, rely = 0.89)

        #----Controls sub-options----
        optionsCanvas.create_text("207 100", text = "Controls", fill = "blue", font = "Arial 40 underline", tags = "ColourChangeOptions1")
        optionsCanvas.create_text("121 173", text = "Left", fill = "white", font = "Arial 20 bold")
        leftControlLabel = Label(optionsCanvas, bg = "#585858", fg = "white", highlightbackground = "white", relief = "solid", font = "Arial 15 bold")
        leftControlLabel.place(relx = 0.05, rely = 0.177, relwidth = 0.075, relheight = 0.025)
        leftRebindButton = Button(optionsCanvas, text = "Re-Bind", bg = "#585858", fg = "white", font = "Arial 12 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = "#585858", activeforeground = "#585858", command = Options.leftControlPress)
        leftRebindButton.place(relx = 0.128, rely = 0.176)
        optionsCanvas.create_text("130 242", text = "Right", fill = "white", font = "Arial 20 bold")
        rightControlLabel = Label(optionsCanvas, bg = "#585858", fg = "white", highlightbackground = "white", relief = "solid", font = "Arial 15 bold")
        rightControlLabel.place(relx = 0.05, rely = 0.24, relwidth = 0.075, relheight = 0.025)
        rightRebindButton = Button(optionsCanvas, text = "Re-Bind", bg = "#585858", fg = "white", font = "Arial 12 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = "#585858", activeforeground = "#585858", command = Options.rightControlPress)
        rightRebindButton.place(relx = 0.128, rely = 0.24)
        optionsCanvas.create_text("135 308", text = "Jump", fill = "white", font = "Arial 20 bold")
        jumpControlLabel = Label(optionsCanvas, bg = "#585858", fg = "white", highlightbackground = "white", relief = "solid", font = "Arial 15 bold")
        jumpControlLabel.place(relx = 0.05, rely = 0.302, relwidth = 0.075, relheight = 0.025)
        jumpRebindButton = Button(optionsCanvas, text = "Re-Bind", bg = "#585858", fg = "white", font = "Arial 12 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = "#585858", activeforeground = "#585858", command = Options.jumpControlPress)
        jumpRebindButton.place(relx = 0.128, rely = 0.302)
        controlDefaultsButton = Button(optionsCanvas, text = "Defaults", bg = "#585858", fg = "white", font = "Arial 18 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = "#585858", activeforeground = "#585858", command = Options.keyBindDefaults)
        controlDefaultsButton.place(relx = 0.045, rely = 0.33)

        #----Special sub-options----
        optionsCanvas.create_text("200 445", text = "Special", fill = "blue", font = "Arial 40 underline")
        coinEpilepsyCheck = Checkbutton(optionsCanvas, text = "Coin Epilepsy Mode", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = coinChangeSpeed, onvalue = 15, offvalue = 150)
        coinEpilepsyCheck.place(relx = 0.0485, rely = 0.45)
        menuEpilepsyCheck = Checkbutton(optionsCanvas, text = "Menu Epilepsy Mode", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = menuChangeSpeed, onvalue = 10, offvalue = 55)
        menuEpilepsyCheck.place(relx = 0.0485, rely = 0.475)
        enemySpeedScale = Scale(optionsCanvas, from_ = 1, to = 50, width = 16, resolution = 1, cursor = "sb_h_double_arrow", label = "Enemy Speed:", font = "Arial 14 bold", bg = "#585858", activebackground = "yellow", fg = "white", troughcolor = "black", highlightthickness = 0, orient = "horizontal", variable = enemySpeed)
        enemySpeedScale.place(relx = 0.0465, rely = 0.513, relwidth = 0.115)

        #----Game sub-options----
        optionsCanvas.create_text("575 100", text = "Game", fill = "blue", font = "Arial 40 underline")
        optionsCanvas.create_text("578 155", text = "Game Update Speed:", fill = "white", font = "Arial 15 bold")
        fourUpdateSpeed = Radiobutton(optionsCanvas, text = "4 Milliseconds", bg = "#585858", fg = "black", activebackground = "#585858", activeforeground = "black", font = "Arial 13", variable = gameUpdateSpeed, value = 4)
        fourUpdateSpeed.place(relx = 0.247, rely = 0.161)
        sixteenUpdateSpeed = Radiobutton(optionsCanvas, text = "16 Milliseconds", bg = "#585858", fg = "black", activebackground = "#585858", activeforeground = "black", font = "Arial 13", variable = gameUpdateSpeed, value = 16)
        sixteenUpdateSpeed.place(relx = 0.247, rely = 0.182)
        thirytwoUpdateSpeed = Radiobutton(optionsCanvas, text = "32 Milliseconds (Debug Only)", bg = "#585858", fg = "black", activebackground = "#585858", activeforeground = "black", font = "Arial 13", variable = gameUpdateSpeed, value = 32)
        thirytwoUpdateSpeed.place(relx = 0.247, rely = 0.203)
        # Checks what the current game update speed is
        # and checks the coresponding radiobutton
        if gameUpdateSpeed.get() == 16:
            sixteenUpdateSpeed.select()
        elif gameUpdateSpeed.get() == 4:
            fourUpdateSpeed.select()
        else:
            thirytwoUpdateSpeed.select()
        gameAnimationsCheck = Checkbutton(optionsCanvas, text = "Coin Animations Off", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = gameAnimations, onvalue = False, offvalue = True)
        gameAnimationsCheck.place(relx = 0.247, rely = 0.235)
        fastScrollCheck = Checkbutton(optionsCanvas, text = "Fast Autoscroll", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = scrollSpeed, onvalue = 1.5, offvalue = 1.49)
        fastScrollCheck.place(relx = 0.247, rely = 0.26)

        #----Menu sub-options----
        optionsCanvas.create_text("943 100", text = "Menu", fill = "blue", font = "Arial 40 underline")
        menuArrowsCheck = Checkbutton(optionsCanvas, text = "Arrows On", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = menuArrows, onvalue = True, offvalue = False)
        menuArrowsCheck.place(relx = 0.446, rely = 0.13)
        menuColourChangeCheck = Checkbutton(optionsCanvas, text = "Colour Change Off", bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = menuColourChange, onvalue = False, offvalue = True)
        menuColourChangeCheck.place(relx = 0.446, rely = 0.153)
        textWobbleCheck = Checkbutton(optionsCanvas, text = "Text Wobble Off", command = Options.optionsTextWobbleUpdate, bg = "#585858", fg = "white", selectcolor = "black", activebackground = "#585858", activeforeground = "white", font = "Arial 15", variable = textWobble, onvalue = "ridge", offvalue = "sunken")
        textWobbleCheck.place(relx = 0.446, rely = 0.185)

        leftControlLabel.config(text = leftControl.upper())
        rightControlLabel.config(text = rightControl.upper())
        jumpControlLabel.config(text = jumpControl.upper())

        #----Buuton clours changes whilst hovered over---
        optionsBackToMenuButton.bind("<Enter>", lambda backToMenuEnter: optionsBackToMenuButton.config(fg = "yellow"))
        optionsBackToMenuButton.bind("<Leave>", lambda backToMenuLeave: optionsBackToMenuButton.config(fg = "white"))
        controlDefaultsButton.bind("<Enter>", lambda defaultsEnter: controlDefaultsButton.config(fg = "yellow"))
        controlDefaultsButton.bind("<Leave>", lambda defaultsLeave: controlDefaultsButton.config(fg = "white"))
        leftRebindButton.bind("<Enter>", lambda bindEnter: leftRebindButton.config(fg = "yellow"))
        leftRebindButton.bind("<Leave>", lambda bindLeave: leftRebindButton.config(fg = "white"))
        rightRebindButton.bind("<Enter>", lambda bindEnter: rightRebindButton.config(fg = "yellow"))
        rightRebindButton.bind("<Leave>", lambda bindLeave: rightRebindButton.config(fg = "white"))
        jumpRebindButton.bind("<Enter>", lambda bindEnter: jumpRebindButton.config(fg = "yellow"))
        jumpRebindButton.bind("<Leave>", lambda bindLeave: jumpRebindButton.config(fg = "white"))

    def scrollbarValueSet():
        pass # I dont even know what this is for, I forgot, so im just going to leave it here ;)

    def optionsTextWobbleUpdate():
        """When the text wobble option is changed it
           updates all of the widgets on the menu"""

        global optionsBackToMenuButton, leftRebindButton, rightRebindButton, jumpRebindButton, controlDefaultsButton

        optionsBackToMenuButton.config(overrelief = textWobble.get())
        leftRebindButton.config(overrelief = textWobble.get())
        rightRebindButton.config(overrelief = textWobble.get())
        jumpRebindButton.config(overrelief = textWobble.get())
        controlDefaultsButton.config(overrelief = textWobble.get())

    def leftControlPress():
        """Left rebind, yes"""

        global leftControlLabel, optionsCanvas

        leftControlLabel.config(text = "Press Key...")
        optionsCanvas.bind("<KeyPress>", Options.keyBinderLeft)

    def rightControlPress():
        """Right rebind, yes"""

        global rightControlLabel, optionsCanvas

        rightControlLabel.config(text = "Press Key...")
        optionsCanvas.bind("<KeyPress>", Options.keyBindRight)

    def jumpControlPress():
        """Jump rebind, yes"""

        global jumpControlLabel, optionsCanvas

        jumpControlLabel.config(text = "Press Key...")
        optionsCanvas.bind("<KeyPress>", Options.keyBindJump)


    def keyBinderLeft(event):
        global leftControlLabel, optionsCanvas, leftControl


        leftControl = event.keysym # Gets what key was just pressed
        leftControlLabel.config(text = leftControl.upper())
        optionsCanvas.unbind("<KeyPress>")

    def keyBindRight(event):
        global rightControlLabel, optionsCanvas, rightControl

        rightControl = event.keysym # Gets what key was just pressed
        rightControlLabel.config(text = rightControl.upper())
        optionsCanvas.unbind("<KeyPress>")

    def keyBindJump(event):
        global jumpControlLabel, optionsCanvas, jumpControl

        jumpControl = event.keysym # Gets what key was just pressed
        jumpControlLabel.config(text = jumpControl.upper())
        optionsCanvas.unbind("<KeyPress>")

    def keyBindDefaults():
        """Resets all of the key binds to defaults:
           Left = a; Right = d; Jump = space"""

        global leftControlLabel, rightControlLabel, jumpControlLabel, leftControl, rightControl, jumpControl

        leftControl = "a"
        leftControlLabel.config(text = leftControl.upper())
        rightControl = "d"
        rightControlLabel.config(text = rightControl.upper())
        jumpControl = "space"
        jumpControlLabel.config(text = jumpControl.upper())


class Statistics:
    """Class for everything to do with the stas throughout the game, such as leaderbaords and stats overall"""

    def statisticsMenu():

        global menuCanvas, selectText, statisticsCanvas, statisticsSelect, leaderboardPointer, leaderboardIncrementButton, leaderboardDecrementButton, leaderboardCurrentForget, leaderboardAllForget
        global whichStage, leaderboardRawTimes

        menuCanvas.destroy()

        # Gets the pointer for the leaderboard from whichStage;
        # which would be the index for the last played stage
        leaderboardPointer = whichStage

        # Creates 3 canvases one for the background of the statistics,
        # the second for the selection bar at the top,
        # and the third for the actual stats display
        statisticsBackground = Canvas(window)
        statisticsBackground.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        statisticsBackground.create_image("0 0", image = menuBackground, anchor = "nw")
        statisticsSelect = Canvas(window, bg = "#585858", highlightthickness = 0)
        statisticsSelect.place(x = 50, y = 42, relheight = 0.15, width = 1820)
        statisticsCanvas = Canvas(window, highlightthickness = 0)
        statisticsCanvas.place(relx = 0, rely = 0.2, relheight = 0.8, relwidth = 1)

        statisticsBackground.create_line("50 42 50 204", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        statisticsBackground.create_line("1870 42 1870 204", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        statisticsBackground.create_line("50 42 1870 42", fill = greyColour, width = 10, capstyle = "round", dash = 255)
        statisticsBackground.create_line("50 204 1870 204", fill = greyColour, width = 10, capstyle = "round", dash = 255)

        leaderboardIncrementButton = Button(statisticsCanvas, text = "Next", font = "Arial 20 bold", bg = "#585858", fg = "green", relief = "ridge", border = 0, activebackground = "#585858", activeforeground = "#585858", command = Statistics.leaderboardIncrement)
        leaderboardDecrementButton = Button(statisticsCanvas, text = "Previous", font = "Arial 20 bold", bg = "#585858", fg = "red", relief = "ridge", border = 0, activebackground = "#585858", activeforeground = "#585858", command = Statistics.leaderboardDecrement)
        leaderboardCurrentForget = Button(statisticsCanvas, text = "Wipe Current Leaderboard", font = "Arial 20 bold", bg = "#585858", fg = "white", overrelief = textWobble.get(), relief = "ridge", border = 0, activebackground = "#585858", activeforeground = "#585858", command = Statistics.currentLeaderboardForget)
        leaderboardAllForget = Button(statisticsCanvas, text = "Wipe All Leaderboards", font = "Arial 20 bold", bg = "#585858", fg = "white", overrelief = textWobble.get(), relief = "ridge", border = 0, activebackground = "#585858", activeforeground = "#585858", command = Statistics.allLeaderboardForget)
        leaderboardRawTimes = Button(statisticsCanvas, text = "Display Raw Times", font = "Arial 20 bold", bg = "#585858", fg = "white", overrelief = textWobble.get(), relief = "ridge", border = 0, activebackground = "#585858", activeforeground = "#585858", command = Statistics.rawTimesDisplay)

        statisticsCanvas.create_image("0 -215", image = menuBackground, anchor = "nw")
        selectText = statisticsCanvas.create_text("950 350", text = "Please Select", fill = "#585858", font = "Arial 75 bold")

        statLeaderboard = Radiobutton(statisticsSelect, text = "Leaderboards", font = "Arial 40 underline", command = Statistics.whichStatSelection, border = 4, indicatoron = 0, selectcolor = "#585858", bg = "#585858", fg = "white", activebackground = "#585858", activeforeground = "white", overrelief = "solid", offrelief = "flat", variable = statSelection, value = "Leaderboard")
        statLeaderboard.place(relx = 0.02, rely = 0.25)
        statTotalStats = Radiobutton(statisticsSelect, text = "Total Stats", font = "Arial 40 underline", command = Statistics.whichStatSelection, border = 4, indicatoron = 0, selectcolor = "#585858", bg = "#585858", fg = "white", activebackground = "#585858", activeforeground = "white", overrelief = "solid", offrelief = "flat", variable = statSelection, value = "TotalStats")
        statTotalStats.place(relx = 0.23, rely = 0.25)
        statsBackToMenuButton = Button(statisticsCanvas, text = "Back To Menu", bg = "#585858", fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 23 bold", activebackground = "#585858", activeforeground = "#585858", command = lambda: windowManipulation.closeMediator("StatsQuit"))
        statsBackToMenuButton.place(relx = 0.03, rely = 0.88)

        # Makes the buttons yellow when hovered over
        statsBackToMenuButton.bind("<Enter>", lambda backToMenuEnter: statsBackToMenuButton.config(fg = "yellow"))
        statsBackToMenuButton.bind("<Leave>", lambda backToMenuLeave: statsBackToMenuButton.config(fg = "white"))
        leaderboardCurrentForget.bind("<Enter>", lambda defaultsEnter: leaderboardCurrentForget.config(fg = "yellow"))
        leaderboardCurrentForget.bind("<Leave>", lambda defaultsLeave: leaderboardCurrentForget.config(fg = "white"))
        leaderboardAllForget.bind("<Enter>", lambda bindEnter: leaderboardAllForget.config(fg = "yellow"))
        leaderboardAllForget.bind("<Leave>", lambda bindLeave: leaderboardAllForget.config(fg = "white"))
        leaderboardRawTimes.bind("<Enter>", lambda bindEnter: leaderboardRawTimes.config(fg = "yellow"))
        leaderboardRawTimes.bind("<Leave>", lambda bindLeave: leaderboardRawTimes.config(fg = "white"))

    def whichStatSelection():
        """Changes the statisticsCanvas depending on which
           Radiobutton is sunken in the statsicticsSelection"""

        global leaderboardIncrementButton, leaderboardDecrementButton, leaderboardCurrentForget, leaderboardAllForget, leaderboardRawTimes

        if statSelection.get() == "Leaderboard":
            statisticsCanvas.delete("all")

            statisticsCanvas.create_image("0 -215", image = menuBackground, anchor = "nw")

            statisticsCanvas.create_line("518 263 518 600", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("288 263 288 600", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("1402 263 1402 600", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("1632 263 1632 600", fill = greyColour, width = 10, capstyle = "round", dash = 255)

            statisticsCanvas.create_line("690 70 690 793", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("1210 70 1210 793", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("690 70 1210 70", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("690 793 1210 793", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_rectangle("690 70 1210 793", fill = greyColour, outline = greyColour)

            leaderboardIncrementButton.place(relx = 0.73, rely = 0.3, relwidth = 0.12, relheight = 0.4)
            leaderboardDecrementButton.place(relx = 0.15, rely = 0.3, relwidth = 0.12, relheight = 0.4)
            leaderboardCurrentForget.place(relx = 0.785, rely = 0.8)
            leaderboardAllForget.place(relx = 0.785, rely = 0.85)
            leaderboardRawTimes.place(relx = 0.785, rely = 0.9)

            Statistics.leaderboardGeneration()

        elif statSelection.get() == "TotalStats":
            statisticsCanvas.delete("all")

            statisticsCanvas.create_image("0 -215", image = menuBackground, anchor = "nw")

            statisticsCanvas.create_line("50 820 1890 820", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("50 50 1890 50", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("50 50 50 820", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_line("1870 50 1870 820", fill = greyColour, width = 10, capstyle = "round", dash = 255)
            statisticsCanvas.create_rectangle("50 50 1870 820", fill = greyColour, outline = greyColour)

            statisticsCanvas.create_text("245 100", text = "Game Stats", fill = "blue", font = "Arial 40 underline")
            statisticsCanvas.create_text("245 160", text = ("Total Jumps: " + str(gameStats["TotalJumps"])), fill = "white", font = "Arial 20 bold")
            statisticsCanvas.create_text("245 195", text = ("Total Deaths: " + str(gameStats["TotalDeaths"])), fill = "white", font = "Arial 20 bold")
            statisticsCanvas.create_text("245 230", text = ("Total Wins: " + str(gameStats["TotalWins"])), fill = "white", font = "Arial 20 bold")
            statisticsCanvas.create_text("245 265", text = ("Total Coins: " + str(gameStats["TotalCoins"])), fill = "white", font = "Arial 20 bold")

            leaderboardIncrementButton.place_forget()
            leaderboardDecrementButton.place_forget()
            leaderboardCurrentForget.place_forget()
            leaderboardAllForget.place_forget()
            leaderboardRawTimes.place_forget()

    def rawTimesDisplay():
        """Generates a top level that displays the times for the current
           leaderboard in chronological order; where individual times can be removed"""

        global leaderboardPointer, rawTimesCanvas

        rawTimesWindow = Toplevel(window)

        # Gets the window title from the currently selected leaderbaord
        rawTimesWindow.title(leaderboardIndexArray[leaderboardPointer][1])
        rawTimesWindow.resizable(False, False)
        rawTimesWindow.focus_set()

        # Centres the window in the centre of the screen
        windowWidth = rawTimesWindow.winfo_reqwidth()
        windowHeight = rawTimesWindow.winfo_reqheight()
        positionRight = int(rawTimesWindow.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(rawTimesWindow.winfo_screenheight()/2 - windowHeight/2)
        rawTimesWindow.geometry("270x320+{}+{}".format(positionRight, positionDown))

        rawTimesFrame = Frame(rawTimesWindow, bg = "#585858", height = 10)
        rawTimesScrollbar = Scrollbar(rawTimesFrame, orient = "vertical")

        # Creates a Listbox that can be scrolled by a scrollbar
        rawTimesCanvas = Listbox(rawTimesFrame, yscrollcommand = rawTimesScrollbar.set,
                                height = 15, bg = "#585858", fg = "white", relief = "flat",
                                highlightthickness = 0, activestyle = "dotbox",
                                font = "Arial 10")
        rawTimesScrollbar.config(command = rawTimesCanvas.yview)
        rawTimesCanvas.config(yscrollcommand = rawTimesScrollbar.set,
                             scrollregion = rawTimesCanvas.bbox("active"))

        Button(rawTimesFrame, text = "Delete", bg = "#585858", fg = "white",
              font = "Arial 14 bold", command = Statistics.rawSelectionRemove,
              activeforeground = "#585858", activebackground = "#585858",
              relief = "ridge", overrelief = textWobble.get(), border = 0
              ).place(relx = 0.05, rely = 0.85)

        Button(rawTimesFrame, text = "Close", bg = "#585858", fg = "white",
              font = "Arial 14 bold", command = rawTimesWindow.destroy,
              activeforeground = "#585858", activebackground = "#585858",
              relief = "ridge", overrelief = textWobble.get(), border = 0
              ).place(relx = 0.63, rely = 0.85)

        rawTimesFrame.pack(expand = True, fill = "both")
        rawTimesScrollbar.pack(side = "right", fill = "y")
        rawTimesCanvas.pack(expand = True, fill = "x", anchor= "n")

        # Gets the times from the associated file and puts them into a 1D array;
        # and cocatonating seconds onto each element
        with open(leaderboardIndexArray[leaderboardPointer][0], "r") as levelOneTimes:
            levelOneTimesList = [int(i.rstrip()) for i in levelOneTimes]
            for i in range(len(levelOneTimesList)):
                rawTimesCanvas.insert(END, str(levelOneTimesList[i]) + " Seconds")

        rawTimesScrollbar.config(command = rawTimesCanvas.yview)

        rawTimesWindow.mainloop()

    def rawSelectionRemove():
        """Removes the selected item from the rawTimesListBox
           from the associated file"""

        global leaderboardPointer, rawTimesCanvas

        selectedDelete = rawTimesCanvas.get("active")[0:-8]
        rawTimesCanvas.delete("active")

        with open(leaderboardIndexArray[leaderboardPointer][0], "r") as levelOneTimes:
            levelOneTimesList = [int(i.rstrip()) for i in levelOneTimes]
            for i in range(len(levelOneTimesList)):
                if int(selectedDelete) == int(levelOneTimesList[i]):
                    levelOneTimesList.remove(levelOneTimesList[i])
                    break

        with open(leaderboardIndexArray[leaderboardPointer][0], "w") as levelOneTimes:
            for i in range(len(levelOneTimesList)):
                levelOneTimes.write("%s\n" % levelOneTimesList[i])
            Statistics.leaderboardGeneration()

    def leaderboardIncrement():
        global leaderboardPointer

        if leaderboardPointer != 10:
            leaderboardPointer += 1
        else:
            leaderboardPointer = 0
        Statistics.leaderboardGeneration()

    def leaderboardDecrement():
        global leaderboardPointer

        if leaderboardPointer != 0:
            leaderboardPointer -= 1
        else:
            leaderboardPointer = 10
        Statistics.leaderboardGeneration()

    def currentLeaderboardForget():
        """Wipes all the times from the currently selected leaderboard"""

        global leaderboardPointer

        with open(leaderboardIndexArray[leaderboardPointer][0], "w") as leaderboardFile:
            leaderboardFile.write("")
            Statistics.leaderboardGeneration()

    def allLeaderboardForget():
        """Iterates through every leaderboard removing all times from local files"""

        for i in range(len(leaderboardIndexArray)):
            with open(leaderboardIndexArray[i][0], "w") as leaderboardFile:
                leaderboardFile.write("")
        Statistics.leaderboardGeneration()

    def leaderboardGeneration():
        """Generates the leaderboard everytime it is changed"""

        global selectText, statisticsCanvas, leaderboardPointer

        statisticsCanvas.delete("Leaderboard")

        # Gets the times from the asociated file and puts them in a 1D array
        with open(leaderboardIndexArray[leaderboardPointer][0], "r") as levelOneTimes:
            levelOneTimesList = [int(i.rstrip()) for i in levelOneTimes]

        # Appends Seconds to every element in the list, and if the list isnt full
        # it adds No Time to the list until the size is 10
        sortedList = sorted(levelOneTimesList)
        for i in range(len(sortedList)):
            sortedList[i] = str(sortedList[i]) + " Seconds"
        if len(sortedList) < 10:
            for i in range(10 - len(sortedList)):
                sortedList.append("No Time")

        statisticsCanvas.delete(selectText)
        statisticsCanvas.create_text("950 150", text = leaderboardIndexArray[leaderboardPointer][1], fill = "white", font = "Arial 75 underline", tags = "Leaderboard")
        statisticsCanvas.create_text("948 275", text = "1st - {}".format(sortedList[0]), fill = "gold", font = "Arial 40 italic", justify = "center", tags = "Leaderboard") #93 diffrence in X
        statisticsCanvas.create_text("942 330", text = "2nd - {}".format(sortedList[1]), fill = "#AAA9AD", font = "Arial 35 italic", justify = "center", tags = "Leaderboard") #943
        statisticsCanvas.create_text("945 385", text = "3rd - {}".format(sortedList[2]), fill = "#804A00", font = "Arial 33 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 467", text = "4th - {}".format(sortedList[3]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 513", text = "5th - {}".format(sortedList[4]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 559", text = "6th - {}".format(sortedList[5]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 605", text = "7th - {}".format(sortedList[6]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 651", text = "8th - {}".format(sortedList[7]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("947 697", text = "9th - {}".format(sortedList[8]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")
        statisticsCanvas.create_text("936 743", text = "10th - {}".format(sortedList[9]), fill = "light blue", font = "Arial 30 italic", justify = "center", tags = "Leaderboard")


class levelGeneration:
    """Class for all worlds and stages generation and manipulation"""

    def canvasAutoscroll():
        """Scrolls the canvas left for all levels"""

        global stageCanvas, gameActive, autoscrollLine, scrolling

        if gameActive and scrolling:
            stageCanvas.xview_scroll(1, "units")
            stageCanvas.move(autoscrollLine, 1, 0)

        stageCanvas.after(1, levelGeneration.canvasAutoscroll)

    def levelSelectionGeneration():
        """Draws the level selection"""

        global levelSelectionCanvas, menuCanvas, greyColour, menuOpen, menuBackground, world1Assets, playingGame

        menuOpen = False
        playingGame = False
        listPositionCount = -1
        menuCanvas.destroy()
        levelSelectionCanvas = Canvas(window, bg = greyColour, highlightthickness = 0)
        levelSelectionCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # Generates all of the canvas objects for the level select screen
        # world1Assets is a 2D array in the SkyClimberAssets module
        for i in range(len(world1Assets)):
            if world1Assets[i][0] == "BackImage":
                levelSelectionCanvas.create_image(world1Assets[i][1], image = world1Assets[i][2], anchor = world1Assets[i][3])
            if world1Assets[i][0] == "HeaderText":
                levelSelectionCanvas.create_text(world1Assets[i][1], text = world1Assets[i][2], fill = world1Assets[i][3], font = world1Assets[i][4])
            if world1Assets[i][0] == "QuitLine" or world1Assets[i][0] == "MapBoxLine":
                levelSelectionCanvas.create_line(world1Assets[i][1], fill = world1Assets[i][2], width = world1Assets[i][3], capstyle = world1Assets[i][4], dash = world1Assets[i][5])
            if world1Assets[i][0] == "QuitRect" or world1Assets[i][0] == "MapRect":
                levelSelectionCanvas.create_rectangle(world1Assets[i][1], fill = world1Assets[i][2], outline = world1Assets[i][3])
            if world1Assets[i][0] == "MapLine":
                levelSelectionCanvas.create_line(world1Assets[i][1], fill = world1Assets[i][2], width = world1Assets[i][3], dash = world1Assets[i][4], capstyle = world1Assets[i][5], stipple = world1Assets[i][6])
            if world1Assets[i][0] == "Oval":
                listPositionCount += 1
                levelSelectionCanvas.create_oval(world1Assets[i][1],  fill = levelSelectColours[listPositionCount], width = world1Assets[i][3], outline = world1Assets[i][4])

        # Generates each button that starts the respective level when pressed
        Button(levelSelectionCanvas, text = "1", bg = levelSelectColours[0],
              fg = "white", relief = "ridge", overrelief = textWobble.get(),
              border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[0],
              activeforeground = levelSelectColours[0], state = buttonDisabled[0],
              command = lambda: levelGeneration.stageGeneration(0)
              ).place(relx = 0.0905, rely = 0.4651, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "2", bg = levelSelectColours[1],
              fg = "white", relief = "ridge", overrelief = textWobble.get(),
              border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[1],
              activeforeground = levelSelectColours[1], state = buttonDisabled[1],
              command = lambda: levelGeneration.stageGeneration(1)
              ).place(relx = 0.1714, rely = 0.425, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "3", bg = levelSelectColours[2],
              fg = "white", relief = "ridge", overrelief = textWobble.get(),
              border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[2], activeforeground = levelSelectColours[2], state = buttonDisabled[2], command = lambda: levelGeneration.stageGeneration(2)).place(relx = 0.2514, rely = 0.3842, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "4", bg = levelSelectColours[3], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[3], activeforeground = levelSelectColours[3], state = buttonDisabled[3], command = lambda: levelGeneration.stageGeneration(3)).place(relx = 0.33, rely = 0.34, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "5", bg = levelSelectColours[4], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[4], activeforeground = levelSelectColours[4], state = buttonDisabled[4], command = lambda: levelGeneration.stageGeneration(4)).place(relx = 0.41, rely = 0.2955, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "6", bg = levelSelectColours[5], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[5], activeforeground = levelSelectColours[5], state = buttonDisabled[5], command = lambda: levelGeneration.stageGeneration(5)).place(relx = 0.496, rely = 0.254, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "7", bg = levelSelectColours[6], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[6], activeforeground = levelSelectColours[6], state = buttonDisabled[6], command = lambda: levelGeneration.stageGeneration(6)).place(relx = 0.581, rely = 0.2955, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "8", bg = levelSelectColours[7], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[7], activeforeground = levelSelectColours[7], state = buttonDisabled[7], command = lambda: levelGeneration.stageGeneration(7)).place(relx = 0.661, rely = 0.34, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "9", bg = levelSelectColours[8], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[8], activeforeground = levelSelectColours[8], state = buttonDisabled[8], command = lambda: levelGeneration.stageGeneration(8)).place(relx = 0.74, rely = 0.3842, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "10", bg = levelSelectColours[9], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[9], activeforeground = levelSelectColours[9], state = buttonDisabled[9], command = lambda: levelGeneration.stageGeneration(9)).place(relx = 0.82, rely = 0.425, relheight = 0.028, relwidth = 0.0128)
        Button(levelSelectionCanvas, text = "B", bg = levelSelectColours[10], fg = "white", relief = "ridge", overrelief = textWobble.get(), border = 0, font = "Arial 15 bold", activebackground = levelSelectColours[10], activeforeground = levelSelectColours[10], state = buttonDisabled[10], command = lambda: levelGeneration.stageGeneration(10)).place(relx = 0.901, rely = 0.4664, relheight = 0.028, relwidth = 0.0128)

        backToMenuButton = Button(levelSelectionCanvas, text = "Back To Menu", bg = greyColour, fg = "white", font = "Arial 23 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = greyColour, activeforeground = greyColour, command = lambda: windowManipulation.closeMediator("BackToMenu"))
        backToMenuButton.place(relx = 0.026, rely = 0.851)
        quitFromLevelButton = Button(levelSelectionCanvas, text = "Quit Game", bg = greyColour, fg = "white", font = "Arial 23 bold", relief = "ridge", overrelief = textWobble.get(), border = 0, activebackground = greyColour, activeforeground = greyColour, command = windowManipulation.quitCheck)
        quitFromLevelButton.place(relx = 0.037, rely = 0.904)

        # Bindings for the buttons on the world 1 selection
        # If the mouse hovers over any of the buttons the text gets turned to yellow
        # When the mouse leaves the text it gets retrurned back to white
        backToMenuButton.bind("<Enter>", lambda menuEnter: backToMenuButton.config(fg = "yellow"))
        backToMenuButton.bind("<Leave>", lambda menuLeave: backToMenuButton.config(fg = "white"))
        quitFromLevelButton.bind("<Enter>", lambda quitLevelEnter: quitFromLevelButton.config(fg = "yellow"))
        quitFromLevelButton.bind("<Leave>", lambda quitLevelLeave: quitFromLevelButton.config(fg = "white"))

    def stageGeneration(whichStageParameter):

        global levelSelectionCanvas, stageCanvas, window, greyColour, movingLeft, characterX, characterY, whichStage, assetCoordsList, dirPathGrassTexture, autoscrollLine, gameActive, scrolling, manualScrollLine

        levelSelectionCanvas.destroy()

        whichStage = whichStageParameter
        scrolling = True
        stageCanvas = Canvas(window, bg = "#95ecfc", width = 2000, highlightthickness = 0, xscrollincrement = scrollSpeed.get())
        stageCanvas.pack(side = "left", expand = True, fill = "both")
        gameActive = True

        Stages.stageOne(stageCanvas, grassCentre, grassEdgeRight, grassEdgeLeft,
                        dirtCentre, dirtEdgeRight, dirtEdgeLeft, stoneCentre, stoneTop, gameBackgroundGrass, sawBlade)

    def stageClear():
        """Changes the ovals on the level seletc to right colour once a level is completed.
           E.G: If level one is completed the first oval will be changed to green;
           and the second oval to red"""

        global whichStage, seconds, minutes

        seconds -= 1
        fileSeconds = seconds + (minutes * 60)

        # Writes the time to the asociated file
        with open(leaderboardIndexArray[whichStage][0], "a") as timeWrite:
            timeWrite.write(str(fileSeconds) + "\n")

        if whichStage == 0 and levelSelectColours[0] != "green":
            levelSelectColours[0] = "green"
            levelSelectColours[1] = "red"
            buttonDisabled[1] = "normal"

        elif whichStage == 1 and levelSelectColours[1] != "green":
            levelSelectColours[1] = "green"
            levelSelectColours[2] = "red"
            buttonDisabled[2] = "normal"

        windowManipulation.completeScreen()


class gameMovement:
    """Class that deals with everything that happens in the actual game"""

    def __init__(self, stageCanvas = None):
        """Initiator method that sets up all the variables needed for the other methods"""

        global pauseOpen, loseOpen, playingGame, dirPathCharacterRight, dirPathCharacterLeft, menuBackground, greyColour, whichStage, gameActive, stopwatchCounting, seconds, minutes, coinCount, headsUpCoinCounter

        playingGame = True
        pauseOpen = False
        loseOpen = False

        stopwatchCounting = True
        seconds = 0
        minutes = 0
        coinCount = 0

        self.stageCanvas = stageCanvas
        self.stageCanvas.config(cursor = "none")

        self.characterX = 0
        self.characterY = 6
        self.xSpeed = 4.5
        self.xDivider = 1
        self.jumpCheck = 0
        self.coinColour = "#ffdd42"
        self.coinColoursList = ["#ffdd42", "#ffce42", "#ffbe42", "#ffae42", "#ff9e42",
                                 "#ff8f42", "#ff7f42", "#ff6f42", "#ff6042", "#ff5042"]
        self.sawBladeList = [sawBlade, sawBlade2, sawBlade3,
                             sawBlade4, sawBlade5, sawBlade6,
                             sawBlade7, sawBlade8]
        self.sawBladePointer = 0

        self.movingUp = False
        self.cannotJump = False
        self.touchingWall = False
        self.particlesCreated = False
        self.flagMoving = True
        self.coinIndex = 0
        self.stopwatchColon = ":"
        self.characterClosestEnemy = ""

        self.characterRight = PhotoImage(file = dirPathCharacterRight)
        self.characterLeft = PhotoImage(file = dirPathCharacterLeft)
        self.characterBound = self.stageCanvas.create_rectangle("40 825 102 920", tags = "character", width = 0)
        self.characterFrame = self.stageCanvas.create_image("70 836", image = self.characterRight, tags = "character")
        self.stageCanvas.focus_set()

        # Binds to keys to the selected keys in Options
        self.stageCanvas.bind("<KeyPress-" + leftControl + ">", self.left)
        self.stageCanvas.bind("<KeyPress-" + rightControl + ">", self.right)
        self.stageCanvas.bind("<KeyPress-" + jumpControl + ">", lambda jumpCheck: self.jump(self) if self.cannotJump == False and self.touchingWall == False else ())
        self.stageCanvas.bind("<KeyRelease-" + leftControl + ">", self.stopLeft)
        self.stageCanvas.bind("<KeyRelease-" + rightControl + ">", self.stopRight)
        self.stageCanvas.bind("<Escape>", lambda pause: windowManipulation.pauseMenu() if pauseOpen == False and loseOpen == False and playingGame == True else (windowManipulation.closeMediator("PauseMenuDestroy")))

        # Gets all of the IDs for every object with these tags to use for colision
        self.eastLineObjects = self.stageCanvas.find_withtag("EastLine")
        self.westLineObjects = self.stageCanvas.find_withtag("WestLine")
        self.northLineObjects = self.stageCanvas.find_withtag("NorthLine")
        self.southLineObjects = self.stageCanvas.find_withtag("SouthLine")
        self.deathLineObjects = self.stageCanvas.find_withtag("DeathLine")
        self.finishLineObjects = self.stageCanvas.find_withtag("FinishLine")
        self.stopScrollObjects = self.stageCanvas.find_withtag("ScrollStopLine")
        self.manualScrollObjects = self.stageCanvas.find_withtag("ManualScrollLine")
        self.coinObjects = self.stageCanvas.find_withtag("Coin")
        self.enemySwapObjects = self.stageCanvas.find_withtag("EnemySwapLine")

        self.movement()
        self.collisionCheckCharacter()
        self.collisionCheckScrollStop()
        self.stageCanvas.after(800, levelGeneration.canvasAutoscroll)

        windowManipulation.headsUpDisplay()
        headsUpCoinCounter.insert(0, 0)

        self.stopwatch()
        self.coinColourChanger()
        self.enemyCollision()
        self.enemyMovement()
        self.enemyAnimation()

    def stopwatch(self):
        global gameActive, seconds, minutes, headsUpCanvas

        if gameActive:
            headsUpCanvas.delete("stopwatch")
            if self.stopwatchColon == " ":
                self.stopwatchColon = ":"
            else:
                self.stopwatchColon = " "
            if seconds < 10:
                headsUpCanvas.create_text("1750 100", text = "0" + (str(minutes) + self.stopwatchColon + "0" + str(seconds)), fill = "dark blue", font = "Arial 50 bold", tags = 'stopwatch')
            else:
                headsUpCanvas.create_text("1750 100", text = "0" + (str(minutes) + self.stopwatchColon + str(seconds)), fill = "dark blue", font = "Arial 50 bold", tags = 'stopwatch')

            seconds += 1
            if seconds == 59:
                seconds = 0
                minutes += 1
            if minutes == 59:
                minutes = 0
                seconds = 0

        self.stageCanvas.after(1000, self.stopwatch)

    def movement(self):
        global gameActive

        if gameActive:
            self.stageCanvas.move(self.characterFrame, self.characterX/self.xDivider, self.characterY)
            self.stageCanvas.move(self.characterBound, self.characterX/self.xDivider, self.characterY)
            if self.cannotJump == False:
                self.characterY = 6
                self.xDivider = 1
            else:
                self.xDivider = 1.4
        self.stageCanvas.after(16, self.movement)

    def enemyMovement(self):
        global gameActive

        if gameActive:
            self.stageCanvas.move(self.characterClosestEnemy, enemySpeed.get(), 0)

        self.stageCanvas.after(16, self.enemyMovement)

    def enemyAnimation(self):
        global gameActive

        if gameActive:
            self.stageCanvas.itemconfig("Enemy", image = self.sawBladeList[self.sawBladePointer])

            if self.sawBladePointer > 0:
                self.sawBladePointer += 1
            else:
                self.sawBladePointer -= 1
            if self.sawBladePointer == 8:
                self.sawBladePointer = -1
            elif self.sawBladePointer == -9:
                self.sawBladePointer = 0

        self.stageCanvas.after(80, self.enemyAnimation)


    def coinColourChanger(self):
        global gameActive

        if gameActive and gameAnimations.get():
            for i in range(len(self.coinColoursList)):
                try:
                    if self.coinColour == self.coinColoursList[i]:
                        self.coinColour = self.coinColoursList[i + 1]
                        break
                except IndexError:
                    self.coinColour = self.coinColoursList[0]

        self.stageCanvas.itemconfig("Coin", fill = self.coinColour)
        self.stageCanvas.after(coinChangeSpeed.get(), self.coinColourChanger)

    def collisionCheckCharacter(self):
        global gameActive, stopwatchCounting, coinCount, headsUpCoinCounter, manualScrollLine, levelQuit, gameStats

        if gameActive:
            self.characterCoordCheck = self.stageCanvas.coords(self.characterBound)
            self.objectsOverlapping = self.stageCanvas.find_overlapping(*self.characterCoordCheck)
            if len(self.objectsOverlapping) > 1:
                for i in self.objectsOverlapping:
                    if i in self.westLineObjects:
                        self.touchingWall = True
                        self.characterX = 0
                        self.stageCanvas.move(self.characterFrame, -3, 0)
                        self.stageCanvas.move(self.characterBound, -3, 0)
                    elif i in self.eastLineObjects:
                        self.touchingWall = True
                        self.characterX = 0
                        self.stageCanvas.move(self.characterFrame, 3, 0)
                        self.stageCanvas.move(self.characterBound, 3, 0)
                    else:
                        self.touchingWall = False
                    if i in self.northLineObjects and self.movingUp == False:
                        self.cannotJump = False
                        self.characterY = 0
                    if i in self.southLineObjects:
                        self.characterY = 4.5
                    if i in self.deathLineObjects or i == self.characterClosestEnemy:
                        gameActive = False
                        stopwatchCounting = False
                        self.stageCanvas.delete(self.characterFrame)
                        self.stageCanvas.delete(self.characterBound)
                        windowManipulation.loseScreen()
                    if i in self.finishLineObjects:
                        gameActive = False
                        stopwatchCounting = False
                        self.stageCanvas.delete(self.characterFrame)
                        self.stageCanvas.delete(self.characterBound)
                        self.characterCentre = self.characterCoordCheck[3] - self.characterCoordCheck[2]
                        levelQuit = False
                        self.flagDrop()
                        levelGeneration.stageClear()
                    if i in self.coinObjects:
                        self.coinID = self.stageCanvas.find_overlapping(*self.characterCoordCheck)
                        self.stageCanvas.delete(self.coinID[self.coinIndex])
                        coinCount += 1
                        gameStats["TotalCoins"] += 1
                        headsUpCoinCounter.delete(0, END)
                        headsUpCoinCounter.insert(0, coinCount)
##                      self.stageCanvas.delete("Particle")
##                      self.particleGenerator()
                    if i in self.manualScrollObjects:
                        self.coinIndex = 1
                        self.stageCanvas.xview_scroll(4, "units")
                        self.stageCanvas.move(manualScrollLine, 3, 0)

        self.stageCanvas.after(gameUpdateSpeed.get(), self.collisionCheckCharacter)

    def collisionCheckScrollStop(self):
        global gameActive, autoscrollLine, scrolling

        if gameActive:
            self.deathLineCoords = self.stageCanvas.coords(autoscrollLine)
            self.deathLineOverlapping = self.stageCanvas.find_overlapping(*self.deathLineCoords)
            for i in self.deathLineOverlapping:
                if i in self.stopScrollObjects:
                    scrolling = False

        self.stageCanvas.after(gameUpdateSpeed.get(), self.collisionCheckScrollStop)

    def particleGenerator(self):

        if self.particlesCreated:
            self.stageCanvas.delete("Particle")
            self.particlesCreated = False
            pass
        else:
            self.particleCoords = self.stageCanvas.coords(self.characterBound)
            self.stageCanvas.create_rectangle(self.particleCoords[0]-0, self.particleCoords[1]+10, self.particleCoords[2]-50, self.particleCoords[3]-60, fill = self.coinColour, outline = self.coinColour, tags = "Particle")
            self.stageCanvas.create_rectangle(self.particleCoords[0]+50, self.particleCoords[1]-30, self.particleCoords[2]+100, self.particleCoords[3]+20, fill = self.coinColour, outline = self.coinColour, tags = "Particle")

            self.particlesCreated = True

            self.stageCanvas.after(250, self.particleGenerator)

    def enemyCollision(self):
        global gameActive, enemySpeed

        if gameActive:
            self.characterClosestEnemy = self.stageCanvas.find_withtag("Enemy")[0]
            self.enemyCoords = self.stageCanvas.bbox(self.characterClosestEnemy)
            self.enemyOverlapping = self.stageCanvas.find_overlapping(*self.enemyCoords)
            for i in self.enemyOverlapping:
                if i in self.enemySwapObjects:
                    if enemySpeed.get() < 0:
                        enemySpeed.set(abs(enemySpeed.get()))
                    else:
                        enemySpeed.set(-enemySpeed.get())

        self.stageCanvas.after(16, self.enemyCollision)

    def flagDrop(self):
        global levelQuit

        if not levelQuit:
            if self.flagMoving:
                self.stageCanvas.move("Flag", 0, 0.2)

            self.flagCoords = self.stageCanvas.coords("Flag")
            self.flagCentre = self.flagCoords[3] - self.flagCoords[2]

            if abs(self.flagCentre - self.characterCentre) <= 1:
                self.flagMoving = False

            self.stageCanvas.after(1, self.flagDrop)

    def jump(self, event):
        global gameStats

        if not self.movingUp:
            self.movingUp = True
        if self.jumpCheck < 1:
            self.cannotJump = True
            self.characterY = -5
            self.jumpCheck = 1
            self.stageCanvas.after(450, lambda: self.jump(event))
        else:
            if self.jumpCheck > 0:
                self.jumpCheck = 0
                gameStats["TotalJumps"] += 1
                self.movingUp = False
                self.characterY = 6

    def left(self, event):
        global gameActive

        if gameActive:
            self.characterCoords = self.stageCanvas.coords(self.characterFrame)
            self.stageCanvas.delete(self.characterFrame)
            self.characterFrame = self.stageCanvas.create_image(self.characterCoords, image = self.characterLeft)
            self.characterX = -9

    def right(self, event):
        global gameActive, scrolling

        if gameActive:
            self.characterCoords = self.stageCanvas.coords(self.characterFrame)
            self.stageCanvas.delete(self.characterFrame)
            self.characterFrame = self.stageCanvas.create_image(self.characterCoords, image = self.characterRight)
            if scrolling:
                self.characterX = 10
            else:
                self.characterX = 5

    def stopLeft(self, event):
        self.characterX = 0

    def stopRight(self, event):
        self.characterX = 0

if __name__ == "__main__":
    windowManipulation.mainMenu()