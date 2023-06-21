# All syscalls are in this file (This is part of the kernel, but it made more sence to put it in a seperate file)

# Imports
import os
import files as files
import user.programs as programs

# All syscalls (names are relatively self-explanatory)
class System:
    def create_file(self, filename, file_contents):
        files.files[filename] = file_contents
   
    def remove_file(self, filename):
        files.files.pop(filename)
    
    def println(self, msg):
        print(f'{msg}\n')

    def get_input(self, prompt):
        return input(prompt)

    def overwrite_file(self, filename, new_contents):
        if filename in files.files:
            files.files[filename] = new_contents
        else:
            return 1

    def find_file(self, filename):
        if filename in files.files:
            return filename
        else:
            return 1

    def run_os_file(self, filename):
        os.startfile(files.files[filename])

    def run_bin_file(self, filename):
        if filename in files.files:
            program = getattr(programs, files.files[filename])
            program()
            return 0
        else:
            return 1
    
    def get_file_contents(self, filename):
        if filename in files.files:
            return files.files[filename]
        else:
            return 1
        
    def listroot(self):
        for i in files.files:
            print(f'{i} :: {len(files.files[i])} bytes')