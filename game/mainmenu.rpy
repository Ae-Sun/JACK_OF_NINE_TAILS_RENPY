screen warning_screen():
    text "Warning!!!"pos (485, 0) size 72 color "ff0000"
    text "         This game contains explicit scenes of sex, extreme violence \n and other shocking content, and therefore it can not be \n recommended to anyone at all. Continuing the game, you confirm \n that you have read this warning and you are an adult. \n         This program is freely available for download and \n distribution and is not a commercial product. All rights for the graphics \n and music are copyrighted by their respective owners. \n These materials have been found in the public domain and are used \n solely for the purpose of parody. \n         Game source code is open, you are free to distribute and \n modify it while keeping this warning and information from the \n 'Credits'" pos(100,100) size 36 color "#ff0000"
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
                action [SetVariable("mc", char[0]),SetVariable("characterOnlyNameIndex",char[3]),SetVariable("mc_normal_selection_textdescription_value",char[0]),Jump("Normal_Start2")]

    imagebutton:
        idle "buttons/close_button.webp" pos (997,12)
        hover "buttons/close_button_hover.webp"
        action MainMenu(confirm=False)



screen character_selection2(x,y):

    textbutton display_name pos (0.60, 0.19) anchor (0.5, 0.5):
        style "display_mc_name"
        action SetVariable("mc_normal_selection_textdescription_value","MC NAME"), Jump("Normal_Start2")
        
    textbutton inicial_difficulty_textvalue pos (765, 195) anchor(0.5,0.5):
        style "difficulty_button" + str(inicial_difficulty_value)
        action Jump("Normal_Start2")

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
            SetVariable("mc_normal_selection_textdescription_value",charactersOnlyName[characterOnlyNameIndex]),
            Jump("Normal_Start2")
        ]
    imagebutton:
        idle "buttons/back_button.webp" pos (265, 665)
        hover "buttons/back_button_hover.webp"
        action [
            ##### this is a genius idea  -rec3ks
            SetVariable("mc",y),
            SetVariable("characterOnlyNameIndex",characterOnlyNameIndex - 2),
            SetVariable("mc_normal_selection_textdescription_value",charactersOnlyName[characterOnlyNameIndex-2]),
            Jump("Normal_Start2")
        ]

    vbox:
        anchor (0.0, 0.0)  # Aligns the anchor to the top-left corner
        spacing 2.5    # Spacing between all buttons
        xpos 310 
        ypos 250  

        add "spacer" size (0,15)  # Create an invisible spacer with 30px height
    
        textbutton strength_textvalue_1:
            style "attribute_button" + str(strength_value_1),
            action SetVariable("mc_normal_selection_textdescription_value","STRENGTH"), Jump("Normal_Start2")

        textbutton personality_textvalue_2:
            style "attribute_button" + str(personality_value_2),
            action SetVariable("mc_normal_selection_textdescription_value","PERSONALITY"), Jump("Normal_Start2")

        textbutton libido_textvalue_4:
            style "attribute_button" + str(libido_value_4),
            action SetVariable("mc_normal_selection_textdescription_value","LIBIDO"), Jump("Normal_Start2")

        textbutton dominance_textvalue_5:
            style "attribute_button" + str(dominance_value_5),
            action SetVariable("mc_normal_selection_textdescription_value","DOMINANCE"), Jump("Normal_Start2")

        # Adding extra spacing here:
        add "spacer" size (0, 20)

        textbutton teaching_textvalue_12:
            style "attribute_button" + str(teaching_value_12),
            action SetVariable("mc_normal_selection_textdescription_value","TEACHING"), Jump("Normal_Start2")

        textbutton stewardship_textvalue_13:
            style "attribute_button" + str(stewardship_value_13),
            action SetVariable("mc_normal_selection_textdescription_value","STEWARDSHIP"), Jump("Normal_Start2")

        textbutton artistry_textvalue_14:
            style "attribute_button" + str(artistry_value_14),
            action SetVariable("mc_normal_selection_textdescription_value","ARTISTRY"), Jump("Normal_Start2")

        textbutton medic_textvalue_15:
            style "attribute_button" + str(medic_value_15),
            action SetVariable("mc_normal_selection_textdescription_value","MEDIC"), Jump("Normal_Start2")

        textbutton fighter_textvalue_16:
            style "attribute_button" + str(fighter_value_16),
            action SetVariable("mc_normal_selection_textdescription_value","FIGHTER"), Jump("Normal_Start2")

        textbutton magic_textvalue_17:
            style "attribute_button" + str(magic_value_17),
            action SetVariable("mc_normal_selection_textdescription_value","MAGIC"), Jump("Normal_Start2")

        textbutton flagellation_textvalue_18:
            style "attribute_button" + str(flagellation_value_18),
            action SetVariable("mc_normal_selection_textdescription_value","FLAGELLATION"), Jump("Normal_Start2")

        textbutton torture_textvalue_19:
            style "attribute_button" + str(torture_value_19),
            action SetVariable("mc_normal_selection_textdescription_value","TORTURE"), Jump("Normal_Start2")

        textbutton binding_textvalue_20:
            style "attribute_button" + str(binding_value_20),
            action SetVariable("mc_normal_selection_textdescription_value","BINDING"), Jump("Normal_Start2")

        textbutton petting_textvalue_21:
            style "attribute_button" + str(petting_value_21),
            action SetVariable("mc_normal_selection_textdescription_value","PETTING"), Jump("Normal_Start2")

        textbutton oral_sex_textvalue_22:
            style "attribute_button" + str(oral_sex_value_22),
            action SetVariable("mc_normal_selection_textdescription_value","ORAL SEX"), Jump("Normal_Start2")

        textbutton penetration_textvalue_23:
            style "attribute_button" + str(penetration_value_23),
            action SetVariable("mc_normal_selection_textdescription_value","PENETRATION"), Jump("Normal_Start2")

        textbutton fetishism_textvalue_24:
            style "attribute_button" + str(fetishism_value_24),
            action SetVariable("mc_normal_selection_textdescription_value","FETISHISM"), Jump("Normal_Start2")

    # Fallback name if mc is not recognized

    text mc_normal_selection_textdescription[mc_normal_selection_textdescription_value][0]:
        pos(0.42,0.37)
        color "#191970"
        size 16
        font "fonts/Segoe Print.ttf"

    textbutton " Faction: [mc_inicial_stats[mc][36]]":
        pos (0.42, 0.80)
        style "simpletext"
        action NullAction()

    textbutton " Sparks: [mc_inicial_stats[mc][37]]":
        pos (0.42, 0.84)
        style "simpletext"
        action NullAction()