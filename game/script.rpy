# Displayables and assets
image bg:
    "images/bg.jpg"
    size (1920, 1080)

image black = "#000000"

init python:
    import random

    class Character(renpy.store.object):
        def __init__(self, name, race, char_class, stats, skills, face_image, rarity, rarity_color):
            self.name = name
            self.race = race
            self.char_class = char_class
            self.stats = stats
            self.strength = stats.get("Strength", 0)
            self.agility = stats.get("Agility", 0)
            self.intelligence = stats.get("Intelligence", 0)
            self.defence = stats.get("Defence", 0)
            self.power = stats.get("Power", 0)
            self.skills = skills
            self.skills_text = ", ".join(skills)
            self.face_image = face_image
            self.rarity = rarity
            self.rarity_color = rarity_color

    # Name pools by race
    names = {
        "Human": ["John", "Alice", "Mark", "Lily", "Simon", "Labretus", "Greg"],
        "Elf": ["Elrond", "Tauriel", "Legolas", "Galadriel"],
        "Dwarf": ["Gimli", "Thorin", "Balin", "Kili"]
    }

    # Available classes and skills
    classes = ["Thief", "Swordman", "Priest"]

    skills = [
        "Stealth", "Sword Mastery", "Healing",
        "Archery", "Magic", "Defense"
    ]

    # Portrait images by race
    face_images = {
        "Human": ["human_face1.png", "human_face2.png", "human_face3.png"],
        "Elf": ["elf_face1.png", "elf_face2.png", "elf_face3.png"],
        "Dwarf": ["dwarf_face1.png", "dwarf_face2.png", "dwarf_face3.png"]
    }

    # Rarity tier configuration
    rarities = {
        "Common": {"stat_modifier": 0, "chance": 70, "color": "#5c6b73"},
        "Uncommon": {"stat_modifier": 1, "chance": 20, "color": "#1b7a43"},
        "Rare": {"stat_modifier": 2, "chance": 8, "color": "#1b5da7"},
        "Legendary": {"stat_modifier": 3, "chance": 2, "color": "#c47a00"}
    }

    def get_rarity():
        tier_list = list(rarities.keys())
        tier_weights = [rarities[k]["chance"] for k in tier_list]
        return random.choices(tier_list, weights=tier_weights, k=1)[0]

    def generate_character():
        race = random.choice(list(names.keys()))
        name = random.choice(names[race])
        char_class = random.choice(classes)
        face_image = random.choice(face_images[race])
        rarity = get_rarity()

        base_stats = {
            "Agility": random.randint(1, 10),
            "Strength": random.randint(1, 10),
            "Intelligence": random.randint(1, 10),
            "Defence": random.randint(1, 10),
            "Power": random.randint(1, 10)
        }

        stat_boost = rarities[rarity]["stat_modifier"]
        stats = {k: v + stat_boost for k, v in base_stats.items()}
        selected_skills = random.sample(skills, k=2)
        rarity_color = rarities[rarity]["color"]

        return Character(
            name=name,
            race=race,
            char_class=char_class,
            stats=stats,
            skills=selected_skills,
            face_image=face_image,
            rarity=rarity,
            rarity_color=rarity_color
        )

# Session state
default current_character = None

# Gacha result card screen
screen gacha_result(character):
    modal True

    frame:
        align (0.5, 0.5)
        xsize 600
        ysize 442
        background "window_background.png"
        padding (42, 38)

        vbox:
            spacing 14
            align (0.5, 0.5)

            hbox:
                spacing 24
                align (0.5, 0.5)

                # Character portrait and rarity badge
                vbox:
                    spacing 8
                    align (0.5, 0.5)

                    frame:
                        background "#00000022"
                        padding (4, 4)
                        align (0.5, 0.5)
                        add character.face_image:
                            align (0.5, 0.5)

                    text "[character.rarity]":
                        size 18
                        bold True
                        color character.rarity_color
                        align (0.5, 0.5)

                # Character details and attributes
                vbox:
                    spacing 4
                    align (0.5, 0.5)

                    text "[character.name]":
                        size 22
                        bold True
                        color "#2c1810"

                    text "[character.race] • [character.char_class]":
                        size 15
                        color "#523c28"

                    null height 4

                    text "Attributes:" size 15 bold True color "#2c1810"
                    hbox:
                        spacing 22
                        vbox:
                            spacing 2
                            text "STR: [character.strength]" size 15 color "#2c1810"
                            text "AGI: [character.agility]" size 15 color "#2c1810"
                            text "INT: [character.intelligence]" size 15 color "#2c1810"
                        vbox:
                            spacing 2
                            text "DEF: [character.defence]" size 15 color "#2c1810"
                            text "POW: [character.power]" size 15 color "#2c1810"

                    null height 4

                    text "Skills: [character.skills_text]":
                        size 15
                        color "#3b2210"

            # Action buttons
            hbox:
                spacing 36
                align (0.5, 0.5)

                textbutton "Gacha Again":
                    action Return("again")
                    text_size 18
                    text_bold True
                    text_color "#4a2810"
                    text_hover_color "#c45c12"

                textbutton "Back to Menu":
                    action Return("menu")
                    text_size 18
                    text_bold True
                    text_color "#4a2810"
                    text_hover_color "#c45c12"

# Main script flow
label start:
    scene bg with dissolve
    "Welcome to the gacha system!"
    jump gacha_menu

label gacha_menu:
    menu:
        "Gacha Character!":
            jump roll_character

        "Exit":
            return

label roll_character:
    show black with vpunch
    pause 0.5
    scene bg with dissolve

    $ current_character = generate_character()
    call screen gacha_result(current_character)

    if _return == "again":
        jump roll_character
    else:
        jump gacha_menu