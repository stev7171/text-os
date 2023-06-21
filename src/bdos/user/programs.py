import syscalls

def test():
    call = syscalls.System()
    call.println("Hello, World!")

def listroot():
    call = syscalls.System()
    call.listroot()

def cli():
    call = syscalls.System()
    import kernel

    while True:
        prompt = call.get_input("> ")

        if prompt == 'exit': quit()
        elif prompt == 'help' or prompt == 'help me':
            call.println("==== HELP MENU ====")
            call.println("help: brings up this menu")
            call.println("println: prints specified message (options: [RESULT])")
            call.println("input: prompts user with specified prompt (returns: [RESULT])")
            call.println("run: runs specified file (options: [RESULT], [INT])")
            call.println("listroot: lists all files that exist")
            call.println("clear: clears the screen")
            call.println("exit: exits the OS")
        else: kernel.run_cmd(prompt+"//")