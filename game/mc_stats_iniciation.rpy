# I can probably merge characters and mc inicial_stats into a giga big dictionaly, but I'm lazy -rec3ks
define dic_characters = [ #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    ("master_noble", "master/master_noble.webp", "master/master_noble_hover.webp",0),
    ("master_torturer", "master/master_torturer.webp", "master/master_torturer_hover.webp",1),
    ("master_pimp", "master/master_pimp.webp", "master/master_pimp_hover.webp",2),
    ("master_vampire", "master/master_vampire.webp", "master/master_vampire_hover.webp",3),
    ("master_fighter", "master/master_fighter.webp", "master/master_fighter_hover.webp",4),
    ("master_teacher", "master/master_teacher.webp", "master/master_teacher_hover.webp",5),
    ("master_impressario", "master/master_impressario.webp", "master/master_impressario_hover.webp",6),
    ("master_butler", "master/master_butler.webp", "master/master_butler_hover.webp",7),
    ("master_doctor", "master/master_doctor.webp", "master/master_doctor_hover.webp",8),
    ("master_werwolf", "master/master_werwolf.webp", "master/master_werwolf_hover.webp",9),
    ("master_granpa", "master/master_granpa.webp", "master/master_granpa_hover.webp",10),
    ("master_nerd", "master/master_nerd.webp", "master/master_nerd_hover.webp",11),
]

##### I should use Json instead of Dict or make a better Dictionary structure, but requiere a lot rework and I'm lazy -rec3ks
define dic_mc_inicial_stats = { #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    "master_noble"      : ["M'lord"     , 4, 4, 0, 2, 4, 0, 0, 0, 5, 0, 5, 2, 2, 3, 2, 4, 0, 4, 3, 0, 3, 2, 4, 3,"Elven Chainmail"     ,""           ,"Fist"         ,"Epée"           ,""                 ,""        ,"Noble Regalia"       ,"","","","","Taurus Great House",8000, "simple difficulty",    5,""                                 , "   An aristocrat with a great education, with \n experience in court and military service. Having all \n the basic skills that are necesarry to teach, the easily \n joined the ranks of the slavers and all agree that a \n wonderful career awaits him..."], 
    "master_torturer"   : ["Robespierre", 5, 1, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 3, 3, 0, 5, 5, 5, 2, 2, 4, 4,"Without armor"       ,""           ,"Fist"         ,"Whip"           ,""                 ,""        ,"Worn clothes"        ,"","","","","Taurus Great House",7000, "simple difficulty",    5,""                                 , "   Once upon a time he was a soldier and fought for \n the king in his colonial wars. Then the king was \n overthrown and the revolution needed executioners. \n More than anything, he is proud to have personally \n decapitated the beautiful, but hanghty queen. In the \n Eternal Rome, a hangman's skills some in handy. "],
    "master_pimp"       : ["Silk Daddy" , 3, 4, 0, 3, 4, 0, 0, 0, 5, 0, 5, 3, 2, 2, 1, 1, 0, 0, 2, 2, 4, 4, 5, 5,"Without armor"       ,""           ,"Fist"         ,"Brass Knuckles" ,""                 ,""        ,"Fashionable Attire"  ,"","","","","Serpis Great House",4500, "simple difficulty",    5,""                                 , "   Everyone has his own idea of success. For Silk \n Daddy, establishing himself as a pimp was a dream \n come true. Now he's in a new world, but the work is \n somewhat similar. Black, white, yellow or tailed - \n bitches will always be bitches. They need a big black \n daddy. And Daddy needs a lot of money."],
    "master_vampire"    : ["Saruman"    , 5, 5, 0, 0, 4, 0, 0, 0, 5, 0, 5, 1, 3, 0, 2, 2, 4, 1, 1, 1, 3, 3, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Wizard Robes"        ,"","","","","Serpis Great House",5000, "simple difficulty",    5,""                                 , "   Saruman was once a revered sorcerer who delved \n into the forbidden arts and was inadvertently cursed \n with vampirism. At first, Saruman embraced his \n transformation, but soon the thrill of the hunt began \n to wane, leaving a deep sense of loneliness. Desiring a \n worthy companion to share eternity with him, he \n obsessively acquired new thralls until one day he \n unexpectedly stumbled into the mists. There he \n chanced across a black medic to lead him to Rome, \n where Saruman hopes to find his true love at last."],
    "master_fighter"    : ["Blade"      , 5, 2, 0, 3, 3, 0, 0, 0, 5, 0, 5, 1, 1, 0, 2, 6, 0, 2, 2, 2, 2, 2, 4, 2,"Yatserin Mail"       ,""           ,"Fist"         ,"Bastard Sword"  ,""                 ,""        ,"Aketon"              ,"","","","","Taurus Great House",6000, "normal difficulty",    3,""                                 , "   In the harsh world where he was born a natural \n physical strength was very much appreciated. Blade \n was one of the best warriors and confidently walked \n to success, but somehow got to the Fog. Although a \n good fighter will not get lost in the Eternal Rome, we \n all somethimes want to change our lives and achieve \n something more than an ordinary service to the \n mighty of this world."],
    "master_teacher"    : ["Teacher"    , 3, 3, 0, 3, 4, 0, 0, 0, 5, 0, 5, 6, 2, 2, 1, 0, 0, 4, 1, 0, 2, 1, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Formal Suit"         ,"","","","","Serpis Great House",3000, "normal difficulty",    3,""                                 , "   He was a ordinary school teacher, nothing \n special. Such a person might find it difficult to adapt \n in the Eternal Rome, but he is hoping that his years \n of experience teaching young minds and maintaining \n strict discipline in the class will be transferable skills. \n Besides, he misses the good old days when you were \n allowed to spank naughty young ladies! Spare the \n rod, spoil the student. But most of all, he simply \n could not bear another class full of nubile girls, so \n close and yet so far."],
    "master_impressario": ["Maestro"    , 2, 4, 0, 1, 3, 0, 0, 0, 5, 0, 5, 3, 1, 6, 0, 0, 0, 3, 0, 0, 3, 5, 4, 1,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Formal Suit"         ,"","","","","Taurus Great House",6000, "normal difficulty",    3,""                                 , "   He was the Impresario, famous in the old world, \n the man that playwrights, composers and stars \n kowtowed to. Literally thousands of young starlets \n have knelt beneath his desk or laid on his casting \n couch. But when his fourth trophy wife left him he \n gave it all up for a fresh start in the Eternal Rome, a \n city that still appreciates true talent. And if he had \n to work with one more spoiled diva... so much \n easier to work with a slave."],
    "master_butler"     : ["Butler"     , 3, 3, 0, 2, 3, 0, 0, 0, 5, 0, 5, 3, 6, 1, 1, 0, 0, 2, 0, 2, 0, 1, 2, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Livery"              ,"","","","","Taurus Great House",5000, "normal difficulty",    3,""                                 , "   Once in the Eternal Rome, he found himself in a \n delicate situation. Of course, an experienced servant \n in useful everywhere, but he doesn't feel like being a \n slave. He put in a lot of effort to gain the status of a \n slaver. After all, no one trains maids better than a \n butler."],
    "master_doctor"     : ["Doc"        , 3, 3, 0, 2, 2, 0, 0, 0, 5, 0, 5, 2, 1, 0, 6, 0, 0, 0, 3, 0, 2, 1, 3, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Medical Gown"        ,"","","","","Serpis Great House",1000, "high difficulty"  ,    2,"He cannot afford an apartment yet", "   He was always a very good doctor with a thriving \n practice. The one little mistake and one huge \n malpractice suit, and suddenly he decided to move \n to the Eternal Rome. It turned out that even Doc has \n insufficient knowledge for the Technosphere's Medical \n Center, but it's no reason to despair, right? He \n always wanted to try to educate witchdoctors in a \n more unfettered manner. Maybe it's his calling?"],
    "master_werwolf"    : ["Fenris"     , 4, 0, 0, 4, 3, 0, 0, 0, 5, 0, 5, 1, 0, 0, 3, 3, 3, 2, 2, 2, 0, 0, 4, 2,"Elven Chaimail"      ,"Morningstar","Katana"       ,"Epée"           ,"Cat o' Nine Tails","Dagger"  ,"Aketon"              ,"","","","","Camira Great House",400 , "high difficulty"  ,    2,"He cannot afford an apartment yet", "   A magical werewolf who must hide his true \n nature. He is constantly on the move to avoid \n detection, which explains his meager circumstances. \n He is a skilled fighter and torturer and has seen his \n share of war. Fenris is an accomplished war medic \n who is known for saving soldiers who had little \n chance of survival. He was also pulled in at times to \n perform interrogations of the enemy while serving in \n various Camira war camps. Fenris miraculously was \n the sole survivor of two war camp slaughters."],
    "master_granpa"     : ["Uncle Tom"  , 2, 1, 0, 0, 1, 0, 0, 0, 5, 0, 5, 2, 1, 0, 1, 0, 0, 2, 0, 0, 4, 3, 1, 4,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Housecoat"           ,"","","","","Serpis Great House",800 , "very high difficulty", 1,"He cannot afford an apartment yet", "   Those things he used to make his daughters do? \n Not his fault, really; the sluts had basically asked for \n it. But now he is old and alone, shunned by his \n family, not allowed to see his own granddaughters! \n So unfair! So how does a lonely, dirty old man \n spend his golden years? He's not your typical slaver \n - erectile issues and kind of creepy - but ins't \n training a young slave to be a good girl basically the \n same as raising a daughter? He cashed in his persion \n and came to the Eternal Rome."],
    "master_nerd"       : ["Johny"      , 2, 1, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 5,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,"Worn clothes"        ,"","","","","Serpis Great House",200 , "extreme difficulty",   0,"He cannot afford an apartment yet", "   People just see a quiet, young nerd. Other kids call \n him 'loser'. But in his dreams? He's a great slave \n master. Womn crawl at his feet...no,{i} bitches...{/i}naked \n bitches...with enormous saggy tits. Oh, the disgusting \n things he would force them to do!! The kid jerks off \n a dozen times a day imagining it. He's learned \n enough magic to find the Fogs, but does this horny \n virgin schoolboy really have what it takes to break \n grown women to his will? Will they take him \n seriously? Or will they just think he's a loser, too? "],
    "Jack"              : ["jack"       , 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"Without armor"       ,""           ,"Fist"         ,"Fist"           ,""                 ,""        ,""                    ,"","","","",""                  ,6000, "Normal"           ,    3,585]           
    }
define dic_charactersOnlyName = ["master_noble", "master_torturer", "master_pimp", "master_vampire", "master_fighter","master_teacher", "master_impressario", "master_butler", "master_doctor", "master_werwolf", "master_granpa", "master_nerd"]

define dic_mc_attribute = { #DO NOT ADD ANY VARIABLE TO THIS DICTIONARY -rec3ks
    "STRENGTH"             : ["Frail"               , "Weak"                 , "Unfit"               , "Vigorous"           , "Strong"            , "Herculean"             ,"{b}Inmortal{/b}"          ,"{b} STRENGTH:{/b} \n Strength commands respect. It is important for a \n trainer  to be strong. Strength affects the force of your \n blows in combat, your endurance in daily tasks, and the \n submissiveness of your slaves. To build and maintain \n strength, avoid lower-quality food, engage in athletics, \n dance, intercourse, or martial arts, firmly discipline \n your slaves, and avoid exhaustion (red energy stars)."],
    "PERSONALITY"          : ["Caitiff"             , "Rube"                 , "Churl"               , "Knave"              , "Vulgarian"         , "Aristocrat"            ,"{b}Aristocrat+{/b}"       ,"{b} PERSONALITY:{/b} \n Charisma, determination and will play a crusial role \n for  a trainer of slaves, as they make it much easier to \n control other people. How you are viewed is a reflection \n of your prestige, which is influenced by your standard \n of living, the location of your residence, the quality \n of your interior decor, and your brand reputation" ],
    "ALLURE"               : ["Repulsive"           , "Unpleasant"           , "Unmemorable"         , "Charming"           , "Captivating"       , "Irresistible"          ,"{b}Irresistible+{/b}" ]   ,
    "LIBIDO"               : ["Impotent"            , "Effete"               , "Lustful"             , "Libidinous"         , "Lubricious"        , "Salacious"             ,"{b}Salacious+{/b} "       ,"{b} LIBIDO:{/b} \n Sex is an essential part of training slaves, and the \n ability to perform without the aid of aphrodisiacs is \n vital. Libido is increased by an active sex life and a \n healthy lifestyle, but is decreased by injuries, illness, \n poor health, and extended periods without sex."],
    "DOMINANCE"            : ["Submissive"          , "Compliant"            , "Passive"             , "Authoritative"      , "Dominant"          , "Imperious"             ,"{b}Imperious+{/b}"        ,"{b} DOMINANCE:{/b} \n Ability to dominate and subdue is just as important \n for a slave trainer as ability to teach. Your level of \n dominance has strong influence on your slave's obedience \n and the effectiveness of some punishments, especially  \n verbals ones. Dominance is also useful when teaching \n sexual skills. Increases automatically when applied."],
    "BRAND REPUTATION"     : ["Unknown"             , "Rumored"              , "Recognized"          , "Celebrity"          , "Famous"            , "Legendary"             ,"{b}Legendary+{/b}"],
    "GUILD REPUTATION"     : ["Guild Fall Guy"      , "Guild Punching Bag"   , "Guild Lackey"        , "Guild Hotshot"      , "Guild Muscle"      , "Guild Boss"            ,"{b}Guild Boss+{/b}"],
    "STANDARD OF LIVING"   : ["Impoverished"        , "Poor"                 , "Basic"               , "Comfortable"        , "Respectable"       , "Luxurious"             ,"{b}Extravagant{/b}"],
    "HYGIENE"              : ["Filthy"              , "Dirty"                , "Unclean"             , "Unsullied"          , "Clean"             , "Pristine"              ,""],
    "MOOD"                 : ["Depressed"           , "Dysphoric"            , "Sullen"              , "Melancholic"        , "Pessimistic"       , "Calm"                  , "Hopeful"          , "Optimistic"        , "Pleased"           , "Euphoric"          , "Ecstatic"           ,"{b}Ecstatic+{/b}",""],
    "INJURIES"             : ["Mortally wounded"    , "Seriously Injured"    , "Moderately Injured"  , "Lightly Injured"    , "Slightly Wounded"  , "Safe and unharmed"     ,""],
    "TEACHING"             : ["Incoherent F-"       , "Tutor D-"             , "Mentor C-"           , "Pedagogue B+"       , "Teacher A+"        , "Lecturer S+"           ,"{b}Lecturer S++{/b}"             ,"{b} TEACHING:{/b} \n Teaching is one of the key skills of the slaver. It \n determines the efficiency of training a slave in any \n non-sexual skill. Skill as a teacher improves as you  \n teach your slaves with outcomes A+ or better."],
    "STEWARDSHIP"          : ["Ingenuous Dweller F-", "Peon D-"              , "Houseboy C-"         , "Homemaker B+"       , "Houselord A+"      , "Steward S+"            ,"{b}Master Steward S++{/b}"       ,"{b} STEWARDSHIP:{/b} \n Stewardship combines the knowledge of cooking, \n household and slave management. A good steward can \n cook dinner himself or clean the house, but more \n importantly he can pass his skills to his slaves."],
    "ARTISTRY"             : ["Tasteless F-"        , "Uncultured D-"        , "Dilettante C-"       , "Artist B+"          , "Prodigy A+"        , "Virtuoso S+"           ,"{b}Maestro S++{/b}"              ,"{b} ARTISTRY:{/b} \n Artistry comes in many forms. Dance, music, the \n ability to paint, acting and roleplay (including \n behaving like an animal)… Skill as an artist improves \n as you teach your slaves relevant skills with outcomes \n A+ or better. "],
    "MEDIC"                : ["Homeopath F-"        , "Quack D-"             , "Paramedic C-"        , "Medic B+"           , "Physician A+"      , "Surgeon S+"            ,"{b}Master Surgeon S++{/b}"       ,"{b} MEDIC:{/b} \n A competent medic and alchemist can train  \n witchdoctors, identify health issues and effectively  \n care for sick and injured slaves."],
    "FIGHTER"              : ["Non-Combatant F-"    , "Brawler D-"           , "Duelist C-"          , "Combatant B+"       , "Warrior A+"        , "Champion S+"           ,"{b}Vanquisher S++{/b}"           ,"{b} FIGHTER:{/b} \n Martial skill is useful both to train a gladiatrix  \n and in real combat. Your capacity to learn special \n techniques from the Colosseum trainer and the duration \n of your strikes' effects are dependent upon your combat \n skill. Skill as a fighter improves as you train your \n slaves in combat with outcomes A+ or better and when  \n you are victorious in battle."],
    "MAGIC"                : ["Mundane F-"          , "Esoterist D-"         , "Warlock C-"          , "Sorcerer B+"        , "Mage A+"           , "Archmage S+"           ,"{b}Demi-God S++{/b}"             ,"{b} MAGIC:{/b} \n This skill is responsible for your ability to cast \n spells using sparks and directly affects the \n effectiveness of these spells. The skill of alchemists and \n enchantresses you personally train cannot exceed your \n skill rank in magic. Trained alchemists can brew useful \n potions for you in the lab, but you will need reagents \n that can be found at the 'Rarities of Mystra' in \n the Outcasts' Quarter. Skill in magic improves as you \n train slaves with outcomes A+ or better and apply \n magic of the highest levels available."],
    "FLAGELLATION"         : ["Cannot Whip F-"      , "Poor Whip Skill D-"   , "Basic Whip Skill C-" , "Good Whip Skill B+" , "Whip Expert A+"    , "Master of the Whip S+" ,"{b}Master of the Whip S++{/b}"   ,"{b} FLAGELLATION:{/b} \n Proper use of belt, whip and lash not only improves \n the efficiency of punishment but also reduces \n the risk of leaving unwanted scars on a slave. Skill \n develops through application." ],
    "TORTURE"              : ["Not a Torturer F-"   , "Needler D-"           , "Tormentor C-"        , "Torturer B+"        , "Inquisitor A+"     , "Master Inquisitor S+"  ,"{b}Master Inquisitor S++{/b}"    ,"{b} TORTURE:{/b} \n If you are using a bulky torture unit, it does \n everything for you. But the master of torture can \n achieve no less using modest materials at hand. More \n importantly, skill in this area prevents spoiling the \n appearance and health of slaves. Requires a dungeon. \n Skill develops through application."],
    "BINDING"              : ["Never Restrained F-" , "Novice Rope Binder D-", "Binds Correctly C-"  , "Binds Skillfully B+", "Binds Artfully A+" , "Master of Rope S+"     ,"{b}Master of Rope S++{/b}"       ,"{b} BLINDING:{/b} \n Blinding allows you to leave a slave unattended to \n receive punishment from the rope. Proper painful or \n erotic bondage can be very effective as an educational \n or exciting action. Skill develops through application."],
    "PETTING"              : ["Never touched F-"    , "Petting D-"           , "Petting C-"          , "Petting B+"         , "Petting A+"        , "Petting S+"            ,"{b}Master of Petting S++{/b}"    ,""],
    "ORAL SEX"             : ["Oral Sex F-"         , "Oral Sex D-"          , "Oral Sex C-"         , "Oral Sex B+"        , "Oral Sex A+"       , "Oral Sex S+"           ,"{b}Master of Oral Sex S++{/b}"   ,""],
    "PENETRATION"          : ["Virgin F-"           , "Penetration D-"       , "Penetration C-"      , "Penetration B+"     , "Penetration A+"    , "Penetration S+"        ,"{b}Master of Penetration S++{/b}",""],
    "FETISHISM"            : ["Unadventurous F-"    , "Fetishism D-"         , "Fetishism C-"        , "Fetishism B+"       , "Fetishism A+"      , "Worst of Perverts S+"  ,"{b}Worst of Perverts S++{/b}"    ,""],
    "REPUTATION"           : ["The Slums"           , "Quarter of the Outcasts","Serpentine Quarter" , "Quarter of the Bull", "Necropolis"        , "White Town"            ,"{b} REPUTATION:{/b} \n Reputation measures your personal notoriety (how \n well you are known by the citizens of the Eternal \n Rome) and determines your access to the higher echelons \n of society and to higher-quality, higher-cost living \n conditions. Living in a shack is cheap but very difficult. \n Satisfying clients will improve your reputation with \n their faction and allow you to rent or purchase a \n residence in their vicinity. "]
}
define dic_mc_normal_selection_textdescription ={ 
    "master_noble":       [dic_mc_inicial_stats["master_noble"][41]," - No particular advantages or disadvantages."],
    "master_torturer":    [dic_mc_inicial_stats["master_torturer"][41]," - No particular advantages or disadvantages."],
    "master_pimp":        [dic_mc_inicial_stats["master_pimp"][41]," - No particular advantages or disadvantages."],
    "master_vampire":     [dic_mc_inicial_stats["master_vampire"][41]," - No particular advantages or disadvantages."],
    "master_fighter":     [dic_mc_inicial_stats["master_fighter"][41]," - Fighter Skills will not naturally decay."],
    "master_teacher":     [dic_mc_inicial_stats["master_teacher"][41]," - Teaching Skills will not naturally decay."],
    "master_impressario": [dic_mc_inicial_stats["master_impressario"][41]," - Artistry Skills will not naturally decay. \n - Get free theather tickets"],
    "master_butler":      [dic_mc_inicial_stats["master_butler"][41]," - Stewardship Skills will not naturally decay."],
    "master_doctor":      [dic_mc_inicial_stats["master_doctor"][41]," - Medic Skills will not naturally decay. \n - Free hospital examination"],
    "master_werwolf":     [dic_mc_inicial_stats["master_werwolf"][41]," - No particular advantages or disadvantages."],
    "master_granpa":      [dic_mc_inicial_stats["master_granpa"][41]," - No particular advantages or disadvantages."],
    "master_nerd":        [dic_mc_inicial_stats["master_nerd"][41]," - No particular advantages or disadvantages."],
    "STRENGTH":            [dic_mc_attribute["STRENGTH"][7]],
    "PERSONALITY":         [dic_mc_attribute["PERSONALITY"][7]],
    "LIBIDO":              [dic_mc_attribute["LIBIDO"][7]],
    "DOMINANCE":           [dic_mc_attribute["DOMINANCE"][7]],
    "TEACHING":            [dic_mc_attribute["TEACHING"][7]],
    "STEWARDSHIP":         [dic_mc_attribute["STEWARDSHIP"][7]],
    "ARTISTRY":            [dic_mc_attribute["ARTISTRY"][7]],
    "MEDIC":               [dic_mc_attribute["MEDIC"][7]],
    "FIGHTER":             [dic_mc_attribute["FIGHTER"][7]],
    "MAGIC":               [dic_mc_attribute["MAGIC"][7]],
    "FLAGELLATION":        [dic_mc_attribute["FLAGELLATION"][7]],
    "TORTURE":             [dic_mc_attribute["TORTURE"][7]],
    "BINDING":             [dic_mc_attribute["BINDING"][7]],
    "PETTING":             [dic_mc_attribute["PETTING"][7]],
    "ORAL SEX":            [dic_mc_attribute["ORAL SEX"][7]],
    "PENETRATION":         [dic_mc_attribute["PENETRATION"][7]],
    "FETISHISM":           [dic_mc_attribute["FETISHISM"][7]],
    "REPUTATION":          [dic_mc_attribute["REPUTATION"][6]],
    "MC NAME":             ["{b} MISCELLANEOUS:{/b} \n Total time played with this character: WIP \n Total number of slave buyed: WIP \n The highest sell slave value: WIP \n Total amount of spark gained: WIP: \n  "],
    "simple difficulty":   ["{b} SIMPLE DIFFICULTY:{/b} \n Perfect for beginners or those looking to enjoy the game \n without too much challenge."],
    "normal difficulty":   ["{b} NORMAL DIFFICULTY:{/b} \n A balanced experience for players seeking a fair \n challenge."],
    "high difficulty":     ["{b} HIGH DIFFICULTY:{/b} \n Designed for experienced players, resources \n are scarcer, and  mistakes are costly."],
    "very high difficulty":["{b} VERY HIGH DIFFICULTY:{/b} \n Only for the truly daring. , resources are rare, and \n every decision counts. One wrong move could be your \n last."],
    "extreme difficulty":  ["{b} EXTREME DIFFICULTY:{/b} \n Brutal and unforgiving. resources are nearly \n nonexistent, and survival demands perfection."],
    "SPARKS":              ["{b} SPARKS:{/b} \n Money, very usefull."],
    "FACTION":             ["{b} FACTION:{/b} \n You can rent a house in this faction at the start of \n game in Trade center, Real State. "],
    "SKILLS":              ["{b} SKILLS:{/b} \n Skills are the abilities and competencies that a person \n develops through learning, practice, or experience,\n which enable them to perform specific tasks \n effectively and efficiently."],
    "SEX TECHNIQUES":      ["{b} SEX TECHNIQUES:{/b} \n Different sex techniques will increase the effectiveness \n of training relevant skills and it will be easier to arouse \n and excite your sexual partners. "],
    "WHITE TOWN":          ["{b} WHITE TOWN:{/b} \n Cannot start in White Town on Normal or Extreme \n difficulty. Only patricians are allowed to live there."],
    "START FAIL":          ["{b} START FAIL:{/b} \n Points must be igual or greater than 0."]
    }
# I know you can use xmaximun and xminimun, just happened I learned that too late, so unless someone want to change it, I will leave it like this with the \n
define dic_custom_character_selection = {
    "master_noble":        ["custom_master/master_noble.webp", "custom_master/master_noble_hover.webp",0],
    "master_torturer":     ["custom_master/master_torturer.webp", "custom_master/master_torturer_hover.webp",1],
    "master_pimp":         ["custom_master/master_pimp.webp", "custom_master/master_pimp_hover.webp",2],
    "master_vampire":      ["custom_master/master_vampire.webp", "custom_master/master_vampire_hover.webp",3],
    "master_fighter":      ["custom_master/master_fighter.webp", "custom_master/master_fighter_hover.webp",4],
    "master_teacher":      ["custom_master/master_teacher.webp", "custom_master/master_teacher_hover.webp",5],
    "master_impressario":  ["custom_master/master_impressario.webp", "custom_master/master_impressario_hover.webp",6],
    "master_butler":       ["custom_master/master_butler.webp", "custom_master/master_butler_hover.webp",7],
    "master_doctor":       ["custom_master/master_doctor.webp", "custom_master/master_doctor_hover.webp",8],
    "master_werwolf":      ["custom_master/master_werwolf.webp", "custom_master/master_werwolf_hover.webp",9],
    "master_granpa":       ["custom_master/master_granpa.webp", "custom_master/master_granpa_hover.webp",10],
    "master_nerd":         ["custom_master/master_nerd.webp", "custom_master/master_nerd_hover.webp",11],
}
define master_caps = {
    "wounds": [10, 20, 40, 80, 160],
    "STRENGTH": [10, 25, 50, 160, 666],
    "PERSONALITY": [10, 20, 40, 80, 160],
    "LIBIDO": [45, 90, 180, 360, 999],
    "BRAND": [5, 15, 30, 70, 100],
    "GUILD REPUTATION": [5, 10, 20, 40, 75],
    "HYGIENE": [10, 20, 40, 60, 80],
    "TEACHING": [15, 75, 150, 300, 600],
    "STEWARDSHIP": [15, 75, 150, 300, 600],
    "ARTISTRY": [15, 75, 150, 300, 600],
    "MEDIC": [15, 75, 150, 300, 600],
    "FIGHTER": [15, 75, 150, 300, 600],
    "MAGIC": [15, 75, 150, 300, 600],
    "DOMINANCE": [45, 90, 180, 360, 999],
    "FLAGELLATION": [1, 20, 40, 80, 160],
    "TORTURE": [1, 20, 40, 80, 160],
    "BINDING": [1, 20, 40, 80, 160],
    "PETTING": [1, 45, 90, 180, 360],
    "ORAL SEX": [1, 45, 90, 180, 360],
    "PENETRATION": [1, 45, 90, 180, 360],
    "FETISHISM": [1, 45, 90, 180, 360],
}
define dic_master_items = {
    "man_rugs": {
        "name": "Worn clothes", 
        "price": 5,
        "desc": "Price: 5 sparks\nThese clothes are worn out and out of fashion. They do not meet any of your goals. It would be better to get some new clothes.",
        "image": "scene/item/item_worn_clothes",
        "size": 0,
        "style": -1,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"neg_worn_clothes": 100}
        }
    },
    "comfy_robes": {
        "name": "Housecoat",
        "price": 25,
        "desc": "Price: 25 sparks\nComfortable and soft housecoat. Does not look very nice, but very convenient and comfortable to wear. Just what you need to relax!",
        "image": "scene/item/item_Housecoat",
        "size": 0,
        "style": -1,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"pos_master_cloth": 100}
        }
    },
    "regal_suit": {
        "name": "Noble Regalia",
        "price": 200,
        "desc": "Price: 200 sparks\nThis heavy clothing is richly decorated with precious inserts and decorative elements, making you look bigger and grander. Beautiful and impressive, of course, but very impractical.",
        "image": "scene/item/item_Noble_regalia",
        "size": 0,
        "style": 2,
        "item_property": False,
        "equiped":False,
        "effect": {
            "master_moodlet": {"neg_master_cloth": 100}
        }
    },
    "fancy_suit": {
        "name": "Fashionable Attire",
        "price": 100,
        "desc": "Price: 100 sparks\nKeeping track of Eternal Rome fashion is almost impossible, but many are trying. In any case, this outfit is a perfect compromise between luxury and convenience.",
        "image": "scene/item/item_Fashionable_attire",
        "size": 0,
        "style": 1,
        "item_property": False,
        "equiped":False,
        "effect": {}
    },
    "formal_suit": {
        "name": "Formal Suit",
        "price": 40,
        "desc": "Price: 40 sparks\nVery formal clothing. Looks old-fashioned and not very charming, but at least you will be taken seriously. It is perfect for the impresario or for an entertainer.",
        "image": "scene/item/item_Formal_suit",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_artdirector": 1}
        }
    },
    "aketon": {
        "name": "Aketon",
        "price": 40,
        "desc": "Price: 40 sparks\nQuilted armor jacket, light enough to be used as everyday wear. Great outfit for a warrior.",
        "image": "scene/item/item_Aketon",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_fighter": 1}
        }
    },
    "livery": {
        "name": "Livery",
        "price": 40,
        "desc": "Price: 40 sparks\nOrnate livery of a senior butler. In this uniform you immediately feel like the sole ruler over your household.",
        "image": "scene/item/item_Livery",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_butler": 1}
        }
    },
    "medic_robes": {
        "name": "Medical Gown",
        "price": 40,
        "desc": "Price: 40 sparks\nVery comfortable and practical clothing for the healthcare worker. Immediately makes you a qualified doctor - even if only due to self-hypnosis.",
        "image": "scene/item/item_Medical_gown",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_medic": 1}
        }
    },
    "wizard_robes": {
        "name": "Wizard Robes",
        "price": 40,
        "desc": "Price: 40 sparks\nThis ritual costume is covered with magical runes. Increases your magical power!",
        "image": "scene/item/item_Wizard robes",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "boost_up": {"master_mage": 1}
        }
    },
    "raven_crown": {
        "name": "Raven Crown",
        "price": 0,
        "desc": "This artifact, called the Raven Crown by its creator, Master Valios, grants permanent auspex, greater insight when looking at others, and strengthens the aura.",
        "image": "",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "auspex": 1,
            "magna_magnifika": 10,
            "item_supermacy_bonus": 1,
        }
    },
    "chimera_earring": {
        "name": "Chimaera’s Gem",
        "price": 0,
        "desc": "This earring, taken from or given to me by the strange hissing creature Garsid, increases libido, strengthens the aura and heals wounds rapidly.",
        "image": "",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 2
        }
    },
    "snake_amulet": {
        "name": "Snake Talisman",
        "price": 0,
        "desc": "This amulet, given to me by its maker, Vujin the Wise of House Serpis, increases concentration, personality, resistance to pain and fear, and strengthens the aura of the wearer, while also blocking scanning.",
        "image": "",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 1
        }
    },
    "bull_ring": {
        "name": "Bull Ring",
        "price": 0,
        "desc": "This normal-looking ring, given to me by Sir Aramus of House Taurus, increases stamina and hardiness in battle and strengthens the aura of the wearer.",
        "image": "",
        "size": 0,
        "style": 0,
        "item_property": False,
        "equiped":False,
        "effect": {
            "item_supermacy_bonus": 1
        }
    }
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

default clothesinventory = {
    'maid_dress': 0,
    'apron': 0,
    'common_apron': 0,
    'nurse_dress': 0,
    'sailor_foku': 0,
    'leotard': 0,
    'chainmail_bikini': 0,
    'enchanter_robe': 0,
    'sun_dress': 0,
    'leather_corset': 0,
    'fluffy_stepins': 0,
    'high_boots': 0,
    'sneakers': 0,
    'tabi': 0,
    'glasses': 0,
    'nekomimi': 0,
    'anal_tail': 0,
    'pony_plume': 0,
    'ponygirl_harness': 0,
    'hoofed_boots': 0,
    'leather_gloves': 0,
    'fluffy_gloves': 0,
    'rubber_gloves': 0,
    'plain_headband': 0,
    'golden_collar': 0,
    'leather_collar': 0,
    'spiked_collar': 0,
}