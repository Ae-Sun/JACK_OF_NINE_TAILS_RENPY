# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
### only use default, you can also use $ but cause a lot of errors -rec3ks 
############ Be caution a stupid colon can make you game explote
init:
    style attribute_buttonS is default
    style attribute_buttonS_text:
        font "fonts/Consolas.ttf"
        color "#06aa00"
        size 17
        kerning 1
    style attribute_buttonA is default
    style attribute_buttonA_text:
        font "fonts/Consolas.ttf"
        color "#02fff2"
        size 17
        kerning 1
    style attribute_buttonB is default
    style attribute_buttonB_text:
        font "fonts/Consolas.ttf"
        color "#0011ff"
        size 17
        kerning 1
    style attribute_buttonC is default
    style attribute_buttonC_text:
        font "fonts/Consolas.ttf"
        color "#cc00ff"
        size 17
        kerning 1
    style attribute_buttonD is default
    style attribute_buttonD_text:
        font "fonts/Consolas.ttf"
        color "#ff00b3"
        size 17
        kerning 1
    style attribute_buttonF is default
    style attribute_buttonF_text:
        font "fonts/Consolas.ttf"
        color "#ff0000"
        size 17
        kerning 1
    
# I can probably merge characters and mc inicial_stats into a giga big dictionaly, but i won't. Im too lazy -rec3ks
default characters = [
    ("master_noble", "master/master_noble.webp", "master/master_noble_hover.webp",0),
    ("master_torturer", "master/master_torturer.webp", "master/master_torturer_hover.webp",1),
    ("master_fighter", "master/master_fighter.webp", "master/master_fighter_hover.webp",2),
    ("master_pimp", "master/master_pimp.webp", "master/master_pimp_hover.webp",3),
    ("master_teacher", "master/master_teacher.webp", "master/master_teacher_hover.webp",4),
    ("master_impressario", "master/master_impressario.webp", "master/master_impressario_hover.webp",5),
    ("master_doctor", "master/master_doctor.webp", "master/master_doctor_hover.webp",6),
    ("master_butler", "master/master_butler.webp", "master/master_butler_hover.webp",7),
    ("master_granpa", "master/master_granpa.webp", "master/master_granpa_hover.webp",8),
    ("master_nerd", "master/master_nerd.webp", "master/master_nerd_hover.webp",9),
    ("master_werwolf", "master/master_werwolf.webp", "master/master_werwolf_hover.webp",10),
    ("master_vampire", "master/master_vampire.webp", "master/master_vampire_hover.webp",11)
]
default mc_inicial_stats = {
"master_noble"      : ["M'lord"     , 4, 4, 0, 2, 4, 0, 0, 0, 5, 0, 5, 2, 2, 3, 2, 4, 0, 4, 3, 0, 3, 2, 4, 3], 
"master_torturer"   : ["Robespierre", 5, 1, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 3, 3, 0, 5, 5, 5, 2, 2, 4, 4],
"master_fighter"    : ["Blade"      , 5, 2, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 2, 5, 0, 2, 2, 2, 2, 2, 4, 2],
"master_pimp"       : ["Silk Daddy" , 3, 4, 0, 3, 4, 0, 0, 0, 5, 0, 5, 3, 2, 2, 1, 1, 0, 0, 4, 4, 2, 5, 5, 5],
"master_teacher"    : ["Teacher"    , 3, 3, 0, 3, 4, 0, 0, 0, 5, 0, 5, 5, 2, 2, 1, 0, 0, 4, 1, 2, 0, 1, 3, 0],
"master_impressario": ["Maestro"    , 2, 4, 0, 1, 3, 0, 0, 0, 5, 0, 5, 3, 1, 5, 0, 0, 0, 3, 0, 3, 0, 5, 4, 1],
"master_doctor"     : ["Doc"        , 3, 3, 0, 2, 2, 0, 0, 0, 5, 0, 5, 2, 1, 0, 5, 0, 0, 0, 3, 2, 0, 1, 3, 0],
"master_butler"     : ["Butler"     , 3, 3, 0, 2, 3, 0, 0, 0, 5, 0, 5, 3, 5, 1, 1, 0, 0, 2, 0, 2, 0, 1, 2, 0],
"master_granpa"     : ["Uncle Tom"  , 2, 1, 0, 0, 1, 0, 0, 0, 5, 0, 5, 2, 1, 0, 1, 0, 0, 2, 0, 4, 0, 3, 1, 4],
"master_nerd"       : ["Johny"      , 2, 1, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 5],
"master_werwolf"    : ["Fenris"     , 4, 0, 0, 4, 3, 0, 0, 0, 5, 0, 5, 1, 0, 0, 3, 3, 3, 2, 2, 2, 0, 0, 4, 2],
"master_vampire"    : ["Saruman"    , 5, 5, 0, 0, 4, 0, 0, 0, 5, 0, 5, 1, 3, 0, 2, 2, 4, 1, 1, 3, 1, 3, 3, 0],
}
default charactersOnlyName = ["master_noble", "master_torturer", "master_fighter", "master_pimp", "master_teacher", 
    "master_impressario", "master_doctor", "master_butler", "master_granpa", "master_nerd", 
    "master_werwolf", "master_vampire"]

default mc_attribute = { #DO NOT ADD ANY VARIABLE TO THIS and ANY DICTIONARY believe me I tried, the game explote -rec3ks
    "STRENGTH": ["Frail", "Weak", "Unfit", "Vigorous", "Strong", "Herculean"],
    "PERSONALITY": ["Caitiff", "Rube", "Churl", "Knave", "Vulgarian", "Aristocrat"],
    "ALLURE": ["Repulsive", "Unpleasant", "Unmemorable", "Charming", "Captivating", "Irresistible"],
    "LIBIDO": ["Impotent", "Effete", "Lustful", "Libidinous", "Lubricious", "Salacious"],
    "DOMINANCE": ["Submissive", "Compliant", "Passive", "Authoritative", "Dominant", "Imperious"],
    "BRAND REPUTATION": ["Unknown", "Rumored", "Recognized", "Celebrity", "Famous", "Legendary"],
    "GUILD REPUTATION": ["Guild Fall Guy", "Guild Punching Bag", "Guild Lackey", "Guild Hotshot", "Guild Muscle", "Guild Boss"],
    "STANDARD OF LIVING": ["Impoverished", "Poor", "Basic", "Comfortable", "Respectable", "Luxurious"],
    "HYGIENE": ["Filthy", "Dirty", "Unclean", "Unsullied", "Clean", "Pristine"],
    "MOOD": ["Depressed", "Dysphoric", "Sullen", "Melancholic", "Pessimistic", "Calm", "Hopeful", "Optimistic", "Pleased", "Euphoric", "Ecstatic"],
    "INJURIES": ["Mortally wounded", "Seriously Injured", "Moderately Injured", "Lightly Injured", "Slightly Wounded", "Safe and unharmed"],
    "TEACHING": ["Incoherent", "Tutor", "Mentor", "Pedagogue", "Teacher", "Lecturer"],
    "STEWARDSHIP": ["Ingenuous Dweller", "Peon", "Houseboy", "Homemaker", "Houselord", "Steward"],
    "ARTISTRY": ["Tasteless", "Uncultured", "Dilettante", "Artist", "Prodigy", "Virtuoso"],
    "MEDIC": ["Homeopath", "Quack", "Paramedic", "Medic", "Physician", "Surgeon"],
    "FIGHTER": ["Non-Combatant", "Brawler", "Duelist", "Combatant", "Warrior", "Champion"],
    "MAGIC": ["Mundane", "Esoterist", "Warlock", "Sorcerer", "Mage", "Archmage"],
    "FLAGELLATION": ["Cannot Whip", "Poor Whip Skill", "Basic Whip Skill", "Good Whip Skill", "Whip Expert", "Master of the Whip"],
    "TORTURE": ["Not a Torturer", "Needler", "Tormentor", "Torturer", "Inquisitor", "Master Inquisitor"],
    "BINDING": ["Unskilled with Rope", "Novice Rope Binder", "Binds Correctly", "Binds Skillfully", "Binds Artfully", "Master of Rope"],
    "PETTING": ["Petting"],
    "ORAL SEX": ["Oral Sex"],
    "PENETRATION": ["Penetration"],
    "FETISHISM": ["Fetishism"]
}
##################################### determinate the text value DO NOT CHANGE THE ORDER 
default strength_value_1 = 0
default personality_value_2 = 0
default allure_value_3 = 0
default libido_value_4 = 0
default dominance_value_5 = 0
default brand_reputation_value_6 = 0
default guild_reputation_value_7 = 0
default standard_of_living_value_8 = 0
default hygiene_value_9 = 0
default mood_value_10 = 0
default not_injuries_value_11 = 0
default teaching_value_12 = 0
default stewardship_value_13 = 0
default artistry_value_14 = 0
default medic_value_15 = 0
default fighter_value_16 = 0
default magic_value_17 = 0
default flagellation_value_18 = 0
default torture_value_19 = 0
default binding_value_20 = 0
default petting_value_21 = 0
default oral_sex_value_22 = 0
default penetration_value_23 = 0
default fetishism_value_24 = 0
############################################# number value -rec3ks

default strength_number_value_1 = 0
default personality_number_value_2 = 0
default allure_number_value_3 = 0
default libido_number_value_4 = 0
default dominance_number_value_5 = 0
default brand_reputation_number_value_6 = 0
default guild_reputation_number_value_7 = 0
default standard_of_living_number_value_8 = 0
default hygiene_number_value_9 = 0
default mood_number_value_10 = 0
default injuries_number_value_11 = 0
default teaching_number_value_12 = 0
default stewardship_number_value_13 = 0
default artistry_number_value_14 = 0
default medic_number_value_15 = 0
default fighter_number_value_16 = 0
default magic_number_value_17 = 0
default flagellation_number_value_18 = 0
default torture_number_value_19 = 0
default binding_number_value_20 = 0
default petting_number_value_21 = 0
default oral_sex_number_value_22 = 0
default penetration_number_value_23 = 0
default fetishism_number_value_24 = 0

#################################################################
default mc ="Jack"
default characterOnlyNameIndex = 0


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
    # add a file (named either "bg room.webp" or "bg room.jpg") to the
    # images directory to show it.

#    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.webp" to the images
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
                action [SetVariable("mc", char[0]),SetVariable("characterOnlyNameIndex",char[3]),Jump("Normal_Start2")]

    imagebutton:
        idle "buttons/close_button.webp" pos (997,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)



screen character_selection2(x,y,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q):
    imagebutton:
        idle "buttons/close_button.webp" pos (997,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)

    add "master/%s.webp" % mc xpos 0.3 ypos 0.24 anchor (0.5, 0.5)
    # Mapping of mc values to names
    imagebutton:
        idle "buttons/forward_button.webp" pos (960, 665)
        hover "buttons/forward_button_hover.webp"
        action [
            ##### this is a genius idea  -rec3ks
            SetVariable("mc",x),
            Jump("Normal_Start2")
        ]
    imagebutton:
        idle "buttons/back_button.webp" pos (265, 665)
        hover "buttons/back_button_hover.webp"
        action [
            ##### this is a genius idea  -rec3ks
            SetVariable("mc",y),
            SetVariable("characterOnlyNameIndex",characterOnlyNameIndex - 2),
            Jump("Normal_Start2")
        ]
    vbox:
        xalign 0.262
        yalign 0.42
        spacing 2.5

        
        #####this part I guess could be improve but i couldn't find a way to work -rec3ks
        textbutton strength_textvalue:
            style "attribute_button" +a
            action Jump("Tutorial")
        textbutton personality_textvalue:
            style "attribute_button" +b
            action Jump("Tutorial")
        textbutton libido_textvalue:
            style "attribute_button" +c
            action Jump("Tutorial")
        textbutton dominance_textvalue:
            style "attribute_button" +d
            action Jump("Tutorial")
    vbox:
        xalign 0.282 #### don't ask me why this is 0.282 and the other is 0.262 Idk 
        yalign 0.805
        spacing 2.5
        textbutton teaching_textvalue:
            style "attribute_button" +e
            action Jump("Tutorial")
        textbutton stewardship_textvalue:
            style "attribute_button" +f
            action Jump("Tutorial")
        textbutton artistry_textvalue:
            style "attribute_button" +g
            action Jump("Tutorial")
        textbutton medic_textvalue:
            style "attribute_button" +h
            action Jump("Tutorial")
        textbutton fighter_textvalue:
            style "attribute_button" +i
            action Jump("Tutorial")
        textbutton magic_textvalue:
            style "attribute_button" +j
            action Jump("Tutorial")
        textbutton flagellation_textvalue:
            style "attribute_button" +k
            action Jump("Tutorial")
        textbutton torture_textvalue:
            style "attribute_button" +l
            action Jump("Tutorial")
        textbutton binding_textvalue:
            style "attribute_button" +m
            action Jump("Tutorial")
        textbutton petting_textvalue:
            style "attribute_button" +n
            action Jump("Tutorial")
        textbutton oral_sex_textvalue:
            style "attribute_button" +o
            action Jump("Tutorial")
        textbutton penetration_textvalue:
            style "attribute_button" +p
            action Jump("Tutorial")
        textbutton fetishism_textvalue:
            style "attribute_button" +q
            action Jump("Tutorial")

    # Fallback name if mc is not recognized
    $ display_name = mc_inicial_stats.get(mc, ["Error - Try restart your game"])[0]
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
    $ strength_textvalue = mc_attribute["STRENGTH"][strength_value]
    $ personality_textvalue = mc_attribute["PERSONALITY"][personality_value]
    $ allure_textvalue = mc_attribute["ALLURE"][allure_value]
    $ libido_textvalue = mc_attribute["LIBIDO"][libido_value]
    $ dominance_textvalue = mc_attribute["DOMINANCE"][dominance_value]
    $ brand_reputation_textvalue = mc_attribute["BRAND REPUTATION"][brand_reputation_value]
    $ guild_reputation_textvalue = mc_attribute["GUILD REPUTATION"][guild_reputation_value]
    $ standard_of_living_textvalue = mc_attribute["STANDARD OF LIVING"][standard_of_living_value]
    $ hygiene_textvalue = mc_attribute["HYGIENE"][hygiene_value]
    $ mood_textvalue = mc_attribute["MOOD"][mood_value]
    $ injuries_textvalue = mc_attribute["INJURIES"][not_injuries_value]
    $ teaching_textvalue = mc_attribute["TEACHING"][teaching_value]
    $ stewardship_textvalue = mc_attribute["STEWARDSHIP"][stewardship_value]
    $ artistry_textvalue = mc_attribute["ARTISTRY"][artistry_value]
    $ medic_textvalue = mc_attribute["MEDIC"][medic_value]
    $ fighter_textvalue = mc_attribute["FIGHTER"][fighter_value]
    $ magic_textvalue = mc_attribute["MAGIC"][magic_value]
    $ flagellation_textvalue = mc_attribute["FLAGELLATION"][flagellation_value]
    $ torture_textvalue = mc_attribute["TORTURE"][torture_value]
    $ binding_textvalue = mc_attribute["BINDING"][binding_value]
    $ petting_textvalue = mc_attribute["PETTING"][petting_value]
    $ oral_sex_textvalue = mc_attribute["ORAL SEX"][oral_sex_value]
    $ penetration_textvalue = mc_attribute["PENETRATION"][penetration_value]
    $ fetishism_textvalue = mc_attribute["FETISHISM"][fetishism_value]
    $ characterOnlyNameIndex = characterOnlyNameIndex +1
    if -5 <= characterOnlyNameIndex <= 11:
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2],"F")
    elif characterOnlyNameIndex >= -5:
        #block of code to run:
        $ characterOnlyNameIndex = 0
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2],"F")
    else:
        $ characterOnlyNameIndex = 6
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2],"F")



label Custom_Start:
    "WIP"
    return
################################################################
#### main menu control page code -rec3ks
###########################################################
transform custom_position:
    xpos 0.23
    ypos 0.12
    xanchor 0 # idk this, i only know it works -rec3ks
    yanchor 0 # idk this, i only know it works -rec3ks
image maincontroltext = ParameterizedText(xalign=0.5, yalign=0.0) 
label mainControls:
    scene donotdelete
    show scroll_large
    show maincontroltext "{size=18}{color=#0000ff}        Controls in this game can be carried out solely with the help of the mouse. Interactive,\n clickable elements will turn your cursor into a hand.\n        Almost all actions are available from the central menu, but there are short cuts for\n most common ones. Orders for cooking, cleanig, bathing, sex milking, punishment and \n rewards can be issued with quick buttons under the character portraits (when correspon- \n ding actions are needed). You can set who will do cleaning and cooking with rules on your\n slave/assistant screen (click their portait or press {b}S{/b} or {b}A{/b} when at home) the big button \n with the image of an academic cap opens a list of training courses. You also can start a \n personal lesson by clicking a skill on the slave screen or order your assistant to teach a\n lesson via buttons on the side of the assitant screen.\n        Some choices are colered gray, which means that they are unavailable. The reason \n for this may be not meeting the requirements. Usually, you can click the grey text (or in \n menus hover over the small arrow in the lower left corner of the button icon) for more\n information.\n        When clickable left and right arrows are displayed, pressing{b} SPACE{/b} is usually \n equivalent to clicking the right arrow. Press {b}ESC{/b} to close some menus and exit some \n locations. At home, you can press{b} D {/b}to open the master screen.\n        Have a nice game!{/color}" at custom_position

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