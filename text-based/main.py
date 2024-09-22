import os
from termcolor import colored,cprint
import sys
import time
from pyfiglet import Figlet

os.system("clear")
def text_animation(self,text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    print()


class Charackter_selection():
    def __init__(self):
        self.char_mapping = {
            "1": "[1] Human",
            "2": "in progress",
            "3": "in progress"
        }
        

    def human_select(self):
        pass
    def update(self):
        os.system("clear")
        text_animation(self,"What will you be?")

        for char in self.char_mapping:
            if char == "2" or char == "3":
                print(colored(self.char_mapping[char],"grey"))
            else:
                print(colored(self.char_mapping[char],"green"))

        while True:
            self.player_choice = input("< ")
            if self.player_choice == "q":
                os.system("clear")
                menu.update()
            elif self.player_choice == "1":
                os.system("clear")
                colored_text = colored("Human","green")
                text_animation(self,f"You selected '{colored_text}'")


charackter_selection = Charackter_selection()
class Menu():
    def __init__(self):
        pass

    def page_about(self):
        os.system("clear")
        print("# About ")
        print("")
        print("This is a Text Based RPG game called PyLegend.")
        print("Have fun exploring!")
        print("")
        print(colored("press 'q' to get back","yellow"))
        print("")

    def update(self):

        f = Figlet(font='standard')
        print(f.renderText('PyLegend'))

        self.char_mapping = {
            "0":"+------------------------------+",
            "n":"         --PyLegend--",
            "l":"+------------------------------+",
            "1": "[1] Start",
            "2": "[2] About",
            "3": "[3] Exit",
            "4":"+------------------------------+"

        }       

        for char in self.char_mapping:
            print(self.char_mapping[char])
        
        self.run = True       
        while self.run:
            self.player_input = input("< ")
        
            if self.player_input == "1":
                self.run = False
                charackter_selection.update()

            if self.player_input == "2":
                menu.page_about()

            if self.player_input == "q":
                os.system("clear")
                menu.update()
            if self.player_input == "3":
                print(colored("Tschüss,Bye","red"))
                sys.exit(0)

class Player():
    def __init__(self):
        pass
    def update(self):
        pass

class Scenes():
    def __init__(self):
        pass
    def update(self):
        pass

if __name__ == "__main__":
    menu = Menu()
    menu.update()


