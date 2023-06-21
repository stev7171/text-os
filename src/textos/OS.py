# Put your OS here!

# This function is where you put the code that runs when your OS starts up
def start():
    import syscalls
    import kernel

    call = syscalls.System()

    call.println("==== TextOS Home Menu ====")
    call.println("[1]: Run file")
    call.println("[2]: List all files")
    call.println("[3]: Edit file")
    call.println("[4]: Exit")

    op = call.get_input("[?]: ")

    if op == "1":
        program = input("Enter program: ")

        if ".BIN" in program:
            call.run_bin_file(program)
        if ".RUN" in program:
            kernel.run(program)
        else:
            call.println("File isn't runnable!")