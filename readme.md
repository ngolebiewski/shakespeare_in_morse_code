# Shakespeare in Morse Code

- Get Romeo and Juliet from Project Gutenberg
- `wget https://www.gutenberg.org/cache/epub/1513/pg1513.txt`

## Version 0 - `0_romeo_n_juliet.py`

- Take a snippet of Romeo and Juliet.
- Output in morse code to terminal.
- Goal: Test text to morse code.

![Screenshot Version 0 basic dialogue to morse code](/images/Screenshot_0_0.png)

## Version 1 - `1_romeo_n_juliet.py`

- Add in code for timing of morse code symbols and spacing.
- Add in some test colors. Overly gendered with Blue for Romeo and Pink for Juliet!
- Add in code for Sense Hat on Raspberry Pi.
    - Instruction to install the sense-hat: https://www.raspberrypi.com/documentation/accessories/sense-hat.html#install
- Git clone Shakespear in Morse Code repo to the Pi
    - `git clone https://github.com/ngolebiewski/shakespeare_in_morse_code.git`
    - Update the code on the PI if not the first install.
        - `git fetch origin` -> Fetch the latest changes from the remote repository
        - `git reset --hard origin/main` -> Reset your local branch to match the remote branch (replace 'main' with your branch name if needed)

![Demo of code with flashing sense hat](/images/version1_demo.gif)

## Version 2 - `2_romeo_n_juliet.py`

- *TODO*
- Parse Romeo and Juliet script to create an object
- Create more colors, assign a color to each actor
- Perhaps: Have a skip forward function?
- Perhaps: display the letter on the LED array while blinking? 

![Portion of play, marked up for style](/images/romeo_parsing.jpg)
