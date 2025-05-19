default inicial_difficulty_textvalue =""
default inicial_difficulty_value = 0
default dic_mc_normal_selection_textdescription_value = "master_noble"
label Normal_Start:

    scene donotdelete
    show scroll_large
    call screen character_selection
label Normal_Start2:
    scene donotdelete
    show scroll_large
    
    # reassinign old variables
    $ characterOnlyNameIndex = characterOnlyNameIndex +1
    
    $ strength_value_1 = dic_mc_inicial_stats[mc][1]
    $ personality_value_2 = dic_mc_inicial_stats[mc][2]
    $ allure_value_3 = dic_mc_inicial_stats[mc][3]
    $ libido_value_4 = dic_mc_inicial_stats[mc][4]
    $ dominance_value_5 = dic_mc_inicial_stats[mc][5]
    $ brand_reputation_value_6 = dic_mc_inicial_stats[mc][6]
    $ guild_reputation_value_7 = dic_mc_inicial_stats[mc][7]
    $ standard_of_living_value_8 = dic_mc_inicial_stats[mc][8]
    $ hygiene_value_9 = dic_mc_inicial_stats[mc][9]
    $ mood_value_10 = dic_mc_inicial_stats[mc][10]
    $ injuries_value_11 = dic_mc_inicial_stats[mc][11]
    $ teaching_value_12 = dic_mc_inicial_stats[mc][12]
    $ stewardship_value_13 = dic_mc_inicial_stats[mc][13]
    $ artistry_value_14 = dic_mc_inicial_stats[mc][14]
    $ medic_value_15 = dic_mc_inicial_stats[mc][15]
    $ fighter_value_16 = dic_mc_inicial_stats[mc][16]
    $ magic_value_17 = dic_mc_inicial_stats[mc][17]
    $ flagellation_value_18 = dic_mc_inicial_stats[mc][18]
    $ torture_value_19 = dic_mc_inicial_stats[mc][19]
    $ binding_value_20 = dic_mc_inicial_stats[mc][20]
    $ petting_value_21 = dic_mc_inicial_stats[mc][21]
    $ oral_sex_value_22 = dic_mc_inicial_stats[mc][22]
    $ penetration_value_23 = dic_mc_inicial_stats[mc][23]
    $ fetishism_value_24 = dic_mc_inicial_stats[mc][24]
    $ faction_36 = dic_mc_inicial_stats[mc][36]
    $ sparks_37 = dic_mc_inicial_stats[mc][37]

    # reassining more variables  -rec3ks
    $ strength_textvalue_1 = dic_mc_attribute["STRENGTH"][strength_value_1]
    $ personality_textvalue_2 = dic_mc_attribute["PERSONALITY"][personality_value_2]
    $ allure_textvalue_3 = dic_mc_attribute["ALLURE"][allure_value_3]
    $ libido_textvalue_4 = dic_mc_attribute["LIBIDO"][libido_value_4]
    $ dominance_textvalue_5 = dic_mc_attribute["DOMINANCE"][dominance_value_5]
    $ brand_reputation_textvalue_6 = dic_mc_attribute["BRAND REPUTATION"][brand_reputation_value_6]
    $ guild_reputation_textvalue_7 = dic_mc_attribute["GUILD REPUTATION"][guild_reputation_value_7]
    $ standard_of_living_textvalue_8 = dic_mc_attribute["STANDARD OF LIVING"][standard_of_living_value_8]
    $ hygiene_textvalue_9 = dic_mc_attribute["HYGIENE"][hygiene_value_9]
    $ mood_textvalue_10 = dic_mc_attribute["MOOD"][mood_value_10]
    $ injuries_textvalue_11 = dic_mc_attribute["INJURIES"][injuries_value_11]
    $ teaching_textvalue_12 = dic_mc_attribute["TEACHING"][teaching_value_12]
    $ stewardship_textvalue_13 = dic_mc_attribute["STEWARDSHIP"][stewardship_value_13]
    $ artistry_textvalue_14 = dic_mc_attribute["ARTISTRY"][artistry_value_14]
    $ medic_textvalue_15 = dic_mc_attribute["MEDIC"][medic_value_15]
    $ fighter_textvalue_16 = dic_mc_attribute["FIGHTER"][fighter_value_16]
    $ magic_textvalue_17 = dic_mc_attribute["MAGIC"][magic_value_17]
    $ flagellation_textvalue_18 = dic_mc_attribute["FLAGELLATION"][flagellation_value_18]
    $ torture_textvalue_19 = dic_mc_attribute["TORTURE"][torture_value_19]
    $ binding_textvalue_20 = dic_mc_attribute["BINDING"][binding_value_20]
    $ petting_textvalue_21 = dic_mc_attribute["PETTING"][petting_value_21]
    $ oral_sex_textvalue_22 = dic_mc_attribute["ORAL SEX"][oral_sex_value_22]
    $ penetration_textvalue_23 = dic_mc_attribute["PENETRATION"][penetration_value_23]
    $ fetishism_textvalue_24 = dic_mc_attribute["FETISHISM"][fetishism_value_24]

    $ inicial_difficulty_textvalue = dic_mc_inicial_stats[mc][38]
    $ inicial_difficulty_value = dic_mc_inicial_stats[mc][39] 

    # defining new variables  
    ########
    $ display_name = dic_mc_inicial_stats.get(mc, ["Error - Try restart your game"])[0]
    if start:
        hide scroll_large
        jump Home
    if dic_mc_normal_selection_textdescription_value_index > 1:
        $ dic_mc_normal_selection_textdescription_value_index = 0
    if -5 <= characterOnlyNameIndex <= 11:
        call screen character_selection2(dic_charactersOnlyName[characterOnlyNameIndex], dic_charactersOnlyName[characterOnlyNameIndex - 2])
    elif characterOnlyNameIndex >= -5:
        $ characterOnlyNameIndex = 0
        call screen character_selection2(dic_charactersOnlyName[characterOnlyNameIndex], dic_charactersOnlyName[characterOnlyNameIndex - 2])
    else:
        $ characterOnlyNameIndex = 6
        call screen character_selection2(dic_charactersOnlyName[characterOnlyNameIndex], dic_charactersOnlyName[characterOnlyNameIndex - 2])

screen character_selection():
    text "SELECT YOUR CHARACTER" color "#000000" pos (520, 60) font "fonts/Segoe Print.ttf" size 17 bold True

    # List of character data (name, image path, hover image path)

    grid 4 3:
        xalign 0.5
        yalign 0.5
        spacing 20

        # Loop through the list of characters to generate buttons dynamically
        for char in dic_characters:
            imagebutton:
                idle char[1]
                hover char[2]
                action [SetVariable("mc", char[0]),SetVariable("characterOnlyNameIndex",char[3]),SetVariable("dic_mc_normal_selection_textdescription_value",char[0]),Jump("Normal_Start2")]

    imagebutton:
        idle "buttons/close_button.webp" pos (983,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)



screen character_selection2(x,y):

    text dic_mc_inicial_stats[mc][40] size 15 pos (765, 230) anchor(0.5,0.5) font "fonts/victoriana.ttf" color "000000"

    textbutton display_name pos (0.60, 0.19) anchor (0.5, 0.5):
        style "display_mc_name"
        action SetVariable("dic_mc_normal_selection_textdescription_value","MC NAME"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0), Jump("Normal_Start2")
        
    textbutton inicial_difficulty_textvalue pos (765, 195) anchor(0.5,0.5):
        style "difficulty_button" + str(inicial_difficulty_value)
        action SetVariable("dic_mc_normal_selection_textdescription_value",inicial_difficulty_textvalue), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0), Jump("Normal_Start2")

    imagebutton:
        idle "buttons/close_button.webp" pos (983,12)
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
            SetVariable("dic_mc_normal_selection_textdescription_value",dic_charactersOnlyName[characterOnlyNameIndex]),
            Jump("Normal_Start2")
        ]
    imagebutton:
        idle "buttons/back_button.webp" pos (265, 665)
        hover "buttons/back_button_hover.webp"
        action [
            ##### this is a genius idea  -rec3ks
            SetVariable("mc",y),
            SetVariable("characterOnlyNameIndex",characterOnlyNameIndex - 2),
            SetVariable("dic_mc_normal_selection_textdescription_value",dic_charactersOnlyName[characterOnlyNameIndex-2]),
            Jump("Normal_Start2")
        ]
    imagebutton:
        idle "buttons/auk_fwrd.webp" pos (950, 580)
        hover "buttons/auk_fwrd_hover.webp"
        action [
            SetVariable("dic_mc_normal_selection_textdescription_value",mc),
            SetVariable("dic_mc_normal_selection_textdescription_value_index",dic_mc_normal_selection_textdescription_value_index+1),
            Jump("Normal_Start2")
        ]
    imagebutton:
        idle "buttons/approve_small.webp" pos (0.5, 0.95) anchor (0.5, 0.5)
        hover "buttons/approve_small_hover.webp"
        action SetVariable("start", True), Jump("Normal_Start2")
    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing 2.5    # Spacing between all buttons
        xpos 310 
        ypos 250  

        add "spacer" size (0,15)  # Create an invisible spacer with 30px height
    
        textbutton strength_textvalue_1:
            style "attribute_button" + str(strength_value_1)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "STRENGTH"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton personality_textvalue_2:
            style "attribute_button" + str(personality_value_2)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "PERSONALITY"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton libido_textvalue_4:
            style "attribute_button" + str(libido_value_4)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "LIBIDO"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton dominance_textvalue_5:
            style "attribute_button" + str(dominance_value_5)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "DOMINANCE"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        add "spacer" size (0, 20)

        textbutton teaching_textvalue_12:
            style "attribute_button" + str(teaching_value_12)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "TEACHING"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton stewardship_textvalue_13:
            style "attribute_button" + str(stewardship_value_13)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "STEWARDSHIP"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton artistry_textvalue_14:
            style "attribute_button" + str(artistry_value_14)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "ARTISTRY"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton medic_textvalue_15:
            style "attribute_button" + str(medic_value_15)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "MEDIC"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton fighter_textvalue_16:
            style "attribute_button" + str(fighter_value_16)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "FIGHTER"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton magic_textvalue_17:
            style "attribute_button" + str(magic_value_17)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "MAGIC"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton flagellation_textvalue_18:
            style "attribute_button" + str(flagellation_value_18)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "FLAGELLATION"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton torture_textvalue_19:
            style "attribute_button" + str(torture_value_19)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "TORTURE"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton binding_textvalue_20:
            style "attribute_button" + str(binding_value_20)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "BINDING"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton petting_textvalue_21:
            style "attribute_button" + str(petting_value_21)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "PETTING"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton oral_sex_textvalue_22:
            style "attribute_button" + str(oral_sex_value_22)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "ORAL SEX"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton penetration_textvalue_23:
            style "attribute_button" + str(penetration_value_23)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "PENETRATION"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

        textbutton fetishism_textvalue_24:
            style "attribute_button" + str(fetishism_value_24)
            action SetVariable("dic_mc_normal_selection_textdescription_value", "FETISHISM"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)


    text dic_mc_normal_selection_textdescription[dic_mc_normal_selection_textdescription_value][dic_mc_normal_selection_textdescription_value_index]:
        pos(0.42,0.37)
        color "#191970"
        size 15
        font "fonts/Segoe Print.ttf"

    textbutton " Faction: [faction_36]":
        pos (0.42, 0.80)
        style "simpletext"
        action SetVariable("dic_mc_normal_selection_textdescription_value","FACTION"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)

    textbutton " Sparks: [sparks_37]":
        pos (0.42, 0.84)
        style "simpletext"
        action SetVariable("dic_mc_normal_selection_textdescription_value","SPARKS"), SetVariable("dic_mc_normal_selection_textdescription_value_index", 0)