# BDOS Bootloader

import syscalls as sysc

call = sysc.System()

kern = call.find_file(filename="KERNEL.BIN")

if kern == 1:
    print("Couldn't find KERNEL.BIN!")
    input("Press enter to quit...")
    quit()
else:
    call.run_os_file(kern)