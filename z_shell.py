## Zed Shell

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
        '''pwd prints working directory'''
        current_dir = os.getcwd()
        print(current_dir)

    def do_exit(self, args):
        '''exit the shell'''
        quit() ### exit the terminal

    def do_help(self, arg: str) -> bool | None:
        '''helps find commands'''
        return super().do_help(arg)
    
    ## change prompt
    def do_set_prompt(self, args):
        '''Changes shell prompt'''
        shell_z.prompt = args + ' '

    ## clear the shell
    def do_cls(self, args):
        '''clears shell'''
        os.system('cls')



if __name__ == "__main__":
    shell = shell_z()
    shell.cmdloop()  # Start the shell prompt loop

