define inicial_girls = [
    ("demo/choose_princess.webp", 0),
    ("demo/choose_amazon.webp", 265),
    ("demo/choose_slave.webp", 530),
]

define slave_attributes = {
    "BEAUTY":        ["Ugly"            ,"Plain"          ,"Cute"          ,"Pretty   "    ,"Beautiful"    ,"Exquisite"      ,"Goddess"     ,"  Natural beauty very strongly influences her market price. Your slave's rank will never rise higher than her beauty or fame (whichever is higher). At auctions, beautiful slaves are sold for higher prices.","   ll your efforts to improve the appearance of the slave will influence style, not beauty. Stylishness is important too, but the value of natural beauty is huge. You can increase beauty only by neoplasty surgery in the Technosphere medical center and only once for each slave. Try to buy beautiful slaves if you intend to train them to high ranks. Beauty is decreased while a slave has scars or bruises until they are removed or healed."],
    "ENDURANCE":     ["Dyinng"          ,"Feeble"         ,"Weakened"      ,"Healthy"      ,"Tough"        ,"Enduring"       ,"Iron"        ,"  Hardy slaves have more energy, can work better and are more attractive for clients. Critical decrease of endurance can kill your slave.","   If your slave is weak, feed her well; it's desirable to prescribe supplements and not let her become exhausted (receive red energy stars), nor over-exercise (when she has purple energy stars, intensive exercise is harmful), nor gain weight if she is overweight, nor end the day with negative calories. Build endurance with gymnastics, athletics, dance, racing, martial arts, pet play or vigorous sex. Heal injuries (a nurse assistant and your own skill helps) and sicknesses, and use drugs sparingly."],
    "ENPATHY":       ["Heartless"       ,"Callous"        ,"Insensitive"   ,"Sensitive"    ,"Caring"       ,"Nurturing"      ,"Nurturing+"  ,"  On one hand the gentle slave is easier affected by stress and stung by punishments. On the other hand she is turned on much faster and is more lively, which makes her attractive for customers.","   Callousness develops quickly with mistreatment. Severe punishments are especially harmful. While a less sensitive slave is hardened against depression and endures suffering, she is also less valuable. There are no reliable ways to increase a slave's empathy, but refined petting and pleasures may help."],
    "TEMPERAMENT":   ["Apathetic"       ,"Cold"           ,"Reserved"      ,"Reactive"     ,"Lively"       ,"Passionate"     ,"Passionate+" ,"  Temperamental slaves are uncontrollable and are less susceptible to education but they are passionate lovers and are more interesting for customers, as they have a bright personality. Calm ones are easier to control.","   Temperament is an ambiguous feature. More emotional slaves are harder to control, but cold ones are less valuable. By suppressing initiative, driving her into depression and silencing her you will eventually lower her temperament. Getting her to express herself or interact openly with the slaver will often increase temperament."],
    "INTELLIGENCE":  ["Retarded"        ,"Stupid"         ,"Dimwitted"     ,"Bright"       ,"Clever"       ,"Intelligent"    ,"Genius"      ,"  Smart slaves master skills faster and are able to cope with accounting better, so they are more valuable on the market. But it is easier to dominate and manipulate stupid ones.","   Smarts are not always useful, as more intellectual slaves are harder to control and manipulate. On the other hand, rational factors of submission and explanatory conversations will be more effective. Allowing a slave to express herself, training secretarial skills and doing household accounting can contribute to intellectual development."],
    "NATURE":        ["Spineless"       ,"Coward"         ,"Uncertain"     ,"Independent"  ,"Determined"   ,"Willful"        ,"Willful+"    ,"  Strong character makes a slave more interesting and independent but lowers her obedience. It is easier to control weak-willed slaves but their value will be lower too.","   Nature is an ambiguous feature. It is very hard to train a willful slave, but a weak will lowers a slave's value. The more you make a slave do what she does not want to do, the more her nature will break. It is difficult to restore nature, so do not overdo it. Victory in duels, martial arts, sleeping in her own room, assisting in training other slaves, and being given a measure of independence or opportunities to socialize can help in the formation of a solid nature."],
    "PRIDE":         ["Arrogant"        ,"Haughty"        ,"Proud"         ,"Aloof"        ,"Open"         ,"Unashamed"      ,"Unashamed+"  ,"  Pride prevents a slave from being open and enjoying sex. It also causes her to resist your will, and refuse humiliating orders.","   Pride is harmful both in training and in the sale, so you should work on her openness. Force her to do dirty, perverted and degrading things, and assign strict rules. Eventually pride will be broken and the slave will become more open. But do not overdo it, as with pride, you can break the very slave."],
    "EXOTICISM":     ["Ordinary"        ,"Quirky"         ,"Mysterious"    ,"Enigmatic"    ,"Exotic"       ,"Mystical"       ,"Mythical+"   ,"  Slaves with unusual, irregular appearance attract attention at once and generally are more interesting for customers.","   Some slaves are exotic inherently. You can increase exoticism with tattoos, piercings, body modifications, as well as flamboyant clothes and wigs."],
    "PHYSICAL":      ["Corpulent"       ,"Chubby"         ,"Voluptuous"    ,"Slender"      ,"Model"        ,"Bony"           ,"Model+"      ,"  You can get more mince from fat slaves but they are not attractive. Weedy starvelings aren't attractive as well, but you can't get a lot of meat from them either. It's better to keep your slave slim, but not skinny.","   Extra weight is generally harmful, as well as a lack of it. To keep your slave slim you need to balance her nutrition in a way that is sufficient, but not excessive. The more a slave works and the more endurance she has, the more food she needs. Physical exercises don't decrease weight directly but are a good way to burn extra calories. If a slave is underweight, feed her well and minimize athletics."],
    "STYLE":         ["Unfashionable"   ,"Unremarkable"   ,"Common"        ,"Stylish"      ,"Refined"      ,"Elegant"        ,"Elegant+"    ,"  A slave's appearance is extremely important during the sale. Customers will like well-groomed and well-dressed slaves, and an unappealing slave can be turned down even if she fits the requirements.","   Style depends little on natural abilities and skills, though it is influenced by the ability to communicate (elocution) and presence (dancing). Style suffers from dirt and sloppiness. Hairstyle, make-up, perfume, beautiful clothes and jewelry - all of these improve style and make the slave more attractive to customers. It is not necessary to constantly maintain style - it plays a role only when it is time to show the girl to the customer."],
    "FAME IN ROME":  ["Unknown"         ,"Rumored"        ,"Recognized"    ,"Celebrity"    ,"Famous"       ,"Legendary"      ,"Legendary+"  ,"  Famous slaves are much more valuable. Your slave's rank can reach the level of her fame, even if she lacks other attributes, beauty included.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum.","   Fame is not the most important parameter for a slave. You can train wonderful product unconcerned about this. Fame will grow with victories in the arena and colosseum."]
    }
define slave_traits = {
    "No brand": "The slave is not branded! You won't be able to sell an unbranded slave to customers, and an unbranded slave will take longer to accept her destiny as a slave. You could put a brand on her yourself if you have a dungeon (through the {b}Anatomy{/b} tab), go to a tattoo parlor in the Quarter of the Outcasts, or use a spell if you have the ability.",
    "sanity_broken": "The slave's spirit is broken. This means that the slave has become a soulless doll - it will reduce her rating, the slave will stop trying and she will also lose the will to live but will fulfill all orders without question. Until her Nature exceeds D-, Pride and Temperament will not rise. Winning battles, a boudoir, the Golden Cage, Garden of Gethsemane and hot springs may help to restore her spirit.",
    "sanity_low": "The state of mind of the slave is approaching dangerously low levels! Be careful with Pride - when pride lowers, the mind weakens. Check the condition of Temperament and Nature - their average should exceed D- for a normal state of mind.",
    "nymphomaniac": "You have noticed that your slave, to put it mildly, is partial to sex. Many sexual practices will be easier for her, but an insatiable desire will drive her crazy.",
    "frigid": "You understand that your slave is completely indifferent to sex. It is practically impossible to excite her and this will clearly complicate the development of many relevant practices and negate all erotic encouragement.",
    "masochist": "Pain does not scare your slave. On the contrary, she strives to be in pain and receives pleasure from it. Flogging a masochist is useless, but there are other ways to influence her…",
    "accustomed_to_pain": "Your slave is able to endure pain. She is not a masochist, but scaring her with ordinary torture will not be easy. However, you can always find other sources of fear in addition to pain…",
    "afraid_of_pain": "Your slave is terribly afraid of the pain and is ready to cry even from the most ordinary spanking. It is necessary to take note of it - painful punishments will be more effective!",
    "exhibitionist": "You notice that your slave takes special joy in demonstration of her naked body. You cannot make her feel ashamed of her nudity, but clearly some lessons will go easier.",
    "shy": "Obviously your slave is insanely shy of her own nudity. It will be difficult to teach the skills required to demonstrate nudity, but this trait can be used to select more effective punishment.",
    "pervert": "It seems that your slave likes things that most people find disgusting. She is particularly excited by the dirtiest and most perverted acts - this is clearly useful in the study of extreme sex skills.",
    "purist": "You notice that your slave doesn't tolerate non-standard and dirty types of sex and everything associated with perversion. Education in extreme sexual practices will be particularly challenging.",
    "lesbian": "Practice shows that your slave is completely indifferent to men but is happy to have sex with women. In most cases, this will create a problem, but even she can be taught something.",
    "bisexual": "You understand that your slave, with equal pleasure, will have sex with both women and men. Such open-mindedness can be quite useful for certain sexual practices.",
    "homophobic": "Your slave is completely incapable of being aroused by sex with another girl. Not that it is a big problem, but still, in some sexual practices she will underperform.",
    "psycho_masochist": "You notice that your slave gets a perverse pleasure when she is degraded and verbally abused. Cursing and threats will get you nowhere, it will only encourage further bad behavior. You should use harsher sanctions.",
    "hysteric": "Someone else's attention is incredibly important for your slave, she always wants to be in the spotlight and craves praise. Verbal encouragement will be particularly effective.",
    "child_of_darkness": "At every opportunity the your slave tends to hide in a dark corner. Looks as if she feels particularly comfortable in the dark. This may reduce the effectiveness of certain punishments.",
    "afraid_of_darkness": "You have noticed that your slave is mortally afraid to remain in the dark. This fear can be used for your benefit: punishments involving the restriction of sight will be particularly effective.",
    "bloodthirsty": "It seems that your slave likes the look and taste of blood. This feature can make some torture less effective, because needles and scalpels will attract, not scare the slave.",
    "afraid_of_blood": "At the sight of blood the slave almost faints. You take note that all tortures associated with the shedding of blood will produce a particularly powerful effect. It's time to sharpen needles and scalpels!",
    "pyromania": "Sounds like your slave is absolutely fascinated by fire. She is so fond of the flame that she even is ready to bravely endure painful burns. This will reduce the effectiveness of certain kinds of torture.",
    "pyrophobia": "Apparently, open flame inspires an animal terror in your slave. This means that using torture associated with fire, you can achieve a much larger effect.",
    "child_of_water": "It seems that your slave loves the water and is not very afraid of the prospect of being drowned. Frightening her with water-based torture will be difficult.",
    "hydrophobia": "Your slave is insanely afraid of choking and is petrified if her head is submerged in the water. It will make all water-related torture much more efficient.",
    "arachnophilia": "Apparently, your slave experiences an unhealthy passion for all sorts of nasty creatures: beetles, scorpions, snakes, rats and spiders especially! So it is impossible to scare her even with the vilest of reptiles.",
    "arachnophobia": "You notice that your slave madly afraid of all kinds of nasty creatures: beetles, scorpions, snakes, rats and spiders in particular. This means that torture with the use of reptiles will be extremely effective.",
    "loves_helplessness": "You notice that the restriction of mobility affects your slave very positively. Looks like she's just glad to be bound or locked in a tight box. This makes a lot of punishment virtually useless.",
    "InuredHelplessness": "You notice restricting her mobility does not seem to trouble your slave nearly as much. Punishments of this type will be less effective on her because of this, but at least they are not entirely useless.",
    "claustrophobic": "When you limit the mobility of the slave, she instantly begins to suffocate from fear. It seems that a sense of helplessness and inability to escape induces her animal terror. You should remember this when choosing a most effective punishment.",
    "lazy": "Watching your slave, you notice that she appreciates the opportunity to slack off. This is not too good for a slave, but some types of incentives will be clearly more effective.",
    "hyperactive": "Your slave just cannot sit still. She is always energetic, always busy with some work. Giving her free time will not earn you special gratitude.",
    "loves_luxury": "Apparently, your slave is crazy about everything that is beautiful, luxurious and brilliant. Dresses and jewelry will easily win her heart.",
    "ascetic": "It seems that your slave is completely indifferent to luxury. She cannot be bribed by shiny ornaments or luxurious dresses. And it's not so good, because you have less means of influence.",
    "sweet_tooth": "You notice that your slave is crazy about everything sweet and tasty. Such gastronomic predilections reveal sizable opportunities for manipulation: for a sweet dessert she'll be ready to go a great length!",
    "does_not_like_sweets": "It seems that your slave is not a gourmet. She eats very little and pays almost no attention to the taste of food. Alas, bribing her with cake or chocolate will not work.",
    "vain": "You notice that the slave blossoms around people. She obviously loves to be the center of attention and chats nonstop. Taking her on dates in the city will be a very effective reward.",
    "hikikomori": "You understand that your slave avoids strangers and doesn't enjoy being in public. It seems that all she wants is to lock herself in the four walls and not go anywhere. Dates will be a continuous stress for her.",
    "foolhardy": "Your slave is not just brave, she is foolhardy. For some reason she is ignorant of fear, and it is impossible to frighten her. People like her can be extremely dangerous, not only for others but for herself, too!",
    "brave": "Your slave is able to easily overcome her fear. Of course, she can still be influenced by fear; she is just much braver than ordinary slaves and thus breaking her with torture will not be easy.",
    "cowardly": "It seems that your slave is a real coward. Just a little bit of pressure - and she is ready to surrender. Even mild punishments will quickly break her will to resist and allow you to dictate your terms.",
    "powerful_metabolism": "Your slave's metabolism is incredibly efficient. She seems to be able to eat whatever she wants without gaining weight. Therefore, you can think less about diets.",
    "good_metabolism": "Your slave has a very good metabolism; she gains excess weight much slower than most people so she can be given some relief in the diet. It's convenient.",
    "weakened_metabolism": "Over time you realize that your slave has problems with metabolism. She gains excess weight faster than others so her diet requires special attention.",
    "weak_metabolism": "The metabolism of your slave is seriously disturbed. Just one extra bun is enough for extra fat grams to appear on the scales. You need to watch her diet very carefully.",
    "sporty": "Your slave is very mobile and gets a lot of pleasure from exercise. It will be not difficult for her to get in excellent physical shape.",
    "apathetic": "You notice that your slave is not fond of exercise and does not push herself. Getting her in proper physical shape will be difficult.",
    "orator": "Your slave shows a talent for self-expression. Developing her etiquette and rhetoric will be easy, and this is clearly good news!",
    "pet": "It seems that your slave really likes to pretend to be a pet. And, most importantly, she is doing it great. Training will go well!",
    "brony": "Apparently, your slave loves to be a horse. What others would consider humiliating and difficult, she finds fun and interesting.",
    "indolent": "Your slave is not in a hurry to use her body or her mind, and likes to just loaf: perhaps she could be more easily turned into a milk cow?",
    "nurse": "Your slave shows remarkable abilities in medicine. It will be easy to make a great nurse from her!",
    "maid": "Your slave seems to take great pleasure in keeping order in the house. This will allow her to become an excellent maid!",
    "cook": "Your slave clearly has a talent for cooking. She enjoys cooking and obviously has a lot of fun fumbling at the stove.",
    "warrior": "Your slave is an innate warrior! Developing her fighting skills will be easy, and these abilities are very much in demand.",
    "witch": "Your slave revealed incredible magic. She'll make a great witch or an alchemist.",
    "painter": "Your slave not only loves to paint but also has a great talent at reproducing anything she has in mind. It will be easy to train a great painter!",
    "musician": "Your slave has perfect pitch. This would be incredibly useful when learning to play a musical instrument. You should pay special attention to the development of her musical talent.",
    "dancer": "Your slave has obvious talent for dancing. She deeply feels the music and catches dance moves on the fly, easily improvising and inventing her own style and choreography.",
    "secretary": "You notice that your slave has excellent instincts for a personal assistant - she is collected, attentive and easily copes with paperwork. You should use this talent to its maximum!",
    "eidetic_memory": "It seems your slave has perfect recall. She can quote from memory whole pages of books. She is unlikely to ever forget what she has already learned.",
    "Forgetful" : "Your slave seems to have a complete mess in her head. She constantly forgets what she was told just a day ago. You only need to stop conducting lessons and her skills are lost at an alarming rate.",
    "Disciplined" :"Looks like your slave is accustomed to strict discipline and is ready to obey, ignoring her own desires. Certainly a useful feature for slaves.",
    "Willful":"Discipline is clearly not one of your slave's strengths. She is disorganized and always does everything as she pleases. You need to always stand over her with a stick.",
    "Delusions of grandeur": "Your slave clearly overestimates her merits and is too confident of her worth. However, it has a bright side: you can give larger rewards to her even for modest merits and not worry about spoiling her.",
    "Guilt_complex": "Your slave constantly feels guilty and feels very bad about any mistake. With such low self-esteem, she feels she deserves severe punishments for even insignificant offenses.",
    "Compassionate": "You understand that your slave feels other people's suffering. This can be used to control her!",
    "Sadist": "Your slave obviously enjoys watching the suffering of other people and might not mind participating in the process. Unfortunately, it narrows your means of influence.",
    "Natural Grace": "Your slave has smooth, fluid, natural, and beautiful movements and body language. There is a natural charm and beauty in whatever she does.",
    "Klutzy" :"Your slave has uncoordinated movements and body language. This will be a challenge for your slave if you make her engage in activities that require graceful movement.",
    "Dexterity": "Your slave is very agile with her fingers. She can move them fast and precisely. This aptitude will be a gift for your slave if you make her engage in artistic activities.",
    "Clumsy": "Your slave is very clumsy with her hands. This will be a challenge for your slave if you make her engage in artistic activities.",
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

    "angst": [
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
