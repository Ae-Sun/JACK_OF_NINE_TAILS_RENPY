default angelika_speech_text_count = 0
default lecture_name = ""
default inicial_girl = "demo/choose_slave.webp"
default demo_girl_text_index = 0
default demo_girl_selection = "Helen"
default all_girls_list = {}
default girl_index = 0
default premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/helen.json"
screen tutorial_bg():
    add "bg/guild.webp"pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 515
screen mistress_angelika():
    add "characters/mistress_angelika.webp"pos(0.3, 0.365) anchor (0.5, 0.5) xsize 795 ysize 515
screen angelika_speech():
    text angelika_speech_text[angelika_speech_text_count] pos (0.02, 0.75) size 20 font "consolas.ttf" xmaximum 750 
screen angelika_buttons():
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
            action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Tutorial")
screen angelika_display():
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
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture1"),Jump("Lecture")
        textbutton "Lecture II: Psychology of submission":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture2"),Jump("Lecture")
        textbutton "Lecture III: Sticks and carrots":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture3"),Jump("Lecture")
        textbutton "Lecture IV: Kitchen slavery":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture4"),Jump("Lecture")
        textbutton "Check the conditions of the exam":
            style "lecture_button"
            action SetVariable("angelika_speech_text_count",0),SetVariable("lecture_name","tutorial_lecture5"),Jump("Lecture")
        textbutton "Start the practical examination":
            style "lecture_button"
            action Jump("choose_inicial_girl")
        textbutton "Leave the guild":
            style "lecture_button"
            action MainMenu(confirm=False)
    text "{color=#000000}I must choose which lecture I want to hear, or I can ask about the conditions of the examination or ask to start when I am ready.{/color}" pos (0.02, 0.75) size 20 font "consolas.ttf" xmaximum 750 
screen lecture_screen():
    text tutorial_lectureGIGA[lecture_name][angelika_speech_text_count] pos (0.02, 0.75) size 20 font "consolas.ttf" xmaximum 750 color "#000000"
screen lecture_screenbuttons():   
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle tutorial_backbutton anchor (0.5, 0.5)
            hover tutorial_backbutton_hover
            action SetVariable("angelika_speech_text_count", max(angelika_speech_text_count - 1,0)),Jump("Lecture")
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action SetVariable("angelika_speech_text_count", angelika_speech_text_count + 1),Jump("Lecture")
screen choose_inicial_girl_screen():
    add "bg/interiors/classic_dungeon.webp"pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 515
    text "Choose your slave" pos(0.315, 0.04) anchor (0.5, 0.5) size 36 color "#ffff00" font "fonts/victoriana.ttf"
    text demo_girl_text[demo_girl_text_index] pos (0.02, 0.75) size 20 font "consolas.ttf" xmaximum 750 color "#000000"

    add inicial_girl pos(0.004,0.007111) anchor (0.0, 0.0) xsize 795 ysize 515
    for girl_path, xpos in inicial_girls:
        button:
            xpos xpos
            ypos 0
            xsize 265
            ysize 515
            action SetVariable("inicial_girl", girl_path), Jump("choose_inicial_girl")
    vbox:
        xpos 850
        ypos 35
        spacing 2
        text "{u}ATTRIBUTES{/u}" font "fonts/Segoe Print.ttf" color "000000" size 16
        for key, values in dic_slave_attributes.items():
            textbutton values[all_girls_list[girl_index]["slave_attributes"][key]]:
                style "attribute_custom_slave" + str(demo_girl_stats[demo_girl_selection][i])
                action Jump("choose_inicial_girl")
        add "spacer" size(0,20) 
        text "{u}TRAITS{/u}"font "fonts/Segoe Print.ttf" color "000000" size 16
        ##### I am a fucking genius
    vbox:
        xalign 0.655
        yalign 0.96
        imagebutton:
            idle tutorial_backbutton anchor (0.5, 0.5)
            hover tutorial_backbutton_hover
            action SetVariable("angelika_speech_text_count",4),SetVariable("Lecture_name",""),Jump("Tutorial")
        imagebutton:
            idle "buttons/auk_fwrd.webp" anchor (0.5, 0.5)
            hover "buttons/auk_fwrd_hover.webp"
            action Jump("iniciation_state")

label choose_inicial_girl:
    $ all_girls_list[girl_index] = load_json(premiun_girl_tutorial_selected_localization)
    hide screen slaver_guild
    scene bg_old
    if inicial_girl == "demo/choose_slave.webp":
        $ demo_girl_text_index = 0
        $ demo_girl_selection = "Helen"
        $ premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/helen.json"

    if inicial_girl == "demo/choose_amazon.webp":
        $ demo_girl_text_index = 1
        $ demo_girl_selection = "Yasmin"
        $ premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/yasmin.json"
        
    if inicial_girl == "demo/choose_princess.webp":
        $ demo_girl_text_index = 2         
        $ demo_girl_selection = "Wilhelmine"
        $ premiun_girl_tutorial_selected_localization = "girl_packs/original_premiun_slaves_pack/wilhelmine.json"
        
    call screen choose_inicial_girl_screen

label Lecture:
    show screen mistress_angelika
    hide screen slaver_guild
    show screen lecture_screen
    show screen angelika_display
    if angelika_speech_text_count == 0:
        $ tutorial_backbutton = "buttons/demo_noback_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_noback_button_hover.webp"
    else:
        $ tutorial_backbutton = "buttons/demo_back_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_back_button_hover.webp"
    if lecture_name == "tutorial_lecture1":
        if angelika_speech_text_count == 8:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture2":
        if angelika_speech_text_count == 27:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture3":
        if angelika_speech_text_count == 24:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture4":
        if angelika_speech_text_count == 11:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    if lecture_name == "tutorial_lecture5":
        if angelika_speech_text_count == 6:
            hide screen mistress_angelika
            hide lecture_screen
            hide screen angelika_display
            call screen slaver_guild
    call screen lecture_screenbuttons

label Tutorial:
    scene bg_old 
    show screen tutorial_bg()
    show screen angelika_buttons()
    show screen mistress_angelika()
    show screen angelika_display()
    hide screen choose_inicial_girl_screen
    if angelika_speech_text_count == 0:
        $ tutorial_backbutton = "buttons/demo_noback_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_noback_button_hover.webp"
    else:
        $ tutorial_backbutton = "buttons/demo_back_button.webp"
        $ tutorial_backbutton_hover = "buttons/demo_back_button_hover.webp"
    if angelika_speech_text_count == 1:
        python:
            name = renpy.input("My name is... (Keep this shorter than 14 character.)", length=13)
            name = name.strip()
            if name != "":
                mc = name
    if angelika_speech_text_count == 2:
        $ mynamebugfix = True
    if angelika_speech_text_count == 4:
        hide screen angelika_buttons
        hide screen mistress_angelika
        hide screen angelika_display
        hide screen lecture_screen
        show screen slaver_guild()
        $ mynamebugfix = False
    call screen angelika_speech()   

    return
label iniciation_state:

    call screen testdemoscreen()

screen testdemoscreen():
    add all_girls_list[girl_index]["fullimage"] + ".webp" pos(0.1,0.1)



label testlabel:

    $ all_girls_list[girl_index] = selected_json_data
    call screen testscreen()
screen testscreen():
    textbutton "CLICK HERE" at truecenter:
        action Function(load_random_json), Jump("testlabel")
    add all_girls_list[girl_index]["fullimage"] + ".webp" pos(0.1,0.1)
    