import dearpygui.dearpygui as dpg
import random
import time as t

class Player:
    def __init__(self):
       self.player_hp = 100
       self.player_name = ""
       self.hp_potions = 3

    def set_player_name(self, name):
       self.player_name = name
    
    def get_player_name(self):
        return self.player_name
    
    def lose_hp(self, hp):
        self.player_hp -= hp
    
    def attack(self, enemy):
        is_crit = random.randint(1,100)
        damage = random.randint(10, 50)
        if is_crit < 25:
            game.input_to_output("\nCRIT DAMAGE!")
            game.input_to_output(f"You deal {damage*2} to {enemy.name}")
            enemy.lose_hp(damage*2)
        else:
            game.input_to_output(f"You deal {damage} to {enemy.name}")
            enemy.lose_hp(damage)

class Spider:
    def __init__(self, name):
        self.spider_hp = 50
        self.name = name
    
    def lose_hp(self, hp):
        self.spider_hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(1, 10)
        if self.spider_hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"Spider deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"Spider deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")


class Game:
    def __init__(self):
        self.primary_window_height = 600
        self.primary_window_width = 1000
        self.output_window_height = 510
        self.output_window_width = 965
        self.console_text = ""
        self.user_input = ""
        self.input_received = False
        self.num_of_floors = random.randint(3, 15)
        self.easy_floors = self.num_of_floors//3
        self.med_floors = self.num_of_floors//3
        self.hard_floors = self.num_of_floors//3
        self.easy_floors += (self.num_of_floors%3)

    def input_to_output(self, app_data):
        if app_data.strip():  # Only process if there is actual input
            self.console_text += app_data + "\n"  # Append input to console_text
            self.user_input = app_data  # Store the user input
            # Update the output box with the new console_text
            dpg.set_value("output_box", self.console_text)
            # Clear the input field
            dpg.set_value("input_box", "")
            # Set the flag to True indicating input is received
            self.input_received = True

    def wait_for_input(self):
        self.input_received = False
        while not self.input_received and dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
    
    def battle_menu(self, player, enemy):
        self.input_to_output("\nWhat will you do?")
        self.input_to_output("1. Attack")
        self.input_to_output("2. Use HP Potion")
        self.input_to_output("3. Check how much HP you have\n")
        self.wait_for_input()
        if self.user_input == "1":
            player.attack(enemy)
            enemy.attack(player)
        elif self.user_input == "2":
            if player.hp_potions > 0:
                player.hp_potions -= 1
                player.player_hp += 50
                self.input_to_output("\nYou used a HP potion and gained 50 HP!")
                self.input_to_output(f"You have {player.hp_potions} HP potions left")
                self.input_to_output(f"You now have {player.player_hp} HP\n")
            else:
                self.input_to_output("\nYou don't have any HP potions left!\n")
        elif self.user_input == "3":
            self.input_to_output(f"\nYou have {player.player_hp} HP left\n")

    def main_game(self, player):
        self.input_to_output("You are standing in front of a cave. You can see the dragon's lair inside the cave.")
        self.input_to_output("What would you like to do? (enter the cave/leave)")
        self.wait_for_input()
        if self.user_input.lower() == "enter the cave":
            self.input_to_output("You have entered the cave!")
        else:
            self.input_to_output("You consider leaving but decide what's the point in standing in front of a cave if you're not going to enter it, so you enter it anyway.")
        self.input_to_output(f"The cave has {self.num_of_floors} floors to beat before you reach the final boss")
        self.input_to_output("Are you ready? (Enter anything to continue)\n")
        self.wait_for_input()
        round = 1
        for i in range(self.easy_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_spider = random.randint(1, 5)
            self.input_to_output(f"You see {num_of_spider} spiders ahead!\n")
            spiders = {}
            for j in range(num_of_spider):
                spider_name = "Spider " + str(j + 1)
                spider = Spider(spider_name)
                spiders[spider_name] = spider
            for spider in spiders:
                self.input_to_output(f"{spider} appears!")
                while player.player_hp > 0 and spiders[spider].spider_hp > 0:
                    self.battle_menu(player, spiders[spider])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        return
            round += 1
        for i in range(self.med_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_spider = random.randint(1, 5)
            round += 1
        
    def init_game(self, player):
        self.input_to_output("WELCOME TO THE GAME")
        self.input_to_output("You are a brave adventurer who has been tasked with saving the kingdom from the evil dragon")
        self.input_to_output("Please enter your character name: ")
        self.wait_for_input()  # Wait for user input
        player_name = self.user_input  # Get the entered name
        player.set_player_name(player_name)
        self.input_to_output(f"Welcome to the game {player.get_player_name()}!")
        self.input_to_output("\nYou are about to embark on a dangerous journey to defeat the dragon and save the kingdom.")
        self.input_to_output("You have 100 HP (Health Points) to start with. If your HP drops to 0, you will be defeated and the game ends.")
        self.input_to_output("Are you ready to begin? (yes/no)")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.input_to_output("Great! Let's get started.")
        else:
            self.input_to_output("That's too bad.")
        self.main_game(player)

    def setup_gui(self):
        dpg.create_context()
        dpg.create_viewport(title='The adventure Game: DND', width=self.primary_window_width, height=self.primary_window_height, resizable=False)

        # Main Window
        with dpg.window(label="Main Window", tag="primary_window"):
            # Input box
            dpg.add_input_text(width=self.primary_window_width-37, pos=(10, self.primary_window_height-70),
                               callback=lambda s, a, u: self.input_to_output(a), on_enter=True, tag="input_box")

        # Output Box
        with dpg.window(label="Output", show=True, width=self.output_window_width, height=self.output_window_height,
                        no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True, pos=(10, 10)):
            dpg.add_input_text(default_value=self.console_text, readonly=True,  # Make it non-editable
                               tag="output_box", multiline=True, width=self.output_window_width-20,
                               height=self.output_window_height-20, pos=(10, 10), callback=None, tracked=True,
                               track_offset=1.0)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("primary_window", True)

    def start(self, player):
        self.setup_gui()
        self.init_game(player)
        dpg.start_dearpygui()
        dpg.destroy_context()

# Run the game
player = Player()
game = Game()
game.start(player)