## Sed Shell

## imports
import os
import cmd
import yaml

class shell_z(cmd.Cmd):
    ## get config data
    with open('config.yaml') as config_file:
        config_data = yaml.safe_load(config_file)

    ## main prompt
    prompt = config_data['prompt']

    ## list fucntion
    def do_dir(self, args):
        '''list items in working directory'''
        dir = os.getcwd()
        items = os.listdir(dir)
        for item in items:
            print(item)
    
    ## get the working directory
    def do_pwd(self, args):
        '''Prints working directory'''
        current_dir = os.getcwd()
        print(current_dir)

    def do_exit(self, args):
        '''Exit the shell'''
        quit() ### exit the terminal

    def do_help(self, arg: str) -> bool | None:
        '''Helps find commands'''
        return super().do_help(arg)
    
    ## change prompt
    def do_set_prompt(self, args):
        '''Changes shell prompt'''
        shell_z.prompt = args + ' '

    ## clear the shell
    def do_cls(self, args):
        '''Clears shell'''
        os.system('cls')

    ## see the contents
    def do_cat(self, args):
        '''Prints the contents of a file(s)'''
        if not args:
            print("Provide a file path")
            return

        try:
            with open(args, 'r') as file:
                contents = file.read()
                print(contents)
        except FileNotFoundError:
            print("File not found.")
        except OSError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    shell = shell_z()
    shell.cmdloop()  # Start the shell prompt loop

