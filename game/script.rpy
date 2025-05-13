# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
### only use default, you can also use $ but cause a lot of errors -rec3ks 
##################################### Text value, DO NOT CHANGE ANY ORDER OF ANY VARIABLE
default strength_textvalue_1 = ""
default personality_textvalue_2 = ""
default allure_textvalue_3 = ""
default libido_textvalue_4 = ""
default dominance_textvalue_5 = ""
default brand_reputation_textvalue_6 = ""
default guild_reputation_textvalue_7 = ""
default standard_of_living_textvalue_8 = ""
default hygiene_textvalue_9 = ""
default mood_textvalue_10 = ""
default not_injuries_textvalue_11 = ""
default teaching_textvalue_12 = ""
default stewardship_textvalue_13 = ""
default artistry_textvalue_14 = ""
default medic_textvalue_15 = ""
default fighter_textvalue_16 = ""
default magic_textvalue_17 = ""
default flagellation_textvalue_18 = ""
default torture_textvalue_19 = ""
default binding_textvalue_20 = ""
default petting_textvalue_21 = ""
default oral_sex_textvalue_22 = ""
default penetration_textvalue_23 = ""
default fetishism_textvalue_24 = ""
default reputation_textvalue_1 = ""
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
default reputation_value_1 = 0

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
default armour_25 = ""
default Shoulder_26 = ""
default left_hand_27 = ""
default righ_hand_28 = ""
default sleeve_holster_29 = ""
default boot_holster_30 = ""
default clothes_31 = ""
default headgear_32 = ""
default earring_33 = ""
default neck_34 = ""
default ring_35 =""
##################################################
default faction_36 =""
default sparks_37 =""
###################################################
default mc ="Jack"
default characterOnlyNameIndex = 0
###################################################################
default angelika_speech_text_count = 0
default speakcolor = "#8B0A50"
##############################

# The game starts here.

########## Warning screen -rec3ks
###########################################################################
screen angelika_speech_bg():
    add "bg/guild.webp"pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 515
screen angelika_angelika():
    add "characters/mistress_angelika.webp"pos(0.3, 0.307) anchor (0.5, 0.5) 
screen angelika_speech():
    text angelika_speech_text[angelika_speech_text_count] pos (0.02, 0.75) size 20 color speakcolor font "consolas.ttf"
screen angelika_speech2():
    text " It indicates here that you have already fully paid the entry fee,\n {b}[mc]{/b}. Good. But consider this: we will not tolerate black \n sheep in our guild, no matter how much they pay. The honor of our \n organization is paramount."pos (0.02, 0.78) size 20 color"#8B0A50"  font "consolas.ttf"
screen angelika_speech3():
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle tutorial_backbutton anchor (0.5, 0.5)
            hover tutorial_backbutton_hover
            action SetVariable("angelika_speech_text_count", max(angelika_speech_text_count - 1,0)),Jump("Tutorial")
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action SetVariable("angelika_speech_text_count", min(angelika_speech_text_count + 1,4)),Jump("Tutorial")
    vbox:
        pos(0.82,0.05)
        text "Mistress Angelika" size 45 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,-10)
        text "Slavers Guild Master"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        text "Neutrals"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,20)
        text "Information for consideration:" size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
    vbox:
        pos(0.650,0.25)
        text attitude_text["haughty"][0] size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
        add "spacer" size (0,60)    
        text "   It seems from this lady depends the final decision about my entry into the guild. Most likely, this is just a formality, but it is necessary to remain vigilant. She looks like a person who does not forgive weakness and enjoys suffering neighbors…" xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
        text "   What the hell?! She looks like a complete bitch, though sexy." xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
screen slaver_guild():
    vbox:
        pos(0.82,0.05)
        text "Slavers Guild" size 45 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,-10)
        text "Vatican Suburbs"size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
        add "spacer" size (0,20)
        text "Information for consideration:" size 30 color "#000000" font "fonts/victoriana.ttf" anchor (0.5, 0.5)
    vbox:
        pos(0.650,0.25)
        text "   Judging by the interior of this place, you can say that the Slavers Guild members have a high place in the social hierarchy. The rooms all distinguish themselves by their apparent class and comfort, with the exception of the prisons and dungeons, of course…" xmaximum 425 size 20 color "#191970" font "fonts/Segoe Print.ttf" anchor (0.0,0.0)
    vbox:
        pos(0.165,0.05)
        spacing 18  
        textbutton "Lecture I: Components of success":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Lecture II: Psychology of submission":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Lecture III: Sticks and carrots":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Lecture IV: Kitchen slavery":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Check the conditions of the exam":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Start the practical examination":
            style "lecture_button"
            action Jump("Tutorial")
        textbutton "Leave the guild":
            style "lecture_button"
            action Jump("Tutorial")
        
label Tutorial:
    scene bg_old 
    show screen angelika_speech3()
    show screen angelika_speech_bg()
    show screen angelika_angelika()
    if angelika_speech_text_count == 0:
        $ tutorial_backbutton = "buttons/demo_noback_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_noback_button_hover.webp"
        $ speakcolor = "#8B0A50"
    else:
        $ tutorial_backbutton = "buttons/demo_back_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_back_button_hover.webp"
    if angelika_speech_text_count == 1:
        python:
            name = renpy.input("My name is... (Keep this shorter than 14 character.)", length=13)
            name = name.strip()
            if name != "":
                mc = name
        $ speakcolor = "#191970"
    if angelika_speech_text_count == 2:
        $ speakcolor = "#000000"
        show screen angelika_speech2()
    else:
        hide screen angelika_speech2
    if angelika_speech_text_count == 3:
        $ speakcolor = "#8B0A50"
    if angelika_speech_text_count == 4:
        $ speakcolor = "#000000"
        hide screen angelika_speech3
        hide screen angelika_angelika
        show screen slaver_guild()
    call screen angelika_speech()

    return
label splashscreen:

    show screen warning_screen

    menu:
        "Yes, I am adult and I want to continue":
            $ result = "Accepted"
            hide screen warning_screen
            jump after_splash

        "Exit immediately":
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

##### Normal Start menu page code -rec3ks
####################################################
######### CHARACTER SELECTION
################################################################################################################
# hover imagen version, nice -rec3ks 


################################################################
#### main menu control page code -rec3ks
###########################################################


        
        
transform custom_position:
    xpos 0.23
    ypos 0.12
    xanchor 0 # idk this, i only know it works -rec3ks
    yanchor 0 # idk this, i only know it works -rec3ks
image maincontroltext = ParameterizedText(xalign=0.5, yalign=0.0) 


label home:
    
    "WIP"
    return
label mainControls:
    scene donotdelete
    show scroll_large
    show maincontroltext "{size=18}{color=#0000ff}        Controls in this game can be carried out solely with the help of the mouse. Interactive,\n clickable elements will turn your cursor into a hand and will hover the element.\n        Almost all actions are available from the central menu, but there are short cuts for\n most common ones. Orders for cooking, cleanig, bathing, sex milking, punishment and \n rewards can be issued with quick buttons under the character portraits (when correspon- \n ding actions are needed). You can set who will do cleaning and cooking with rules on your\n slave/assistant screen (click their portait or press {b}S{/b} or {b}A{/b} when at home) the big button \n with the image of an academic cap opens a list of training courses. You also can start a \n personal lesson by clicking a skill on the slave screen or order your assistant to teach a\n lesson via buttons on the side of the assitant screen.\n        Some choices are colered gray, which means that they are unavailable. The reason \n for this may be not meeting the requirements. Usually, you can click the grey text (or in \n menus hover over the small arrow in the lower left corner of the button icon) for more\n information.\n        When clickable left and right arrows are displayed, pressing{b} SPACE{/b} is usually \n equivalent to clicking the right arrow. Press {b}ESC{/b} to close some menus and exit some \n locations. At home, you can press{b} D {/b}to open the master screen.\n        Have a nice game!{/color}" at custom_position

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