import dearpygui.dearpygui as dpg
import random
import time as t

# Intended to be unique every time you play it

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
        self.hp_potions = 2
        self.attack_power = 0
        self.gold = 0

    def attack(self, enemy):
        is_crit = random.randint(1,100)
        base_damage = random.randint(10, 50)
        total_damage = base_damage + self.attack_power
        if is_crit < 25:
            game.input_to_output("\nCRIT DAMAGE!!")
            game.input_to_output(f"You deal {total_damage*2} to {enemy.name}")
            enemy.lose_hp(total_damage*2)
        else:
            game.input_to_output(f"\nYou deal {total_damage} to {enemy.name}")
            enemy.lose_hp(total_damage)

# Spider Class

class Spider:
    def __init__(self, name):
        self.hp = 50
        self.name = name
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(1, 10)
        if self.hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"{self.name} deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\n{self.name} deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Slime Class

class Slime:
    def __init__(self, name):
        self.hp = 50
        self.name = name
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(1, 10)
        if self.hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"{self.name} deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\n{self.name} deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Skeleton Class

class Skeleton:
    def __init__(self, name):
        self.hp = 100
        self.name = name
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(10, 20)
        if self.hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"{self.name} deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\n{self.name} deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Orc Class

class Orc:
    def __init__(self, name):
        self.hp = 150
        self.name = name
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(20, 30)
        if self.hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"{self.name} deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\n{self.name} deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Imp Class

class Imp:
    def __init__(self, name):
        self.hp = 200
        self.name = name
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def attack(self, player):
        is_crit = random.randint(1,200)
        damage = random.randint(30, 40)
        if self.hp >= 0:
            if is_crit < 25:
                game.input_to_output("\nCRIT DAMAGE!")
                game.input_to_output(f"{self.name} deals {damage*2} to {player.get_player_name()}")
                player.lose_hp(damage*2)
            else:
                game.input_to_output(f"\n{self.name} deals {damage} to {player.get_player_name()}")
                player.lose_hp(damage)
        else:
            game.input_to_output(f"{self.name} has been defeated!")

# Game Class

class Game:
# Random Enemy Names Class Attribute
    ENEMY_NAMES = [
    "Abaddon", "Azazel", "Balrog", "Belphegor", "Beleth", "Cerberon", "Daemonis", "Diavolos", "Erebus", "Hecatross",
    "Infernum", "Malphas", "Zarathus", "Apollyon", "Asmodeus", "Barbatos", "Bathin", "Bilegor", "Caligoth", "Choronzon",
    "Dagonis", "Eligos", "Furcas", "Galthor", "Hadeson", "Iblith", "Jezalthar", "Karnathos", "Lilithon", "Lucianor",
    "Malthael", "Morgrith", "Nergash", "Nyxathos", "Ozarath", "Pazuthar", "Qalzor", "Rahvok", "Rimmonis", "Samael",
    "Scylthos", "Seraxis", "Shalgaroth", "Tanaros", "Thalgrin", "Torvaloth", "Umbraxis", "Valtharion", "Velgorth", "Xaziron",
    "Zarvok", "Zerathis", "Blightborn", "Dreadveil", "Hellforge", "Soulflayer", "Bloodpyre", "Shadowbane", "Doomcaller", "Infernal",
    "Painbringer", "Darkthorn", "Flamewretch", "Ashveil", "Doomrend", "Shadowspire", "Hellshade", "Gravetalon", "Soulburn", "Wretchfiend",
    "Chaosfang", "Maliceborn", "Deathwhisper", "Fiendgrin", "Voidspike", "Hellmaw", "Boneclaw", "Blightfang", "Netherthorn", "Infernalor",
    "Bloodveil", "Soulmire", "Dreadspire", "Nightshade", "Darkspire", "Venomborn", "Voidmaw", "Pyrefiend", "Netherlord", "Blazewrath",
    "Plaguespire", "Hellwrath", "Foulthorn", "Dreadmaw", "Deathforge", "Rotbane", "Voidrend", "Cinderfang", "Flamescourge", "Maligore"
]
    
# Initialize Game Class Attributes

    def __init__(self):
        self.primary_window_height = 630
        self.primary_window_width = 1000
        self.output_window_height = 510
        self.output_window_width = 965
        self.console_text = ""
        self.user_input = ""
        self.input_received = False
        self.total_num_enemies = 0 ##### TODO: Add more stats to end game
        self.num_of_floors = random.randint(3, 15)
        # Adds a change of difficulty to the game (more interesting)
        self.easy_floors = self.num_of_floors//3 # Num of easy floors
        self.med_floors = self.num_of_floors//3 # Num of medium floors
        self.hard_floors = self.num_of_floors//3 # Num of hard floors
        self.easy_floors += (self.num_of_floors%3) # Add the remainder to the easy floors



# Player Drops

    def drops(self, player):
        hp_potion_chance = random.randint(1, 100)
        better_weapon_chance = random.randint(1, 100)
        gold_chance = random.randint(1, 100)
        gold_amount = random.randint(10, 200)
        if gold_chance < 30:
            player.gold += gold_amount
            game.input_to_output(f"\nYou found {gold_amount} gold!\n")
        if hp_potion_chance < 15:
            player.hp_potions += 1
            game.input_to_output("\nYou found a HP potion!\n")
        if better_weapon_chance < 15:
            player.attack_power += 5
            game.input_to_output("\nYou found a better weapon!")
            game.input_to_output("Your attack power has increased\n")
        if hp_potion_chance >= 15 and better_weapon_chance >= 15 and gold_chance >= 30:
            game.input_to_output("\nYou found nothing useful\n")
        self.update_labels(player.player_hp, player.gold, player.hp_potions, player.attack_power)

# Input and Output

    def input_to_output(self, app_data):
        if app_data.strip():  # Only process if there is actual input
            self.console_text += app_data + "\n"  # Append input to console_text
            self.user_input = app_data  # Store the user input
            # Update the output box with the new console_text
            dpg.set_value("output_box", self.console_text)
            # Clear the input field
            dpg.set_value("input_box", "")
            dpg.focus_item("input_box")
            # Set the flag to True indicating input is received
            self.input_received = True

    def wait_for_input(self):
        self.input_received = False
        dpg.set_y_scroll("output_window", dpg.get_y_scroll_max("output_window")+1000000000)
        while not self.input_received and dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()

# Game Over

    def game_over(self):
        self.input_to_output("Game Over!")
        self.input_to_output("\nStats:\n")
        self.input_to_output(f"Name: {player.get_player_name()}")
        self.input_to_output(f"Gold: {player.gold}")
        self.input_to_output(f"HP Potions: {player.hp_potions}")
        self.input_to_output(f"Weapon attack gains: {player.attack_power}")
        self.input_to_output("Would you like to play again? (yes/no)\n")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.init_game(player)
        else:
            self.input_to_output("Thanks for playing!")
            dpg.stop_dearpygui()

# Game Win

    def game_win(self):
        self.input_to_output("Congratulations!")
        self.input_to_output("You have defeated the dragon and saved the kingdom!\n")
        self.input_to_output("\nStats:\n")
        self.input_to_output(f"Name: {player.get_player_name()}")
        self.input_to_output(f"Gold: {player.gold}")
        self.input_to_output(f"HP Potions: {player.hp_potions}")
        self.input_to_output(f"Weapon attack gains: {player.attack_power}")
        self.input_to_output("Would you like to play again? (yes/no)\n")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.init_game(player)
        else:
            self.input_to_output("Thanks for playing!")
            dpg.stop_dearpygui()
        

# Battle Menu

    def battle_menu(self, player, enemy):
        self.input_to_output("\nWhat will you do?")
        self.input_to_output("1. Attack")
        self.input_to_output(f"2. Use HP Potion (You currently have {player.player_hp} hp)")
        self.input_to_output("3. Shop\n")
        self.wait_for_input()
        if self.user_input == "1":
            player.attack(enemy)
            enemy.attack(player)
        elif self.user_input == "2":
            if player.hp_potions > 0:
                player.hp_potions -= 1
                player.player_hp += 50
                self.input_to_output("\nYou used a HP potion and gained 50 HP!\n")
                enemy.attack(player)
            else:
                self.input_to_output("\nYou don't have any HP potions left!\n")
        elif self.user_input == "3":
            self.input_to_output("\nYou have entered the shop!")
            self.input_to_output("What would you like to buy?")
            self.input_to_output("1. HP Potion (50 gold)")
            self.input_to_output("2. Better Weapon (100 gold)")
            self.input_to_output("3. Leave\n")
            self.wait_for_input()
            if self.user_input == "1":
                if player.gold >= 50:
                    player.gold -= 50
                    player.hp_potions += 1
                    self.input_to_output("\nYou bought a HP potion!\n")
                else:
                    self.input_to_output("\nYou don't have enough gold!\n")
            elif self.user_input == "2":
                if player.gold >= 100:
                    player.gold -= 100
                    player.attack_power += 5
                    self.input_to_output("\nYou bought a better weapon!")
                    self.input_to_output("Your attack power has increased\n")
                else:
                    self.input_to_output("\nYou don't have enough gold!\n")
            elif self.user_input == "3":
                self.input_to_output("\nYou have left the shop\n")
        self.update_labels(player.player_hp, player.gold, player.hp_potions, player.attack_power)
        

# Main Game

    def main_game(self, player):
        self.input_to_output("You are standing in front of a cave. You can see the dragon's lair inside the cave.")
        self.input_to_output("What would you like to do? (enter the cave/leave)\n")
        self.wait_for_input()
        if self.user_input.lower() == "enter the cave" or self.user_input.lower() == "enter cave" or self.user_input.lower() == "enter":
            self.input_to_output("\nYou have entered the cave!\n")
        else:
            self.input_to_output("\nYou consider leaving but decide what's the point in standing in front of a cave if you're not going to enter it, so you enter it anyway.\n")
        self.input_to_output(f"The cave has {self.num_of_floors} floors to beat before you reach the final boss")
        self.input_to_output("Are you ready? (Enter anything to continue)\n")
        self.wait_for_input()
        round = 1
        for i in range(self.easy_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_spider = random.randint(1, 2)
            num_of_slime = random.randint(1, 4)
            self.input_to_output(f"You see {num_of_spider} spiders and {num_of_slime} slimes ahead!\n")
            enemies = []
            for j in range(num_of_spider):
                spider_name = random.choice(self.enemy_names) + " the spider"
                self.enemy_names.remove(spider_name.split(" the spider")[0]) # Remove the name from the list so it doesn't repeat
                spider = Spider(spider_name)
                enemies.append(spider)
            for k in range(num_of_slime):
                slime_name = random.choice(self.enemy_names) + " the slime"
                self.enemy_names.remove(slime_name.split(" the slime")[0])
                slime = Slime(slime_name)
                enemies.append(slime) 
            random.shuffle(enemies)
            for enemy in enemies:
                self.input_to_output(f"\n{enemy.name} appears!")
                while player.player_hp > 0 and enemy.hp > 0:
                    self.battle_menu(player, enemy)
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            round += 1
        for i in range(self.med_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_spider = random.randint(1, 3)
            num_of_skeleton = random.randint(2, 5)
            self.input_to_output(f"You see {num_of_spider} spiders and {num_of_skeleton} skeletons ahead!\n")
            enemies = []
            for j in range(num_of_spider):
                spider_name = random.choice(self.enemy_names) + " the spider"
                self.enemy_names.remove(spider_name.split(" the spider")[0])
                spider = Spider(spider_name)
                enemies.append(spider) 
            for k in range(num_of_skeleton):
                skeleton_name = random.choice(self.enemy_names) + " the skeleton"
                self.enemy_names.remove(skeleton_name.split(" the skeleton")[0])
                skeleton = Skeleton(skeleton_name)
                enemies.append(skeleton) 
            random.shuffle(enemies)
            for enemy in enemies:
                self.input_to_output(f"\n{enemy.name} appears!")
                while player.player_hp > 0 and enemy.hp > 0:
                    self.battle_menu(player, enemy)
                    if player.player_hp <= 0:
                        self.input_to_output("You have been defeated!")
                        self.game_over()
                self.drops(player)
            round += 1
        for i in range(self.hard_floors):
            self.input_to_output(f"\nFloor {round}\n")
            num_of_skeleton = random.randint(1, 2)
            num_of_orc = random.randint(2, 4)
            num_of_imp = random.randint(2, 4)
            self.input_to_output(f"You see {num_of_skeleton} skeletons, {num_of_orc} orcs and {num_of_imp} imps ahead!\n")
            enemies = []
            for j in range(num_of_skeleton):
                skeleton_name = random.choice(self.enemy_names) + " the skeleton"
                self.enemy_names.remove(skeleton_name.split(" the skeleton")[0])
                skeleton = Skeleton(skeleton_name)
                enemies.append(skeleton) 
            for k in range(num_of_orc):
                orc_name = random.choice(self.enemy_names) + " the orc"
                self.enemy_names.remove(orc_name.split(" the orc")[0])
                orc = Orc(orc_name)
                enemies.append(orc) 
            for l in range(num_of_imp):
                imp_name = random.choice(self.enemy_names) + " the imp"
                self.enemy_names.remove(imp_name.split(" the imp")[0])
                imp = Imp(imp_name)
                enemies.append(imp) 
            random.shuffle(enemies)
            for enemy in enemies:
                self.input_to_output(f"\n{enemy.name} appears!")
                while player.player_hp > 0 and enemy.hp > 0:
                    self.battle_menu(player, enemy)
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
        self.enemy_names = self.ENEMY_NAMES.copy()
        self.input_to_output("WELCOME TO THE GAME")
        self.input_to_output("You are a brave adventurer who has been tasked with saving the kingdom from the evil dragon\n")
        self.input_to_output("Please enter your character name: ")
        self.wait_for_input()  # Wait for user input
        player_name = self.user_input  # Get the entered name
        player.set_player_name(player_name)
        player.reset_stats()
        self.update_player_name_label(player.get_player_name())
        self.update_labels(player.player_hp, player.gold, player.hp_potions, player.attack_power)
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

# Update GUI labels

    def update_player_name_label(self, player_name):
        dpg.set_value("player_name_label", f"Name: {player_name}")

    def update_labels(self, player_hp, gold, hp_potions, weapon_attack):
        dpg.set_value("player_hp_label", f"HP: {player_hp}")
        dpg.set_value("gold_label", f"Gold: {gold}")
        dpg.set_value("hp_potions_label", f"HP Potions: {hp_potions}")
        dpg.set_value("weapon_attack_label", f"Additional Damage: {weapon_attack}")

# GUI

    def setup_gui(self):
        dpg.create_context()
        dpg.create_viewport(title='The adventure Game: DND', width=self.primary_window_width, height=self.primary_window_height, resizable=False)

        # Main Window
        with dpg.window(label="Main Window", tag="primary_window"):
            # Player Stats
            dpg.add_text(default_value="Name: ", tag="player_name_label", pos=(10, self.primary_window_height-100))
            dpg.add_text(default_value="HP: 0", tag="player_hp_label", pos=(100, self.primary_window_height-100))
            dpg.add_text(default_value="Gold: 0", tag="gold_label", pos=(200, self.primary_window_height-100))
            dpg.add_text(default_value="HP Potions: 0", tag="hp_potions_label", pos=(380, self.primary_window_height-100))
            dpg.add_text(default_value="Additional Damage: 0", tag="weapon_attack_label", pos=(590, self.primary_window_height-100))
            # Input box
            dpg.add_input_text(width=self.primary_window_width-37, pos=(10, self.primary_window_height-70),
                               callback=lambda s, a, u: self.input_to_output(a), on_enter=True, tag="input_box")

        # Output Box
        with dpg.window(label="Output",tag="output_window" ,show=True, width=self.output_window_width, height=self.output_window_height,
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

# Start Game

    def start(self, player):
        self.setup_gui()
        self.init_game(player)
        dpg.start_dearpygui()
        dpg.destroy_context()

# Run the game
player = Player()
game = Game()
game.start(player)