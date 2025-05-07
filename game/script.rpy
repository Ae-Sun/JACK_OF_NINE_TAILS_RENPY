# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
### only use default, you can also use $ but cause a lot of errors -rec3ks 
############ Be caution a stupid colon can make you game explote
init:
################################################# attribute button style 
    style attribute_button0 is default
    style attribute_button0_text:
        font "fonts/Consolas.ttf"
        color "#CD0000"
        size 17
        kerning 1
        hover_color  "#ffff00"
    style attribute_button1 is default
    style attribute_button1_text:
        font "fonts/Consolas.ttf"
        color "#EA0090"
        size 17
        kerning 1
        hover_color  "#ffff00"
    style attribute_button2 is default
    style attribute_button2_text:
        font "fonts/Consolas.ttf"
        color "#6B0084"
        size 17
        kerning 1
        hover_color  "#ffff00"
    style attribute_button3 is default
    style attribute_button3_text:
        font "fonts/Consolas.ttf"
        color "#002BA7"
        size 17
        kerning 1
        hover_color  "#ffff00"
    style attribute_button4 is default
    style attribute_button4_text:
        font "fonts/Consolas.ttf"
        color "#009FEF"
        size 17
        kerning 1
        hover_color  "#ffff00"
    style attribute_button5 is default
    style attribute_button5_text:
        font "fonts/Consolas.ttf"
        color "#009900"
        size 17
        kerning 1
        hover_color  "#ffff00"
################################################## difficulty button style
    style difficulty_button0 is default
    style difficulty_button0_text:
        font "fonts/victoriana.ttf"
        color "#CD0000"
        size 48
        hover_color "#ffff00"

    style difficulty_button1 is default
    style difficulty_button1_text:
        font "fonts/victoriana.ttf"
        color "#EA0090"
        size 48
        hover_color "#ffff00"

    style difficulty_button2 is default
    style difficulty_button2_text:
        font "fonts/victoriana.ttf"
        color "#6B0084"
        size 48
        hover_color "#ffff00"

    style difficulty_button3 is default
    style difficulty_button3_text:
        font "fonts/victoriana.ttf"
        color "#002BA7"
        size 48
        hover_color "#ffff00"

    style difficulty_button4 is default
    style difficulty_button4_text:
        font "fonts/victoriana.ttf"
        color "#009FEF"
        size 48
        hover_color "#ffff00"

    style difficulty_button5 is default
    style difficulty_button5_text:
        font "fonts/victoriana.ttf"
        color "#009900"
        size 48
        hover_color "#ffff00"


# I can probably merge characters and mc inicial_stats into a giga big dictionaly, but not now -rec3ks
default characters = [
    ("master_noble", "master/master_noble.webp", "master/master_noble_hover.webp",0),
    ("master_torturer", "master/master_torturer.webp", "master/master_torturer_hover.webp",1),
    ("master_pimp", "master/master_pimp.webp", "master/master_pimp_hover.webp",2),
    ("master_vampire", "master/master_vampire.webp", "master/master_vampire_hover.webp",3),
    ("master_fighter", "master/master_fighter.webp", "master/master_fighter_hover.webp",4),
    ("master_teacher", "master/master_teacher.webp", "master/master_teacher_hover.webp",5),
    ("master_impressario", "master/master_impressario.webp", "master/master_impressario_hover.webp",6),
    ("master_doctor", "master/master_doctor.webp", "master/master_doctor_hover.webp",7),
    ("master_butler", "master/master_butler.webp", "master/master_butler_hover.webp",8),
    ("master_werwolf", "master/master_werwolf.webp", "master/master_werwolf_hover.webp",9),
    ("master_granpa", "master/master_granpa.webp", "master/master_granpa_hover.webp",10),
    ("master_nerd", "master/master_nerd.webp", "master/master_nerd_hover.webp",11),
]
default mc_inicial_stats = {
    "master_noble"      : ["M'lord"     , 4, 4, 0, 2, 4, 0, 0, 0, 5, 0, 5, 2, 2, 3, 2, 4, 0, 4, 3, 0, 3, 2, 4, 3,"simple difficulty",    5,"   An aristocrat with a great education, with \n experience in court and military service. Having all \n the basic skills that are necesarry to teach, the easily \n joined the ranks of the slavers and all agree that a \n wonderful career awaits him..."], 
    "master_torturer"   : ["Robespierre", 5, 1, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 3, 3, 0, 5, 5, 5, 2, 2, 4, 4,"simple difficulty",    5,"wip"],
    "master_pimp"       : ["Silk Daddy" , 3, 4, 0, 3, 4, 0, 0, 0, 5, 0, 5, 3, 2, 2, 1, 1, 0, 0, 4, 4, 2, 5, 5, 5,"simple difficulty",    5,"wip"],
    "master_vampire"    : ["Saruman"    , 5, 5, 0, 0, 4, 0, 0, 0, 5, 0, 5, 1, 3, 0, 2, 2, 4, 1, 1, 3, 1, 3, 3, 0,"simple difficulty",    5,"wip"],
    "master_fighter"    : ["Blade"      , 5, 2, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 2, 5, 0, 2, 2, 2, 2, 2, 4, 2,"normal difficulty",    3,"wip"],
    "master_teacher"    : ["Teacher"    , 3, 3, 0, 3, 4, 0, 0, 0, 5, 0, 5, 5, 2, 2, 1, 0, 0, 4, 1, 2, 0, 1, 3, 0,"normal difficulty",    3,"wip"],
    "master_impressario": ["Maestro"    , 2, 4, 0, 1, 3, 0, 0, 0, 5, 0, 5, 3, 1, 5, 0, 0, 0, 3, 0, 3, 0, 5, 4, 1,"normal difficulty",    3,"wip"],
    "master_doctor"     : ["Doc"        , 3, 3, 0, 2, 2, 0, 0, 0, 5, 0, 5, 2, 1, 0, 5, 0, 0, 0, 3, 2, 0, 1, 3, 0,"high difficulty",      2,"wip"],
    "master_butler"     : ["Butler"     , 3, 3, 0, 2, 3, 0, 0, 0, 5, 0, 5, 3, 5, 1, 1, 0, 0, 2, 0, 2, 0, 1, 2, 0,"high difficulty",      2,"wip"],
    "master_werwolf"    : ["Fenris"     , 4, 0, 0, 4, 3, 0, 0, 0, 5, 0, 5, 1, 0, 0, 3, 3, 3, 2, 2, 2, 0, 0, 4, 2,"high difficulty",      2,"wip"],
    "master_granpa"     : ["Uncle Tom"  , 2, 1, 0, 0, 1, 0, 0, 0, 5, 0, 5, 2, 1, 0, 1, 0, 0, 2, 0, 4, 0, 3, 1, 4,"very high difficulty", 1,"wip"],
    "master_nerd"       : ["Johny"      , 2, 1, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 5,"maximum difficulty",   0,"wip"]
    }
default charactersOnlyName = ["master_noble", "master_torturer", "master_pimp", "master_vampire", "master_fighter","master_teacher", "master_impressario", "master_doctor", "master_butler", "master_werwolf", "master_granpa", "master_nerd"]

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
    "TEACHING": ["Incoherent F-", "Tutor D-", "Mentor C-", "Pedagogue B+", "Teacher A+", "Lecturer S+"],
    "STEWARDSHIP": ["Ingenuous Dweller F-", "Peon D-", "Houseboy C-", "Homemaker B+", "Houselord A+", "Steward S+"],
    "ARTISTRY": ["Tasteless F-", "Uncultured D-", "Dilettante C-", "Artist B+", "Prodigy A+", "Virtuoso S+"],
    "MEDIC": ["Homeopath F-", "Quack D-", "Paramedic C-", "Medic B+", "Physician A+", "Surgeon S+"],
    "FIGHTER": ["Non-Combatant F-", "Brawler D-", "Duelist C-", "Combatant B+", "Warrior A+", "Champion S+"],
    "MAGIC": ["Mundane F-", "Esoterist D-", "Warlock C-", "Sorcerer B+", "Mage A+", "Archmage S+"],
    "FLAGELLATION": ["Cannot Whip F-", "Poor Whip Skill D-", "Basic Whip Skill C-", "Good Whip Skill B+", "Whip Expert A+", "Master of the Whip S+"],
    "TORTURE": ["Not a Torturer F-", "Needler D-", "Tormentor C-", "Torturer B+", "Inquisitor A+", "Master Inquisitor S+"],
    "BINDING": ["Unskilled with Rope F-", "Novice Rope Binder D-", "Binds Correctly C-", "Binds Skillfully B+", "Binds Artfully A+", "Master of Rope S+"],
    "PETTING": ["Petting F-", "Petting D-", "Petting C-", "Petting B+", "Petting A+", "Petting S+"],
    "ORAL SEX": ["Oral Sex F-", "Oral Sex D-", "Oral Sex C-", "Oral Sex B+", "Oral Sex A+", "Oral Sex S+"],
    "PENETRATION": ["Penetration F-", "Penetration D-", "Penetration C-", "Penetration B+", "Penetration A+", "Penetration S+"],
    "FETISHISM": ["Unadventurous F-", "Fetishism D-", "Fetishism C-", "Fetishism B+", "Fetishism A+", "Worst of Perverts S+"]
}
##################################### Text value, DO NOT CHANGE ANY ORDER OF ANY VARIABLE
default strength_textvalue_1 = 0
default personality_textvalue_2 = 0
default allure_textvalue_3 = 0
default libido_textvalue_4 = 0
default dominance_textvalue_5 = 0
default brand_reputation_textvalue_6 = 0
default guild_reputation_textvalue_7 = 0
default standard_of_living_textvalue_8 = 0
default hygiene_textvalue_9 = 0
default mood_textvalue_10 = 0
default not_injuries_textvalue_11 = 0
default teaching_textvalue_12 = 0
default stewardship_textvalue_13 = 0
default artistry_textvalue_14 = 0
default medic_textvalue_15 = 0
default fighter_textvalue_16 = 0
default magic_textvalue_17 = 0
default flagellation_textvalue_18 = 0
default torture_textvalue_19 = 0
default binding_textvalue_20 = 0
default petting_textvalue_21 = 0
default oral_sex_textvalue_22 = 0
default penetration_textvalue_23 = 0
default fetishism_textvalue_24 = 0
################################## values -rec3ks

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
default injuries_value_11 = 0
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

############################################ textvalue track - herculean
############################################ value track - 5
############################################ number value track 999/999

default inicial_difficulty_textvalue =""
default inicial_difficulty_value = 0

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



screen character_selection2(x,y):

    textbutton inicial_difficulty_textvalue pos (765, 195) anchor(0.5,0.5):
        style "difficulty_button" + str(inicial_difficulty_value)
        action Jump("Tutorial")

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
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing 2.5    # Spacing between all buttons
        xpos 310 
        ypos 250  

        add "spacer" size (0,15)  # Create an invisible spacer with 30px height
    
        textbutton strength_textvalue_1:
            style "attribute_button" + str(strength_value_1)
            action Jump("Tutorial")

        textbutton personality_textvalue_2:
            style "attribute_button" + str(personality_value_2)
            action Jump("Tutorial")

        textbutton libido_textvalue_4:
            style "attribute_button" + str(libido_value_4)
            action Jump("Tutorial")

        textbutton dominance_textvalue_5:
            style "attribute_button" + str(dominance_value_5)
            action Jump("Tutorial")

        # Adding extra spacing here:
        add "spacer" size (0, 20)

        textbutton teaching_textvalue_12:
            style "attribute_button" + str(teaching_value_12)
            action Jump("Tutorial")

        textbutton stewardship_textvalue_13:
            style "attribute_button" + str(stewardship_value_13)
            action Jump("Tutorial")

        textbutton artistry_textvalue_14:
            style "attribute_button" + str(artistry_value_14)
            action Jump("Tutorial")

        textbutton medic_textvalue_15:
            style "attribute_button" + str(medic_value_15)
            action Jump("Tutorial")

        textbutton fighter_textvalue_16:
            style "attribute_button" + str(fighter_value_16)
            action Jump("Tutorial")

        textbutton magic_textvalue_17:
            style "attribute_button" + str(magic_value_17)
            action Jump("Tutorial")

        textbutton flagellation_textvalue_18:
            style "attribute_button" + str(flagellation_value_18)
            action Jump("Tutorial")

        textbutton torture_textvalue_19:
            style "attribute_button" + str(torture_value_19)
            action Jump("Tutorial")

        textbutton binding_textvalue_20:
            style "attribute_button" + str(binding_value_20)
            action Jump("Tutorial")

        textbutton petting_textvalue_21:
            style "attribute_button" + str(petting_value_21)
            action Jump("Tutorial")

        textbutton oral_sex_textvalue_22:
            style "attribute_button" + str(oral_sex_value_22)
            action Jump("Tutorial")

        textbutton penetration_textvalue_23:
            style "attribute_button" + str(penetration_value_23)
            action Jump("Tutorial")

        textbutton fetishism_textvalue_24:
            style "attribute_button" + str(fetishism_value_24)
            action Jump("Tutorial")

    # Fallback name if mc is not recognized
    $ display_name = mc_inicial_stats.get(mc, ["Error - Try restart your game"])[0]
    text display_name:
        size 72
        pos (0.60, 0.19)
        color "#000000"
        font "fonts/Victoriana.ttf"
        anchor (0.5, 0.5)
    text mc_inicial_stats[mc][27]:
        pos(0.40,0.37)
        color "#191970"
        size 16
        font "fonts/Segoe Print.ttf"



label Normal_Start:
    scene donotdelete
    show scroll_large
    call screen character_selection
label Normal_Start2:
    scene donotdelete
    show scroll_large

    $ characterOnlyNameIndex = characterOnlyNameIndex +1
    
    $ strength_value_1 = mc_inicial_stats[mc][1]
    $ personality_value_2 = mc_inicial_stats[mc][2]
    $ allure_value_3 = mc_inicial_stats[mc][3]
    $ libido_value_4 = mc_inicial_stats[mc][4]
    $ dominance_value_5 = mc_inicial_stats[mc][5]
    $ brand_reputation_value_6 = mc_inicial_stats[mc][6]
    $ guild_reputation_value_7 = mc_inicial_stats[mc][7]
    $ standard_of_living_value_8 = mc_inicial_stats[mc][8]
    $ hygiene_value_9 = mc_inicial_stats[mc][9]
    $ mood_value_10 = mc_inicial_stats[mc][10]
    $ injuries_value_11 = mc_inicial_stats[mc][11]
    $ teaching_value_12 = mc_inicial_stats[mc][12]
    $ stewardship_value_13 = mc_inicial_stats[mc][13]
    $ artistry_value_14 = mc_inicial_stats[mc][14]
    $ medic_value_15 = mc_inicial_stats[mc][15]
    $ fighter_value_16 = mc_inicial_stats[mc][16]
    $ magic_value_17 = mc_inicial_stats[mc][17]
    $ flagellation_value_18 = mc_inicial_stats[mc][18]
    $ torture_value_19 = mc_inicial_stats[mc][19]
    $ binding_value_20 = mc_inicial_stats[mc][20]
    $ petting_value_21 = mc_inicial_stats[mc][21]
    $ oral_sex_value_22 = mc_inicial_stats[mc][22]
    $ penetration_value_23 = mc_inicial_stats[mc][23]
    $ fetishism_value_24 = mc_inicial_stats[mc][24]

    # more variables  -rec3ks
    $ strength_textvalue_1 = mc_attribute["STRENGTH"][mc_inicial_stats[mc][1]]
    $ personality_textvalue_2 = mc_attribute["PERSONALITY"][mc_inicial_stats[mc][2]]
    $ allure_textvalue_3 = mc_attribute["ALLURE"][mc_inicial_stats[mc][3]]
    $ libido_textvalue_4 = mc_attribute["LIBIDO"][mc_inicial_stats[mc][4]]
    $ dominance_textvalue_5 = mc_attribute["DOMINANCE"][mc_inicial_stats[mc][5]]
    $ brand_reputation_textvalue_6 = mc_attribute["BRAND REPUTATION"][mc_inicial_stats[mc][6]]
    $ guild_reputation_textvalue_7 = mc_attribute["GUILD REPUTATION"][mc_inicial_stats[mc][7]]
    $ standard_of_living_textvalue_8 = mc_attribute["STANDARD OF LIVING"][mc_inicial_stats[mc][8]]
    $ hygiene_textvalue_9 = mc_attribute["HYGIENE"][mc_inicial_stats[mc][9]]
    $ mood_textvalue_10 = mc_attribute["MOOD"][mc_inicial_stats[mc][10]]
    $ injuries_textvalue_11 = mc_attribute["INJURIES"][mc_inicial_stats[mc][11]]
    $ teaching_textvalue_12 = mc_attribute["TEACHING"][mc_inicial_stats[mc][12]]
    $ stewardship_textvalue_13 = mc_attribute["STEWARDSHIP"][mc_inicial_stats[mc][13]]
    $ artistry_textvalue_14 = mc_attribute["ARTISTRY"][mc_inicial_stats[mc][14]]
    $ medic_textvalue_15 = mc_attribute["MEDIC"][mc_inicial_stats[mc][15]]
    $ fighter_textvalue_16 = mc_attribute["FIGHTER"][mc_inicial_stats[mc][16]]
    $ magic_textvalue_17 = mc_attribute["MAGIC"][mc_inicial_stats[mc][17]]
    $ flagellation_textvalue_18 = mc_attribute["FLAGELLATION"][mc_inicial_stats[mc][18]]
    $ torture_textvalue_19 = mc_attribute["TORTURE"][mc_inicial_stats[mc][19]]
    $ binding_textvalue_20 = mc_attribute["BINDING"][mc_inicial_stats[mc][20]]
    $ petting_textvalue_21 = mc_attribute["PETTING"][mc_inicial_stats[mc][21]]
    $ oral_sex_textvalue_22 = mc_attribute["ORAL SEX"][mc_inicial_stats[mc][22]]
    $ penetration_textvalue_23 = mc_attribute["PENETRATION"][mc_inicial_stats[mc][23]]
    $ fetishism_textvalue_24 = mc_attribute["FETISHISM"][mc_inicial_stats[mc][24]]

    $ inicial_difficulty_textvalue = mc_inicial_stats[mc][25] #need to fix number later
    $ inicial_difficulty_value = mc_inicial_stats[mc][26] #need to fix number later

    if -5 <= characterOnlyNameIndex < 11:
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])
    elif characterOnlyNameIndex >= -5:
        $ characterOnlyNameIndex = 0
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])
    else:
        $ characterOnlyNameIndex = 6
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])


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