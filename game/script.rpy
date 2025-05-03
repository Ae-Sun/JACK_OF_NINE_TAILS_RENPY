# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mc ="Jack"
default characters = [
    ("master_noble", "master/master_noble.png", "master/master_noble_hover.png"),
    ("master_torturer", "master/master_torturer.png", "master/master_torturer_hover.png"),
    ("master_fighter", "master/master_fighter.png", "master/master_fighter_hover.png"),
    ("master_pimp", "master/master_pimp.png", "master/master_pimp_hover.png"),
    ("master_teacher", "master/master_teacher.png", "master/master_teacher_hover.png"),
    ("master_impressario", "master/master_impressario.png", "master/master_impressario_hover.png"),
    ("master_doctor", "master/master_doctor.png", "master/master_doctor_hover.png"),
    ("master_butler", "master/master_butler.png", "master/master_butler_hover.png"),
    ("master_granpa", "master/master_granpa.png", "master/master_granpa_hover.png"),
    ("master_nerd", "master/master_nerd.png", "master/master_nerd_hover.png"),
    ("master_werwolf", "master/master_werwolf.png", "master/master_werwolf_hover.png"),
    ("master_vampire", "master/master_vampire.png", "master/master_vampire_hover.png")
]



# The game starts here.

########## Warning screen -rec3ks
###########################################################################
label splashscreen:
    # Show the warning message
    show warning

    # Display two options (Accept or Quit) after the warning
    menu:
        
        "Yes, I am adult and I want to continue":
            # Logic for when the player chooses "Accept"
            $ result = "Accepted"
            jump after_splash

        "Exit immediately":
            # Logic for when the player chooses "Quit"
            $ result = "Quit"
            $ renpy.quit()

label after_splash:
    # Handle the outcome after the player selects an option
    if result == "Accepted":
        "You accepted the warning and continue the game."
    elif result == "Quit":
        "You chose to quit the game."

    return

###########################################################################
label Tutorial:
    "WIP"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

#    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#    show eileen happy

    # These display lines of dialogue.

#    e "You've created a new Ren'Py game."

#    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
##### Normal Start menu page code -rec3ks
####################################################
######### CHARACTER SELECTION
################################################################################################################
# hover imagen version, nice -rec3ks 
screen character_selection():
    text "SELECT YOUR CHARACTER" color "#000000" pos (520, 60) font "fonts/Segoe Print.ttf" size 17 bold True

    # List of character data (name, image path, hover image path)

    grid 4 3:
        xalign 0.5
        yalign 0.5
        spacing 20

        # Loop through the list of characters to generate buttons dynamically
        for char in characters:
            imagebutton:
                idle char[1]
                hover char[2]
                action [SetVariable("mc", char[0]), Jump("Normal_Start2")]

    imagebutton:
        idle "buttons/close_button.png" pos (997,12)
        hover "buttons/close_button_hover.png"
        action MainMenu(confirm=False)

screen character_selection2():
    imagebutton:
        idle "buttons/close_button.png" pos (997,12)
        hover "buttons/close_button_hover.png"
        action MainMenu(confirm=False)

    add "master/%s.png" % mc xpos 0.3 ypos 0.24 anchor (0.5, 0.5)
    # Mapping of mc values to names
    default mc_names = {
        "master_noble": "M'lord",
        "master_torturer": "Robespierre",
        "master_fighter": "Blade",
        "master_pimp": "Silk Daddy",
        "master_teacher": "Teacher",
        "master_impressario": "Maestro",
        "master_doctor": "Doc",
        "master_butler": "Butler",
        "master_granpa": "Uncle Tom",
        "master_nerd": "Johny",
        "master_werwolf": "Fenris",
        "master_vampire": "Saruman"
    }

    imagebutton:
        idle "buttons/forward_button.png" pos (960, 665)
        hover "buttons/forward_button_hover.png"
        action [
            ##### I need to find a way to make this bottom works  -rec3ks
            If(lambda: mc == "master_noble", 
            SetVariable("mc","master_torturer")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_torturer", 
            SetVariable("mc", "master_fighter")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_fighter", 
            SetVariable("mc", "master_pimp")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_pimp", 
            SetVariable("mc", "master_teacher")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_teacher", 
            SetVariable("mc", "master_impressario")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_impressario", 
            SetVariable("mc", "master_doctor")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_doctor", 
            SetVariable("mc", "master_butler")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_butler", 
            SetVariable("mc", "master_granpa")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_granpa", 
            SetVariable("mc", "master_nerd")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_nerd", 
            SetVariable("mc", "master_werwolf")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_werwolf", 
            SetVariable("mc", "master_vampire")),
            Jump("Normal_Start2"),
            If(lambda: mc == "master_vampire", 
            SetVariable("mc", "master_noble")),
            Jump("Normal_Start2")

        ]
    imagebutton:
        idle "buttons/back_button.png" pos (265, 665)
        hover "buttons/back_button_hover.png"
        action MainMenu(confirm=False)
    
    # Fallback name if mc is not recognized
    $ display_name = mc_names.get(mc, "Error - Try restart your game")

    text display_name:
        size 72
        pos (0.60, 0.19)
        color "#000000"
        font "fonts/Victoriana.ttf"
        anchor (0.5, 0.5)

label Normal_Start:
    scene donotdelete
    show scroll_large
    call screen character_selection
label Normal_Start2:
    scene donotdelete
    show scroll_large
    
    call screen character_selection2

label Custom_Start:
    "WIP"
    return
################################################################
#### main menu control page code -rec3ks
###########################################################
transform custom_position:
    xpos 0.23
    ypos 0.1
    xanchor 0 # -this shit does nothing but if delete control text wont show correctly. Probably some quirk -rec3ks
    yanchor 0 # -this shit does nothing but if delete control text wont show correctly. Probably some quirk -rec3ks
image maincontroltext = ParameterizedText(xalign=0.5, yalign=0.0) 
label mainControls:
    scene donotdelete
    show scroll_large
    show maincontroltext "{size=18}{color=#0000ff}        Controls in this game can be carried out solely with the help of the mouse. Interactive,\n clickable elements will turn your cursor into a hand.\n        Almost all actions are available from the central menu, but there are short cuts for\n most common ones. Orders for cooking, cleanig, bathing, sex milking, punishment and \n rewards can be issued with quick buttons under the character portraits (when correspon- \n ding actions are needed). You can set who will do cleaning and cooking with rules on your\n slave/assistant screen (click their portait or press {b}S{/b} or {b}A{/b} when at home) the big button \n with the image of an academic cap opens a list of training courses. You also can start a \n personal lesson by clicking a skill on the slave screen or order your assistant to teach a\n lesson via buttons on the side of the assitant screen.\n        Some choices are colered gray, which means that they are unavailable. The reason \n for this may be not meeting the requirements. Usually, you can click the grey text (or in \n menus hover over the small arrow in the lower left corner of the button icon) for more\n information.\n        When clickable left and right arrows are displayed, pressing{b} SPACE{/b} is usually \n equivalent to clicking the right arrow. Press {b}ESC{/b} to close some menus and exit some \n locations. At home, you can press{b} D {/b}to open the master screen\n        Have a nice game!{/color}" at custom_position

    "Click to return"
    return
#####################################################################
###### Code that someday I may fix. Dont touch it -rec3ks 
#######################################################################
label mainload:
    call screen load
    return  # Ends the new game session if user cancels load

label mainpreferences:
    call screen preferences
    return  # Ends the new game session if user cancels load
label mainabout:
    call screen about
    return  # Ends the new game session if user cancels load
#######################################################################