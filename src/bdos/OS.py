# Put your OS here!

# This function is where you put the code that runs when your OS starts up
def start():
    import syscalls

    call = syscalls.System()

    call.println("Hello from TextOS!")