"""
 duck2python converts DuckyScript scripts for the USB Rubber Ducky by hak5 to python scripts that function the same way
thus offering a convenient way of testing a script without requiring to load it on a Rubber Ducky each time.
its a modified script from CedArctic (https://github.com/CedArctic/ducky2python)
to match zero-hid project script the turns rpi zero to work like rubber ducky
"""

# Print Ascii Art:
print("     _            _          ____              _   _                 ")
print("  __| |_   _  ___| | ___   _|___ \\ _ __  _   _| |_| |__   ___  _ __  ")
print(" / _` | | | |/ __| |/ / | | | __) | '_ \\| | | | __| '_ \\ / _ \\| '_ \\ ")
print("| (_| | |_| | (__|   <| |_| |/ __/| |_) | |_| | |_| | | | (_) | | | |")
print(" \\__,_|\\__,_|\\___|_|\\_\\\\__, |_____| .__/ \\__, |\\__|_| |_|\\___/|_| |_|")
print("                       |___/      |_|    |___/ \tmodified by DARKSWORDMAN     ")
print("\n\n")

# Load Ducky Script and create Python Output file:
duckyScriptPath = input("Drag and drop the ducky script txt file:\n")
f = open(duckyScriptPath, "r", encoding='utf-8')
pythonScript = open("zeroHidScript.py", "w", encoding='utf-8')

# Write module imports to output file:
pythonScript.write("from zero_hid import Keyboard, KeyCodes\n")
pythonScript.write("from zero_hid.hid import keycodes\n")
pythonScript.write("from zero_hid import Mouse\n")
pythonScript.write("from time import sleep\n")
pythonScript.write("\nk = Keyboard()\n")
pythonScript.write("m = Mouse()\n")

# Convert the Ducky Script lines to a list and stip whitespaces:
duckyScript = f.readlines()
duckyScript = [x.strip() for x in duckyScript]

''' Ducky Statements fall into one of the following 6 categories:
1. Default Delay	2.Comment	3.Delay 	4.String	5.Repeat	6.Command '''

# Check if there is a default delay:
defaultDelay = 0
if duckyScript[0][:7] == "DEFAULT":
    # Divide by 1000 because the time.sleep command takes seconds as an argument, not ms
    defaultDelay = int(duckyScript[0][:13]) / 1000

# Variables:
previousStatement = ""

# Parallel command lists: 
# The Dictionary contains the ducky commands.
ducky_to_zero_hid = {
    "WINDOWS": "KeyCodes.MOD_LEFT_GUI",
    "GUI": "KeyCodes.MOD_LEFT_GUI",
    "APP": "KeyCodes.KEY_APPLICATION",
    "MENU": "KeyCodes.KEY_MENU",
    "SHIFT": "KeyCodes.MOD_LEFT_SHIFT",
    "ALT": "KeyCodes.MOD_LEFT_ALT",
    "CONTROL": "KeyCodes.MOD_LEFT_CONTROL",
    "CTRL": "KeyCodes.MOD_LEFT_CONTROL",
    "DOWNARROW": "KeyCodes.KEY_DOWN",
    "DOWN": "KeyCodes.KEY_DOWN",
    "LEFTARROW": "KeyCodes.KEY_LEFT",
    "LEFT": "KeyCodes.KEY_LEFT",
    "RIGHTARROW": "KeyCodes.KEY_RIGHT",
    "RIGHT": "KeyCodes.KEY_RIGHT",
    "UPARROW": "KeyCodes.KEY_UP",
    "UP": "KeyCodes.KEY_UP",
    "BREAK": "KeyCodes.KEY_PAUSE",
    "PAUSE": "KeyCodes.KEY_PAUSE",
    "CAPSLOCK": "KeyCodes.KEY_CAPSLOCK",
    "DELETE": "KeyCodes.KEY_DELETE",
    "END": "KeyCodes.KEY_END",
    "ESC": "KeyCodes.KEY_ESC",
    "ESCAPE": "KeyCodes.KEY_ESC",
    "HOME": "KeyCodes.KEY_HOME",
    "INSERT": "KeyCodes.KEY_INSERT",
    "NUMLOCK": "KeyCodes.KEY_NUMLOCK",
    "PAGEUP": "KeyCodes.KEY_PAGEUP",
    "PAGEDOWN": "KeyCodes.KEY_PAGEDOWN",
    "PRINTSCREEN": "KeyCodes.KEY_SYSRQ",
    "SCROLLLOCK": "KeyCodes.KEY_SCROLLLOCK",
    "SPACE": "KeyCodes.KEY_SPACE",
    "TAB": "KeyCodes.KEY_TAB",
    "ENTER": "KeyCodes.KEY_ENTER",
    "a": "KeyCodes.KEY_A",
    "b": "KeyCodes.KEY_B",
    "c": "KeyCodes.KEY_C",
    "d": "KeyCodes.KEY_D",
    "e": "KeyCodes.KEY_E",
    "f": "KeyCodes.KEY_F",
    "g": "KeyCodes.KEY_G",
    "h": "KeyCodes.KEY_H",
    "i": "KeyCodes.KEY_I",
    "j": "KeyCodes.KEY_J",
    "k": "KeyCodes.KEY_K",
    "l": "KeyCodes.KEY_L",
    "m": "KeyCodes.KEY_M",
    "n": "KeyCodes.KEY_N",
    "o": "KeyCodes.KEY_O",
    "p": "KeyCodes.KEY_P",
    "q": "KeyCodes.KEY_Q",
    "r": "KeyCodes.KEY_R",
    "s": "KeyCodes.KEY_S",
    "t": "KeyCodes.KEY_T",
    "u": "KeyCodes.KEY_U",
    "v": "KeyCodes.KEY_V",
    "w": "KeyCodes.KEY_W",
    "x": "KeyCodes.KEY_X",
    "y": "KeyCodes.KEY_Y",
    "z": "KeyCodes.KEY_Z",
    "A": "KeyCodes.KEY_A",
    "B": "KeyCodes.KEY_B",
    "C": "KeyCodes.KEY_C",
    "D": "KeyCodes.KEY_D",
    "E": "KeyCodes.KEY_E",
    "F": "KeyCodes.KEY_F",
    "G": "KeyCodes.KEY_G",
    "H": "KeyCodes.KEY_H",
    "I": "KeyCodes.KEY_I",
    "J": "KeyCodes.KEY_J",
    "K": "KeyCodes.KEY_K",
    "L": "KeyCodes.KEY_L",
    "M": "KeyCodes.KEY_M",
    "N": "KeyCodes.KEY_N",
    "O": "KeyCodes.KEY_O",
    "P": "KeyCodes.KEY_P",
    "Q": "KeyCodes.KEY_Q",
    "R": "KeyCodes.KEY_R",
    "S": "KeyCodes.KEY_S",
    "T": "KeyCodes.KEY_T",
    "U": "KeyCodes.KEY_U",
    "V": "KeyCodes.KEY_V",
    "W": "KeyCodes.KEY_W",
    "X": "KeyCodes.KEY_X",
    "Y": "KeyCodes.KEY_Y",
    "Z": "KeyCodes.KEY_Z",
    "F1": "KeyCodes.KEY_F1",
    "F2": "KeyCodes.KEY_F2",
    "F3": "KeyCodes.KEY_F3",
    "F4": "KeyCodes.KEY_F4",
    "F5": "KeyCodes.KEY_F5",
    "F6": "KeyCodes.KEY_F6",
    "F7": "KeyCodes.KEY_F7",
    "F8": "KeyCodes.KEY_F8",
    "F9": "KeyCodes.KEY_F9",
    "F10": "KeyCodes.KEY_F10",
    "F11": "KeyCodes.KEY_F11",
    "F12": "KeyCodes.KEY_F12",
}

# Process each line from the Ducky Script:
for line in duckyScript:

    # Check if the statement is a comment
    if line[0:3] == "REM":
        previousStatement = line.replace("REM", "#")

    # Check if the statement is a delay
    elif line[0:5] == "DELAY":
        previousStatement = "sleep(" + str(float(line[6:]) / 1000) + ")"

    # Check if the statement is a string
    elif line[0:6] == "STRING":
        previousStatement = f"k.type('{line[7:]}', 0.02)"

    # Check if the statement is a repeat command - in which case write the previous command times-1 since
    # we write it once more at the end of the for loop anyways
    elif line[0:6] == "REPEAT":
        for i in range(int(line[7:]) - 1):
            pythonScript.write(previousStatement)
            pythonScript.write("\n")

    # If we reach this point, the statement must be a command
    else:
        previousStatement = "k.press("

        # Go through the parallel array and check if the examined key is in the command
        if len(line.split(" ")) > 1:
            commands = line.split(" ")
            last_command = commands[-1]
            previousStatement = previousStatement + "["
            for command in commands[:-1]:
                previousStatement = previousStatement + ducky_to_zero_hid[command] + ","

            previousStatement = previousStatement[:-1] + "]"
            previousStatement += f", {ducky_to_zero_hid[last_command]})"
        else:
            command = ' '.join(line.split(" "))
            last_command = ''
            previousStatement = previousStatement + "[], " + ducky_to_zero_hid[command] + ")"

    # Write Default Delay if it exists:
    if defaultDelay != 0:
        previousStatement = "sleep(" + defaultDelay + ")"

    # Write command to output file and add a new line \n :
    pythonScript.write(previousStatement)
    pythonScript.write("\n")

# Close output file before exiting
pythonScript.close()
input("\nConversion complete!\n\nPress any key to close.")
