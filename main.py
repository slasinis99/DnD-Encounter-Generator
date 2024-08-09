import os, shutil
import pickle

monster_list_master = ['Young White Dragon']
name = ''
stat_block_str = '''

    

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
    tex = f'\\documentclass[10pt,twoside,openany,nodeprecatedcode]{{dndbook}}\n\n\\usepackage[english]{{babel}}\n\\usepackage[utf8]{{inputenc}}\n\\usepackage{{multicol}}\n\\usepackage{{graphicx}}\n\n\\begin{{document}}\n\n\t\\chapter*{{{encounter_name}}}\n\n\t'
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
    # save_stat_block(name, stat_block_str)
    build_encounter('Icespire Hold', ['Young White Dragon', 'Ice Mephit', 'Sivak Draconian', 'Veteran'])
    return

if __name__ == '__main__':
    main()