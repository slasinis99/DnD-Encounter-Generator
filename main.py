import os, shutil
import pickle

monster_list_master = ['Young White Dragon', 'Ice Mephit', 'Sivak Draconian', 'Veteran', 'Dragon Army Dragonnel', 'Ancient Aspect of Nihil', 'Corrupted Baaz Draconian', 'Corrupted Kapak Draconian', 'Corrupted Sivak Draconian']
name = 'Ancient Aspect of Nihil'
corrupted_baaz_draconian = '''

    \\begin{DndMonster}[width=\\textwidth]{Corrupted Baaz Draconian}
        \\begin{multicols}{2}
            \\DndMonsterType{Medium Dragon (Draconian), Typically Chaotic Evil}

            \\DndMonsterBasics[
                armor-class = {14 (natural armor)},
                hit-points = {\\DndDice{5d8 + 10}},
                speed = {30 ft.},
            ]

            \\DndMonsterAbilityScores[
                str = 15,
                dex = 10,
                con = 14,
                int = 8,
                wis = 11,
                cha = 10,
            ]

            \\DndMonsterDetails[
                saving-throws = {Str +4, Con +4},
                damage-resistances = {Necrotic, Psychic},
                senses = {Darkvision 60 ft., passive Perception 10},
                languages = {Common, Draconic},
                challenge = 1,
            ]

            \\DndMonsterAction{Corrupting Aura}
            Creatures within 10 feet of the Baaz Draconian must succeed on a DC 10 Wisdom saving throw or have disadvantage on Wisdom checks and saving throws until they leave the aura's area. While in the aura, creatures also experience faint whispers and shadowy visions, as if reality itself is bending.

            \\DndMonsterSection{Actions}

            \\DndMonsterAction{Multiattack}
            The Baaz Draconian makes two Eldritch Claw attacks.

            \\DndMonsterMelee[
                name=Eldritch Claw,
                mod=+4,
                reach=5 ft.,
                targets=one target,
                dmg=\\DndDice{1d6 + 2},
                dmg-type=slashing,
                extra={and the target must make a DC 10 Charisma saving throw or be disoriented, suffering disadvantage on their next attack roll.}
            ]

            \\DndMonsterAction{Death Throes}
            When the Baaz Draconian dies, its body crumbles into a twisted, shadowy statue, which explodes. Each creature within 5 feet must succeed on a DC 12 Dexterity saving throw or take \\DndDice{2d6} necrotic damage as the statue bursts into a dark cloud of psychic energy.

        \\end{multicols}
    \\end{DndMonster}

'''
corrupted_kapak_draconian = '''

    \\begin{DndMonster}[width=\\textwidth]{Corrupted Kapak Draconian}
        \\begin{multicols}{2}
            \\DndMonsterType{Medium Dragon (Draconian), Typically Chaotic Evil}

            \\DndMonsterBasics[
                armor-class = {15 (natural armor)},
                hit-points = {\\DndDice{7d8 + 14}},
                speed = {30 ft.},
            ]

            \\DndMonsterAbilityScores[
                str = 14,
                dex = 16,
                con = 15,
                int = 9,
                wis = 10,
                cha = 11,
            ]

            \\DndMonsterDetails[
                saving-throws = {Dex +5, Wis +2},
                skills = {Stealth +5},
                damage-resistances = {Necrotic, Psychic},
                senses = {Darkvision 60 ft., passive Perception 10},
                languages = {Common, Draconic},
                challenge = 2,
            ]

            \\DndMonsterAction{Corrupting Aura}
            Creatures within 10 feet of the Kapak Draconian must succeed on a DC 12 Wisdom saving throw or have disadvantage on Dexterity checks and saving throws until they leave the aura's area. The air around the Kapak feels oppressive, as if shadows cling to everything.

            \\DndMonsterSection{Actions}

            \\DndMonsterAction{Multiattack}
            The Kapak Draconian makes two Shadowed Dagger attacks.

            \\DndMonsterMelee[
                name=Shadowed Dagger,
                mod=+5,
                reach=5 ft.,
                targets=one target,
                dmg=\\DndDice{1d4 + 3},
                dmg-type=piercing,
                extra={and the target takes an additional \\DndDice{1d6} necrotic damage as shadows latch onto the wound, attempting to draw life from it.}
            ]

            \\DndMonsterAction{Death Throes}
            When the Kapak Draconian dies, its body dissolves into a pool of black ichor. Any creature within 5 feet must succeed on a DC 12 Dexterity saving throw or take \\DndDice{2d6} necrotic damage as the ichor splashes and spreads corrupting energy.

        \\end{multicols}
    \\end{DndMonster}

'''
corrupted_sivak_draconian = '''

    \\begin{DndMonster}[width=\\textwidth]{Corrupted Sivak Draconian}
        \\begin{multicols}{2}
            \\DndMonsterType{Large Dragon (Draconian), Typically Chaotic Evil}

            \\DndMonsterBasics[
                armor-class = {16 (natural armor)},
                hit-points = {\\DndDice{9d10 + 27}},
                speed = {30 ft., fly 60 ft.},
            ]

            \\DndMonsterAbilityScores[
                str = 18,
                dex = 14,
                con = 16,
                int = 10,
                wis = 11,
                cha = 12,
            ]

            \\DndMonsterDetails[
                saving-throws = {Str +7, Con +6},
                skills = {Perception +4},
                damage-resistances = {Necrotic, Psychic},
                senses = {Darkvision 60 ft., passive Perception 14},
                languages = {Common, Draconic},
                challenge = 4,
            ]

            \\DndMonsterAction{Corrupting Aura}
            Creatures within 15 feet of the Sivak Draconian must succeed on a DC 14 Wisdom saving throw or have disadvantage on Strength checks and saving throws. While in the aura, creatures feel a heavy, pressing weight as shadows cling to their movements.

            \\DndMonsterSection{Actions}

            \\DndMonsterAction{Multiattack}
            The Sivak Draconian makes two Eldritch Slash attacks.

            \\DndMonsterMelee[
                name=Eldritch Slash,
                mod=+7,
                reach=10 ft.,
                targets=one target,
                dmg=\\DndDice{2d6 + 4},
                dmg-type=slashing,
                extra={and the target takes an additional \\DndDice{1d6} psychic damage as tendrils of shadow lash out from the Draconian's blade, latching onto the target's mind.}
            ]

            \\DndMonsterAction{Death Throes}
            When the Sivak Draconian dies, its form twists into the appearance of the creature that killed it, as usual. However, this shadowy mimicry is haunted with whispering shadows that impose disadvantage on Wisdom saving throws for any creature within 10 feet of it.

        \\end{multicols}
    \\end{DndMonster}

'''





def save_stat_block(name: str, stat_block_str: str) -> bool:
    d: dict = {}
    if os.path.exists(f'{os.getcwd()}\\stat_blocks.sav'):
        with open(f'{os.getcwd()}\\stat_blocks.sav', 'rb') as file:
            d = pickle.load(file)
    d[name] = stat_block_str
    with open(f'{os.getcwd()}\\stat_blocks.sav', 'wb') as file:
        pickle.dump(d, file)
        print(f'Successfully saved {name}!')

def build_encounter(encounter_name: str, monster_list: list[str]) -> bool:
    tex = f'\\documentclass[10pt,twoside,openany,nodeprecatedcode]{{dndbook}}\n\n\\usepackage[english]{{babel}}\n\\usepackage[utf8]{{inputenc}}\n\\usepackage{{multicol}}\n\\usepackage{{graphicx}}\n\n\\begin{{document}}\n\n\t\\section*{{{encounter_name}}}\n\n\t'
    if os.path.exists(f'{os.getcwd()}\\stat_blocks.sav'):
        with open(f'{os.getcwd()}\\stat_blocks.sav', 'rb') as file:
            d = pickle.load(file)
        for m in monster_list:
            if d.get(m) is None:
                continue
            tex += d[m]
            tex += '\n'
    tex += '\n\n\\end{document}'
    p = os.getcwd()
    if not os.path.exists(f'{p}\\LaTeX\\'):
        os.makedirs(f'{p}\\LaTeX\\')
    with open(f'{os.getcwd()}\\LaTeX\\main.tex', 'w') as file:
        file.write(tex)
    if os.path.exists('main.pdf'):
        os.remove('main.pdf')
    os.chdir(f'{p}\\LaTeX')
    os.system("pdflatex main.tex")
    shutil.move('main.pdf', f'{p}')
    return True

def main():
    # save_stat_block('Corrupted Kapak Draconian', corrupted_kapak_draconian)
    build_encounter('Ancient Cave', ['Corrupted Baaz Draconian', 'Corrupted Kapak Draconian', 'Corrupted Sivak Draconian', 'Ancient Aspect of Nihil'])
    return

if __name__ == '__main__':
    main()