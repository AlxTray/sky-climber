# Location for all the arrays that contain the assets for Sky Climber
import os
from tkinter import *

class levelSelection:


    def world1AssetsArray(menuBackground, greyColour):

        world1Assests = [["BackImage", "0 0", menuBackground, "nw"],
                     ["HeaderText", "975 100", "Level Select", greyColour, "Arial 110 bold"],
                     ["QuitLine", "33 907 295 907", greyColour, 10, "round", 255],
                     ["QuitLine", "38 1048 295 1048", greyColour, 10, "round", 255],
                     ["QuitLine", "33 1048 33 888", greyColour, 10, "round", 255],
                     ["QuitLine", "295 911 295 1048", greyColour, 10, "round", 255],
                     ["QuitRect", "295 907 33 1048", greyColour, greyColour],
                     ["MapBoxLine", "90 260 1815 260", greyColour, 10, "round", 255],
                     ["MapBoxLine", "89 563 1815 563", greyColour, 10, "round", 255],
                     ["MapBoxLine", "90 260 90 565", greyColour, 10, "round", 255],
                     ["MapBoxLine", "1815 260 1815 565", greyColour, 10, "round", 255],
                     ["MapRect", "1815 260 90 563", greyColour, greyColour],
                     ["MapLine", "962 285 134 535", "light blue", 10, 200, "round", "gray50"],
                     ["MapLine", "1787 537 961 283", "light blue", 10, 200, "round", "gray50"],
                     ["Oval", "166 497 206 537", "red", 2, "yellow"],
                     ["Oval", "321 454 361 494", "black", 2, "yellow"],
                     ["Oval", "474 409 514 449", "black", 2, "yellow"],
                     ["Oval", "627 361 667 401", "black", 2, "yellow"],
                     ["Oval", "780 313 820 353", "black", 2, "yellow"],
                     ["Oval", "944 269 984 309", "black", 2, "yellow"],
                     ["Oval", "1108 313 1148 353", "black", 2, "yellow"],
                     ["Oval", "1261 361 1301 401", "black", 2, "yellow"],
                     ["Oval", "1413 409 1453 449", "black", 2, "yellow"],
                     ["Oval", "1566 454 1606 494", "black", 2, "yellow"],
                     ["Oval", "1722 499 1762 539", "black", 5, "yellow"]]

        return world1Assests

class Stages:

    def stageOne(stageCanvas, grassCentre, grassEdgeRight, grassEdgeLeft, dirtCentre, dirtEdgeRight, dirtEdgeLeft, stoneCentre, stoneTop, gameBackgroundGrass):

        stageCanvas.create_image("0 20", image = gameBackgroundGrass, anchor = "n", tag = "UpperBackground")
        stageCanvas.create_image("1920 20", image = gameBackgroundGrass, anchor = "n", tag = "UpperBackground")
        stageCanvas.create_image("3840 20", image = gameBackgroundGrass, anchor = "n", tag = "UpperBackground")
        stageCanvas.create_image("5760 20", image = gameBackgroundGrass, anchor = "n", tag = "UpperBackground")
        stageCanvas.create_rectangle("0 1080 20000 1080", width = 0, tags = "DeathLine")
        stageCanvas.create_rectangle("10 10 10 1080", width = 0, tags = "EastLine")

        stageCanvas.create_image("0 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("77 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("154 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("231 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("308 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("385 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("462 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("539 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("616 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("693 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("770 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("847 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("924 925", image = grassEdgeRight, anchor = "nw")
        stageCanvas.create_image("0 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("77 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("154 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("231 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("308 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("385 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("462 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("539 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("616 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("693 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("770 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("847 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("924 1002", image = dirtEdgeRight, anchor = "nw")
        stageCanvas.create_rectangle("0 923 1000 935", width = 0, tag = "NorthLine")
        stageCanvas.create_rectangle("1000 936 1000 1080", width = 0, tag = "EastLine")

        stageCanvas.create_image("1200 925", image = grassEdgeLeft, anchor = "nw")
        stageCanvas.create_image("1277 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1354 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1431 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1508 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1585 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1662 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1739 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1816 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("1893 925", image = grassEdgeRight, anchor = "nw")
        stageCanvas.create_image("1200 1002", image = dirtEdgeLeft, anchor = "nw")
        stageCanvas.create_image("1277 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1354 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1431 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1508 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1585 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1662 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1739 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1816 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("1893 1002", image = dirtEdgeRight, anchor = "nw")
        stageCanvas.create_rectangle("1200 923 1970 935", width = 0, tags = "NorthLine")
        stageCanvas.create_rectangle("1200 936 1200 1080", width = 0, tags = "WestLine")
        stageCanvas.create_rectangle("1970 936 1970 1080", width = 0, tags = "EastLine")
        stageCanvas.create_rectangle("1180 910 1200 940", width = 0, tags = "EnemySwapLine")
        stageCanvas.create_rectangle("1970 910 1990 940", width = 0, tags = "EnemySwapLine")

        stageCanvas.create_image("2150 1002", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2150 924", image = stoneTop, anchor = "nw")
        stageCanvas.create_rectangle("2150 922 2227 934", width = 0, tags = "NorthLine")
        stageCanvas.create_rectangle("2150 935 2150 1080", width = 0, tags = "WestLine")
        stageCanvas.create_rectangle("2227 935 2227 1080", width = 0, tags = "EastLine")

        stageCanvas.create_image("2370 1002", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2370 924", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2370 846", image = stoneTop, anchor = "nw")
        stageCanvas.create_rectangle("2370 844 2447 854", width = 0, tags = "NorthLine")
        stageCanvas.create_rectangle("2370 855 2370 1080", width = 0, tags = "WestLine")
        stageCanvas.create_rectangle("2447 855 2447 1080", width = 0, tags = "EastLine")

        stageCanvas.create_image("2590 1002", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2590 924", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2590 846", image = stoneCentre, anchor = "nw")
        stageCanvas.create_image("2590 768", image = stoneTop, anchor = "nw")
        stageCanvas.create_rectangle("2590 766 2667 776", width = 0, tags = "NorthLine")
        stageCanvas.create_rectangle("2590 777 2590 1080", width = 0, tags = "WestLine")
        stageCanvas.create_rectangle("2667 777 2667 1080", width = 0, tags = "EastLine")

        stageCanvas.create_image("2900 925", image = grassEdgeLeft, anchor = "nw")
        stageCanvas.create_image("2977 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3054 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3131 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3208 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3285 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3362 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3439 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3516 925", image = grassCentre, anchor = "nw")
        stageCanvas.create_image("3593 925", image = grassEdgeRight, anchor = "nw")
        stageCanvas.create_image("2900 1002", image = dirtEdgeLeft, anchor = "nw")
        stageCanvas.create_image("2977 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3054 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3131 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3208 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3285 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3362 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3439 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3516 1002", image = dirtCentre, anchor = "nw")
        stageCanvas.create_image("3593 1002", image = dirtEdgeRight, anchor = "nw")
        stageCanvas.create_rectangle("2900 923 3593 935", width = 0, tags = "NorthLine")
        stageCanvas.create_rectangle("2900 936 2900 1080", width = 0, tags = "WestLine")
        stageCanvas.create_rectangle("3593 936 3593 1080", width = 0, tags = "EastLine")
        stageCanvas.create_rectangle("3500 550 3520 925", width = 0, tags = "FinishLine")
        stageCanvas.create_rectangle("3500 550 3520 925", fill = "white")
        stageCanvas.create_rectangle("3500 550 3350 585", fill = "green", tags = "Flag")
        stageCanvas.create_rectangle("2200 875 2210 2210", width = 0, tags = "ScrollStopLine")

        stageCanvas.create_oval("550 750 590 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("630 750 670 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("710 750 750 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("1505 750 1545 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("1585 750 1625 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("1665 750 1705 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("1080 750 1120 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("2170 749 2210 789", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("2390 671 2430 711", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("2610 593 2650 633", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("3100 750 3140 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")
        stageCanvas.create_oval("3180 750 3220 790", fill = "yellow", outline = "white", width = 3, tags = "Coin")

if __name__ == "__main__":
    print("This is not the Sky Climber game.")