# BDOS Kernel (Syscalls are in "syscalls.py")
Version = "1.0.0"

# How to use this in your projects:
#   1. set "os" variable to True
#   2. in "OS.py", make your os (you can use multiple files, but make sure your main file is "os.py")
#   3. have fun with your OS!

# Don't touch anything else unless you know what you're doing!

os = True




# Imports
import syscalls
import OS
import os as o

call = syscalls.System()

def run(task):
    # Log the task we're running so that I don't have to figure it out myself
    print(f"Running task: {task}")

    # We don't want to run files that aren't runnables (.RUN)
    if '.RUN' in task:
        program = call.get_file_contents(task)

        # If the file exists, run it. Otherwise, throw an error
        if program != 1:
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            slash_count = 0

            sysret = ''

            # Iterate through the program
            for i in program:
                if i == "\\":
                    continue

                if i == '/':
                    slash_count += 1

                if slash_count == 2:

                    # Commands
                    if command == "println":
                        if arg_1 == "[RESULT]": call.println(sysret)
                        else: call.println(arg_1)
                    if command == "run":
                        if arg_1 == "[RESULT]": call.run_bin_file(sysret)
                        elif arg_1 == "KERNEL.BIN": print("ERROR: You do not have permission to run this file.")
                        else: call.run_bin_file(arg_1)
                    if command == "listroot":
                        call.listroot(arg_1)
                    if command == "input":
                        sysret = call.get_input(arg_1)
                    if command == "clear":
                        o.system("cls")

                    # Reset variables
                    arg_count = 0
                    arg_1 = ''
                    arg_2 = ''
                    command = ''
                    slash_count = 0

                # Add [i] to the command or the arguments depending on what [arg_count] is
                if i == ':': arg_count += 1
                elif arg_count == 0 and i != ':' and i != '/': command += i
                elif arg_count == 1 and i != ':' and i != '/': arg_1 += i
                elif arg_count == 2 and i != ':' and i != '/': arg_2 += i
        else:
            print("ERROR: file does not exist!")
    else:
        print("ERROR: incorrect format")

# sysret is used in run_cmd
# if it was in run_cmd, certain commands wouldn't work
sysret = ''

def run_cmd(program):
    global sysret

    arg_count = 0
    arg_1 = ''
    arg_2 = ''
    command = ''
    slash_count = 0

    for i in program:
        if i == "\\":
            continue

        if i == '/':
            slash_count += 1

        if slash_count == 2:

            # Commands
            if command == "println":
                if arg_1 == "[RESULT]": call.println(sysret)
                else: call.println(arg_1)
            if command == "run":
                if arg_1 == "[RESULT]": call.get_input(sysret)
                elif arg_1 == "[INT]": run(arg_2)
                elif arg_1 == "KERNEL.BIN": print("ERROR: You do not have permission to run this file.")
                else: call.run_bin_file(arg_1)
            if command == "listroot":
                call.listroot()
            if command == "input":
                sysret = call.get_input(arg_1)
            if command == "clear":
                o.system("cls")
            if command == "BDOS":
                if arg_1 == "[VER]": call.println(f"Bearded Dragon Kernel version {Version}\nMade by stev7171")
                elif arg_1 == "[CREDIT]": call.println("Bearded Dragon Kernel\nMade by stev7171\nInspired by U-Kernel on Scratch")
                else: call.println("USAGE: BDOS:<COMMAND>")

            # Reset variables
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            slash_count = 0

        # Add [i] to the command or the arguments depending on what [arg_count] is
        if i == ':': arg_count += 1
        elif arg_count == 0 and i != ':' and i != '/': command += i
        elif arg_count == 1 and i != ':' and i != '/': arg_1 += i
        elif arg_count == 2 and i != ':' and i != '/': arg_2 += i

if __name__ == '__main__':
    if os:
        OS.start()
    else:
        cli = call.find_file("CLI.BIN")

        if cli != 1:
            call.run_bin_file("CLI.BIN")
        else:
            print("ERROR: Could not find \"CLI.BIN\"")
            input("Press enter to quit...")
            quit()