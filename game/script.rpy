# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


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
######### CHARACTER SELECTION COMPONENT REUTILIZABLE
################################################################################################################
# hover imagen version, nice -rec3ks 
screen imagebutton_grid():
    text "SELECT YOUR CHARACTER"color "#000000" pos (520, 60) font "fonts/Segoe Print.ttf" size 17 bold True
    grid 4 3:
        xalign 0.5
        yalign 0.5
        spacing 20
        imagebutton:
            idle "master/master_noble.png"
            hover "master/master_noble_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_torturer.png"
            hover "master/master_torturer_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_fighter.png"
            hover "master/master_fighter_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_pimp.png"
            hover "master/master_pimp_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_teacher.png"
            hover "master/master_teacher_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_impressario.png"
            hover "master/master_impressario_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_doctor.png"
            hover "master/master_doctor_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_butler.png"
            hover "master/master_butler_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_granpa.png"
            hover "master/master_granpa_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_nerd.png"
            hover "master/master_nerd_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_werwolf.png"
            hover "master/master_werwolf_hover.png"
            action Jump("mainabout")
        imagebutton:
            idle "master/master_vampire.png"
            hover "master/master_vampire_hover.png"
            action Jump("mainabout")
    imagebutton:
        idle "buttons/close_button.png" pos (980,20)
        hover "buttons/close_button_hover.png"
        action Return()

##### Normal Start menu page code -rec3ks
####################################################


label Normal_Start:
    scene donotdelete
    show scroll_large
    call screen imagebutton_grid

    return
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
    show maincontroltext "{size=18}{color=#0000ff}        Controls in this game can be carried out solely with the help of the mouse. Interactive,\n clickable elements will turn your cursor into a hand.\n        Almost all actions are available from the central menu, but there are short cuts for\n most common ones. Orders for cooking, cleanig, bathing, sex milking, punishment and \n rewards can be issued with quick buttons under the character portraits (when correspon- \n ding actions are needed). You can set who will do cleaning and cooking with rules on your\n slave/assistant screen (click their portait or press S or A when at home) the big button \n with the image of an academic cap opens a list of training courses. You also can start a \n personal lesson by clicking a skill on the slave screen or order your assistant to teach a\n lesson via buttons on the side of the assitant screen.\n        Some choices are colered gray, which means that they are unavailable. The reason \n for this may be not meeting the requirements. Usually, you can click the grey text (or in \n menus hover over the small arrow in the lower left corner of the button icon) for more\n information.\n        When clickable left and right arrows are displayed, pressing SPACE is usually \n equivalent to clicking the right arrow. Press ESC to close some menus and exit some \n locations. At home, you can press D to open the master screen\n        Have a nice game!{/color}" at custom_position

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