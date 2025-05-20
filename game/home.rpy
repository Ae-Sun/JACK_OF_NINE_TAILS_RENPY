default bgstyle = "bg_main_old.webp"
default home_decoration = "bg/interiors/slum_study_large.webp"
default day_tracker = 1
default home_menu_image1 = "ui overhaul/activity.webp"
default home_menu_image2 = "ui overhaul/slave_assignments.webp"
default home_menu_image3 = "ui overhaul/domestic_issues.webp"
default home_menu_image4 = "ui overhaul/cast_spell.webp"
default home_menu_image5 = "ui overhaul/assistant_assignments.webp"
default home_menu_image6 = "ui overhaul/end_day.webp"
default energy_image1 = "ui overhaul/energy/energy_green.webp"
default energy_image2 = "ui overhaul/energy/energy_green_half.webp"
default mc_image = ""
default energy_value = 0
default current_menu = 0
default next_day_check = True
default is_main_slave = False
default is_assistant_assigned = False
default mood_value = 0
label Home:
    show screen bg_home()
    if next_day_check:
        $ energy_value = strength_value_1 *2 + 2
        if girl_index in all_girls_list:
            if "attributes" in all_girls_list[girl_index] and "endurance" in all_girls_list[girl_index]["attributes"]:
                $ all_girls_list[girl_index]["energy"] = all_girls_list[girl_index]["attributes"]["endurance"] * 2 + 2
                $ is_main_slave = True
        $ next_day_check = False
    if is_tutorial == True:
        if current_menu == 0:
            show screen goguild()
        else:
            hide screen goguild
        $mc_image = "master/master_noble.webp"
    else:
        if is_normal_start == True:
            $mc_image = dic_custom_character_selection[mc][0]
        else:
            $mc_image = dic_custom_character_selection[dic_charactersOnlyName[characterOnlyNameIndex]][0]

    show screen home_attributes_menu()
    show screen sparks_menu()
    if current_menu == 0:
        call screen home_menu()
    elif current_menu == 1:
        call screen slave_activities_menu()
    elif current_menu == 2:
        call screen slave_assignments_menu()
screen goguild():
    zorder 10
    textbutton "Go to Guild" xalign 0.10 yalign 0.76:
        style "home_button"
        action SetVariable("angelika_speech_text_count", 4),Hide("home_attributes_menu"),Jump("Tutorial")
    add "ui overhaul/guild.webp" xalign 0.05 yalign 0.755 size(50,50)
screen home_menu():
    vbox:
        yalign 0.5
        xalign 0.10
        if is_main_slave:
            $ home_menu_image1 = "ui overhaul/activity.webp"
            textbutton "Slave activities":
                style "home_button"
                action SetVariable("current_menu", 1), Jump("Home")
        else:
            $ home_menu_image1 = "ui overhaul/activity_gray.webp"
            textbutton "Slave activities":
                style "home_button_grey"
                action NullAction()
        if is_main_slave:
            $ home_menu_image2 = "ui overhaul/slave_assignments.webp"
            textbutton "Slaves assignments":
                style "home_button"
                action SetVariable("current_menu", 2), Jump("Home")
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
            action NullAction()
        textbutton "Cast a spell":
            style "home_button"
            action NullAction()
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

screen home_attributes_menu():
    vbox:
        pos(0.90,0.05)
        add mc_image size(140,140) anchor (0.5,0.0)
        add "spacer" size(0,33)
        text "Calm" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Contented" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        text "Pristine" anchor (0.5,0.5) color "#000000" font "fonts/Segoe Print.ttf" size 12
        add "spacer" size(0,60)
        if girl_index in all_girls_list and "ava_clear" in all_girls_list[girl_index]:
            add all_girls_list[girl_index]["ava_clear"] + ".webp" size(140,140) anchor (0.5,0.5) 
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
