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
default follow_story = False
default follow_story_count = 0
default mc_name_save ="rec3ks"
default customcheck = True
default customboxcheck = False
default mc_normal_selection_textdescription_value_index = 0
default custom_start_difficulty_selection_index_index = 1
default alltier_s = False
default custom_points = 0
default green_or_red = "#009900"
default difficult_sparks_mantain = True
default pre_characterOnlyNameIndex = 0
default buttonimage = ""
default buttonimage_hover = ""
# The game starts here.

########## Warning screen -rec3ks
###########################################################################
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



label Normal_Start:

    scene donotdelete
    show scroll_large
    call screen character_selection
label Normal_Start2:
    scene donotdelete
    show scroll_large
    
    # reassinign old variables
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
    $ faction_36 = mc_inicial_stats[mc][36]
    $ sparks_37 = mc_inicial_stats[mc][37]

    # reassining more variables  -rec3ks
    $ strength_textvalue_1 = mc_attribute["STRENGTH"][strength_value_1]
    $ personality_textvalue_2 = mc_attribute["PERSONALITY"][personality_value_2]
    $ allure_textvalue_3 = mc_attribute["ALLURE"][allure_value_3]
    $ libido_textvalue_4 = mc_attribute["LIBIDO"][libido_value_4]
    $ dominance_textvalue_5 = mc_attribute["DOMINANCE"][dominance_value_5]
    $ brand_reputation_textvalue_6 = mc_attribute["BRAND REPUTATION"][brand_reputation_value_6]
    $ guild_reputation_textvalue_7 = mc_attribute["GUILD REPUTATION"][guild_reputation_value_7]
    $ standard_of_living_textvalue_8 = mc_attribute["STANDARD OF LIVING"][standard_of_living_value_8]
    $ hygiene_textvalue_9 = mc_attribute["HYGIENE"][hygiene_value_9]
    $ mood_textvalue_10 = mc_attribute["MOOD"][mood_value_10]
    $ injuries_textvalue_11 = mc_attribute["INJURIES"][injuries_value_11]
    $ teaching_textvalue_12 = mc_attribute["TEACHING"][teaching_value_12]
    $ stewardship_textvalue_13 = mc_attribute["STEWARDSHIP"][stewardship_value_13]
    $ artistry_textvalue_14 = mc_attribute["ARTISTRY"][artistry_value_14]
    $ medic_textvalue_15 = mc_attribute["MEDIC"][medic_value_15]
    $ fighter_textvalue_16 = mc_attribute["FIGHTER"][fighter_value_16]
    $ magic_textvalue_17 = mc_attribute["MAGIC"][magic_value_17]
    $ flagellation_textvalue_18 = mc_attribute["FLAGELLATION"][flagellation_value_18]
    $ torture_textvalue_19 = mc_attribute["TORTURE"][torture_value_19]
    $ binding_textvalue_20 = mc_attribute["BINDING"][binding_value_20]
    $ petting_textvalue_21 = mc_attribute["PETTING"][petting_value_21]
    $ oral_sex_textvalue_22 = mc_attribute["ORAL SEX"][oral_sex_value_22]
    $ penetration_textvalue_23 = mc_attribute["PENETRATION"][penetration_value_23]
    $ fetishism_textvalue_24 = mc_attribute["FETISHISM"][fetishism_value_24]

    $ inicial_difficulty_textvalue = mc_inicial_stats[mc][38]
    $ inicial_difficulty_value = mc_inicial_stats[mc][39] 

    # defining new variables  
    ########
    $ display_name = mc_inicial_stats.get(mc, ["Error - Try restart your game"])[0]
    if mc_normal_selection_textdescription_value_index > 1:
        $ mc_normal_selection_textdescription_value_index = 0
    if -5 <= characterOnlyNameIndex <= 11:
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])
    elif characterOnlyNameIndex >= -5:
        $ characterOnlyNameIndex = 0
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])
    else:
        $ characterOnlyNameIndex = 6
        call screen character_selection2(charactersOnlyName[characterOnlyNameIndex], charactersOnlyName[characterOnlyNameIndex - 2])


label Custom_Start:
    scene donotdelete
    show scroll_large
    if customcheck:
        $ mc_name_save = mc
        $ mc ="Jack"
        $ reputation_value_1 = 0
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
        $ mc = mc_name_save
        $ customcheck = False
        # creating new temporal values
        $ namechange = False

  
    if alltier_s:
        $ reputation_value_1         = 5
        $ strength_value_1           = 6
        $ personality_value_2        = 6
        $ allure_value_3             = 6
        $ libido_value_4             = 6
        $ dominance_value_5          = 6
        $ brand_reputation_value_6   = 6
        $ guild_reputation_value_7   = 6
        $ standard_of_living_value_8 = 6
        $ hygiene_value_9            = 6
        $ mood_value_10              = 6
        $ injuries_value_11          = 6
        $ teaching_value_12          = 6
        $ stewardship_value_13       = 6
        $ artistry_value_14          = 6
        $ medic_value_15             = 6
        $ fighter_value_16           = 6
        $ magic_value_17             = 6
        $ flagellation_value_18      = 6
        $ torture_value_19           = 6
        $ binding_value_20           = 6
        $ petting_value_21           = 6
        $ oral_sex_value_22          = 6
        $ penetration_value_23       = 6
        $ fetishism_value_24         = 6
        $ sparks_37                  = 999999
        $ alltier_s                  = False
    if difficult_sparks_mantain:
        $ sparks_37 = custom_start_difficulty_selection[custom_start_difficulty_selection_index[custom_start_difficulty_selection_index_index]][1]
        $ difficult_sparks_mantain = False
    # creating new temporal values
    $ reputationstyle= 2
    # reassining variables  -rec3ks
    
    if follow_story_count % 2 == 1:
        $ buttonimage = "buttons/unsel_button.webp"
        $ buttonimage_hover = "buttons/unsel_button_hover.webp"
        $ follow_story = True
    else:
        $ buttonimage = "buttons/sel_button.webp"
        $ buttonimage_hover = "buttons/sel_button_hover.webp"
        $ follow_story = False
    #####################################
    $ strength_textvalue_1 = mc_attribute["STRENGTH"][strength_value_1]
    $ personality_textvalue_2 = mc_attribute["PERSONALITY"][personality_value_2]
    $ allure_textvalue_3 = mc_attribute["ALLURE"][allure_value_3]
    $ libido_textvalue_4 = mc_attribute["LIBIDO"][libido_value_4]
    $ dominance_textvalue_5 = mc_attribute["DOMINANCE"][dominance_value_5]
    $ brand_reputation_textvalue_6 = mc_attribute["BRAND REPUTATION"][brand_reputation_value_6]
    $ guild_reputation_textvalue_7 = mc_attribute["GUILD REPUTATION"][guild_reputation_value_7]
    $ standard_of_living_textvalue_8 = mc_attribute["STANDARD OF LIVING"][standard_of_living_value_8]
    $ hygiene_textvalue_9 = mc_attribute["HYGIENE"][hygiene_value_9]
    $ mood_textvalue_10 = mc_attribute["MOOD"][mood_value_10]
    $ injuries_textvalue_11 = mc_attribute["INJURIES"][injuries_value_11]
    $ teaching_textvalue_12 = mc_attribute["TEACHING"][teaching_value_12]
    $ stewardship_textvalue_13 = mc_attribute["STEWARDSHIP"][stewardship_value_13]
    $ artistry_textvalue_14 = mc_attribute["ARTISTRY"][artistry_value_14]
    $ medic_textvalue_15 = mc_attribute["MEDIC"][medic_value_15]
    $ fighter_textvalue_16 = mc_attribute["FIGHTER"][fighter_value_16]
    $ magic_textvalue_17 = mc_attribute["MAGIC"][magic_value_17]
    $ flagellation_textvalue_18 = mc_attribute["FLAGELLATION"][flagellation_value_18]
    $ torture_textvalue_19 = mc_attribute["TORTURE"][torture_value_19]
    $ binding_textvalue_20 = mc_attribute["BINDING"][binding_value_20]
    $ petting_textvalue_21 = mc_attribute["PETTING"][petting_value_21]
    $ oral_sex_textvalue_22 = mc_attribute["ORAL SEX"][oral_sex_value_22]
    $ penetration_textvalue_23 = mc_attribute["PENETRATION"][penetration_value_23]
    $ fetishism_textvalue_24 = mc_attribute["FETISHISM"][fetishism_value_24]
    $ reputation_textvalue_1 = mc_attribute["REPUTATION"][reputation_value_1]
    $ custom_difficulty_textvalue = custom_start_difficulty_selection[custom_start_difficulty_selection_index[custom_start_difficulty_selection_index_index]][0]
    $ custom_points = custom_start_difficulty_selection[custom_start_difficulty_selection_index[custom_start_difficulty_selection_index_index]][2]
    $ custom_points = custom_points - custom_skill_cost_value[strength_value_1] - custom_skill_cost_value[personality_value_2] - custom_skill_cost_value[allure_value_3] - custom_skill_cost_value[libido_value_4] - custom_skill_cost_value[dominance_value_5] - custom_skill_cost_value[brand_reputation_value_6] - custom_skill_cost_value[guild_reputation_value_7] - custom_skill_cost_value[standard_of_living_value_8] - custom_skill_cost_value[hygiene_value_9] - custom_skill_cost_value[mood_value_10] - custom_skill_cost_value[injuries_value_11] - custom_skill_cost_value[teaching_value_12] - custom_skill_cost_value[stewardship_value_13] - custom_skill_cost_value[artistry_value_14] - custom_skill_cost_value[medic_value_15] - custom_skill_cost_value[fighter_value_16] - custom_skill_cost_value[magic_value_17] - custom_skill_cost_value[flagellation_value_18] - custom_skill_cost_value[torture_value_19] - custom_skill_cost_value[binding_value_20] - custom_skill_cost_value[petting_value_21] - custom_skill_cost_value[oral_sex_value_22] - custom_skill_cost_value[penetration_value_23] - custom_skill_cost_value[fetishism_value_24] - custom_skill_cost_value[reputation_value_1] - int((sparks_37 - custom_start_difficulty_selection[custom_start_difficulty_selection_index[custom_start_difficulty_selection_index_index]][1])/10)
    $ characterOnlyNameIndex = pre_characterOnlyNameIndex % 12
    if custom_points < 0:
        $ green_or_red = "#CD0000"
    else:
        $ green_or_red = "#009900"
    if namechange == True:
        python:
            name = renpy.input("Give your character a name. Keep this shorter than 14 character.", length=13)
            name = name.strip()
            if name != "":
                mc = name
        $ namechange = False
    if custom_start_difficulty_selection_index_index == 0:
        show screen s_tier_button
        hide screen points_tier_text
        if reputationstyle + reputation_value_1 == 7:
            $ reputationstyle = 3
    else:
        hide screen s_tier_button
        show screen points_tier_text
        if reputation_value_1 > 4:
            $ reputation_value_1 = 4
            $ reputation_textvalue_1 = mc_attribute["REPUTATION"][reputation_value_1]
            $ mc_normal_selection_textdescription_value = "WHITE TOWN"
            show screen custom_value_information

    if customboxcheck:
        show screen custom_selection
        call screen custom_value_information
    call screen custom_selection()
################################################################
#### main menu control page code -rec3ks
###########################################################
screen custom_value_information():
    zorder 1
    add "gui/confirm_frame.png" at truecenter

    text mc_normal_selection_textdescription[mc_normal_selection_textdescription_value][mc_normal_selection_textdescription_value_index]:
        pos (0.33, 0.28)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"

    text " Press space to close this window.":
        pos (0.33, 0.65)
        color "#191970"
        size 14
        font "fonts/Segoe Print.ttf"

    imagebutton:
        idle "buttons/ok-icon.webp" pos (0.5, 0.7)
        hover "buttons/ok-icon_hover.webp"
        action Hide("custom_value_information"),SetVariable("customboxcheck", False)

    key "K_SPACE" action Hide("custom_value_information"),SetVariable("customboxcheck", False)

screen s_tier_button():
    zorder 2
    imagebutton:
        idle "buttons/teach_s.webp" pos (0.29, 0.35)
        hover "buttons/teach_s_hover.webp"
        action SetVariable("alltier_s", True),Jump("Custom_Start")
screen points_tier_text():
    zorder 3
    vbox:
        xpos 0.65
        ypos 0.13
        xanchor 0.5
        yanchor 0.0
        text "Points:":
            size 42
            color "000000"
            font "fonts/Victoriana.ttf"
            yalign 0.5
            xalign 0.5            
        text str(custom_points):
            size 42
            color green_or_red
            font "fonts/Victoriana.ttf"
            yalign 0.5
            xalign 0.5
        text "APPEARANCE":
            size 45
            color "000000"
            font "fonts/Victoriana.ttf"
            yalign 0.5
            xalign 0.5
        add "spacer" size (0, 5)
        add custom_character_selection[charactersOnlyName[characterOnlyNameIndex]][0] at truecenter          
        add "spacer" size (0, 5)
        text "{u}Ignore story:{u}":
            size 17
            color "000000"
            font "fonts/segoe print.ttf"
            yalign 0.5
            xalign 0.3
        add "spacer" size (0, -7.5)
        text "{u}CUSTOMIZATION COST:{/u}":
            color "000000"
            size 17
            font "fonts/segoe print.ttf"
            yalign 0.5
            xalign 0.5
        text "Perfection      160 pnts":
            color "996515"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Astonishing     80  pnts":
            color "009900"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Excellent         40  pnts":
            color "009FEF"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Good              20  pnts":
            color "0000D8"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Mediocre         10  pnts":
            color "6B0084"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Bad                5   pnts":
            color "EA0090"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
        text "Awful              0   pnts":
            color "CD0000"
            font "fonts/segoe print.ttf"
            size 16
            yalign 0.0
            xalign 0.0
    imagebutton:
        idle buttonimage pos (0.69, 0.55)
        hover buttonimage_hover
        action SetVariable("follow_story_count", follow_story_count+1), Jump("Custom_Start")
    imagebutton:
        idle "buttons/forward_button.webp" pos (0.725,0.265 )
        hover "buttons/forward_button_hover.webp"
        action [
            SetVariable("pre_characterOnlyNameIndex",pre_characterOnlyNameIndex +1),
            Jump("Custom_Start")
        ]
    imagebutton:
        idle "buttons/back_button.webp" pos (0.535, 0.265)
        hover "buttons/back_button_hover.webp"
        action [
            SetVariable("pre_characterOnlyNameIndex",pre_characterOnlyNameIndex -1),
            Jump("Custom_Start")
        ]
screen custom_selection():
    zorder 0

    hbox:
        xpos 0.5
        ypos 0.015
        xanchor 0.5
        yanchor 0.0

        text "Difficulty:":
            size 48
            color "000000"
            font "fonts/Victoriana.ttf"
            yalign 0.5

        imagebutton:
            idle "buttons/Minus.webp"
            hover "buttons/Minus_hover.webp"
            action (
                SetVariable("difficult_sparks_mantain", True),
                SetVariable("custom_start_difficulty_selection_index_index", max(custom_start_difficulty_selection_index_index - 1, 0)),
                Jump("Custom_Start")
)            yalign 0.5
        text custom_difficulty_textvalue:
            size 48
            color "000000"
            font "fonts/Victoriana.ttf"
            yalign 0.5
        imagebutton:
            idle "buttons/Plus.webp"
            hover "buttons/Plus_hover.webp"
            action (
                SetVariable("difficult_sparks_mantain", True),
                SetVariable("custom_start_difficulty_selection_index_index", min(custom_start_difficulty_selection_index_index + 1, 2)),
                Jump("Custom_Start")
)            yalign 0.5
    hbox:
        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 0.0

        text "Sparks:":
            size 48
            color "000000"
            font "fonts/Victoriana.ttf"
            yalign 0.5

        imagebutton:
            idle "buttons/Minus.webp"
            hover "buttons/Minus_hover.webp"
            action SetVariable("sparks_37",max(sparks_37-100,200)), Jump("Custom_Start")
            yalign 0.5
        text str(sparks_37):
            size 30
            color "0000ff"
            font "fonts/Victoriana.ttf"
            yalign 0.5
        imagebutton:
            idle "buttons/Plus.webp"
            hover "buttons/Plus_hover.webp"
            action SetVariable("sparks_37",min(sparks_37+100,custom_selection_max_cap_sparks[custom_start_difficulty_selection_index_index])), Jump("Custom_Start")
            yalign 0.5
        
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 360 
        ypos 115 

        textbutton reputation_textvalue_1:
            style "attribute_button_custom" + str(reputation_value_1 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "REPUTATION")

        textbutton strength_textvalue_1:
            style "attribute_button_custom" + str(strength_value_1 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "STRENGTH")

        textbutton personality_textvalue_2:
            style "attribute_button_custom" + str(personality_value_2 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "PERSONALITY")

        textbutton libido_textvalue_4:
            style "attribute_button_custom" + str(libido_value_4 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "LIBIDO")

        textbutton dominance_textvalue_5:
            style "attribute_button_custom" + str(dominance_value_5 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "DOMINANCE")

        add "spacer" size (0, 35)

        textbutton teaching_textvalue_12:
            style "attribute_button_custom" + str(teaching_value_12 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "TEACHING")

        textbutton stewardship_textvalue_13:
            style "attribute_button_custom" + str(stewardship_value_13 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "STEWARDSHIP")

        textbutton artistry_textvalue_14:
            style "attribute_button_custom" + str(artistry_value_14 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "ARTISTRY")

        textbutton medic_textvalue_15:
            style "attribute_button_custom" + str(medic_value_15 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "MEDIC")

        textbutton fighter_textvalue_16:
            style "attribute_button_custom" + str(fighter_value_16 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "FIGHTER")

        textbutton magic_textvalue_17:
            style "attribute_button_custom" + str(magic_value_17 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "MAGIC")

        textbutton flagellation_textvalue_18:
            style "attribute_button_custom" + str(flagellation_value_18 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "FLAGELLATION")

        textbutton torture_textvalue_19:
            style "attribute_button_custom" + str(torture_value_19 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "TORTURE")

        textbutton binding_textvalue_20:
            style "attribute_button_custom" + str(binding_value_20 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "BINDING")

        add "spacer" size (0, 20)

        textbutton petting_textvalue_21:
            style "attribute_button_custom" + str(petting_value_21 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "PETTING")

        textbutton oral_sex_textvalue_22:
            style "attribute_button_custom" + str(oral_sex_value_22 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "ORAL SEX")

        textbutton penetration_textvalue_23:
            style "attribute_button_custom" + str(penetration_value_23 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "PENETRATION")

        textbutton fetishism_textvalue_24:
            style "attribute_button_custom" + str(fetishism_value_24 + 1)
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "FETISHISM")
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 290 
        ypos 115 

        textbutton "[[+]":
            style "attribute_button_custom" + str(reputation_value_1 + reputationstyle)
            action SetVariable("reputation_value_1", min(reputation_value_1 + 1, 5)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(strength_value_1 + 2)
            action SetVariable("strength_value_1", min(strength_value_1 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(personality_value_2 + 2)
            action SetVariable("personality_value_2", min(personality_value_2 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(libido_value_4 + 2)
            action SetVariable("libido_value_4", min(libido_value_4 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(dominance_value_5 + 2)
            action SetVariable("dominance_value_5", min(dominance_value_5 + 1, 6)), Jump("Custom_Start")

        add "spacer" size (0, 35)

        textbutton "[[+]":
            style "attribute_button_custom" + str(teaching_value_12 + 2)
            action SetVariable("teaching_value_12", min(teaching_value_12 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(stewardship_value_13 + 2)
            action SetVariable("stewardship_value_13", min(stewardship_value_13 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(artistry_value_14 + 2)
            action SetVariable("artistry_value_14", min(artistry_value_14 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(medic_value_15 + 2)
            action SetVariable("medic_value_15", min(medic_value_15 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(fighter_value_16 + 2)
            action SetVariable("fighter_value_16", min(fighter_value_16 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(magic_value_17 + 2)
            action SetVariable("magic_value_17", min(magic_value_17 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(flagellation_value_18 + 2)
            action SetVariable("flagellation_value_18", min(flagellation_value_18 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(torture_value_19 + 2)
            action SetVariable("torture_value_19", min(torture_value_19 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(binding_value_20 + 2)
            action SetVariable("binding_value_20", min(binding_value_20 + 1, 6)), Jump("Custom_Start")

        add "spacer" size (0, 20)

        textbutton "[[+]":
            style "attribute_button_custom" + str(petting_value_21 + 2)
            action SetVariable("petting_value_21", min(petting_value_21 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(oral_sex_value_22 + 2)
            action SetVariable("oral_sex_value_22", min(oral_sex_value_22 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(penetration_value_23 + 2)
            action SetVariable("penetration_value_23", min(penetration_value_23 + 1, 6)), Jump("Custom_Start")

        textbutton "[[+]":
            style "attribute_button_custom" + str(fetishism_value_24 + 2)
            action SetVariable("fetishism_value_24", min(fetishism_value_24 + 1, 6)), Jump("Custom_Start")
       
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing -1.5    # Spacing between all buttons
        xpos 328
        ypos 115 
       
        textbutton "[[-]":
            style "attribute_button_custom" + str(reputation_value_1),
            action SetVariable("reputation_value_1", max(reputation_value_1 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(strength_value_1),
            action SetVariable("strength_value_1", max(strength_value_1 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(personality_value_2),
            action SetVariable("personality_value_2", max(personality_value_2 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(libido_value_4),
            action SetVariable("libido_value_4", max(libido_value_4 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(dominance_value_5),
            action SetVariable("dominance_value_5", max(dominance_value_5 - 1, 0)), Jump("Custom_Start")

        # Adding extra spacing here:
        add "spacer" size (0, 35)

        textbutton "[[-]":
            style "attribute_button_custom" + str(teaching_value_12),
            action SetVariable("teaching_value_12", max(teaching_value_12 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(stewardship_value_13),
            action SetVariable("stewardship_value_13", max(stewardship_value_13 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(artistry_value_14),
            action SetVariable("artistry_value_14", max(artistry_value_14 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(medic_value_15),
            action SetVariable("medic_value_15", max(medic_value_15 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(fighter_value_16),
            action SetVariable("fighter_value_16", max(fighter_value_16 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(magic_value_17),
            action SetVariable("magic_value_17", max(magic_value_17 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(flagellation_value_18),
            action SetVariable("flagellation_value_18", max(flagellation_value_18 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(torture_value_19),
            action SetVariable("torture_value_19", max(torture_value_19 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(binding_value_20),
            action SetVariable("binding_value_20", max(binding_value_20 - 1, 0)), Jump("Custom_Start")

        add "spacer" size (0, 20)

        textbutton "[[-]":
            style "attribute_button_custom" + str(petting_value_21),
            action SetVariable("petting_value_21", max(petting_value_21 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(oral_sex_value_22),
            action SetVariable("oral_sex_value_22", max(oral_sex_value_22 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(penetration_value_23),
            action SetVariable("penetration_value_23", max(penetration_value_23 - 1, 0)), Jump("Custom_Start")

        textbutton "[[-]":
            style "attribute_button_custom" + str(fetishism_value_24),
            action SetVariable("fetishism_value_24", max(fetishism_value_24 - 1, 0)), Jump("Custom_Start")
    vbox:
        anchor (0.0, 0.0)
        xpos 315
        ypos 120
        spacing 1.12  # Adjusted for cleaner spacing

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"

        null height 35  # Spacer

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"

        null height 20  # Spacer

        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
        text "/" color "#000000"
    imagebutton:
        idle "buttons/close_button.webp" pos (997,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)
    hbox:
        pos (290, 85)
        spacing 2
        text "Name: [mc]" font "fonts/Segoe Print.ttf" color "#002BA7" size 16 yalign 0.5

        textbutton "[[change]":
            style "change_button"
            yalign 0.5
            action SetVariable("namechange", True), Jump("Custom_Start")
    vbox:
        xpos 290
        ypos 258
        textbutton "{u}SKILLS:{/u}":
            style "custom_information",
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "SKILLS")

        null height 230  # Spacer
        textbutton "{u}SEX TECHNIQUES:{/u}":
            style "custom_information",
            action Show("custom_value_information"), SetVariable("customboxcheck", True), SetVariable("mc_normal_selection_textdescription_value", "SEX TECHNIQUES")


        
        
transform custom_position:
    xpos 0.23
    ypos 0.12
    xanchor 0 # idk this, i only know it works -rec3ks
    yanchor 0 # idk this, i only know it works -rec3ks
image maincontroltext = ParameterizedText(xalign=0.5, yalign=0.0) 
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