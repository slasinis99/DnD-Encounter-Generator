# D&D 5e Encounter Generator
This encounter generator is not a random encounter generator; rather, it will create a pdf file containing the stat blocks of the monsters you with to have in your encounter. This is provided that those monsters' stat blocks are located in the save file for them. The Python script will create a .tex file containing the stat blocks and generate the pdf for you to use during your sessions. 

## Compatibility
In order for the Python script to generate the latex file, you must have pdflatex/miktex installed on your machine as well as have installed the [DnD 5e LaTeX Template](https://github.com/rpgtex/DND-5e-LaTeX-Template). Instructions for how to install can be found on that Github page.

## Adding New Stat Blocks
In the Python file **main.py**, you can type the name of the monster to be added in the **name** variable. You must also type in the latex code into the **stat_block_str** variable. Ensure that any backslashes are double backslashes to ensure that proper character is being represented in the string. For examples and templates of what this should look like, there is a .tex file in the Source folder. This folder is where you can store all of your stat blocks in order to ensure they will compile properly before using Python to store them in the **stat_blocks.sav** save file. Simply run the **save_stat_block** method in main, and the save file will be updated.

## Creating the PDF
Once you have a list of monsters and a name for your encounter, you can run the **build_encounter** method making sure to fill in the **encounter_name** and **monster_list** parameters. Running the script will then produce **main.pdf**. An example of the final product can be found in the repository.
