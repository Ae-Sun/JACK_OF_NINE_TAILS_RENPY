default bgstyle = "bg_main_old.webp"
default bgstyle2 = "bg_old.webp"
default bgstyle3 = "bg_stat_old.webp"
default home_decoration = "bg/interiors/slum_study_large.webp"
default home_decoration_mini = "bg/interiors/slum_study.webp"
default home_menu_image1 = "ui overhaul/activity.webp"
default home_menu_image2 = "ui overhaul/slave_assignments.webp"
default home_menu_image3 = "ui overhaul/domestic_issues.webp"
default home_menu_image4 = "ui overhaul/cast_spell.webp"
default home_menu_image5 = "ui overhaul/assistant_assignments.webp"
default home_menu_image6 = "ui overhaul/end_day.webp"
default energy_image1 = "ui overhaul/energy/energy_green.webp"
default energy_image2 = "ui overhaul/energy/energy_green_half.webp"
default dic_spellbook_info_index = "default"
default mc_image = ""
default mc_image2 = ""
default text_slave_conditions_index = "default"
default next_day_check = True
default is_main_slave = False
default show_main_slave = False
default is_assistant_assigned = False
default energy_value = 0
default current_menu = 0
default mood_value = 0
default number_of_rules = 0
default day_tracker = 1
default boobs1 =" marshmallowy tits"
default boobs2 =" motherly breasts"
default boobs3 =" empty breast-sacks"
default boobs4 =" round tits"
default boobs5 =" firm melons"
default boobs6 =" shapely balloons"


label iniciation_label:
    if is_tutorial == True:
        $mc_image = "master/master_noble.webp"
        $ all_girls_list[girl_index]["day_bought"] = day_tracker
        if current_menu == 0:
            show screen goguild()
        else:
            hide screen goguild
    else:
        if is_normal_start == True:
            $mc_image = dic_custom_character_selection[mc][0]
        else:
            $mc_image = dic_custom_character_selection[dic_charactersOnlyName[characterOnlyNameIndex]][0]
    $ mc_image2 = mc_image.replace(".webp", "_hover.webp")
    jump Home


label Home:
    show screen bg_home()
    $ infobox_jump = "Home"
    if next_day_check:
        $ energy_value = strength_value_1 *2 + 2
        if girl_index in all_girls_list:
            $ all_girls_list[girl_index]["energy"] = all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2
            $ is_main_slave = True
        $ next_day_check = False
    if show_main_slave:
        show screen main_slave_image() 

    show screen home_attributes_menu()
    show screen sparks_menu()
    if customboxcheck:
        hide screen tutorial_description
        hide screen tutorial_description2
        hide screen tutorial_descriptionphysical
        show screen tutorial_attribute()
    if attribute_checkbox:
        if attributeisphysical:
            show screen tutorial_descriptionphysical()
        else:
            show screen tutorial_description()
        hide screen tutorial_attribute
    ### this may look stupid, but it's not. Think how back feature works in renpy. -rec3ks
    if current_menu == 0:
        $ show_main_slave = False
        hide screen main_slave_image
        hide screen screen_rules
        call screen home_menu()
    elif current_menu == 1:
        call screen slave_activities_menu()
    elif current_menu == 2:
        call screen slave_assignments_menu()
    elif current_menu == 3:
        call screen domestic_issues_menu()
    elif current_menu == 4:
        call screen cast_spell_menu()
    elif current_menu == 41:
        call screen spellbook_info()
    elif current_menu == 100:
        hide screen goguild
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_rules_menu()
    elif current_menu == 101:
        hide screen goguild
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_anatomy_menu()
    elif current_menu == 102:
        hide screen goguild
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_equipment_menu()
    elif current_menu == 103:
        hide screen goguild
        hide screen sparks_menu
        hide screen home_attributes_menu
        show screen screen_rules
        call screen slave_aura_menu()
screen main_slave_image():
    add all_girls_list[girl_index]["fullimage"] + ".webp" xalign 0.2 yalign 0.9999 size(795,535)

screen goguild():
    zorder 10
    textbutton "Go to Guild" xalign 0.10 yalign 0.76:
        style "home_button"
        action SetVariable("angelika_speech_text_count", 4),Hide("home_attributes_menu"),Jump("Tutorial")
    add "ui overhaul/guild.webp" xalign 0.05 yalign 0.755 size(50,50)
screen spellbook_info():
    key "K_SPACE" action SetVariable("current_menu", 4),Jump("Home")
    add bgstyle2 xsize 1280 ysize 720
    add home_decoration_mini pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 535
    text dic_spellbook_info[dic_spellbook_info_index] pos (0.02, 0.78) size 20 color "#000000" font "consolas.ttf" xmaximum 750 
    vbox:
        yalign 0.3
        xalign 0.10
        textbutton "Basics":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "basics"),Jump("Home")
        textbutton "Auspex":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "auspex"),Jump("Home")
        textbutton "Magna Magnifika":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "magna"),Jump("Home")
        textbutton "Sententia Veritas":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "sententia"),Jump("Home")
        textbutton "Back":
            style "home_button"
            action SetVariable("current_menu", 4),Jump("Home")
    vbox:
        yalign 0.3
        xalign 0.4
        textbutton "Tremendio":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "tremendio"),Jump("Home")
        textbutton "Cruciato":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "cruciato"),Jump("Home")
        textbutton "Delikacia":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "delikacia"),Jump("Home")
        textbutton "Domini Dictum":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "domini"),Jump("Home")
        textbutton "Adverto Servili":
            style "home_button"
            action SetVariable("dic_spellbook_info_index", "adverto"),Jump("Home")
    vbox:
        yalign 0.29
        xalign 0.05
        add "ui overhaul/basics.webp" size(50,50)
        add "ui overhaul/auspex spellbook.webp" size(50,50)
        add "ui overhaul/cruciato spellbook.webp" size(50,50)
        add "ui overhaul/domini dictum spellbook.webp" size(50,50)
        add "ui overhaul/back_city_use.webp" size(50,50)
    vbox:
        yalign 0.29
        xalign 0.3132
        add "ui overhaul/tremendio spellbook.webp" size(50,50)
        add "ui overhaul/cruciato spellbook.webp" size(50,50)
        add "ui overhaul/delikacia spellbook.webp" size(50,50)
        add "ui overhaul/domini dictum spellbook.webp" size(50,50)
        add "ui overhaul/adverto servili spellbook.webp" size(50,50)


screen cast_spell_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Spellbook":
            style "home_button"
            action SetVariable("current_menu", 41),SetVariable("dic_spellbook_info_index", "default"),Jump("Home")
        textbutton "Auspex":
            style "home_button"
            action NullAction()
        textbutton "Magna Magnifika":
            style "home_button"
            action NullAction()
        textbutton "Sententia Veritas":
            style "home_button"
            action NullAction()
        textbutton "Tremendio":
            style "home_button"
            action NullAction()
        textbutton "Cruciato":
            style "home_button"
            action NullAction()
        textbutton "Delikacia":
            style "home_button"
            action NullAction()
        textbutton "Domini Dictum":
            style "home_button"
            action NullAction()
        textbutton "Adverto Servili":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.48
        xalign 0.05
        add "ui overhaul/spellbook.webp" size(50,50)
        add "ui overhaul/auspex.webp" size(50,50)
        add "ui overhaul/magna magnifika.webp" size(50,50)
        add "ui overhaul/sententia veritas.webp" size(50,50)
        add "ui overhaul/tremendio.webp" size(50,50)
        add "ui overhaul/cruciato.webp" size(50,50)
        add "ui overhaul/delikacia.webp" size(50,50)
        add "ui overhaul/domini dictum.webp" size(50,50)
        add "ui overhaul/adverto servili.webp" size(50,50)
screen domestic_issues_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Take a bath":
            style "home_button"
            action NullAction()
        textbutton "Prepare a meal":
            style "home_button"
            action NullAction()
        textbutton "Tidy up the house":
            style "home_button"
            action NullAction()
        textbutton "Take a drug":
            style "home_button"
            action NullAction()
        textbutton "Drink a potion":
            style "home_button"
            action NullAction()
        textbutton "Accounting":
            style "home_button"
            action NullAction()
        textbutton "Business":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.49
        xalign 0.05
        add "ui overhaul/take_bath.webp" size(50,50)
        add "ui overhaul/prepare_a_meal.webp" size(50,50)
        add "ui overhaul/tidy_up_the_house.webp" size(50,50)
        add "ui overhaul/take a drug.webp" size(50,50)
        add "ui overhaul/drink a potion.webp" size(50,50)
        add "ui overhaul/accounting.webp" size(50,50)
        add "ui overhaul/business.webp" size(50,50)

screen home_menu():
    vbox:
        yalign 0.5
        xalign 0.10
        if is_main_slave:
            $ home_menu_image1 = "ui overhaul/activity.webp"
            textbutton "Slave activities":
                style "home_button"
                action SetVariable("current_menu", 1),SetVariable("show_main_slave", True), Jump("Home")
        else:
            $ home_menu_image1 = "ui overhaul/activity_gray.webp"
            textbutton "Slave activities":
                style "home_button_grey"
                action NullAction()
        if is_main_slave:
            $ home_menu_image2 = "ui overhaul/slave_assignments.webp"
            textbutton "Slaves assignments":
                style "home_button"
                action SetVariable("current_menu", 2),SetVariable("show_main_slave", True), Jump("Home")
        elif is_assistant_assigned:
            $ home_menu_image2 = "ui overhaul/assistant_assignments.webp"
            textbutton "Train assistant":
                style "home_button"
                action NullAction()
        else:
            $ home_menu_image2 = "ui overhaul/slave_assignments_gray.webp"
            textbutton "Slave assignments":
                style "home_button_grey"
                action NullAction()
        textbutton "Domestic issues":   
            style "home_button"
            action SetVariable("current_menu", 3), Jump("Home")
        textbutton "Cast a spell":
            style "home_button"
            action SetVariable("current_menu", 4), Jump("Home")
        if is_assistant_assigned:
            $ home_menu_image5 = "ui overhaul/assistant_assignments.webp"
            textbutton "Assistant assignments":
                style "home_button"
                action NullAction()
        else:
            $ home_menu_image5 = "ui overhaul/appoint_assignments_gray.webp"
            textbutton "Appoint assistant":
                style "home_button_grey"
                action NullAction()
        textbutton "End of the day":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.49
        xalign 0.05
        add home_menu_image1 size(50,50)
        add home_menu_image2 size(50,50)
        add home_menu_image3 size(50,50)
        add home_menu_image4 size(50,50)
        add home_menu_image5 size(50,50)
        add home_menu_image6 size(50,50)
screen slave_activities_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Talk":
            style "home_button"
            action NullAction()
        textbutton "Sex":
            style "home_button"
            action NullAction()
        textbutton "conduct a lesson":
            style "home_button"
            action NullAction()
        textbutton "Sex education":
            style "home_button"
            action NullAction()
        textbutton "Invite a tutor (5-25$)":
            style "home_button"
            action NullAction()
        textbutton "Reward":   
            style "home_button"
            action NullAction()
        textbutton "Punish":
            style "home_button"
            action NullAction()
        textbutton "Get rid of her":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.49
        xalign 0.05
        add "ui overhaul/talk.webp" size(50,50)
        add "ui overhaul/sex.webp" size(50,50)
        add "ui overhaul/conduct a lesson.webp" size(50,50)
        add "ui overhaul/sex education.webp" size(50,50)
        add "ui overhaul/invite a tutor.webp" size(50,50)
        add "ui overhaul/reward.webp" size(50,50)
        add "ui overhaul/punish.webp" size(50,50)
        add "ui overhaul/get rid of her.webp" size(50,50)
screen slave_assignments_menu():
    key "K_SPACE" action SetVariable("current_menu", 0),Jump("Home")
    imagebutton pos(0.02,0.4):
        idle "ui overhaul/back.webp"
        hover "ui overhaul/back_hover.webp"
        action SetVariable("current_menu", 0),Jump("Home")
    vbox:
        yalign 0.5
        xalign 0.10
        textbutton "Attend classes (2-12$)":
            style "home_button"
            action NullAction()
        textbutton "Gymnastics":
            style "home_button"
            action NullAction()
        textbutton "Tidy up the house":
            style "home_button"
            action NullAction()
        textbutton "Prepare dinner":
            style "home_button"
            action NullAction()
        textbutton "Take a bath":
            style "home_button"
            action NullAction()
        textbutton "Milk the Fiend":
            style "home_button"
            action NullAction()
        textbutton "Serve me":
            style "home_button"
            action NullAction()
        textbutton "Take a drug":
            style "home_button"
            action NullAction()
        textbutton "Drink a potion":
            style "home_button"
            action NullAction()
    vbox:
        yalign 0.48
        xalign 0.05
        add "ui overhaul/attend classes_s.webp" size(50,50)
        add "ui overhaul/gymnastics_s.webp" size(50,50)
        add "ui overhaul/tidy up the house_s.webp" size(50,50)
        add "ui overhaul/prepare dinner_s.webp" size(50,50)
        add "ui overhaul/take a bath_s.webp" size(50,50)
        add "ui overhaul/milk the fiend_s.webp" size(50,50)
        add "ui overhaul/serve me_s.webp" size(50,50)
        add "ui overhaul/take a drug.webp" size(50,50)
        add "ui overhaul/drink a potion.webp" size(50,50)
screen sparks_menu():
    zorder 10
    hbox:
        xalign 0.01
        yalign 0.01
        textbutton "Day: " + str(day_tracker) :
            style "day_tracker_button"
            action NullAction()
        add "spacer" size(4,0) 
        text "(" + str(sparks_37) + "$)":
            style "day_tracker_button_text"
screen slave_anatomy_menu():
    add "bg/page_blank.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    if all_girls_list[girl_index]["lactation"]:
        $boobs1 = "milk-swollen breasts"
        $boobs2 = "milk-swollen breasts"
        $boobs3 = "milk-distended breasts"
        $boobs4 = "milk-swollen breasts"
        $boobs5 = "milk-swollen breasts"
        $boobs6 = "milk-swollen breasts"
    else:
        $boobs1 =" marshmallowy tits"
        $boobs2 =" motherly breasts"
        $boobs3 =" empty breast-sacks"
        $boobs4 =" round tits"
        $boobs5 =" firm melons"
        $boobs6 =" shapely balloons"
    hbox:
        pos(0.205,0.07)
        add "girls/body/" + all_girls_list[girl_index]["boobs_img"] + ".webp" size(372,250)
        add "spacer" size(20,0)
        add "girls/body/" + all_girls_list[girl_index]["pussy_img"] + ".webp" size(372,250)  
    vbox:
        pos(0.21,0.42)

        if all_girls_list[girl_index]["age"]==0:
            text dic_girl_boobs_text["young"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        elif all_girls_list[girl_index]["age"]==1:
            text dic_girl_boobs_text["loli"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        elif all_girls_list[girl_index]["age"]==2:
            text dic_girl_boobs_text["mature"][all_girls_list[girl_index]["boobs"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        if all_girls_list[girl_index]["lactation"]:
            text "Lactating" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        else:
            text "Not lactating" size 16 color "#000000" font "fonts/Segoe Print.ttf" 
        if all_girls_list[girl_index]["nipples_pierced"]:
            text "Nipples pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        else:
            text "Nipples not pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text dic_girl_breast_modification[all_girls_list[girl_index]["breast_modification"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text dic_girl_age_text[all_girls_list[girl_index]["age"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
    vbox:
        pos(0.64,0.42)
        text dic_girl_vaginal_tightness[all_girls_list[girl_index]["vaginal_tightness"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_anal_tightness[all_girls_list[girl_index]["anal_tightness"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        if all_girls_list[girl_index]["clitoris_pierced"]:
            text "Clitoris pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        else:
            text "Clitoris not pierced" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_vagina_modification[all_girls_list[girl_index]["vagina_modification"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        text dic_girl_brand[all_girls_list[girl_index]["brand"]] size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
    vbox:
        pos(0.215,0.62)
        text "Beauty = Natural Beauty + Neoplasty - (No Scars + Bruises + Physique)" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
        text "Style = Clothes + Natural Beauty + Tangled Hair + Scent, Nails & Pelage + Natural Grace - Hygiene" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
        text "Exoticism = Natural Exoticism + No Tattoos + No Piercings + Clothes" xalign 0.5 size 14 color "#000000" font "fonts/Segoe Print.ttf" 
screen slave_equipment_menu():
    add "bg/page_blank.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
screen slave_aura_menu():
    add "page_aura.webp" xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
screen slave_rules_menu():
    add all_girls_list[girl_index]["fullimage"] + ".webp" xalign 0.5 yalign 0.1838 size(795,535)  
    add "padding.webp" xsize 230 ysize 535 pos(0.2835,0.42) anchor (0.5,0.5)
    add "padding.webp" xsize 230 ysize 535 pos(0.724,0.42) anchor (0.5,0.5)
    key "K_SPACE" action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    text dic_slave_conditions[text_slave_conditions_index] size 18 color "#000000" font "fonts/Consolas.ttf" pos(0.21,0.82) xmaximum 750
   
    vbox:
        pos(0.20,0.05)
        anchor (0.0,0.0)
        text "SLEEP:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"
        add "spacer" size(0,138)
        text "DIET:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"  
        add "spacer" size(0,138)
        text "PORTION SIZE:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"
        add "spacer" size(0,110)
        text "CALORIES REMAINING:" size 16 color "#FFD700" font "fonts/Segoe Print.ttf"

  
    vbox:
        pos(0.205,0.095)
        anchor (0.0,0.0)
        spacing 6
        for i in range(5):
            if all_girls_list[girl_index]["sleep"] == i:
                imagebutton:
                    idle "buttons/sel_button.webp"
                    hover "buttons/sel_button_hover.webp"
                    action NullAction()
            else:
                imagebutton:
                    idle "buttons/unsel_button.webp"
                    hover "buttons/unsel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "sleep", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_sleep[i]), Jump("Home")
        add "spacer" size(0,19.5)
        for i in range(3):
            if all_girls_list[girl_index]["diet"] == i:
                imagebutton:
                    idle "buttons/sel_button.webp"
                    hover "buttons/sel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index", dic_slave_conditions_food[3]), Jump("Home")
            else:
                imagebutton:
                    idle "buttons/unsel_button.webp"
                    hover "buttons/unsel_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", i),SetVariable("text_slave_conditions_index", dic_slave_conditions_food[i]), Jump("Home")
        if all_girls_list[girl_index]["your_leftovers"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "your_leftovers", False), SetVariable("text_slave_conditions_index","No_leftovers"), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "your_leftovers", True), SetVariable("text_slave_conditions_index","Eats_leftovers"), Jump("Home")
        if all_girls_list[girl_index]["supplements"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "supplements", False), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index], "supplements", True),SetVariable("text_slave_conditions_index","supplements"), Jump("Home")
        add "spacer" size(0,19.5)
       
        if all_girls_list[girl_index]["diet"] != 3:
            for i in range(4):
                if all_girls_list[girl_index]["portion_size"] == i:
                    imagebutton:
                        idle "buttons/sel_button.webp"
                        hover "buttons/sel_button_hover.webp"
                        action NullAction()
                else:
                    imagebutton:
                        idle "buttons/unsel_button.webp"
                        hover "buttons/unsel_button_hover.webp"
                        action SetDict(all_girls_list[girl_index], "portion_size", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[i]), Jump("Home")
        else:
            for i in range(4):
                imagebutton:
                    idle "buttons/unactive_button.webp"
                    hover "buttons/unactive_button_hover.webp"
                    action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", i),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")


    vbox:
        pos(0.225,0.09)
        anchor (0.0,0.0)
        textbutton "- In the cells": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 0),SetVariable("text_slave_conditions_index","in_the_cells"), Jump("Home")
        textbutton "- On the floor": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 1),SetVariable("text_slave_conditions_index","On_the_floor"), Jump("Home")
        textbutton "- On a bedroll": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 2),SetVariable("text_slave_conditions_index","On_a_bedroll"), Jump("Home")
        textbutton "- In my bed": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 3),SetVariable("text_slave_conditions_index","In_my_bed"), Jump("Home")
        textbutton "- Do not sleep": 
            style "slave_screen_order_button"
            action SetDict(all_girls_list[girl_index], "sleep", 4),SetVariable("text_slave_conditions_index","Do_not_sleep"), Jump("Home")
        add "spacer" size(0,25)
        if all_girls_list[girl_index]["diet"] == 0:
            textbutton "- Dehydrated food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Dehydrated food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
        if all_girls_list[girl_index]["diet"] == 1:
            textbutton "- Canned food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Canned food": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[1]), Jump("Home")
        if all_girls_list[girl_index]["diet"] == 2:
            textbutton "- Fiend's cum": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[3]), Jump("Home")
        else:
            textbutton "- Fiend's cum": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[2]), Jump("Home")
        if all_girls_list[girl_index]["your_leftovers"]:
            textbutton "- Your leftovers": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "your_leftovers", False), SetVariable("text_slave_conditions_index","No_leftovers"), Jump("Home")
        else:
            textbutton "- Your leftovers": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "your_leftovers", True), SetVariable("text_slave_conditions_index","Eats_leftovers"), Jump("Home")
        if all_girls_list[girl_index]["supplements"]:
            textbutton "- Supplements": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "supplements", False), Jump("Home")
        else:
            textbutton "- Supplements": 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "supplements", True),SetVariable("text_slave_conditions_index","supplements"), Jump("Home")
        add "spacer" size(0,25)
        if all_girls_list[girl_index]["diet"] != 3:
            textbutton "- Restricted":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[0]), Jump("Home")
            textbutton "- Moderate":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[1]), Jump("Home")
            textbutton "- Generous":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[2]), Jump("Home")
            textbutton "- Calculated":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "portion_size", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_portion[3]), Jump("Home")
        else:
            textbutton "- Restricted":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 0),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Moderate":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 1),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Generous":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 2),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
            textbutton "- Calculated":
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index], "diet", 0),SetDict(all_girls_list[girl_index], "portion_size", 3),SetVariable("text_slave_conditions_index",dic_slave_conditions_food[0]), Jump("Home")
                
        add "spacer" size(0,25)
        textbutton "  2000":
            style "slave_screen_order_button"
            action NullAction()
    vbox:
        pos(0.807,0.05)
        anchor (1.0,0.0)
        if number_of_rules > 2:
            text "{color=#FFD700}RULES: ([str(number_of_rules)]){/color}" size 16 font "fonts/Segoe Print.ttf"
        else:
            text "{color=#FFD700}RULES: ({/color}{color=#CD0000}[str(number_of_rules)]{/color}{color=#FFD700}){/color}" size 16 font "fonts/Segoe Print.ttf"
    vbox:
        pos(0.802,0.095)
        anchor (1.0,0.0)
        spacing 6
        if all_girls_list[girl_index]["rules"]["act_as_cook"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", False),SetVariable("text_slave_conditions_index","cook_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", True),SetVariable("text_slave_conditions_index","cook_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")

        if all_girls_list[girl_index]["rules"]["act_as_maid"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", False),SetVariable("text_slave_conditions_index","maid_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", True),SetVariable("text_slave_conditions_index","maid_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["bath_slave"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", False),SetVariable("text_slave_conditions_index","bath_slave_abort_rule"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", True),SetVariable("text_slave_conditions_index","bath_slave_rule"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_alarm"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", False),SetVariable("text_slave_conditions_index","behave_alarm_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", True),SetVariable("text_slave_conditions_index","behave_alarm_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_humility"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", False),SetVariable("text_slave_conditions_index","behave_humility_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", True),SetVariable("text_slave_conditions_index","behave_humility_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_pet"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", False),SetVariable("text_slave_conditions_index","behave_pet_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", True),SetVariable("text_slave_conditions_index","behave_pet_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_silence"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", False),SetVariable("text_slave_conditions_index","behave_silence_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", True),SetVariable("text_slave_conditions_index","behave_silence_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_toilet"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", False),SetVariable("text_slave_conditions_index","behave_toilet_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", True),SetVariable("text_slave_conditions_index","behave_toilet_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_urinal"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", False),SetVariable("text_slave_conditions_index","behave_urinal_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", True),SetVariable("text_slave_conditions_index","behave_urinal_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_orgasm"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", False),SetVariable("text_slave_conditions_index","deny_orgasm_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", True),SetVariable("text_slave_conditions_index","deny_orgasm_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_toileting"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", False),SetVariable("text_slave_conditions_index","deny_toileting_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", True),SetVariable("text_slave_conditions_index","deny_toileting_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["milk_the_fiend"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", False),SetVariable("text_slave_conditions_index","slave_tentacle_rule_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", True),SetVariable("text_slave_conditions_index","slave_tentacle_rule"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["no_masturbation"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", False),SetVariable("text_slave_conditions_index","no_masturbation_rules_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", True),SetVariable("text_slave_conditions_index","no_masturbation_rules"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["use_vaginal_beads"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", False),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule_abort"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", True),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["enforce_rules"]:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", False),SetVariable("text_slave_conditions_index","enforce_rules_abort"), Jump("Home")
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", True),SetVariable("text_slave_conditions_index","enforce_rules"), Jump("Home")

    vbox:
        pos(0.65,0.09)
        anchor (0.0,0.0)
        if all_girls_list[girl_index]["rules"]["act_as_cook"]:
            textbutton "Act as cook -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", False),SetVariable("text_slave_conditions_index","cook_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Act as cook -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_cook", True),SetVariable("text_slave_conditions_index","cook_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["act_as_maid"]:
            textbutton "Act as maid -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", False),SetVariable("text_slave_conditions_index","maid_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Act as maid -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "act_as_maid", True),SetVariable("text_slave_conditions_index","maid_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["bath_slave"]:
            textbutton "Bath slave -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", False),SetVariable("text_slave_conditions_index","bath_slave_rule"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Bath slave -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "bath_slave", True),SetVariable("text_slave_conditions_index","bath_slave_abort_rule"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_alarm"]:
            textbutton "Behave: alarm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", False),SetVariable("text_slave_conditions_index","behave_alarm_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: alarm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_alarm", True),SetVariable("text_slave_conditions_index","behave_alarm_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_humility"]:
            textbutton "Behave: humility -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", False),SetVariable("text_slave_conditions_index","behave_humility_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: humility -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_humility", True),SetVariable("text_slave_conditions_index","behave_humility_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_pet"]:
            textbutton "Behave: pet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", False),SetVariable("text_slave_conditions_index","behave_pet_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: pet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_pet", True),SetVariable("text_slave_conditions_index","behave_pet_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        
        if all_girls_list[girl_index]["rules"]["behave_silence"]:
            textbutton "Behave: silence -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", False),SetVariable("text_slave_conditions_index","behave_silence_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: silence -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_silence", True),SetVariable("text_slave_conditions_index","behave_silence_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_toilet"]:
            textbutton "Behave: toilet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", False),SetVariable("text_slave_conditions_index","behave_toilet_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: toilet -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_toilet", True),SetVariable("text_slave_conditions_index","behave_toilet_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["behave_urinal"]:
            textbutton "Behave: urinal -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", False),SetVariable("text_slave_conditions_index","behave_urinal_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Behave: urinal -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "behave_urinal", True),SetVariable("text_slave_conditions_index","behave_urinal_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_orgasm"]:
            textbutton "Deny orgasm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", False),SetVariable("text_slave_conditions_index","deny_orgasm_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Deny orgasm -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_orgasm", True),SetVariable("text_slave_conditions_index","deny_orgasm_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["deny_toileting"]:
            textbutton "Deny toileting -" xalign 1.0: 
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", False),SetVariable("text_slave_conditions_index","deny_toileting_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Deny toileting -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "deny_toileting", True),SetVariable("text_slave_conditions_index","deny_toileting_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["milk_the_fiend"]:
            textbutton "Milk the fiend -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", False),SetVariable("text_slave_conditions_index","slave_tentacle_rule"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Milk the fiend -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "milk_the_fiend", True),SetVariable("text_slave_conditions_index","slave_tentacle_rule_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["no_masturbation"]:
            textbutton "No masturbation -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", False),SetVariable("text_slave_conditions_index","no_masturbation_rules"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "No masturbation -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "no_masturbation", True),SetVariable("text_slave_conditions_index","no_masturbation_rules_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["use_vaginal_beads"]:
            textbutton "Use vaginal beads -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", False),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule"),SetVariable("number_of_rules",number_of_rules-1), Jump("Home")
        else:
            textbutton "Use vaginal beads -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "use_vaginal_beads", True),SetVariable("text_slave_conditions_index","use_vaginal_beads_rule_abort"),SetVariable("number_of_rules",number_of_rules+1), Jump("Home")
        if all_girls_list[girl_index]["rules"]["enforce_rules"]:
            textbutton "Enforce rules -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", False),SetVariable("text_slave_conditions_index","enforce_rules_abort"), Jump("Home")
        else:
            textbutton "Enforce rules -" xalign 1.0:
                style "slave_screen_order_button"
                action SetDict(all_girls_list[girl_index]["rules"], "enforce_rules", True),SetVariable("text_slave_conditions_index","enforce_rules"), Jump("Home")



screen screen_rules():   
    add bgstyle3 xsize 1280 ysize 720
    add home_decoration_mini xsize 795 ysize 535 pos(0.5028,0.42) anchor (0.5,0.5)
    imagebutton:
        idle "buttons/close_button.webp" pos (1004,1)
        hover "buttons/close_button_hover.webp"
        action SetVariable("current_menu", 0),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
    hbox: 
        pos(0.475,0.01)
        anchor (0.5,0.0)
        spacing 122
        textbutton "Rules":
            style "slave_screen_button"
            action SetVariable("current_menu", 100),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
        textbutton "Anatomy":
            style "slave_screen_button"
            action SetVariable("current_menu", 101),Jump("Home")
        textbutton "Equipment":
            style "slave_screen_button"
            action SetVariable("current_menu", 102),Jump("Home")
        textbutton "Aura":
            style "slave_screen_button"
            action SetVariable("current_menu", 103),Jump("Home")   
    hbox: 
        pos(0.525,0.005)
        anchor (0.50,0.0)
        spacing 162 
        if current_menu == 100:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 100),SetVariable("text_slave_conditions_index", "default"),Jump("Home")
        if current_menu == 101:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 101),Jump("Home")
        if current_menu == 102:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp"
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 102),Jump("Home")
        if current_menu == 103:
            imagebutton:
                idle "buttons/sel_button.webp"
                hover "buttons/sel_button_hover.webp"
                action NullAction()
        else:
            imagebutton:
                idle "buttons/unsel_button.webp" 
                hover "buttons/unsel_button_hover.webp"
                action SetVariable("current_menu", 103),Jump("Home")
   
    vbox:
        pos(0.01,0.02)
        text "Name: " + all_girls_list[girl_index]["name"] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Age: " + dic_girl_age_text[all_girls_list[girl_index]["age"]] size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Owned for: " + str(day_tracker - all_girls_list[girl_index]["day_bought"]) + " days" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "Rank:" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "{u}ATTRIBUTES{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        for key, values in dic_slave_attributes.items():
            if key in all_girls_list[girl_index]["attributes"]:
                if key != "physical":
                    textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                        style "attribute_custom_slave" + str(all_girls_list[girl_index]["attributes"][key])
                        action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),Jump("Home")
                else:
                    textbutton values[all_girls_list[girl_index]["attributes"][key]]:
                        style "attribute_custom_physical" + str(all_girls_list[girl_index]["attributes"][key])
                        action SetVariable("attribute_track_index",key),SetVariable("attribute_track_basic",key),SetVariable("dictionary_track_index",7),SetVariable("dictionary_name",dic_slave_attributes),SetVariable("attribute_checkbox",True),SetVariable("attributeisphysical",True),Jump("Home")                    
        text "Mood" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        text "{u}TRAITS{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf"
        for key, values in dic_traits_skills.items():

            $ skill_info = traits_skills[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)
            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                # Make sure values[val] exists or adjust to keys, here example:
                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_skills_descriptions), SetVariable("customboxcheck", True), Jump("Home")
     
            ################ - i'm a genus -rec3ks
        for key, values in dic_traits_sexual.items():
           
            $ skill_info = traits_sexual[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                # Get the description from values dict or list
                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key), SetVariable("dictionary_track_index", val), SetVariable("dictionary_name", dic_traits_sexual_description), SetVariable("customboxcheck", True), Jump("Home")
        for key, values in dic_traits_miscellaneous.items():

            $ skill_info = traits_miscellaneous[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_miscellaneous_description),SetVariable("customboxcheck", True),Jump("Home")
        for key, values in dic_traits_aura.items():

            $ skill_info = traits_aura[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_aura_description),SetVariable("customboxcheck", True),Jump("Home")
        for key, values in dic_traits_attributes.items():

            $ skill_info = traits_attributes[key]
            $ val = skill_info.get("value", 0)
            $ revealed = skill_info.get("revealed", False)

            if val != 0 and revealed:
                if val == -1:
                    $ style_used = "slave_traits_bad1"
                elif val == -2:
                    $ style_used = "slave_traits_bad2"
                elif val == 1:
                    $ style_used = "slave_traits_good1"
                elif val == 2:
                    $ style_used = "slave_traits_good2"
                else:
                    $ style_used = "default_style"

                $ label_text = values.get(val, "Unknown") if isinstance(values, dict) else values[val]

                textbutton label_text:
                    style style_used
                    action SetVariable("attribute_track_index", key),SetVariable("dictionary_track_index", val),SetVariable("dictionary_name", dic_traits_attributes_description),SetVariable("customboxcheck", True),Jump("Home")
    vbox:
        pos(0.99,0.02)
        anchor (1.0,0.0)
        text "{u}                     SKILLS{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        for key, values in dic_slave_skills.items():
            if key in all_girls_list[girl_index]["skills"]:
                textbutton values[all_girls_list[girl_index]["skills"][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["skills"][key]) xalign 1.0
                    action NullAction()
        text "{u}     SEX TECHNIQUES{/u}" size 16 color "#000000" font "fonts/Segoe Print.ttf" xalign 1.0
        for key, values in dic_slave_skills_sexual.items():
            if key in all_girls_list[girl_index]["sex_experience"][key]:
                textbutton values[all_girls_list[girl_index]["sex_experience"][key][key]]:
                    style "attribute_custom_slave" + str(all_girls_list[girl_index]["sex_experience"][key][key]) xalign 1.0
                    action NullAction()
screen home_attributes_menu():
    vbox:
        pos(0.90,0.05)
        imagebutton anchor (0.5,0.0):
            idle mc_image
            hover mc_image2
            action NullAction()
            at avatar_scale
        add "spacer" size(0,33)
        text "Calm" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Contented" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Pristine" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(0,60)
        if girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index]:
            imagebutton anchor (0.5,0.5):
                idle all_girls_list[girl_index]["ava_clear"] + ".webp"
                hover all_girls_list[girl_index]["ava_clear"] + "_sepia.webp"
                action SetVariable("current_menu", 100),Jump("Home")
                at avatar_scale
        else:
            add "blank_ava.webp" size(140,140) anchor (0.5,0.5)
        add "spacer" size(0,-38)
        if is_main_slave:
            text "Calm" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "No achievements" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "Pristine" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        else:
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
            text "" color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(0,63)
        add "blank_ava.webp" size(140,140) anchor (0.5,0.5)
        add "spacer" size(0,-55)
        text "No assistant" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "immaculate" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Cannned food" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
    hbox:
        pos(0.91,0.260)
        anchor (0.5,0.0)
        text "Energy" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(-10,0)
        $ full_energy = energy_value // 2
        $ has_half = energy_value % 2 == 1
        for i in range(full_energy):
            add energy_image1 size(7,7) anchor (0.5,0.5)
        if has_half:
            add energy_image2 size(7,7) anchor (0.5,0.5)
    if not is_main_slave:
        text "No slave" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12 pos(0.90,0.575)
    hbox:
        pos(0.91,0.575)
        anchor (0.5,0.0)
        if girl_index in all_girls_list and "energy" in all_girls_list[girl_index]:
            text "Energy" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
            add "spacer" size(-10,0)
            $ full_energy = all_girls_list[girl_index]["energy"] // 2
            $ has_half = all_girls_list[girl_index]["energy"] % 2 == 1
            for i in range(full_energy):
                add energy_image1 size(7,7) anchor (0.5,0.5)
            if has_half:
                add energy_image2 size(7,7) anchor (0.5,0.5)

screen bg_home():
    add bgstyle xsize 1280 ysize 720
    add home_decoration xsize 1000 ysize 675 pos (0.002,0.057)
