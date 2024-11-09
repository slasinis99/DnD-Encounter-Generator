import os, shutil
import pickle

monster_list_master = ['Young White Dragon', 'Ice Mephit', 'Sivak Draconian', 'Veteran', 'Dragon Army Dragonnel', 'Ancient Aspect of Nihil', 'Corrupted Baaz Draconian', 'Corrupted Kapak Draconian', 'Corrupted Sivak Draconian', 'Malric DeLorne, Necromancer', 'Skeleton Archer', 'Skeleton Warrior', 'Fire Giant Skeleton']
spell_list_master = ['Fireball', 'Malric DeLorne Spells']
name = 'Malric DeLorne Spells'
stat_block = '''

    \\spell{Chill Touch}{Cantrip necromancy}{1 action}{120 feet}{V, S}{1 round}
    You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn. If the target is undead, it also has disadvantage on attack rolls against you until the end of your next turn. The spell's damage increases by 1d8 at 5th, 11th, and 17th levels.

    \\spell{Toll the Dead}{Cantrip necromancy}{1 action}{60 feet}{V, S}{Instantaneous}
    You point at one creature you can see within range, and the sound of a dolorous bell fills the air around it for a moment. The target must succeed on a Wisdom saving throw or take 1d8 necrotic damage (1d12 if the target is missing any of its hit points). The damage increases by 1d8 or 1d12 at 5th, 11th, and 17th levels.

    \\spell{Ray of Frost}{Cantrip evocation}{1 action}{60 feet}{V, S}{Instantaneous}
    A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn. The spell's damage increases by 1d8 at 5th, 11th, and 17th levels.

    \\spell{Minor Illusion}{Cantrip illusion}{1 action}{30 feet}{S, M (a bit of fleece)}{1 minute}
    You create a sound or an image of an object within range that lasts for the duration. If you create a sound, it can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound. If you create an image, it must be no larger than a 5-foot cube and cannot make noise or move. Physical interaction reveals it to be an illusion.

    \\spell{Mage Armor}{1st-level abjuration}{1 action}{Touch}{V, S, M (a piece of cured leather)}{8 hours}
    You touch a willing creature who isn't wearing armor, and a magical force surrounds it until the spell ends. The target's base AC becomes 13 + its Dexterity modifier. The spell ends if the target dons armor or you dismiss it as an action.

    \\spell{Magic Missile}{1st-level evocation}{1 action}{120 feet}{V, S}{Instantaneous}
    You create three glowing darts of magical force. Each dart hits a creature of your choice within range that you can see. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several. When cast using a higher-level spell slot, you create one additional dart per slot level above 1st.

    \\spell{Shield}{1st-level abjuration}{1 reaction, which you take when you are hit by an attack or targeted by the magic missile spell}{Self}{V, S}{1 round}
    An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile.

    \\spell{Detect Magic}{1st-level divination}{1 action}{Self}{V, S}{Concentration, up to 10 minutes}
    For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.

    \\spell{Mirror Image}{2nd-level illusion}{1 action}{Self}{V, S}{1 minute}
    Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting positions to make it difficult to track which image is real. Each time a creature targets you with an attack, roll a d20 to see if it hits a duplicate. Each duplicate has an AC of 13 and vanishes if it is hit.

    \\spell{Misty Step}{2nd-level conjuration}{1 bonus action}{Self}{V}{Instantaneous}
    Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.

    \\spell{Ray of Enfeeblement}{2nd-level necromancy}{1 action}{60 feet}{V, S}{Concentration, up to 1 minute}
    A black beam of enervating energy springs from your finger toward a creature within range. Make a ranged spell attack against the target. On a hit, the target deals only half damage with weapon attacks that use Strength until the spell ends. At the end of each of the target's turns, it can make a Constitution saving throw against the spell. On a success, the spell ends.

    \\spell{Counterspell}{3rd-level abjuration}{1 reaction, which you take when you see a creature within 60 feet of you casting a spell}{60 feet}{S}{Instantaneous}
    You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a success, the creature's spell fails.

    \\spell{Animate Dead}{3rd-level necromancy}{1 minute}{10 feet}{V, S, M (a drop of blood, a piece of flesh, and a pinch of bone dust)}{Instantaneous}
    This spell creates an undead servant. Choose a pile of bones or a corpse within range. Your spell imbues the target with a foul mimicry of life, raising it as an undead creature. The creature is under your control for 24 hours, after which it stops obeying your commands. To maintain control, you must recast this spell every 24 hours.

    \\spell{Vampiric Touch}{3rd-level necromancy}{1 action}{Self}{V, S}{Concentration, up to 1 minute}
    The touch of your shadow-wreathed hand can siphon life force. Make a melee spell attack against a creature within your reach. On a hit, the target takes 3d6 necrotic damage, and you regain hit points equal to half the damage dealt. Until the spell ends, you can make the attack again on each of your turns as an action.

    \\spell{Blight}{4th-level necromancy}{1 action}{30 feet}{V, S}{Instantaneous}
    Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality. The target makes a Constitution saving throw, taking 8d8 necrotic damage on a failed save, or half as much on a success. If the target is a plant or plant creature, it makes the save with disadvantage and takes maximum damage.

    \\spell{Phantasmal Killer}{4th-level illusion}{1 action}{120 feet}{V, S}{Concentration, up to 1 minute}
    You tap into the nightmares of a creature you can see, creating an illusory manifestation of its deepest fears. The target must make a Wisdom saving throw, taking 4d10 psychic damage on a failed save and becoming frightened for the duration. At the end of each of the target's turns, it can make a Wisdom save to end the effect.

    \\spell{Cloudkill}{5th-level conjuration}{1 action}{120 feet}{V, S}{Concentration, up to 10 minutes}
    You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a point you choose. The fog spreads around corners and heavily obscures its area. Each creature in the fog when it appears or that starts its turn there must make a Constitution save, taking 5d8 poison damage on a failure or half as much on a success. The fog moves 10 feet away from you at the start of each of your turns.

    \\spell{Enervation}{5th-level necromancy}{1 action}{60 feet}{V, S}{Concentration, up to 1 minute}
    A tendril of shadowy energy reaches from you to a creature within range. The target must make a Dexterity saving throw, taking 4d8 necrotic damage on a failed save or half as much on a success. Until the spell ends, you can use your action on each turn to automatically deal 4d8 necrotic damage to the target if it remains within range.


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
    tex = f'\\documentclass[10pt,twoside,openany,nodeprecatedcode]{{dndbook}}\n\n\\usepackage[english]{{babel}}\n\\usepackage[utf8]{{inputenc}}\n\\usepackage{{multicol}}\n\\usepackage{{graphicx}}\n\\newcommand{{\\spell}}[6]{{\n\\noindent\\textbf{{#1}} \\textit{{#2}} \\\n\\textbf{{Casting Time:}} #3 \\\n\\textbf{{Range:}} #4 \\\n\\textbf{{Components:}} #5 \\\n\\textbf{{Duration:}} #6 \\\n}}\n\\begin{{document}}\n\n\t\\section*{{{encounter_name}}}\n\n\t'
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
    # save_stat_block(name, stat_block)
    build_encounter('Triboar Necromancer', ['Skeleton Archer', 'Skeleton Warrior', 'Fire Giant Skeleton', 'Malric DeLorne, Necromancer', 'Malric DeLorne Spells'])
    return

if __name__ == '__main__':
    main()