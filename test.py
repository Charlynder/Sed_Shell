'''
test.v1
shell test
import cmd

class MyShell(cmd.Cmd):
    prompt = ">> "  # Set the prompt string

    def do_greet(self, arg):
        """Greet the user"""
        print("Hello, user!")

    def do_sum(self, arg):
        """Add two numbers"""
        try:
            nums = arg.split()
            if len(nums) == 2:
                num1 = float(nums[0])
                num2 = float(nums[1])
                result = num1 + num2
                print("Sum:", result)
            else:
                print("Please provide two numbers.")
        except ValueError:
            print("Invalid input. Please provide numbers.")

    def do_quit(self, arg):
        """Exit the shell"""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    shell = MyShell()
    shell.cmdloop()  # Start the shell prompt loop
'''

'''
test.v2
aliases test
import cmd

class MyShell(cmd.Cmd):
    prompt = ">> "
    aliases = {
        'g': 'git',
        'ls': 'ls -la'
    }

    def do_alias(self, arg):
        """Create or modify an alias. Usage: alias <alias_name> <command>"""
        parts = arg.split()
        if len(parts) == 2:
            alias_name = parts[0]
            command = parts[1]
            self.aliases[alias_name] = command
            print(f"Alias '{alias_name}' created/modified.")
        else:
            print("Invalid usage. Usage: alias <alias_name> <command>")

    def do_unalias(self, arg):
        """Remove an alias. Usage: unalias <alias_name>"""
        if arg in self.aliases:
            del self.aliases[arg]
            print(f"Alias '{arg}' removed.")
        else:
            print(f"Alias '{arg}' not found.")

    def precmd(self, line):
        parts = line.split(maxsplit=1)
        command = parts[0]
        if command in self.aliases:
            line = self.aliases[command] + ' ' + (parts[1] if len(parts) > 1 else '')
        return line

    def postcmd(self, stop, line):
        return stop

    def default(self, line):
        print("Command not found.")

    def emptyline(self):
        pass

    def do_exit(self): 
        quit()

if __name__ == "__main__":
    shell = MyShell()
    shell.cmdloop()

'''