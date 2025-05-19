define dic_custom_start_difficulty_selection = {
    "Free mode": ["Free mode",10000,999999],
    "Normal":    ["Normal"   ,6000 ,590   ],
    "Maximun":   ["Maximun"  ,400  ,340   ]
}
define dic_custom_start_difficulty_selection_index = ["Free mode","Normal","Maximun"]
define custom_skill_cost_value = [0,5,15,35,75,155,315]
define custom_selection_max_cap_sparks = [999999,8000,400]

define dic_home_state = {
    "slum_house": {
        "prestige": 0,
        "slaves_rooms":{
            "squalid_room": 1,
            "cramped_room": 0,
            "comfortable_room": 0,
            "luxurios_boudoir": 0
        },
        "size": 50,
        "base_security": 0,
        "state_property": {
            "owner": False,
            "rent": 5,
            "rent_increase": 2
        }
    },
    "kamira_house":{
        "prestige": 1,
        "slaves_rooms":{
            "squalid_room": 0,
            "cramped_room": 1,
            "comfortable_room": 0,
            "luxurios_boudoir": 0
        },
        "size": 200,
        "base_security": 100,
        "state_property": {
            "owner": False,
            "rent": 100,
            "rent_increase": 5
        }
    },
    "serpis_house":{
        "prestige": 2,
        "slaves_rooms":{
            "squalid_room": 0,
            "cramped_room": 2,
            "comfortable_room": 0,
            "luxurios_boudoir": 0
        },
        "size": 500,
        "base_security": 250,
        "state_property": {
            "owner": False,
            "rent": 300,
            "rent_increase": 10
        }
    },
    "taurus_house":{
        "prestige": 3,
        "slaves_rooms":{
            "squalid_room": 0,
            "cramped_room": 2,
            "comfortable_room": 1,
            "luxurios_boudoir": 0
        },
        "size": 1000,
        "base_security": 400,
        "state_property": {
            "owner": False,
            "rent": 650,
            "rent_increase": 15
        }
    },
    "korvus_house":{
        "prestige": 4,
        "slaves_rooms":{
            "squalid_room": 0,
            "cramped_room": 0,
            "comfortable_room": 3,
            "luxurios_boudoir": 0
        },
        "size": 1500,
        "base_security": 750,
        "state_property": {
            "owner": False,
            "rent": 1400,
            "rent_increase": 20
        }
    },
    "white_house":{
        "prestige": 5,
        "slaves_rooms":{
            "squalid_room": 0,
            "cramped_room": 0,
            "comfortable_room": 2,
            "luxurios_boudoir": 3
        },
        "size": 2500,
        "base_security": 1500,
        "state_property": {
            "owner": False,
            "rent": 3000,
            "rent_increase": 25
        }
    }
}
define dic_improvement_rooms ={
    "kitchen": {
        "Deplorable kitchen": {
            "cost": 150,
            "size": 50,
            "risk": 10,
            "modifier": -3
        },
        "Basic kitchen": {
            "cost": 500,
            "size": 100,
            "risk": 50,
            "modifier": -1
        },
        "Well-equipped kitchen": {
            "cost": 1200,
            "size": 150,
            "risk": 100,
            "modifier": +1
        },
        "Gourmet kitchen": {
            "cost": 2500,
            "size": 200,
            "risk": 300,
            "modifier": +3
        }
    },
    "slaves_rooms":{
        "squalid_room":{
            "cost": 50,
            "size": 20,
            "risk": 5,
            "modifier": -3
        },
        "cramped_room":{
            "cost": 150,
            "size": 30,
            "risk": 20,
            "modifier": -1
        },
        "comfortable_room":{
            "cost": 500,
            "size": 50,
            "risk": 50,
            "modifier": +1
        },
        "luxurios_boudoir":{
            "cost": 1500,
            "size": 100,
            "risk": 150,
            "modifier": +3
        }
    },
    "barn": {
        "Collapsing barn": {  
            "cost": 100,
            "size": 80,
            "risk": 15,
            "modifier": -3
        },
        "Worn barn": {  
            "cost": 400,
            "size": 120,
            "risk": 60,
            "modifier": -1
        },
        "Sturdy barn": { 
            "cost": 1000,
            "size": 160,
            "risk": 120,
            "modifier": +1
        },
        "Masterwork barn": {  
            "cost": 2200,
            "size": 220,
            "risk": 250,
            "modifier": +3
        }
    },
    "laboratory": {
        "Makeshift lab": {  # Very Bad
            "cost": 200,
            "size": 40,
            "risk": 15,
            "modifier": -3
        },
        "Crude lab": {  # Bad
            "cost": 600,
            "size": 80,
            "risk": 60,
            "modifier": -1
        },
        "Proper lab": {  # Good
            "cost": 1400,
            "size": 120,
            "risk": 120,
            "modifier": +1
        },
        "Advanced laboratory": {  # Very Good
            "cost": 3000,
            "size": 180,
            "risk": 250,
            "modifier": +3
        }
    }
}


