# Put your OS here!

# This function is where you put the code that runs when your OS starts up
def start():
    import syscalls
    import kernel
    import os

    Version = "1.0.0"

    call = syscalls.System()

    call.println(f"TextOS version {Version}")
    call.println("==== TextOS Home Menu ====")
    call.println("[1]: Run file")
    call.println("[2]: List all files")
    call.println("[3]: Edit file")
    call.println("[4]: New File")
    call.println("[5]: Delete File")
    call.println("[6]: Exit")
    call.println("[7]: Restart")

    while True:
        op = call.get_input("[?]: ")

        if op == "1":
            program = input("Enter program: ")

            if ".BIN" in program:
                if program != "KERNEL.BIN":
                    call.run_bin_file(program)
                else: call.println("You do not have permission to run that file.")
            if ".RUN" in program:
                kernel.run(program)
        elif op == "2":
            call.listroot()
        elif op == "3":
            f = input("File: ")
            e = call.find_file(f)
            
            if e == 1:
                print("File doesn't exist!")
            else:
                new_contents = input("Enter new contents: ")
                call.overwrite_file(f, new_contents)
        elif op == "4":
            name = input("File name: ")
            contents = input("File contents: ")
            call.create_file(name, contents)
        elif op == "5":
            name = input("File name: ")
            call.remove_file(name)
        elif op == "6":
            s = input("Exiting will delete all your files! Are you sure? [Y/N]: ")
            if s.lower() == "y":
                quit()
            else: call.println("Aborting shutdown...")
        elif op == "7":
            s = input("Restarting will delete all your files! Are you sure? [Y/N]: ")
            if s.lower() == "y":
                os.startfile("boot.py")
                quit()
            else: call.println("Aborting restart...")