import dearpygui.dearpygui as dpg
import random
import time as t
class Game:
    def __init__(self):
        self.primary_window_height = 600
        self.primary_window_width = 1000
        self.output_window_height = 510
        self.output_window_width = 965
        self.console_text = ""
        self.user_input = ""
        self.input_received = False
        self.player_hp = 100
        self.player_name = ""
        self.num_of_floors = random.randint(1, 15)


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
        while not self.input_received:
            dpg.render_dearpygui_frame()

    def main_game(self):
        self.input_to_output("You are standing in front of a cave. You can see the dragon's lair inside the cave.")
        self.input_to_output("What would you like to do? (enter the cave/leave)")
        self.wait_for_input()
        if self.user_input.lower() == "enter the cave":
            self.input_to_output("You have entered the cave!")
        else:
            self.input_to_output("You consider leaving but decide what's the point in standing in front of a cave if you're not going to enter it, so you enter it anyway.")
        self.input_to_output(f"The cave has {self.num_of_floors} floors to beat before you reach the final boss")

    def init_game(self):
        self.input_to_output("WELCOME TO THE GAME")
        self.input_to_output("You are a brave adventurer who has been tasked with saving the kingdom from the evil dragon")
        self.input_to_output("Please enter your character name: ")
        self.wait_for_input()  # Wait for user input
        self.player_name = self.user_input  # Get the entered name
        self.input_to_output(f"Welcome to the game {self.player_name}!")
        self.input_to_output("\nYou are about to embark on a dangerous journey to defeat the dragon and save the kingdom.")
        self.input_to_output("You have 100 HP (Health Points) to start with. If your HP drops to 0, you will be defeated and the game ends.")
        self.input_to_output("Are you ready to begin? (yes/no)")
        self.wait_for_input()
        if self.user_input.lower() == "yes":
            self.input_to_output("Great! Let's get started.")
            self.main_game()
        else:
            self.input_to_output("That's too bad. Maybe next time.")
            dpg.stop_dearpygui()

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
                               height=self.output_window_height-20, pos=(10, 10), callback=None, tracked=True)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("primary_window", True)

    def start(self):
        self.setup_gui()
        self.init_game()
        dpg.start_dearpygui()
        dpg.destroy_context()

# Run the game
game = Game()
game.start()
