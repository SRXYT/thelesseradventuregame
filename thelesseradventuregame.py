import dearpygui.dearpygui as dpg
import random
import time as t

# Player Class

class Player:
    def __init__(self):
       self.player_hp = 100
       self.player_name = ""
       self.hp_potions = 2
       self.attack_power = 0
       self.gold = 0

    def set_player_name(self, name):
       self.player_name = name
    
    def get_player_name(self):
        return self.player_name
    
    def lose_hp(self, hp):
        self.player_hp -= hp
    
    def reset_stats(self):
        self.player_hp = 100
        self.hp_potions = 3
        self.attack_power = 0
        self.gold = 0

    def attack(self, enemy):
        is_crit = random.randint(1,100)
        base_damage = random.randint(10, 50)
        total_damage = base_damage + self.attack_power
        if is_crit < 25:
            game.input_to_output("\nCRIT DAMAGE!")
            game.input_to_output(f"You deal {total_damage*2} to {enemy.name}")
            enemy.lose_hp(total_damage*2)
        else:
            game.input_to_output(f"You deal {total_damage} to {enemy.name}")
            enemy.lose_hp(total_damage)

# Spider Class

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
                game.input_to_output(f"\nSpider deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Slime Class

class Slime:
    def __init__(self, name):
        self.slime_hp = 50
        self.name = name
    
    def lose_hp(self, hp):
        self.slime_hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(1, 10)
        if self.slime_hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"Slime deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\nSlime deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Skeleton Class

class Skeleton:
    def __init__(self, name):
        self.skeleton_hp = 100
        self.name = name
    
    def lose_hp(self, hp):
        self.skeleton_hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(10, 20)
        if self.skeleton_hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"Skeleton deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\nSkeleton deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Orc Class

class Orc:
    def __init__(self, name):
        self.orc_hp = 150
        self.name = name
    
    def lose_hp(self, hp):
        self.orc_hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(20, 30)
        if self.orc_hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"Orc deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\nOrc deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Imp Class

class Imp:
    def __init__(self, name):
        self.imp_hp = 200
        self.name = name
    
    def lose_hp(self, hp):
        self.imp_hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(30, 40)
        if self.imp_hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"Imp deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\nImp deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Game Class

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

# Player Drops

    def drops(self, player):
        hp_potion_chance = random.randint(1, 100)
        better_weapon_chance = random.randint(1, 100)
        gold_chance = random.randint(1, 100)
        gold_amount = random.randint(10, 100)
        if gold_chance < 30:
            player.gold += gold_amount
            game.input_to_output(f"\nYou found {gold_amount} gold!")
            game.input_to_output(f"You now have {player.gold} gold\n")
        if hp_potion_chance < 15:
            player.hp_potions += 1
            game.input_to_output("\nYou found a HP potion!")
            game.input_to_output(f"You now have {player.hp_potions} HP potions\n")
        if better_weapon_chance < 15:
            player.attack_power += 10
            game.input_to_output("\nYou found a better weapon!")
            game.input_to_output("Your attack power has increased\n")
        if hp_potion_chance >= 25 and better_weapon_chance >= 15 and gold_chance >= 50:
            game.input_to_output("\nYou found nothing useful\n")

# Input and Output

    def input_to_output(self, app_data):
        if app_data.strip():  # Only process if there is actual input
            self.console_text += app_data + "\n"  # Append input to console_text
            self.user_input = app_data  # Store the user input
            # Update the output box with the new console_text
            dpg.set_value("output_box", self.console_text)
            # Scroll to botom of output box

            # Clear the input field
            dpg.set_value("input_box", "")
            dpg.focus_item("input_box")
            # Set the flag to True indicating input is received
            self.input_received = True

    def wait_for_input(self):
        self.input_received = False
        while not self.input_received and dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()

# Game Over

    def game_over(self):
        self.input_to_output("Game Over!")
        self.input_to_output("/nStats:/n")
        self.input_to_output(f"Name: {player.get_player_name()}")
        self.input_to_output(f"Gold: {player.gold}")
        self.input_to_output(f"HP Potions: {player.hp_potions}")
        self.input_to_output(f"Weapon attack gains: {player.attack_power}")
        self.input_to_output("Would you like to play again? (yes/no)")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.init_game(player)
        else:
            self.input_to_output("Thanks for playing!")
            t.sleep(2)
            dpg.stop_dearpygui()
    
    def game_win(self):
        self.input_to_output("Congratulations!")
        self.input_to_output("You have defeated the dragon and saved the kingdom!")
        self.input_to_output("/nStats:/n")
        self.input_to_output(f"Name: {player.get_player_name()}")
        self.input_to_output(f"Gold: {player.gold}")
        self.input_to_output(f"HP Potions: {player.hp_potions}")
        self.input_to_output(f"Weapon attack gains: {player.attack_power}")
        self.input_to_output("Would you like to play again? (yes/no)")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.init_game(player)
        else:
            self.input_to_output("Thanks for playing!")
            t.sleep(2)
            dpg.stop_dearpygui()
        

# Battle Menu

    def battle_menu(self, player, enemy):
        self.input_to_output("\nWhat will you do?")
        self.input_to_output("1. Attack")
        self.input_to_output("2. Use HP Potion")
        self.input_to_output("3. Shop")
        self.input_to_output(f"You have {player.player_hp} HP!\n")
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
                enemy.attack(player)
            else:
                self.input_to_output("\nYou don't have any HP potions left!\n")
        elif self.user_input == "3":
            self.input_to_output("\nYou have entered the shop!")
            self.input_to_output(f"You have {player.gold} gold")
            self.input_to_output("What would you like to buy?")
            self.input_to_output("1. HP Potion (50 gold)")
            self.input_to_output("2. Better Weapon (100 gold)")
            self.input_to_output("3. Leave\n")
            self.wait_for_input()
            if self.user_input == "1":
                if player.gold >= 50:
                    player.gold -= 50
                    player.hp_potions += 1
                    self.input_to_output("\nYou bought a HP potion!")
                    self.input_to_output(f"You now have {player.hp_potions} HP potions")
                    self.input_to_output(f"You now have {player.gold} gold\n")
                else:
                    self.input_to_output("\nYou don't have enough gold!\n")
            elif self.user_input == "2":
                if player.gold >= 100:
                    player.gold -= 100
                    player.attack_power += 10
                    self.input_to_output("\nYou bought a better weapon!")
                    self.input_to_output("Your attack power has increased\n")
                    self.input_to_output(f"You now have {player.gold} gold\n")
                else:
                    self.input_to_output("\nYou don't have enough gold!\n")
            elif self.user_input == "3":
                self.input_to_output("\nYou have left the shop\n")
        

# Main Game

    def main_game(self, player):
        self.input_to_output("You are standing in front of a cave. You can see the dragon's lair inside the cave.")
        self.input_to_output("What would you like to do? (enter the cave/leave)\n")
        self.wait_for_input()
        if self.user_input.lower() == "enter the cave":
            self.input_to_output("\nYou have entered the cave!\n")
        else:
            self.input_to_output("\nYou consider leaving but decide what's the point in standing in front of a cave if you're not going to enter it, so you enter it anyway.\n")
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
                self.input_to_output(f"\n{spider} appears!")
                while player.player_hp > 0 and spiders[spider].spider_hp > 0:
                    self.battle_menu(player, spiders[spider])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            round += 1
        for i in range(self.med_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_spider = random.randint(1, 3)
            num_of_skeleton = random.randint(2, 5)
            self.input_to_output(f"You see {num_of_spider} spiders and {num_of_skeleton} ahead!\n")
            spiders = {}
            skeletons = {}
            for j in range(num_of_spider):
                spider_name = "Spider " + str(j + 1)
                spider = Spider(spider_name)
                spiders[spider_name] = spider
            for k in range(num_of_skeleton):
                skeleton_name = "Skeleton " + str(k + 1)
                skeleton = Skeleton(skeleton_name)
                skeletons[skeleton_name] = skeleton 
            for spider in spiders:
                self.input_to_output(f"\n{spider} appears!")
                while player.player_hp > 0 and spiders[spider].spider_hp > 0:
                    self.battle_menu(player, spiders[spider])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            for skeleton in skeletons:
                self.input_to_output(f"\n{skeleton} appears!")
                while player.player_hp > 0 and skeletons[skeleton].skeleton_hp > 0:
                    self.battle_menu(player, skeletons[skeleton])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            round += 1
        for i in range(self.hard_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_skeleton = random.randint(1, 2)
            num_of_orc = random.randint(2, 3)
            num_of_imp = random.randint(2, 4)
            self.input_to_output(f"You see {num_of_skeleton} skeletons, {num_of_orc} orcs and {num_of_imp} imps ahead!\n")
            skeletons = {}
            orcs = {}
            imps = {}
            for j in range(num_of_skeleton):
                skeleton_name = "Skeleton " + str(j + 1)
                skeleton = Skeleton(skeleton_name)
                skeletons[skeleton_name] = skeleton
            for k in range(num_of_orc):
                orc_name = "Orc " + str(k + 1)
                orc = Orc(orc_name)
                orcs[orc_name] = orc
            for l in range(num_of_imp):
                imp_name = "Imp " + str(l + 1)
                imp = Imp(imp_name)
                imps[imp_name] = imp
            for skeleton in skeletons:
                self.input_to_output(f"\n{skeleton} appears!")
                while player.player_hp > 0 and skeletons[skeleton].skeleton_hp > 0:
                    self.battle_menu(player, skeletons[skeleton])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            for orc in orcs:
                self.input_to_output(f"\n{orc} appears!")
                while player.player_hp > 0 and orcs[orc].orc_hp > 0:
                    self.battle_menu(player, orcs[orc])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            for imp in imps:
                self.input_to_output(f"\n{imp} appears!")
                while player.player_hp > 0 and imps[imp].imp_hp > 0:
                    self.battle_menu(player, imps[imp])
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            round += 1

# Initialize Game

    def init_game(self, player):
        self.console_text = ""
        self.user_input = ""
        self.num_of_floors = random.randint(3, 15)
        self.easy_floors = self.num_of_floors//3
        self.med_floors = self.num_of_floors//3
        self.hard_floors = self.num_of_floors//3
        self.easy_floors += (self.num_of_floors%3)
        self.input_to_output("WELCOME TO THE GAME")
        self.input_to_output("You are a brave adventurer who has been tasked with saving the kingdom from the evil dragon\n")
        self.input_to_output("Please enter your character name: ")
        self.wait_for_input()  # Wait for user input
        player_name = self.user_input  # Get the entered name
        player.set_player_name(player_name)
        player.reset_stats()
        self.input_to_output(f"\nWelcome to the game {player.get_player_name()}!")
        self.input_to_output("\nYou are about to embark on a dangerous journey to defeat the dragon and save the kingdom.")
        self.input_to_output("You have 100 HP (Health Points) to start with. If your HP drops to 0, you will be defeated and the game ends.")
        self.input_to_output("Are you ready to begin? (yes/no)\n")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.input_to_output("\nGreat! Let's get started.")
        else:
            self.input_to_output("\nThat's too bad.")
        self.main_game(player)


# GUI

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
            # dpg.add_input_text(default_value=self.console_text, readonly=True,  # Make it non-editable
            #                    tag="output_box", multiline=True, width=self.output_window_width-20,
            #                    height=self.output_window_height-20, pos=(10, 10), callback=None, tracked=True,
            #                    track_offset=1.0)
            dpg.add_text(default_value=self.console_text,  # Make it non-editable
                tag="output_box", wrap=self.output_window_width-20)

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