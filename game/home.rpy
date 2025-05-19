<<<<<<< HEAD
default bgstyle = "bg_main_old.webp"
default home_decoration = "bg/interiors/slum_study_large.webp"
default day_tracker = 1
label Home:
    show screen bg_home()
    call screen testscreen()
    
screen testscreen():
    hbox:
        xalign 0.007
        yalign 0.005
        textbutton "Day: " + str(day_tracker) :
            style "day_tracker_button"
            action SetVariable("day_tracker",day_tracker + 1)
        add "spacer" size(4,0) 
        text "(" + str(sparks_37) + "$)":
            style "day_tracker_button_text"
screen bg_home():
    add bgstyle xsize 1280 ysize 720
    add home_decoration xsize 1000 ysize 675 pos (0.002,0.057)
=======
default home_background = ""
default estate = ""
label Home:
    hide screen tutorial_bg
    scene basic_study
    call screen testscreen()

screen testscreen():
    text "hola"
>>>>>>> 561ca5603234ef96c31ed5d07d940766efb95635
