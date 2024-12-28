import streamlit as st
from PIL import Image

# Define the questions, answers, and logic
questions = {
    "start": {
        "tag": "filler",
        "text": "# **Pick a cat**",
        "image": "images/group_cats.jpg",
        "options": {
            "Pau": "pau_1",
            "Magatha": "magatha_1",
            "Ami": "ami_1",
            "Jana": "jana_1",
            "Jus": "jus_1",
            "Martin": "martin_1",
            "Kay": "kay_1",
            "Des": "des_1",
            "Angel": "angel_1",
            "Shelly": "shelly_1",
            "Ron": "ron_1"

        },
    },
    "pau_1": {
        "text": """You pick *Pau* and *Pau* licks their paw and tells you to hop on the Y line to visit Mewhattan with them. Your fee is an ounce of catnip. :herb: Do you pay your train fee?""",
        "image": "images/pau.jpg",
        "options": {
            "Yes": "mewnolia",
            "No": "pau_1_no",
        },
        "tag": "filler"
    },
    "magatha_1": {
        "text": """You pick the studious cat, *Magatha*. The page they're reading says, 'Having fun isn't hard when you got a library card!' It also has a photo of a Tardis from Doctor Cat. :blue_book: Are you sure you want to be escorted by this cat?""",
        "image": "images/magatha.jpg",
        "options": {
            "Yes! I love Doctor Cat!": "box_science",
            "Yes?": "box_science",
            "I don't talk to nerds": "magatha_1_no"
        },
        "tag": "filler"
    },
    "ami_1": {
        "text": """You pick a royal cat from the :sparkles: Magikal Kingdom :sparkles: where all dreams come true. Their breath smells of fresh fish and their fur is shiny and well-groomoed. They meow and say, 'Call me Your Majesty *Ami*. I'll be your guide today in Mew York City. Would you like to go to Catten Island or Cateens first?'""",
        "image": "images/ami.jpg",
        "options": {"You bow and say, 'Cateens, Your Majesty.'": "ami_1_catten_island",
                    "You salute and say 'Catten Island, Your Majesty!'": "ami_1_cateens",
                    "You curtsy and say that is a pleasure to spend the day with Your Majesty and ask for them to choose a place that they would want to visit instead.": "paw_salon"
                    },
                    "tag": "filler"
    
    },
    "jana_1": {
        "text": """You pick *Jana*, the calm gray cat with the icy blue eyes :small_blue_diamond:. *Jana* unexpectedly screams with joy and their eyes dance with excitement, shattering their cool demeanor. 'OH MY GOD. THANKS FOR CHOOSING MOI! LET ME TAKE YOU TO ALL AROUND CATTEN ISLAND, FUR REAL FUR REAL!""",
        "image": "images/jana.jpg",
        "options": {"""You love Jana's energy and enthusiastically goes along with them.""": "paw_salon",
                    """You're an introvert and already feel your social battery draining next to this cat, but you go along with them because you're a pushover.""": "paw_salon",
                    "You say no thanks and walk in the other direction.": "jana_no_1"},
                    "tag": "filler"
    },
    "jus_1": {
        "text": """You pick *Jus*, the skinny yellow-eyed cat who seems to have multiple scratches on their body as if they have been in a brawl with other cats. :scream_cat: *Jus* says, 'Rough day at work. But, here I am. Ready to be your escort for today.'""",
        "image": "images/jus.jpg",
        "options": {"""You're worried for Jus and asks if they are ok.""": "jus_1_yes",
                    """You're curious about what Jus does for work as a cat so you ask them""": "jus_1_yes",
                    """You don't trust Jus because it feels like they are part of a cat mafia, so you tell them you'll find another cat to escort you.""": "end_jus"},
                    "tag": "filler"
    },
    "martin_1": {
        "text": """You pick *Martin*, the cat with the top-hat :tophat: and monocle. *Martin* tips their top hat at seeing you and says, 'Welcome, welcome to Mew York City. I'll be at your service today. Where would you like to go first, kind human? Cateens or Mewhattan?""",
        "image": "images/martin.jpg",
        "options": {"""You also tip your top-hat and pull out a monocle from your back-pocket and tell Martin you want to go to Mewhattan, the fishiest of the places in Mew York City.""": "mewnolia",
                    """You don't like this Martin's gentlecattly behavior because you have never been treated with respect before, so you ask them to fetch you another cat to be your escort for the day.""": "martin_1_no"
                    },
        "tag": "filler"
    }, 
    "kay_1": {
        "text": """You pick *Kay*, the yellow cat who seems to be entangled with a ball :red_circle: of red yarn. The disheveled *Kay* looks at you and says, 'Ah! Hello! While I detangle myself from this yarn, decide where you'll want to go first! Meow!""",
        "image": "images/kay.jpg",
        "options" : { """You think to yourself that this cat is cute but doesn't seem to be dependable, but you're a kind person and asks if Kay needs any help detangling from the yarn.""": "pizza",
                        "Can you bring me to Brooknyan?": "yoga",
                        "Can you bring me to The Box?": "box_science"},
        "tag": "filler"
    },
    "des_1": {
        "text": """You pick *Des*, the calico with the big round eyes that seem to peer deep in your lost soul :eyes:. *Des* says, 'Welcome to your destiny. You're gonna follow me or get banned. Now come along, human.""",
        "image": "images/des.jpg",
        "options": {"You think to yourself that this cat is sus but their aura is too powerful for you to refuse, so you follow them obediently.": "mewnolia",
                    "No one tells you what to do. You refuse to go with this crazy calico.": "end_des"},
         "tag": "filler"
    },
    "angel_1": {
        "text": """You pick the funky purple cat with the tiara and microphone, *Angel*. Angel picks up the microphone :microphone: and whispers, 'I can show you the world. Shining, shimmering, splendid. Tell me human now when did you last let your heart decide? Mewhattan, Brooknyan or Cateens?'""",
        "image": "images/angel.jpg",
        "options": {"""You sing along, 'A whole new world! A new fantastic point of view. No one to tell us no. Or where to go...'""": "mewnolia",
                    "You pick Cateens, the Queens of Mew York City.": "speakeasy",
                    "You pick Brooknyan, you heard it has the best pizza, therefore the best rats.": "pizza"},
         "tag": "filler"
    },
    "shelly_1": {
        "text": """You pick the mysteriously ordinary looking gray cat who was winking at you, *Shelly* :dizzy:. *Shelly* says, 'Oh, hello! You picked a witch's apprentice, how lucky! You're in good paws. I can bring you to the Box, Mewhattan, and Cateens. Where would you like to go first?""",
        "image": "images/shelly.jpg",
        "options": {"You don't like witches, let alone a witch's apprentice. You're afraid of them casting a love spell on you like one witch did in your past, which left you bankrupt. So, you ask Shelly if you can get another cat to escort you.": "end_shelly",
                    "Witches aren't real, you say to yourself. You think this cat is high, but whatever. You tell Shelly you want to go to Mewhattan.": "mewnolia",
                    "You tell Shelley to pick a place randomly for you as you don't have a preference." : "mewnolia",
                    "You tell Shelly you want to go to the Box." : "box_science",
                    "You are excited to be in the presence of a witch's apprentice as you secretly admired witches for the past 3.14 years of your life. And you know the lore that witches lives in Cateens so you pick Cateens.": "yarnball"
                    },
        "tag": "filler"
        
    },
    "ron_1": {
        "tag": "filler",
        "text": """You pick the silly cat with the Christmas tree hat, *Ron* :evergreen_tree:. *Ron* says, 'Did you know this hat is from Miu Miu? It's the latest model, made from the finest yarns. Ah. The best yarns can be found in Mewhattan. I can bring you there, or if you like, I can also bring you to Cateens and Brooknyan first. Where would you like to go?'""",
        "image": "images/ron.jpg",
        "options": {"You LOVE designer things. You tell Ron that you want to go to Mewhattan.": "mewnolia",
                    "You don't have much money to shop for the finest Christmas tree hats, unfortunately, so you tell Ron that you'll rather go to Cateens where the food was said to be cheap and eXoTiC.": "speakeasy",
                    "Brooknyan": "pizza"}
    },
    "pau_1_no": {
         "tag": "filler",
        "text": "Pau scowls at you and calls someone on their walkie talkie. A purple cat with a tiara and a microphone appears. Do you go with Angel, the purple cat?",
        "image": "images/angel.jpg",
        "options": {"yes": "pau_angel",
                    "no": "pau_des"},
    },
    "pau_angel": {
         "tag": "filler",
        "text": "#Angel says we’ll take the free W line. Do you want to stay in Mewhattan or go to Brooknyan or Cateens?",
        "image": "images/ai/train.jpg",
        "options": {"Mancattan":"mewnolia",
                    "Brooklynan": "yoga",
                    "Cateens": "yarnball"},
    },
    "pau_des": {
         "tag": "filler",
        "text": "Angel looks offended. They sings a sad tune on their karaoke mic and another cat named Des appears. Des says, 'This is your last chance which will determine your destiny. Come with me or get banned.'",
        "image": "images/des.jpg",
        "options": {"Go with Des": "cattail"},
    },

    "mewnolia_1": {
         "tag": "mewnolia",
        "text": "At your sneeze, you get transported to Mewnolia bakery where the smells of freshly baked tuna pastries make you drool. Your escort cat says, 'Pick a pastry. Any pastry.'",
        "image": "images/ai/mewnolia.jpg",
        "options": {"You choose the bluefin salmon cake with the catnip on top.": "end_des",
                    "You pick the classic tuna fish pastry and you ask your escort cat which pastry they like and offers to buy one for them to thank them for their time.": "lion"}
    },
    "magatha_1_no": {
         "tag": "filler",
        "text": "All the escort cats have scattered except for an ordinary gray cat who winks at you. You have no choice but to follow Shelly. Shelly introduces themself as a witch's apprentice and says that since you have no choice but to be escorted by them, they will bring you to Cateens.",
        "image": "images/shelly.jpg",
        "options": {"Oh great. I don't like witches but, I have no choice. Cateens it is.": "speakeasy",
                    }
    },
    "jana_no_1": {
         "tag": "filler",
        "text": "Jana's excitement scares away all the cats except for a demure, white cat with a pink bow. The remaining cat introduces themselves as Ami, a royal cat from the Magikal Kingdom. They politely give you the choices of Catten Island or Cateens to visit. Which do you choose?",
        "image": "images/ami.jpg",
        "options": {"Cateens. The Queens of Mew York City.": "speakeasy",
                    "Catten Island. Never heard of this place before. Is it even part of Mew York City?": "paw_salon"}
                    
    },
    "jus_1_yes": {
         "tag": "speakeasy",
        "text": "Jus tells you that they are actually a stay at home cat-parent and the scratches are just from wrestling with their kittens. They then decide to bring you to Cateens to visit the Siamese speakeasy for a drink to unwind.",
        "image": "images/ai/speakeasy.jpg",
        "options": {"OoOo...Get me a cosmewpolitan, will you?": "jus_2",
                    "I'm more curious about Jus' kittens. I wonder what life is like for kittens in Mew York City.": "box_science",
                    },
    },
    "jus_2": {
         "tag": "catstones",
        "text": "You get a cosmewpolitan at the Siamese speakeasy and didn't realize that cat alcohol is very strong. You brown out and by the time you're aware, you find yourself in the a block part in the Catstones in Brooknyan. It looked like a local cat paradise- cats selling homemade fish fritters, cat jungle gyms on the street and Doja Cat music playing in the background.",
        "image": "images/ai/catstones.jpg",
        "options": {"Wow! This is fantastic. I could stay in this carnival for hours!": "end_catstones",
                    "I wonder if these cats are strays or pets and where their homes are?": "kitty_field",
                }
    },
    "martin_1_no": {
         "tag": "filler",
        "text": "After refusing your first escort cat, you notice that all the escort cats have disappeared except for a yellow cat entangled in red yarn who is struggling with unknotting themself from the mess. You walk over and the yellow cat chirps, 'Hello! I'm Kay! I'll be right with you. Nya.",
        "image": "images/kay.jpg",
        "options": {"You think to yourself that this cat is cute but doesn't seem to be dependable, but you're a kind person and asks if Kay needs any help detangling from the yarn.""": "pizza",
                    "You like to watch cats suffer so you just smirk and watch Kay struggle with untangling themself.": "end_kay"
                       
        }
    },
    "ami_1_catten_island": {
         "tag": "filler",
        "text": "You wanted to go to Cateens? Nah, let's go to Catten Island instead.",
        "image": "images/ami.jpg",
        "options": {"You have no options to say no to Your Majesty. You go to Catten Island with them.": "paw_salon"}

    },
    "ami_1_cateens": {
         "tag": "filler",
        "text": "You want to go to Catten Island? I kind of want to go to Cateens. Let's go to Cateens instead!.",
        "image":"images/ami.jpg",
        "options": {"You have no options to say no to Your Majesty. You go to Cateens with them.": "speakeasy"}
    },
    "yarnball": {
         "tag": "yarnball",
        "text": "For the next stop, your escort cat brings you to stroll in a large park with the World's Fair Yarnball in Cateeens, the original source of all yarn in Mew York City. The Yarnball has every type, color, material, texture of yarn imaginable for cats in MYC. But, it has been forgotten and is more of a relic now since cats have found other, cheaper ways of extracting yarn from other places outside of MYC. ",
        "image": "images/ai/yarnball.jpg",
        "options": {"You stare at awe at the yarnball and wonder how cats can harvest any type of yarn from it.": "fishing",
                    "You have a strong desire to knit and/or crochet or just to create something artsy when looking at the magnificient yarn ball.": "fishing",
                    "Why do cats worship yarn so much? What is the point?": "dump"}
    },
    "speakeasy": {
         "tag": "speakeasy",
        "text": "You arrive in Cateens on the W line and get escorted to the Siamese Speakeasy off of Cateensboro Plaza. There was a line to get into the speakeasy, but your escort insists that you wait for a table or a spot at the bar to open up. After a few cat hours, you get seated.",
        "image": "images/ai/speakeasy.jpg",
        "options": {"You order a cosmewpolitan and enjoy your time flirting with the cute bartender.": "yoga",
                    "You order a mocktail because you don't drink alcohol.": "yarnball",
                    "SHOTS SHOTS SHOTS SHOTS SHOTS SHOTS SHOTS SHOTS SHOTS! EVERYBODY!": "end_speakeasy",
                    },
    },
     "mewnolia": {
         "tag": "mewnolia",
        "text": "Your escort cat guides you to the train and you arrive at Mewnolia Bakery in a couple of minutes. The aroma of freshly baked fish pastries and meaty bread hits you as you enter the store. Your escort says it is their treat and asks you to pick something!",
        "image": "images/ai/mewnolia.jpg",
        "options": {"You choose the bluefin salmon cake with the catnip on top.": "yarnball",
                    "You pick the classic tuna fish pastry and thank your escort cat for the treat!": "lion",
                    "You pick the cookie called 'If you give a mouse a cookie'. (Later you find out it is made of mouse meat).":"lion",
                    "You say that you aren't hungry and that you don't like fish. (GASP)": "paw_salon"}

    },
    "lion": {
         "tag": "lion",
        "text": "After the treat, you and your escort cat goes on to the next stop. The Lion King. The legendary musical acted by the cats who have been selected through an arduous auditioning process. They're all on top of the food chain, tapped into their innate predatorial and majestic insticts which many pet cats lost.",
        "image": "images/ai/lion.jpg",
        "options": {"You are starstruck by the roles the cats were playing in The Lion King. You are so eager to get the lead's paw print that you wander off after the show to find the lead cat.": "end_lion",
                    "You want to digest the show you have just witnessed with your escort cat and ask them to bring you to a place for a drink.":"speakeasy",}
    },
    "cattail": {
         "tag": "cattail",
        "text": "Des brings to ride the M line to Mewhattan's Cattail Park. Des says, 'These are my favorite plants. They make all the humans I know sneeze. I like to hear people sneeze. It's like music to my ears.",
        "image": "images/ai/cattail_park.jpg",
        "options": {"You sneeze.": "mewnolia_1",
                    "Where will you bring me next?": "end_des"}
    },
    "box_science": {
         "tag": "box_science",
        "text": "Your escort cat waves a paw and you arrive at the Box Science Kitten School! Box Science is a prestigious school for kitties where they get groomed to serve the Boss Cats. Some of the kittens become Boss Cats themselves, but the majority of them decide to serve the Boss Cats because it's just easier and more peaceful to earn their fish that way. The Box Science School is the fishiest ticket out of having to eat dried, tasteless cat food every day.",
        "image": "images/ai/box_science.jpg",
        "options": {"You think about how capitalism has affected Mew York City and wonder how you can use this knowledge to your advantage.": "mall_2",
                    "What is this? thank u, next.": "catstones"}
    },
    "dump": {
         "tag": "dump",
        "text": "You and your escort cat then rides the train to reach a dumpster, a treasure trove for cats of Mew York City. The dumpster is full of boxes, rats, leftovers- entertainment and snacks abound.",
        "image": "images/ai/dump.jpg",
        "options": {"You're furious that your escort cat brought you to a dumpster of all places. The Mew York City you read about was all glam and glitter.": "end_dump",
                    "You appreciate the contrast of the glam and glitter you read about Mew York City and the garbage dump you see in reality.": "box_science",
                }
    },
    "zoo": {
         "tag": "zoo",
        "text": "Your escort cat says it will bring you to the Box Zoo. You hop on an overcrowded train and arrive at the Box Zoo and see many rectangular boxes at the zoo. On closer examination, you realize that there are humans in the boxes, some cooking, doing household chores, some in suits and working in an office like setting on their computers. It seems like the Box Zoo is a mini replica of a human city.",
        "image": "images/ai/zoo.jpg",
        "options": {"You tell your cat escort that you are getting thirsty and could use a drink and a snack.": "speakeasy",
                    "You think that this zoo is inhumane and wonder if the people in the boxes know that they are in boxes. You demand to see the manager of the zoo.": "end_zoo",
                    "You are fascinated by the zoo's exhibits and how accurate it portrays modern human life. You thank your cat escort and ask them where they will take you next.": "yoga"}
    }, 
    "paw_salon": {
         "tag": "salon",
        "text": "Your escort cat licks their paw three times and you are transported to Catten Island's fanciest paw salon, 'Purrfect Paws'. Here, there are cats taking naps, getting massages, getting brushed and being pampered.",
        "image": "images/ai/salon.jpg",
        "options": {"Ah. I could use a spa day too. You ask for a cat massage.": "end_salon",
                    "You're frustrated that your cat brought you to a salon. You just want to explore the city not be in a salon!": "dump"
                    }
    },
    "fishing": {
         "tag": "fishing",
        "text": "'Let's take a break and go fishing,' your escort cat says. You take a short train ride and arrive at the pier and your escort cat whips out two fishing poles, some bait and a hat. 'Do you like to fish?'",
        "image": "images/ai/fishing.jpg",
        "options": {"You tell your escort that you have never fished before but would like to learn.": "end_fishing",
                    "You tell your escort that you didn't come to Mew York City to fish and that you don't need a fishing break. You'll rather be exploring the rest of the city.": "paw_salon",
                    "You're seasoned at fishing and love the activity, so you spend the rest of the day fishing with your escort cat": "end_fishing" }
    },
    "mall": {
         "tag": "mall",
        "text": "'You could use a new wardrobe', your cat escort says. With a wink of an eye, you get transported to Catten Island Mall, where there is budget to luxury cat brands, from your generic brands to Fancy Feast.",
        "image": "images/ai/mall.jpg",
        "options": {"You think that you could use a new t-shirt, preferably one that says 'I love Mew York'. You ask your escort cat where you can find one like that.": "mall_1",
                    "You don't need a new wardrobe and don't want to buy into consumersim too much, so you ask your escort cat to take you somewhere else.": "paw_salon",
                     }
    },
    "mall_2": {
         "tag": "mall",
        "text": "'I know what you're thinking, your cat escort says. You wish to consume and what better place to go next than to a mall for some retail therapy? With a wink of an eye, you get transported to Catten Island Mall, where there is budget to luxury cat brands, from your generic brands to Fancy Feast.",
        "image": "images/ai/mall.jpg",
        "options": {"You think that you could use a new t-shirt, preferably one that says 'I love Mew York'. You ask your escort cat where you can find one like that.": "end_mall",
                    "You don't need a new wardrobe and don't want to buy into consumersim too much, so you ask your escort cat to take you somewhere else.": "pizza",
                     }
    },
    "yoga": {
         "tag": "yoga",
        "text": "After a long pause, your escort cat says, 'Mew Cat City has many yoga studios. Let me take you to a well known one that teaches Catonah Yoga,' your escort cat says. Your escort takes you down multiple levels into the underground subway and you both commute to Brooknyan's Catonah Yoga studio. You take a 75 minute yoga class with your escort.",
        "image": "images/yoga.jpg",
        "options" :{"You feel so relaxed in yoga class and fall asleep in savasana (corpse pose), sleeping away the whole day.": "end_yoga"
        }
    },
    "end_yoga": {
        "tag": "filler",
        "text": "You wake up to find yourself turned into a micro-calico cat on top of a red rose in full bloom. You'll turn back into a human eventually, but now you get the chance to experience Mew York City like a local!",
        "image": "images/rose.jpg",
        "options": {}
    },
    "pizza": { 
         "tag": "pizza",
        "text": "Your escort cat meows and tells you to follow them for a treat and brings you to Catnip Pizza. There, you find that cats enjoy toppings of fish, rat tails, bird sausage, chopped liver, and of course the classic catnip.",
        "image": "images/ai/pizza.jpg",
        "options" : {"Your curiosity causes you to try the rat tail pizza topping.": "catstones",
                     "Bird sausage is just chicken sausage, right? I'll have a slice of that. It seems safe.": "end_pizza",
                     "No toppings for me- just the cat-cheese pizza please.": "catstones"}
    },
    "end_pizza": {
        "tag":"filler",
        "text":  "Cat cheese and bird sausage on pizza is a whole other beast. You spend the rest of the day on the toilet.",
        "image":"images/ai/end_toilet.jpg",
        "options": {}
    },
    "catstones": {
        "tag":"catstones",
        "text": "Your escort cat says that they heard through the cat network that there's a block party in the Catstones in Brooknyan. You both venture to the Catstones and see a local cat paradise- cats selling homemade fish fritters, cat jungle gyms on the street and Doja Cat music playing in the background.",
        "image": "images/ai/catstones.jpg",
        "options": {"You think that the block party is lit! You can stay here for hours!": "end_catstones",
                    "You're getting tired of seeing fish in all the food and wished for a hot-dog": "kitty_field",
                    }
    },
    "end_catstones": {
        "tag":"filler",
        "text": "You party the whole day and night at the Catstones, find yourself a cat partner and end up having a sleepover at their place where you both knit blankets until the next day.",
        "image": "images/ai/end_catstones.jpg",
        "options": {}
    },
    "kitty_field":{
        "tag":"kitty_field",
        "text": "'I know that the best hot dogs can be found in Kitty Field, home of the Mew York Pets,' your cat says. There is a game today and I got us tickets to go watch it.' You both go to the game and you get your hot-dog. The Pets lost.",
        "image": "images/ai/kitty_field.jpg",
        "options": {"You think to yourself that you have never seen so many cats gathered in one stadium before. As the only human, you feel a little estranged and you secretly wish there was another human with you now.": "zoo",
                    "I liked eating the hot-dog more than watching the game.": "end_kitty_field",
                    "I wonder where my cat will escort me to next?": "zoo"}
    },
    "end_kitty_field": {
        "tag":"filler",
        "text": "###### The hot dog was good, but it's not the hot dog you know. You end up glued on the toilet the rest of the day.",
        "image": "images/ai/end_kitty_field.jpg",
        "options": {}
    },
    "end_fishing": {
        "tag": "filler",
        "text": "You catch a bucket full of fish and it turns out that your escort cat is a sushi chef. They prepare all the fresh fish, safe to be consumed raw, and you get a 3 Mewchilen Star meal made by your private cat chef.",
        "image":"images/ai/end_fishing.jpg",
        "options":{}
    },
    "end_speakeasy":{
        "tag": "filler",
        "text": "What did you expect with the shots? You pass out and your escort cat calls the Cat Bus to bring you back home.",
        "image": "images/ai/end_speakeasy.jpg",
        "options": {}
    },
    "end_lion":{
        "tag": "filler",
        "text": "You get lost in the crowd of other cats trying to get the lead's autograph. You get separated from your escort cat and a human without an escort in Mew York City gets lost real quick. You get sent to the Mew York City Lost and Found and spend the rest of the day there.",
        "image": "images/ai/end_lion.jpg",
        "options": {}

    },
    "end_zoo":{
        "tag": "filler",
        "text": "The manager comes to see you and with a twitch of their whiskers, puts you in a box and you are transported back home. The manager puts you on display in the zoo and you are trapped in the Box Zoo exhibit for the rest of the day.",
        "image": "images/ai/end_zoo.jpg",
        "options": {}

    },
    "end_dump":{
        "tag": "filler",
        "text": "Your escort cat glares at you and says, 'If you can't handle Mew York City at her worst, you don't deserve Mew York City at her best.'",
        "image": "images/ai/end_dump.jpg",
        "options": {}

    },
    "end_salon":{
        "tag": "filler",
        "text": "You get a full-body cat massage. It was so relaxing that you fall asleep. It is etiquette in cat salons to not wake any sleeping cats or humans, so you end up sleeping in the salon for the rest of the day.",
        "image": "images/ai/end_salon.jpg",
        "options": {}

    },
    "end_mall":{
        "tag": "filler",
        "text": "You end up going on a shopping spree, buying all Mew York City merch. By the time you are done shopping, the traffic to leave the mall was so heavy that it was already past midnight.",
        "image": "images/ai/end_mall.jpg",
        "options": {}

    },
    "end_shelly": {
         "tag": "filler",
        "text": "You never say no to a witch's apprentice. ;)",
        "image": "images/shelly.jpg",
        "options": {}
    },
     "end_jus": {
         "tag": "filler",
        "text": "You were right that Jus is part of the cat mafia. You just rejected the lead of the cat mafia's offer. A clowder of cats swarm at you and claw at your body. You scream as you wake up from this nightmare.",
        "image": "images/ai/end_jus.jpg",
        "options": {}
    },
     "end_des": {
         "tag": "filler",
        "text": "###### Des says that you are banned.",
        "image": "images/ai/end_des.jpg",
        "options": {}
    }

    
}


def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
        return None
tag_list = []
# Main app logic

def main():
    st.title("A Day in Mew York City")

    # Initialize session state
    if "current_question" not in st.session_state:
        st.session_state.current_question = "start"

    # Initialize the tag_list in session state
    if "tag_list" not in st.session_state:
        st.session_state.tag_list = []

    # Get the current question data
    current_question = questions[st.session_state.current_question]

    # Display question image
    image = load_image(current_question["image"])
    if image:
        st.image(image, use_container_width=True)

    # Display question text
    st.markdown(current_question["text"])


    # Display options if any
    if current_question["options"]:
        for option_text, next_question in current_question["options"].items():
            if st.button(option_text):
                # Update session state with the next question
                st.session_state.current_question = next_question

                # Append the current question's tag
                if current_question["tag"] not in st.session_state.tag_list:
                    st.session_state.tag_list.append(current_question["tag"])

                # Append the next question's tag
                next_question_tag = questions[next_question]["tag"]
                if next_question_tag not in st.session_state.tag_list:
                    st.session_state.tag_list.append(next_question_tag)

                # Rerun to display the next question
                st.rerun()

    else:
        # Add the tag of the final question
        if current_question["tag"] not in st.session_state.tag_list:
            st.session_state.tag_list.append(current_question["tag"])

        # Count unique tags excluding "filler"
        unique_tags = [tag for tag in set(st.session_state.tag_list) if tag != "filler"]
        counter = len(unique_tags)

        # Display results
        #st.write(f"Tags visited: {set(st.session_state.tag_list)}")
        st.write(f"You visited {counter} places out of 15 places in Mew York City! Thanks for playing!")

if __name__ == "__main__":
    main()

   