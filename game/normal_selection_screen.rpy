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

    text mc_inicial_stats[mc][40] size 15 pos (765, 230) anchor(0.5,0.5) font "fonts/Victoriana.ttf" color "000000"

    textbutton display_name pos (0.60, 0.19) anchor (0.5, 0.5):
        style "display_mc_name"
        action SetVariable("mc_normal_selection_textdescription_value","MC NAME"), Jump("Normal_Start2")
        
    textbutton inicial_difficulty_textvalue pos (765, 195) anchor(0.5,0.5):
        style "difficulty_button" + str(inicial_difficulty_value)
        action SetVariable("mc_normal_selection_textdescription_value",inicial_difficulty_textvalue), Jump("Normal_Start2")

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
    imagebutton:
        idle "buttons/auk_fwrd.webp" pos (960, 580)
        hover "buttons/auk_fwrd_hover.webp"
        action [
            SetVariable("mc_normal_selection_textdescription_value",mc),
            SetVariable("mc_normal_selection_textdescription_value_index",mc_normal_selection_textdescription_value_index+1),
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
            action SetVariable("mc_normal_selection_textdescription_value", "STRENGTH")

        textbutton personality_textvalue_2:
            style "attribute_button" + str(personality_value_2)
            action SetVariable("mc_normal_selection_textdescription_value", "PERSONALITY")

        textbutton libido_textvalue_4:
            style "attribute_button" + str(libido_value_4)
            action SetVariable("mc_normal_selection_textdescription_value", "LIBIDO")

        textbutton dominance_textvalue_5:
            style "attribute_button" + str(dominance_value_5)
            action SetVariable("mc_normal_selection_textdescription_value", "DOMINANCE")

        add "spacer" size (0, 20)

        textbutton teaching_textvalue_12:
            style "attribute_button" + str(teaching_value_12)
            action SetVariable("mc_normal_selection_textdescription_value", "TEACHING")

        textbutton stewardship_textvalue_13:
            style "attribute_button" + str(stewardship_value_13)
            action SetVariable("mc_normal_selection_textdescription_value", "STEWARDSHIP")

        textbutton artistry_textvalue_14:
            style "attribute_button" + str(artistry_value_14)
            action SetVariable("mc_normal_selection_textdescription_value", "ARTISTRY")

        textbutton medic_textvalue_15:
            style "attribute_button" + str(medic_value_15)
            action SetVariable("mc_normal_selection_textdescription_value", "MEDIC")

        textbutton fighter_textvalue_16:
            style "attribute_button" + str(fighter_value_16)
            action SetVariable("mc_normal_selection_textdescription_value", "FIGHTER")

        textbutton magic_textvalue_17:
            style "attribute_button" + str(magic_value_17)
            action SetVariable("mc_normal_selection_textdescription_value", "MAGIC")

        textbutton flagellation_textvalue_18:
            style "attribute_button" + str(flagellation_value_18)
            action SetVariable("mc_normal_selection_textdescription_value", "FLAGELLATION")

        textbutton torture_textvalue_19:
            style "attribute_button" + str(torture_value_19)
            action SetVariable("mc_normal_selection_textdescription_value", "TORTURE")

        textbutton binding_textvalue_20:
            style "attribute_button" + str(binding_value_20)
            action SetVariable("mc_normal_selection_textdescription_value", "BINDING")

        textbutton petting_textvalue_21:
            style "attribute_button" + str(petting_value_21)
            action SetVariable("mc_normal_selection_textdescription_value", "PETTING")

        textbutton oral_sex_textvalue_22:
            style "attribute_button" + str(oral_sex_value_22)
            action SetVariable("mc_normal_selection_textdescription_value", "ORAL SEX")

        textbutton penetration_textvalue_23:
            style "attribute_button" + str(penetration_value_23)
            action SetVariable("mc_normal_selection_textdescription_value", "PENETRATION")

        textbutton fetishism_textvalue_24:
            style "attribute_button" + str(fetishism_value_24)
            action SetVariable("mc_normal_selection_textdescription_value", "FETISHISM")


    text mc_normal_selection_textdescription[mc_normal_selection_textdescription_value][mc_normal_selection_textdescription_value_index]:
        pos(0.42,0.37)
        color "#191970"
        size 16
        font "fonts/Segoe Print.ttf"

    textbutton " Faction: [faction_36]":
        pos (0.42, 0.80)
        style "simpletext"
        action SetVariable("mc_normal_selection_textdescription_value","FACTION")

    textbutton " Sparks: [sparks_37]":
        pos (0.42, 0.84)
        style "simpletext"
        action SetVariable("mc_normal_selection_textdescription_value","SPARKS")