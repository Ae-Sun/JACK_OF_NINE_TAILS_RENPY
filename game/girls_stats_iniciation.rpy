define inicial_girls = [
    ("demo/choose_princess.webp", 0),
    ("demo/choose_amazon.webp", 265),
    ("demo/choose_slave.webp", 530),
]
define dic_slave_attributes_keys = {
    "beauty":       "BEAUTY",
    "endurance":    "ENDURANCE",
    "empathy":      "EMPATHY",
    "temperament":  "TEMPERAMENT",
    "intelligence": "INTELLIGENCE",
    "nature":       "NATURE",
    "pride":        "PRIDE",
    "exoticism":    "EXOTICISM",
    "physical":     "PHYSICAL",
    "style":        "STYLE",
    "fame":         "FAME",
}


define dic_slave_attributes = {
    "beauty":        ["Ugly"            ,"Plain"          ,"Cute"          ,"Pretty   "    ,"Beautiful"    ,"Exquisite"      ,"Goddess"     ,"{b}BEAUTY:{/b}\n  Natural beauty very strongly influences her market price. Your slave's rank will never rise higher than her beauty or fame (whichever is higher). At auctions, beautiful slaves are sold for higher prices.","   ll your efforts to improve the appearance of the slave will influence style, not beauty. Stylishness is important too, but the value of natural beauty is huge. You can increase beauty only by neoplasty surgery in the Technosphere medical center and only once for each slave. Try to buy beautiful slaves if you intend to train them to high ranks. Beauty is decreased while a slave has scars or bruises until they are removed or healed."],
    "endurance":     ["Dyinng"          ,"Feeble"         ,"Weakened"      ,"Healthy"      ,"Tough"        ,"Enduring"       ,"Iron"        ,"{b}ENDURANCE:{/b}\n  Hardy slaves have more energy, can work better and are more attractive for clients. Critical decrease of endurance can kill your slave.","   If your slave is weak, feed her well; it's desirable to prescribe supplements and not let her become exhausted (receive red energy stars), nor over-exercise (when she has purple energy stars, intensive exercise is harmful), nor gain weight if she is overweight, nor end the day with negative calories. Build endurance with gymnastics, athletics, dance, racing, martial arts, pet play or vigorous sex. Heal injuries (a nurse assistant and your own skill helps) and sicknesses, and use drugs sparingly."],
    "empathy":       ["Heartless"       ,"Callous"        ,"Insensitive"   ,"Sensitive"    ,"Caring"       ,"Nurturing"      ,"Nurturing+"  ,"{b}EMPATHY:{/b}\n  On one hand the gentle slave is easier affected by stress and stung by punishments. On the other hand she is turned on much faster and is more lively, which makes her attractive for customers.","   Callousness develops quickly with mistreatment. Severe punishments are especially harmful. While a less sensitive slave is hardened against depression and endures suffering, she is also less valuable. There are no reliable ways to increase a slave's empathy, but refined petting and pleasures may help."],
    "temperament":   ["Apathetic"       ,"Cold"           ,"Reserved"      ,"Reactive"     ,"Lively"       ,"Passionate"     ,"Passionate+" ,"{b}TEMPERAMENT:{/b}\n  Temperamental slaves are uncontrollable and are less susceptible to education but they are passionate lovers and are more interesting for customers, as they have a bright personality. Calm ones are easier to control.","   Temperament is an ambiguous feature. More emotional slaves are harder to control, but cold ones are less valuable. By suppressing initiative, driving her into depression and silencing her you will eventually lower her temperament. Getting her to express herself or interact openly with the slaver will often increase temperament."],
    "intelligence":  ["Retarded"        ,"Stupid"         ,"Dimwitted"     ,"Bright"       ,"Clever"       ,"Intelligent"    ,"Genius"      ,"{b}INTELLIGENCE:{/b}\n  Smart slaves master skills faster and are able to cope with accounting better, so they are more valuable on the market. But it is easier to dominate and manipulate stupid ones.","   Smarts are not always useful, as more intellectual slaves are harder to control and manipulate. On the other hand, rational factors of submission and explanatory conversations will be more effective. Allowing a slave to express herself, training secretarial skills and doing household accounting can contribute to intellectual development."],
    "nature":        ["Spineless"       ,"Coward"         ,"Uncertain"     ,"Independent"  ,"Determined"   ,"Willful"        ,"Willful+"    ,"{b}NATURE:{/b}\n  Strong character makes a slave more interesting and independent but lowers her obedience. It is easier to control weak-willed slaves but their value will be lower too.","   Nature is an ambiguous feature. It is very hard to train a willful slave, but a weak will lowers a slave's value. The more you make a slave do what she does not want to do, the more her nature will break. It is difficult to restore nature, so do not overdo it. Victory in duels, martial arts, sleeping in her own room, assisting in training other slaves, and being given a measure of independence or opportunities to socialize can help in the formation of a solid nature."],
    "pride":         ["Arrogant"        ,"Haughty"        ,"Proud"         ,"Aloof"        ,"Open"         ,"Unashamed"      ,"Unashamed+"  ,"{b}PRIDE:{/b}\n  Pride prevents a slave from being open and enjoying sex. It also causes her to resist your will, and refuse humiliating orders.","   Pride is harmful both in training and in the sale, so you should work on her openness. Force her to do dirty, perverted and degrading things, and assign strict rules. Eventually pride will be broken and the slave will become more open. But do not overdo it, as with pride, you can break the very slave."],
    "exoticism":     ["Ordinary"        ,"Quirky"         ,"Mysterious"    ,"Enigmatic"    ,"Exotic"       ,"Mystical"       ,"Mythical+"   ,"{b}EXOTICISM:{/b}\n  Slaves with unusual, irregular appearance attract attention at once and generally are more interesting for customers.","   Some slaves are exotic inherently. You can increase exoticism with tattoos, piercings, body modifications, as well as flamboyant clothes and wigs."],
    "physical":      ["Corpulent"       ,"Chubby"         ,"Voluptuous"    ,"Slender"      ,"Model"        ,"Bony"           ,"Model+"      ,"{b}PHYSICAL:{/b}\n  You can get more mince from fat slaves but they are not attractive. Weedy starvelings aren't attractive as well, but you can't get a lot of meat from them either. It's better to keep your slave slim, but not skinny.","   Extra weight is generally harmful, as well as a lack of it. To keep your slave slim you need to balance her nutrition in a way that is sufficient, but not excessive. The more a slave works and the more endurance she has, the more food she needs. Physical exercises don't decrease weight directly but are a good way to burn extra calories. If a slave is underweight, feed her well and minimize athletics."],
    "style":         ["Unfashionable"   ,"Unremarkable"   ,"Common"        ,"Stylish"      ,"Refined"      ,"Elegant"        ,"Elegant+"    ,"{b}STYLE:{/b}\n  A slave's appearance is extremely important during the sale. Customers will like well-groomed and well-dressed slaves, and an unappealing slave can be turned down even if she fits the requirements.","   Style depends little on natural abilities and skills, though it is influenced by the ability to communicate (elocution) and presence (dancing). Style suffers from dirt and sloppiness. Hairstyle, make-up, perfume, beautiful clothes and jewelry - all of these improve style and make the slave more attractive to customers. It is not necessary to constantly maintain style - it plays a role only when it is time to show the girl to the customer."],
    "fame":          ["Unknown"         ,"Rumored"        ,"Recognized"    ,"Celebrity"    ,"Famous"       ,"Legendary"      ,"Legendary+"  ,"{b}FAME:{/b}\n  Famous slaves are much more valuable. Your slave's rank can reach the level of her fame, even if she lacks other attributes, beauty included.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum."]
    }
define dic_slave_skills = {
    "maid": ["Not a Maid F-", "Drudge D-", "Skivvy C-", "Maid B+", "Handmaid A+", "Housekeeper S+", "Mistress of the Manor S++"],
    "cooking": ["Not a Cook F-", "Scullery Trainee D-", "Kitchener C-", "Cook B+", "Chef A+", "Culinary Artist S+", "Gastronomic Legend S++"],
    "secretary": ["Not a Secretary F-", "Paper Shuffler D-", "Novice Clerk C-", "Secretary B+", "Comptroller A+", "Procurator S+", "Chancellor of Ledgers S++"],
    "elocution": ["Not an Elocutionist F-", "Inarticulate D-", "Raconteuse C-", "Elocutionist B+", "Orator A+", "Rhetorician S+", "Voice of the Realm S++"],
    "nursing": ["Not a Nurse F-", "Anatomy Student D-", "Triage Aid C-", "Nurse B+", "Ward Sister A+", "Matron S+", "Healer Supreme S++"],
    "alchemy": ["Not an Alchemist F-", "Potion Apprentice D-", "Alembic Attendant C-", "Alchemist B+", "Arcanist A+", "Mistress of Arcanum S+", "Transmuter of Essence S++"],
    "witchcraft": ["Not a Witch F-", "Young Hag D-", "Theurgist C-", "Witch B+", "Enchantress A+", "Sorceress S+", "Archwitch Eternal S++"],
    "athletics": ["Bedridden F-", "Plodder D-", "Walker C-", "Athlete B+", "Sprinter A+", "Marathonist S+", "Olympian S++"],
    "gladiatrix": ["Not a Gladiatrix F-", "Bustuāria D-", "Prōvocātrīx C-", "Gladiatrix B+", "Bellātrīx A+", "Amazon S+", "Queen Amazon S++"],
    "dance": ["Not a Dancer F-", "Two Left Feet D-", "Figurant C-", "Dancer B+", "Coryphée A+", "Étoile S+", "Divine Muse S++"],
    "music": ["Not a Musician F-", "Solfège Initiate D-", "Trained Ear C-", "Musician B+", "Prodigy A+", "Virtuoso S+", "Maestra S++"],
    "painting": ["Not a Painter F-", "Dauber D-", "Sketcher C-", "Painter B+", "Colorist A+", "Artifex S+", "Master of the Canvas S++"],
    "pet": ["Not a Pet F-", "Feral D-", "Housebroken C-", "Pet B+", "Domesticated A+", "Animalistic S+", "Primal Companion S++"],
    "pony": ["Not a Pony F-", "Nag D-", "Hackney C-", "Pony B+", "Trotter A+", "Racehorse S+", "Champion Steed S++"],
    "cow": ["Not a Cow F-", "Barely Bovine D-", "Learning to Moo C-", "Cow B+", "Heifer A+", "Queen of Kine S+", "Divine Bovine S++"],
}
define dic_slave_skills_sexual = {
    "oral_pleasure": ["Oral Pleasure F-", "Oral Pleasure D-", "Oral Pleasure C-", "Oral Pleasure B+", "Oral Pleasure A+", "Oral Pleasure S+", "Oral Pleasure S++"],
    "penetration": ["Penetration F-", "Penetration D-", "Penetration C-", "Penetration B+", "Penetration A+", "Penetration S+", "Penetration S++"],
    "orgy": ["Group Sex F-", "Group Sex D-", "Group Sex C-", "Group Sex B+", "Group Sex A+", "Group Sex S+", "Group Sex S++"],
    "roleplay": ["Demonstration F-", "Demonstration D-", "Demonstration C-", "Demonstration B+", "Demonstration A+", "Demonstration S+", "Demonstration S++"],
    "fetishism": ["Fetishism F-", "Fetishism D-", "Fetishism C-", "Fetishism B+", "Fetishism A+", "Fetishism S+", "Fetishism S++"],
    "xenophily": ["Xenophily F-", "Xenophily D-", "Xenophily C-", "Xenophily B+", "Xenophily A+", "Xenophily S+", "Xenophily S++"]
}
define dic_traits_skills = {
    "maidtrait":         ["Average", "Good Maid", "Excellent Maid", "Disastrous Maid", "Bad Maid"],
    "cookingtrait":      ["Average", "Good Cook", "Excellent Cook", "Disastrous Cook", "Bad Cook"],
    "secretarytrait":    ["Average", "Good Secretary", "Excellent Secretary", "Disastrous Secretary", "Bad Secretary"],
    "elocutiontrait":    ["Average", "Good Speaker", "Excellent Speaker", "Disastrous Speaker", "Bad Speaker"],
    "nursingtrait":      ["Average", "Good Nurse", "Excellent Nurse", "Disastrous Nurse", "Bad Nurse"],
    "alchemytrait":      ["Average", "Good Alchemist", "Excellent Alchemist", "Disastrous Alchemist", "Bad Alchemist"],
    "witchcrafttrait":   ["Average", "Good Witch", "Excellent Witch", "Disastrous Witch", "Bad Witch"],
    "athleticstrait":    ["Average", "Good Athlete", "Excellent Athlete", "Disastrous Athlete", "Bad Athlete"],
    "gladiatrixtrait":   ["Average", "Good Gladiatrix", "Excellent Gladiatrix", "Disastrous Gladiatrix", "Bad Gladiatrix"],
    "dancetrait":        ["Average", "Good Dancer", "Excellent Dancer", "Disastrous Dancer", "Bad Dancer"],
    "musictrait":        ["Average", "Good Musician", "Excellent Musician", "Disastrous Musician", "Bad Musician"],
    "paintingtrait":     ["Average", "Good Painter", "Excellent Painter", "Disastrous Painter", "Bad Painter"],
    "pettrait":          ["Average", "Good Pet", "Excellent Pet", "Disastrous Pet", "Bad Pet"],
    "ponytrait":         ["Average", "Good Pony", "Excellent Pony", "Disastrous Pony", "Bad Pony"],
    "cowtrait":          ["Average", "Good Cow", "Excellent Cow", "Disastrous Cow", "Bad Cow"]
}
define dic_traits_skills_descriptions = {
    "maidtrait": [
        "Null",
        "{b}Good Maid{/b} \nYour slave seems to take great pleasure in keeping order in the house. This will allow her to become an excellent maid!",
        "{b}Excellent Maid{/b} \nYour slave seems to take great pleasure in keeping order in the house. This will allow her to become an excellent maid! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Maid{/b} \nYour slave shows little interest in maintaining order around the house. Becoming a good maid may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Maid{/b} \nYour slave shows little interest in maintaining order around the house. Becoming a good maid may prove difficult for her."
    ],
    "cookingtrait": [
        "Null",
        "{b}Good Cook{/b} \nYour slave enjoys cooking and often prepares tasty meals. This will allow her to become an excellent cook!",
        "{b}Excellent Cook{/b} \nYour slave enjoys cooking and often prepares tasty meals. This will allow her to become an excellent cook! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Cook{/b} \nYour slave shows little interest in cooking. Becoming a good cook may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Cook{/b} \nYour slave shows little interest in cooking. Becoming a good cook may prove difficult for her."
    ],
    "secretarytrait": [
        "Null",
        "{b}Good Secretary{/b} \nYour slave has excellent instincts for a personal assistant – she is collected, attentive, and easily copes with paperwork. You should use this talent to its maximum!",
        "{b}Excellent Secretary{/b} \nYour slave has excellent instincts for a personal assistant – she is collected, attentive, and easily copes with paperwork. You should use this talent to its maximum! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Secretary{/b} \nYour slave shows little interest in administrative tasks. Becoming a good secretary may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Secretary{/b} \nYour slave shows little interest in administrative tasks. Becoming a good secretary may prove difficult for her."
    ],
    "elocutiontrait": [
        "Null",
        "{b}Good Speaker{/b} \nYour slave shows a talent for self-expression. Developing her etiquette and rhetoric will be easy, and this is clearly good news!",
        "{b}Excellent Speaker{/b} \nYour slave shows a talent for self-expression. Developing her etiquette and rhetoric will be easy, and this is clearly good news! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Speaker{/b} \nYour slave shows little interest in speaking skills. Becoming a good orator may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Speaker{/b} \nYour slave shows little interest in speaking skills. Becoming a good orator may prove difficult for her."
    ],
    "nursingtrait": [
        "Null",
        "{b}Good Nurse{/b} \nYour slave shows care and attention toward others. This will allow her to become an excellent nurse!",
        "{b}Excellent Nurse{/b} \nYour slave shows care and attention toward others. This will allow her to become an excellent nurse! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Nurse{/b} \nYour slave shows little interest in nursing. Becoming a good nurse may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Nurse{/b} \nYour slave shows little interest in nursing. Becoming a good nurse may prove difficult for her."
    ],
    "alchemytrait": [
        "Null",
        "{b}Good Alchemist{/b} \nYour slave enjoys experimenting with potions and ingredients. This will allow her to become an excellent alchemist!",
        "{b}Excellent Alchemist{/b} \nYour slave enjoys experimenting with potions and ingredients. This will allow her to become an excellent alchemist! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Alchemist{/b} \nYour slave shows little interest in alchemy. Becoming a good alchemist may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Alchemist{/b} \nYour slave shows little interest in alchemy. Becoming a good alchemist may prove difficult for her."
    ],
    "witchcrafttrait": [
        "Null",
        "{b}Good Witch{/b} \nYour slave is attuned to magical forces. This will allow her to become an excellent witch!",
        "{b}Excellent Witch{/b} \nYour slave is attuned to magical forces. This will allow her to become an excellent witch! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Witch{/b} \nYour slave shows little interest in witchcraft. Becoming a good witch may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Witch{/b} \nYour slave shows little interest in witchcraft. Becoming a good witch may prove difficult for her."
    ],
    "athleticstrait": [
        "Null",
        "{b}Good Athlete{/b} \nYour slave is energetic and enjoys physical activity. This will allow her to become an excellent athlete!",
        "{b}Excellent Athlete{/b} \nYour slave is energetic and enjoys physical activity. This will allow her to become an excellent athlete! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Athlete{/b} \nYour slave shows little interest in athletics. Becoming a good athlete may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Athlete{/b} \nYour slave shows little interest in athletics. Becoming a good athlete may prove difficult for her."
    ],
    "gladiatrixtrait": [
        "Null",
        "{b}Good Gladiatrix{/b} \nYour slave shows confidence and determination in combat training. This will allow her to become an excellent gladiatrix!",
        "{b}Excellent Gladiatrix{/b} \nYour slave shows confidence and determination in combat training. This will allow her to become an excellent gladiatrix! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Gladiatrix{/b} \nYour slave shows little interest in combat training. Becoming a good gladiatrix may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Gladiatrix{/b} \nYour slave shows little interest in combat training. Becoming a good gladiatrix may prove difficult for her."
    ],
    "dancetrait": [
        "Null",
        "{b}Good Dancer{/b} \nYour slave moves gracefully and enjoys expressing herself through dance. This will allow her to become an excellent dancer!",
        "{b}Excellent Dancer{/b} \nYour slave moves gracefully and enjoys expressing herself through dance. This will allow her to become an excellent dancer! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Dancer{/b} \nYour slave shows little interest in dancing. Becoming a good dancer may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Dancer{/b} \nYour slave shows little interest in dancing. Becoming a good dancer may prove difficult for her."
    ],
    "musictrait": [
        "Null",
        "{b}Good Musician{/b} \nYour slave enjoys playing music and has a good sense of rhythm. This will allow her to become an excellent musician!",
        "{b}Excellent Musician{/b} \nYour slave enjoys playing music and has a good sense of rhythm. This will allow her to become an excellent musician! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Musician{/b} \nYour slave shows little interest in music. Becoming a good musician may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Musician{/b} \nYour slave shows little interest in music. Becoming a good musician may prove difficult for her."
    ],
    "paintingtrait": [
        "Null",
        "{b}Good Painter{/b} \nYour slave has a good eye for detail and enjoys creating art. This will allow her to become an excellent painter!",
        "{b}Excellent Painter{/b} \nYour slave has a good eye for detail and enjoys creating art. This will allow her to become an excellent painter! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Painter{/b} \nYour slave shows little interest in painting. Becoming a good painter may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Painter{/b} \nYour slave shows little interest in painting. Becoming a good painter may prove difficult for her."
    ],
    "pettrait": [
        "Null",
        "{b}Good Pet{/b} \nIt seems that your slave really likes to pretend to be a pet. And, most importantly, she is doing it great. Training will go well!",
        "{b}Excellent Pet{/b} \nIt seems that your slave really likes to pretend to be a pet. And, most importantly, she is doing it great. Training will go well! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Pet{/b} \nYour slave shows little interest in pet play. Becoming a good pet may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Pet{/b} \nYour slave shows little interest in pet play. Becoming a good pet may prove difficult for her."
    ],
    "ponytrait": [
        "Null",
        "{b}Good Pony{/b} \nApparently, your slave loves to be a horse. What others would consider humiliating and difficult, she finds fun and interesting. This will allow her to become an excellent pony!",
        "{b}Excellent Pony{/b} \nApparently, your slave loves to be a horse. What others would consider humiliating and difficult, she finds fun and interesting. This will allow her to become an excellent pony! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Pony{/b} \nYour slave shows little interest in pony play. Becoming a good pony may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Pony{/b} \nYour slave shows little interest in pony play. Becoming a good pony may prove difficult for her."
    ],
    "cowtrait": [
        "Null",
        "{b}Good Cow{/b} \nYour slave is not in a hurry to use her body or her mind, and likes to just loaf: perhaps she could be more easily turned into a milk cow?",
        "{b}Excellent Cow{/b} \nYour slave is not in a hurry to use her body or her mind, and likes to just loaf: perhaps she could be more easily turned into a milk cow? She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Disastrous Cow{/b} \nYour slave shows little interest in the cow lifestyle. Becoming a good cow slave may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Bad Cow{/b} \nYour slave shows little interest in the cow lifestyle. Becoming a good cow slave may prove difficult for her."
    ]
}
define dic_traits_sexual = {
    "pettingtrait":      ["None", "Likes Petting", "Loves Petting", "Hates Petting", "Dislikes Petting"],
    "oral_pleasuretrait":["None", "Likes Oral Pleasure", "Loves Oral Pleasure", "Hates Oral Pleasure", "Dislikes Oral Pleasure"],
    "penetrationtrait":  ["None", "Likes Penetration", "Loves Penetration", "Hates Penetration", "Dislikes Penetration"],
    "group_sextrait":    ["None", "Likes Group Sex", "Loves Group Sex", "Hates Group Sex", "Dislikes Group Sex"],
    "demotrationtrait":  ["None", "Likes Demonstrations", "Loves Demonstrations", "Hates Demonstrations", "Dislikes Demonstrations"],
    "fetishismtrait":    ["None", "Likes Fetishism", "Loves Fetishism", "Hates Fetishism", "Dislikes Fetishism"],
    "xenophily":         ["None", "Likes Xenophily", "Loves Xenophily", "Hates Xenophily", "Dislikes Xenophily"]
}

define dic_traits_sexual_description = {
    "pettingtrait": [
        "Null",
        "{b}Likes Petting{/b} \nYour slave absolutely loves being petted and craves physical closeness. This will greatly enhance her sensuality!",
        "{b}Loves Petting{/b} \nYour slave absolutely loves being petted and craves physical closeness. This will greatly enhance her sensuality! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Petting{/b} \nYour slave shows little interest in petting and gentle touch. Becoming affectionate may prove difficult for her. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Petting{/b} \nYour slave shows little interest in petting and gentle touch. Becoming affectionate may prove difficult for her."
    ],
    "oral_pleasuretrait": [
        "Null",
        "{b}Likes Oral Pleasure{/b} \nYour slave has a strong passion for oral intimacy and excels at it. This will heighten her desirability!",
        "{b}Loves Oral Pleasure{/b} \nYour slave has a strong passion for oral intimacy and excels at it. This will heighten her desirability! She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Oral Pleasure{/b} \nYour slave shows little interest in oral pleasure. Developing skills here may be challenging. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Oral Pleasure{/b} \nYour slave shows little interest in oral pleasure. Developing skills here may be challenging."
    ],
    "penetrationtrait": [
        "Null",
        "{b}Likes Penetration{/b} \nYour slave loves penetration and finds great pleasure in it, enhancing her sexual experiences.",
        "{b}Loves Penetration{/b} \nYour slave loves penetration and finds great pleasure in it, enhancing her sexual experiences. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Penetration{/b} \nYour slave dislikes penetration and avoids it whenever possible. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Penetration{/b} \nYour slave dislikes penetration and avoids it whenever possible."
    ],
    "group_sextrait": [
        "Null",
        "{b}Likes Group Sex{/b} \nYour slave loves group sex and thrives in shared intimate situations.",
        "{b}Loves Group Sex{/b} \nYour slave loves group sex and thrives in shared intimate situations. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Group Sex{/b} \nYour slave shows little interest in group sex and prefers one-on-one encounters. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Group Sex{/b} \nYour slave shows little interest in group sex and prefers one-on-one encounters."
    ],
    "demotrationtrait": [
        "Null",
        "{b}Likes Demonstrations{/b} \nYour slave loves being the center of attention and enjoys sexual demonstrations.",
        "{b}Loves Demonstrations{/b} \nYour slave loves being the center of attention and enjoys sexual demonstrations. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Demonstrations{/b} \nYour slave shows little interest in demonstrating her skills openly. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Demonstrations{/b} \nYour slave shows little interest in demonstrating her skills openly."
    ],
    "fetishismtrait": [
        "Null",
        "{b}Likes Fetishism{/b} \nYour slave loves exploring fetishes and alternative sexual interests.",
        "{b}Loves Fetishism{/b} \nYour slave loves exploring fetishes and alternative sexual interests. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Fetishism{/b} \nYour slave shows little interest in fetishism and prefers vanilla intimacy. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Fetishism{/b} \nYour slave shows little interest in fetishism and prefers vanilla intimacy."
    ],
    "xenophily": [
        "Null",
        "{b}Likes Xenophily{/b} \nYour slave loves trying new experiences and partners, showing strong xenophily.",
        "{b}Loves Xenophily{/b} \nYour slave loves trying new experiences and partners, showing strong xenophily. She has a natural talent for this skill, which will allow her to reach new heights.",
        "{b}Hates Xenophily{/b} \nYour slave shows little interest in unfamiliar partners or new experiences. She lacks talent in this area, which will limit her potential for improvement.",
        "{b}Dislikes Xenophily{/b} \nYour slave shows little interest in unfamiliar partners or new experiences."
    ]
}
define dic_traits_miscellaneous = {
    "lust_driver":       ["None", "Pervert", "Nymphomanic", "Asexual", "frigid"],
    "masochism":         ["None", "Accustomed to pain", "Masochism", "Pain averse", "Pain sensitive"],
    "exhibitionism":     ["None", "Likes Exhibitionism", "Loves Exhibitionism", "Hates Exhibitionism", "Dislikes Exhibitionism"],
    "sexual_orientation":["None", "Bi-curious", "Bisexual", "Homosexual", "Homoflexible"],
    "abuse_attitude":    ["None", "Likes Roughness", "Loves Roughness", "Hates Roughness", "Dislikes Roughness"],
    "darkness_attitude": ["None", "Likes Darkness", "Loves Darkness", "Hates Darkness", "Dislikes Darkness"],
    "blood_attitude":    ["None", "Likes Blood", "Loves Blood", "Hates Blood", "Dislikes Blood"],
    "fire_attitude":     ["None", "Likes Fire", "Loves Fire", "Hates Fire", "Dislikes Fire"],
    "water_attitude":    ["None", "Likes Water", "Loves Water", "Hates Water", "Dislikes Water"],
    "spider_attitude":   ["None", "Likes Spiders", "Loves Spiders", "Hates Spiders", "Dislikes Spiders"],
    "passion_comfort":   ["None", "Likes Comfort", "Loves Comfort", "Hates Comfort", "Dislikes Comfort"],
    "passion_fame":      ["None", "Likes Fame", "Loves Fame", "Hates Fame", "Dislikes Fame"],
    "passion_luxury":    ["None", "Likes Luxury", "Loves Luxury", "Hates Luxury", "Dislikes Luxury"],
    "passion_sweets":    ["None", "Likes Sweets", "Loves Sweets", "Hates Sweets", "Dislikes Sweets"],
    "fertility":         ["None", "Fertile", "Very Fertile", "Very Infertile", "Infertile"]
}

define dic_traits_miscellaneous_description = {
    "lust_driver": [
        "Null",
        "{b}Pervert{/b}\nYour slave shows a noticeable sexual drive, which influences her desires and responsiveness.",
        "{b}Nymphomanic{/b}\nYour slave is a nymphomaniac, constantly craving and seeking out sexual pleasure.",
        "{b}Asexual{/b}\nYour slave is completely asexual, showing no interest in sexual activity, which greatly limits intimacy.",
        "{b}frigid{/b}\nYour slave is frigid and indifferent to sexual advances, making sexual connection very difficult."
    ],
    "masochism": [
        "Null",
        "{b}Accustomed to pain{/b}\nYour slave is somewhat accustomed to pain and can tolerate it in intimate settings.",
        "{b}Masochism{/b}\nYour slave embraces masochism, finding pleasure in pain and submission.",
        "{b}Pain averse{/b}\nYour slave is extremely pain averse, avoiding even mild discomfort during intimacy.",
        "{b}Pain sensitive{/b}\nYour slave is highly sensitive to pain and any discomfort greatly distresses her."
    ],
    "exhibitionism": [
        "Null",
        "{b}Likes Exhibitionism{/b}\nYour slave occasionally enjoys being watched during intimate moments.",
        "{b}Loves Exhibitionism{/b}\nYour slave loves exhibitionism and thrills at the idea of being seen.",
        "{b}Hates Exhibitionism{/b}\nYour slave strongly fears or hates exhibitionism, finding it very distressing.",
        "{b}Dislikes Exhibitionism{/b}\nYour slave is deeply uncomfortable with any form of exposure or being watched."
    ],
    "sexual_orientation": [
        "Null",
        "{b}Bi-curious{/b}\nYour slave is bi-curious, open to exploring her sexuality with different genders.",
        "{b}Bisexual{/b}\nYour slave identifies as bisexual and embraces attraction to multiple genders.",
        "{b}Homosexual{/b}\nYour slave is exclusively homosexual, showing strong preference for the same sex.",
        "{b}Homoflexible{/b}\nYour slave is homoflexible, mostly attracted to one sex but occasionally open."
    ],
    "abuse_attitude": [
        "Null",
        "{b}Likes Roughness{/b}\nYour slave likes roughness in intimacy, which adds excitement to her experiences.",
        "{b}Loves Roughness{/b}\nYour slave loves roughness and seeks dominant, forceful encounters.",
        "{b}Hates Roughness{/b}\nYour slave strongly dislikes roughness and prefers gentle, tender interactions.",
        "{b}Dislikes Roughness{/b}\nYour slave is deeply averse to any rough or abusive behavior during intimacy."
    ],
    "darkness_attitude": [
        "Null",
        "{b}Likes Darkness{/b}\nYour slave likes the allure of darkness and mystery in her intimate moments.",
        "{b}Loves Darkness{/b}\nYour slave loves darkness, finding it stimulating and intriguing.",
        "{b}Hates Darkness{/b}\nYour slave strongly dislikes darkness and prefers well-lit environments.",
        "{b}Dislikes Darkness{/b}\nYour slave is deeply uncomfortable or fearful of darkness."
    ],
    "blood_attitude": [
        "Null",
        "{b}Likes Blood{/b}\nYour slave has a mild fascination with blood in her erotic play.",
        "{b}Loves Blood{/b}\nYour slave loves incorporating blood into her intimate experiences.",
        "{b}Hates Blood{/b}\nYour slave strongly dislikes blood and avoids any activity that involves it.",
        "{b}Dislikes Blood{/b}\nYour slave is disturbed by blood and cannot tolerate it."
    ],
    "fire_attitude": [
        "Null",
        "{b}Likes Fire{/b}\nYour slave enjoys the warmth and thrill that fire brings to intimacy.",
        "{b}Loves Fire{/b}\nYour slave loves fire play and finds it deeply arousing.",
        "{b}Hates Fire{/b}\nYour slave strongly fears fire and avoids any related activities.",
        "{b}Fears Fire{/b}\nYour slave fears fire and refuses any exposure to it."
    ],
    "water_attitude": [
        "Null",
        "{b}Likes Water{/b}\nYour slave likes water and often enjoys aquatic intimacy.",
        "{b}Loves Water{/b}\nYour slave loves water play and finds it sensual and refreshing.",
        "{b}Hates Water{/b}\nYour slave strongly dislikes water and avoids any contact.",
        "{b}Dislikes Water{/b}\nYour slave is uncomfortable with water and refuses any contact."
    ],
    "spider_attitude": [
        "Null",
        "{b}Likes Spiders{/b}\nYour slave is somewhat curious about spiders and their symbolism.",
        "{b}Loves Spiders{/b}\nYour slave loves spiders and loves to include them in her fantasy play.",
        "{b}Hates Spiders{/b}\nYour slave strongly fears or dislikes spiders and panics at the sight of them.",
        "{b}Terrified of Spiders{/b}\nYour slave is terrified of spiders and avoids them."
    ],
    "passion_comfort": [
        "Null",
        "{b}Likes Comfort{/b}\nYour slave likes comfort and values cozy, safe environments.",
        "{b}Loves Comfort{/b}\nYour slave loves comfort and seeks luxurious relaxation.",
        "{b}Dislikes Comfort{/b}\nYour slave dislikes comfort, finding it restrictive or dull.",
        "{b}Rejects Comfort{/b}\nYour slave rejects comfort entirely and prefers harsh conditions."
    ],
    "passion_fame": [
        "Null",
        "{b}Likes Fame{/b}\nYour slave likes the idea of fame and recognition.",
        "{b}Loves Fame{/b}\nYour slave loves being famous and craves public attention.",
        "{b}Dislikes Fame{/b}\nYour slave strongly dislikes fame and shuns the spotlight.",
        "{b}Uncomfortable with Fame{/b}\nYour slave is deeply uncomfortable with any form of recognition."
    ],
    "passion_luxury": [
        "Null",
        "{b}Likes Luxury{/b}\nYour slave enjoys luxury and the finer things in life.",
        "{b}Loves Luxury{/b}\nYour slave loves luxury and indulges in extravagance.",
        "{b}Dislikes Luxury{/b}\nYour slave strongly dislikes luxury and prefers simplicity.",
        "{b}Rejects Luxury{/b}\nYour slave rejects luxury completely and avoids indulgence."
    ],
    "passion_sweets": [
        "Null",
        "{b}Likes Sweets{/b}\nYour slave likes sweets and enjoys occasional treats.",
        "{b}Loves Sweets{/b}\nYour slave loves sweets and often craves sugary delights.",
        "{b}Dislikes Sweets{/b}\nYour slave strongly dislikes sweets and avoids sugary foods.",
        "{b}Aversion to Sweets{/b}\nYour slave has a strong aversion to sweets and refuses them."
    ],
    "fertility": [
        "Null",
        "{b}Fertile{/b}\nYour slave is fertile and capable of conceiving children.",
        "{b}Very Fertile{/b}\nYour slave is very fertile and likely to conceive easily.",
        "{b}Very Infertile{/b}\nYour slave is very infertile and has very little chance to conceive children.",
        "{b}Infertile{/b}\nYour slave is infertile, with little chance of conception."
    ]
}
define dic_traits_aura = {
    "feartrait":       ["None", "Fearful", "Terrified", "Moronic", "Brave"],
    "despairtrait":    ["None", "Positive", "High-spirited", "Crushed Spirit", "Hopeless"],
    "awarenesstrait":  ["None", "Observant", "Highly Perceptive", "Oblivious", "Clueless"],
    "tamingtrait":     ["None", "Easily Tamed", "Naturally Submissive", "Untamable", "Rebellious"],
    "habittrait":      ["None", "Well-behaved", "Disciplined", "Undisciplined", "Inconsistent"],
    "spoiltrait":      ["None", "Self-sufficient", "Stoic", "Spoiled Rotten", "Pampered"],
    "devotiontrait":   ["None", "Loyal", "Fanatically Devoted", "Disloyal", "Detached"]
}

define dic_traits_aura_description = {
    "feartrait": [
        "None",
        "{b}Fearful{/b} \nYour slave shows a healthy level of fear that ensures obedience and respect. She is deeply fearful and compliant, making her extremely easy to control.",
        "{b}Terrified{/b} \nYour slave shows a healthy level of fear that ensures obedience and respect. She is deeply fearful and compliant, making her extremely easy to control. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Moronic{/b} \nYour slave is brave and unshaken, which may hinder submissive training. She lacks any fear or caution, acting recklessly and challenging authority. She has a dim aura, which will limit her potential for improvement.",
        "{b}Brave{/b} \nYour slave is brave and unshaken, which may hinder submissive training. She lacks any fear or caution, acting recklessly and challenging authority."
    ],
    "despairtrait": [
        "None",
        "{b}Positive{/b} \nYour slave remains optimistic and adapts well to her circumstances. She is exceptionally spirited and unshakably hopeful, even in adversity.",
        "{b}High-spirited{/b} \nYour slave remains optimistic and adapts well to her circumstances. She is exceptionally spirited and unshakably hopeful, even in adversity. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Crushed Spirit{/b} \nYour slave has become hopeless and emotionally unstable. Her spirit is completely crushed, making it hard for her to recover emotionally. She has a dim aura, which will limit her potential for improvement.",
        "{b}Hopeless{/b} \nYour slave has become hopeless and emotionally unstable. Her spirit is completely crushed, making it hard for her to recover emotionally."
    ],
    "awarenesstrait": [
        "None",
        "{b}Observant{/b} \nYour slave is observant and notices small details others may miss. She is highly perceptive and aware of her surroundings and dynamics.",
        "{b}Highly Perceptive{/b} \nYour slave is observant and notices small details others may miss. She is highly perceptive and aware of her surroundings and dynamics. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Oblivious{/b} \nYour slave is clueless and slow to catch on to changes or instructions. She is oblivious to what's going on, which limits her effectiveness. She has a dim aura, which will limit her potential for improvement.",
        "{b}Clueless{/b} \nYour slave is clueless and slow to catch on to changes or instructions. She is oblivious to what's going on, which limits her effectiveness."
    ],
    "tamingtrait": [
        "None",
        "{b}Easily Tamed{/b} \nYour slave is easily guided and responds well to training. She is naturally submissive and quickly accepts her role.",
        "{b}Naturally Submissive{/b} \nYour slave is easily guided and responds well to training. She is naturally submissive and quickly accepts her role. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Untamable{/b} \nYour slave is rebellious and resists taming efforts. She is wild and rejects all forms of control or authority. She has a dim aura, which will limit her potential for improvement.",
        "{b}Rebellious{/b} \nYour slave is rebellious and resists taming efforts. She is wild and rejects all forms of control or authority."
    ],
    "habittrait": [
        "None",
        "{b}Well-behaved{/b} \nYour slave behaves properly and follows routine with little guidance. She is highly disciplined and consistent in her actions.",
        "{b}Disciplined{/b} \nYour slave behaves properly and follows routine with little guidance. She is highly disciplined and consistent in her actions. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Undisciplined{/b} \nYour slave is inconsistent and unreliable in her behavior. She struggles with following rules and frequently acts out. She has a dim aura, which will limit her potential for improvement.",
        "{b}Inconsistent{/b} \nYour slave is inconsistent and unreliable in her behavior. She struggles with following rules and frequently acts out."
    ],
    "spoiltrait": [
        "None",
        "{b}Self-sufficient{/b} \nYour slave is content with little and rarely demands special treatment. She remains stoic and emotionally resilient, even without luxury.",
        "{b}Stoic{/b} \nYour slave is content with little and rarely demands special treatment. She remains stoic and emotionally resilient, even without luxury. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Spoiled Rotten{/b} \nYour slave is pampered and expects constant comfort and attention. She is spoiled rotten and throws tantrums if not indulged. She has a dim aura, which will limit her potential for improvement.",
        "{b}Pampered{/b} \nYour slave is pampered and expects constant comfort and attention. She is spoiled rotten and throws tantrums if not indulged."
    ],
    "devotiontrait": [
        "None",
        "{b}Loyal{/b} \nYour slave is loyal and shows clear dedication to her master. She is fanatically devoted and lives to serve without question.",
        "{b}Fanatically Devoted{/b} \nYour slave is loyal and shows clear dedication to her master. She is fanatically devoted and lives to serve without question. She has a bright aura with a special intensity, which will allow her to reach new heights.",
        "{b}Disloyal{/b} \nYour slave is emotionally detached and resists forming bonds. She is disloyal and may turn against her master when challenged. She has a dim aura, which will limit her potential for improvement.",
        "{b}Detached{/b} \nYour slave is emotionally detached and resists forming bonds. She is disloyal and may turn against her master when challenged."
    ]
}
define dic_traits_attributes = {
    "beautytrait":       ["None", "Attractive", "Divine beauty", "Hideous", "Unattractive"],
    "endurancetrait":    ["None", "Tough", "Fortitude", "Very Frail", "Weak"],
    "empathytrait":      ["None", "Compassionate", "Emotional resonancer", "Cold-hearted", "Insensitive"],
    "temperamenttrait":  ["None", "Warm-hearted", "Fervent", "Very calm", "Calm"],
    "intelligencetrait": ["None", "Smart", "Prodigy", "Very Dull", "Slow"],
    "naturetrait":       ["None", "Tenacious disposition", "Unbreakable resolve", "Faint-hearted disposition", "Insecure disposition"],
    "pridetrait":        ["None", "Meekness", "Very Meekness", "Confident", "Overbearing"],
    "physicaltrait":     ["None", "Good metabolism", "Excellent metabolism", "Very bad metabolism", "bad metabolism"],
    "exorticismtrait":   ["None", "Distinctive", "Strikingly Exotic", "Completely common", "Unremarkable"]
}
define dic_traits_attributes_description = {
    "beautytrait": [
        "None",
        "{b}Attractive{/b} \nYour slave is attractive and pleasant to look at. She turns heads and draws attention with her charm. She possesses a divine beauty that captivates all who see her. Her appearance is mesmerizing and unforgettable.",
        "{b}Divine beauty{/b} \nYour slave is attractive and pleasant to look at. She turns heads and draws attention with her charm. She possesses a divine beauty that captivates all who see her. Her appearance is mesmerizing and unforgettable. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Hideous{/b} \nYour slave is unattractive and plain. Her appearance doesn't stand out in any positive way. She is hideous to behold, with features that repel rather than attract. Her looks often make others uncomfortable. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Unattractive{/b} \nYour slave is unattractive and plain. Her appearance doesn't stand out in any positive way. She is hideous to behold, with features that repel rather than attract. Her looks often make others uncomfortable."
    ],
    "endurancetrait": [
        "None",
        "{b}Tough{/b} \nYour slave is tough and endures hardship without complaint. She can handle physical strain well. She has an unshakable fortitude that makes her nearly tireless and able to push through even the harshest conditions.",
        "{b}Fortitude{/b} \nYour slave is tough and endures hardship without complaint. She can handle physical strain well. She has an unshakable fortitude that makes her nearly tireless and able to push through even the harshest conditions. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very Frail{/b} \nYour slave is weak and struggles with even moderate effort. She tires easily and lacks resilience. She is extremely frail and collapses easily under pressure. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Weak{/b} \nYour slave is weak and struggles with even moderate effort. She tires easily and lacks resilience. She is extremely frail and collapses easily under pressure."
    ],
    "empathytrait": [
        "None",
        "{b}Compassionate{/b} \nYour slave is compassionate and responds to others emotions with care. She connects easily with people. She possesses emotional resonance that lets her deeply understand and soothe others.",
        "{b}Emotional resonancer{/b} \nYour slave is compassionate and responds to others emotions with care. She connects easily with people. She possesses emotional resonance that lets her deeply understand and soothe others. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Cold-hearted{/b} \nYour slave is insensitive and oblivious to others feelings. She struggles with empathy and emotional expression. She is cold-hearted and indifferent to others. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Insensitive{/b} \nYour slave is insensitive and oblivious to others feelings. She struggles with empathy and emotional expression. She is cold-hearted and indifferent to others."
    ],
    "temperamenttrait": [
        "None",
        "{b}Warm-hearted{/b} \nYour slave is warm-hearted and brings comfort to those around her. Her emotional presence is soothing. She burns with fervent emotion and passion, often inspiring those near her with her intensity.",
        "{b}Fervent{/b} \nYour slave is warm-hearted and brings comfort to those around her. Her emotional presence is soothing. She burns with fervent emotion and passion, often inspiring those near her with her intensity. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very calm{/b} \nYour slave is calm and composed. She keeps her feelings in check but may seem emotionally distant. She is overly calm, to the point of being detached. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Calm{/b} \nYour slave is calm and composed. She keeps her feelings in check but may seem emotionally distant. She is overly calm, to the point of being detached."
    ],
    "intelligencetrait": [
        "None",
        "{b}Smart{/b} \nYour slave is smart and quick-witted. She picks up new concepts with ease and adapts quickly. She is a prodigy with exceptional intellect, easily mastering complex tasks beyond normal expectations.",
        "{b}Prodigy{/b} \nYour slave is smart and quick-witted. She picks up new concepts with ease and adapts quickly. She is a prodigy with exceptional intellect, easily mastering complex tasks beyond normal expectations. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very Dull{/b} \nYour slave is slow and often confused. She learns slowly and needs repeated guidance. She is very dull and struggles to grasp even simple concepts. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Slow{/b} \nYour slave is slow and often confused. She learns slowly and needs repeated guidance. She is very dull and struggles to grasp even simple concepts."
    ],
    "naturetrait": [
        "None",
        "{b}Tenacious disposition{/b} \nYour slave has a tenacious disposition and rarely gives up. She holds strong even under pressure. Her unbreakable resolve drives her forward through all hardship.",
        "{b}Unbreakable resolve{/b} \nYour slave has a tenacious disposition and rarely gives up. She holds strong even under pressure. Her unbreakable resolve drives her forward through all hardship. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Faint-hearted disposition{/b} \nYour slave has an insecure disposition, doubting herself constantly and often giving in to fear. She is faint-hearted and easily discouraged. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Insecure disposition{/b} \nYour slave has an insecure disposition, doubting herself constantly and often giving in to fear. She is faint-hearted and easily discouraged."
    ],
    "pridetrait": [
        "None",
        "{b}Meekness{/b} \nYour slave displays meekness and knows her place. She acts with humility and rarely challenges authority. She is extremely meek, almost to a fault, making her utterly obedient.",
        "{b}Very Meekness{/b} \nYour slave displays meekness and knows her place. She acts with humility and rarely challenges authority. She is extremely meek, almost to a fault, making her utterly obedient. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Confident{/b} \nYour slave is overbearing and believes herself superior. She resists subservience and expects special treatment. She is confident and bold, often asserting herself. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Overbearing{/b} \nYour slave is overbearing and believes herself superior. She resists subservience and expects special treatment. She is confident and bold, often asserting herself."
    ],
    "physicaltrait": [
        "None",
        "{b}Good metabolism{/b} \nYour slave has a good metabolism, maintaining her health and energy easily. She handles physical labor well. She possesses an excellent metabolism, giving her great physical vitality and stamina.",
        "{b}Excellent metabolism{/b} \nYour slave has a good metabolism, maintaining her health and energy easily. She handles physical labor well. She possesses an excellent metabolism, giving her great physical vitality and stamina. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Very bad metabolism{/b} \nYour slave has a bad metabolism and struggles with energy and body regulation. She tires quickly and lacks fitness. She suffers from a very bad metabolism, gaining weight or losing energy easily. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Bad metabolism{/b} \nYour slave has a bad metabolism and struggles with energy and body regulation. She tires quickly and lacks fitness. She suffers from a very bad metabolism, gaining weight or losing energy easily."
    ],
    "exorticismtrait": [
        "None",
        "{b}Distinctive{/b} \nYour slave is distinctive and stands out with a unique charm. Her look draws attention and interest. She is strikingly exotic and exudes an allure few can resist.",
        "{b}Strikingly Exotic{/b} \nYour slave is distinctive and stands out with a unique charm. Her look draws attention and interest. She is strikingly exotic and exudes an allure few can resist. She has a gifted attribute, which will allow her to reach new heights.",
        "{b}Completely common{/b} \nYour slave is unremarkable, lacking any distinguishing features. Her look fails to attract attention in any way. She is completely common in appearance and blends into the crowd. She has an ungifted attribute, which will limit her potential for improvement.",
        "{b}Unremarkable{/b} \nYour slave is unremarkable, lacking any distinguishing features. Her look fails to attract attention in any way. She is completely common in appearance and blends into the crowd."
    ]
}
default aura_descriptions = {
    "obedience": [
        "You try to find signs of obedience, but stable structures cannot form. There are no spikes of rebellion, alas there are no buds of obedience as well.",
        "You concentrate on the signs of obedience, but you can only see {color=#009900}one open bud of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}a pair of open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}three open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}four open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}five open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}six open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}seven open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}eight open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}nine open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#009900}a lot of open buds of obedience{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}one sharp thorn of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}a pair of sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}three sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}four sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}five sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}six sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}seven sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}eight sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}nine sharp thorns of rebellion{/color}.",
        "You concentrate on the signs of obedience and count {color=#cd0000}a lot of sharp thorns of rebellion{/color}."
    ],

    "supermacy": [
        "{color=#cd0000}The aura of your slave shines considerably brighter than yours{/color}.",
        "{color=#EA0090}The aura of your slave shines brighter than yours{/color}.",
        "{color=#0000D8}The aura of your slave is approximately equal to yours{/color}.",
        "{color=#009900}The aura of your slave is fainter than yours{/color}.",
        "{color=#009900}The aura of your slave is considerably fainter than yours{/color}."
    ]
}


default aura_descriptions2 = {
    "lust": [
        "{color=#000000}The aura moves slowly and smoothly, almost without pulsation. You don’t notice any signs of sexual desire.{/color}",
        "{color=#000000}Light twitching of the aura suggests to you that there is slight sexual desire present.{/color}",
        "{color=#000000}Sensual aura fluctuations indicate the presence of significant sexual arousal.{/color}",
        "{color=#000000}The aura is clearly trembling, twisting and then unwinding in an erotic rhythm. This indicates a strong sexual arousal.{/color}",
        "{color=#000000}The aura is pulsing sensually and eagerly, stretching and arching your way. This is a sign of powerful sexual arousal and almost uncontrollable desire.{/color}",
        "{color=#000000}Almost epileptic flicker speed and modulations suggest ultimate sexual arousal. All colors are mixed in a fast paced whirlwind, like on the surface of a spinning whirligig.{/color}"

    ],

    "fear": [
        "{color=#960018}Ruby flashes of fear{/color}{color=#009900} are insignificant{/color}.",
        "{color=#960018}Ruby flashes of fear{/color} are rare, in one minute you noticed just {color=#EA0090}one{/color}.",
        "{color=#960018}Ruby flashes of fear{/color} appear from time to time, you counted {color=#6B0084}a pair{/color} of them in a minute.",
        "{color=#960018}Ruby flashes of fear{/color} appear quite often. You counted {color=#0000D8}three{/color} of them.",
        "{color=#960018}Ruby flashes of fear{/color} are quite bright and noticeable. You counted {color=#EA0090}four{/color} especially strong ones.",
        "{color=#960018}Ruby flashes of fear{/color} appear one by one and are not in a hurry to fade, pulsing like a heart overflowing with adrenaline. You counted as many as {color=#CD0000}five{/color} just in one minute."
    ],

    "despair": [
        "{color=#464451}Anthracite colored despair{/color}{color=#009900} is almost imperceptible{/color}.",
        "{color=#464451}Anthracite colored despair{/color} has formed {color=#cd0000}one{/color} tentacle, permeating through the whole aura of your slave.",
        "{color=#464451}Anthracite colored despair{/color} has formed {color=#cd0000}two{/color} tentacles, tightly gripping the aura of your slave from both sides.",
        "{color=#464451}Anthracite colored despair{/color} has formed a dense clot, with {color=#cd0000}three{/color} disgusting writhing tentacles sticking from it.",
        "{color=#464451}Anthracite colored despair{/color} has grown and released {color=#009FEF}four{/color} tentacles, engulfing the aura of your slave from all sides.",
        "{color=#464451}Anthracite colored despair{/color} permeates the entire aura of your slave. You can clearly see {color=#cd0000}five{/color} fat, disgusting writhing tentacles, which tear all other colors to shreds."
    ],

    "awareness": [
        "{color=#B452CD}Amethyst core of awareness{/color}{color=#cd0000} is not formed{/color}.",
        "{color=#B452CD}Amethyst core of awareness{/color} is very small, being formed by {color=#EA0090}only one{/color} globule.",
        "{color=#B452CD}Amethyst core of awareness{/color} is formed by {color=#6B0084}two{/color} tightly agglutinated globules.",
        "{color=#B452CD}Amethyst core of awareness{/color} is medium-sized. You counted {color=#0000D8}three{/color} globules in it.",
        "{color=#B452CD}Amethyst core of awareness{/color} is big and dense, formed by {color=#009FEF}four{/color} crisp globules.",
        "{color=#B452CD}Amethyst core of awareness{/color} predominates in the central portion. Its shape indicates the presence of at least {color=#009900}five{/color} well-formed globules."
    ],

    "taming": [
        "{color=#CD9B1D}Golden strings of taming{/color}{color=#cd0000} are hardly noticeable{/color}.",
        "{color=#CD9B1D}Golden strings of taming{/color} are hardly formed. Just {color=#EA0090}one{/color} of them seems to be strong enough.",
        "{color=#CD9B1D}Golden strings of taming{/color} are seen here and there. You find {color=#6B0084}a pair{/color} of strong ones.",
        "{color=#CD9B1D}Golden strings of taming{/color} are noticeable in lots of places. {color=#0000D8}Three{/color} of them seem to be particularly strong.",
        "{color=#CD9B1D}Golden strings of taming{/color} are seen everywhere. {color=#009FEF}Four{/color} especially bright coils pass on the perimeter of the aura, like the meridians on the globe.",
        "{color=#CD9B1D}Golden strings of taming{/color}{color=#009900} cover the whole aura{/color}, making it look like a piece of ham in a tight braid."
    ],

    "habit": [
        "{color=#082567}Sapphire flicker of habit{/color}{color=#cd0000} is completely absent{/color}.",
        "{color=#082567}Sapphire flicker of habit{/color} looks very dull and only noticeable in {color=#EA0090}one{/color} place.",
        "{color=#082567}Sapphire flicker of habit{/color} appears rather poorly and only in {color=#6B0084}a pair{/color} of places.",
        "{color=#082567}Sapphire flicker of habit{/color} is fairly stable. You find {color=#0000D8}three{/color} points of its concentration.",
        "{color=#082567}Sapphire flicker of habit{/color} meanders over the entire surface of the aura of your slave, covering it from {color=#009FEF}four{/color} sides.",
        "{color=#082567}Sapphire flicker of habit{/color}{color=#009900} envelops the whole aura{/color} of your slave, like a soft misty haze. It softens and masks all angles, ledges and bright colors."
    ],

    "spoil": [
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color}{color=#009900} does not spoil the aura{/color} of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} is gathered in {color=#009FEF}one{/color} place, forming a disgusting wormhole.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}two{/color} loathsome sores in the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}three{/color} nasty sores in the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color} forms {color=#cd0000}four{/color} ugly ulcerations on the aura of your slave.",
        "{color=#EE1289}Vulgar-pink iridescence of spoiling{/color}{color=#cd0000} is seen everywhere{/color}, speckling your slave’s aura with bloody sore-like structures."
    ],

    "devotion": [
        "{color=#00a86b}Emerald glow of devotion{/color}{color=#cd0000} does not manifest at all{/color}.",
        "{color=#00a86b}Emerald glow of devotion{/color} is seen {color=#EA0090}just in one{/color} place, like a dim star on the cloudy sky.",
        "{color=#00a86b}Emerald glow of devotion{/color} forms {color=#6B0084}a pair{/color} of softly shining stars.",
        "{color=#00a86b}Emerald glow of devotion{/color} comes from {color=#0000D8}three{/color} well-marked stars.",
        "{color=#00a86b}Emerald glow of devotion{/color} comes from {color=#009FEF}four{/color} bright stars, illuminating the aura of your slave.",
        "{color=#00a86b}Emerald glow of devotion{/color} dominates the aura of your slave, dotting it with {color=#009900}myriads{/color} of bright and clear stars."
    ]
}
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################
###############################################################################################################################################################################################################


default demo_girl_stats = {
    "Helen":      [3,3,3,3,5,3,3,0,2,0,0],
    "Yasmin":     [4,5,2,5,4,4,1,3,5,0,0],
    "Wilhelmine": [5,2,5,5,3,5,1,2,5,0,0]
}
default dic_girl_age_text ={
    0: "Young",
    1: "Loli",
    2: "Madure"
}
