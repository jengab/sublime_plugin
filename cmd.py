import subprocess, sublime_plugin,sublime,threading

class CmdCommand(sublime_plugin.TextCommand):
    commands=[]

    def run(self, edit):
        file_name=self.view.file_name()
        path=file_name.split("/")
        current_driver=path[0]
        file=path.pop()
        current_directory="/".join(path)
        #to set xterm window title        
        self.commands=['echo -ne \'\033]2;Python program\007\'']
        self.commands+=['cd '+current_directory,'python '+file]
        #We run these commands to stop in the end
        self.commands+=['printf \'\\nPress a key to exit...\\n\'','read']
        if not file.strip().endswith(".py"):
            sublime.error_message("Only python files can be run!")
        else:
            threading.Thread(target=CmdCommand.runProgram,args=(self,)).start()

    def runProgram(self):
        with open('/home/gabor/sublime.log','w') as File:
            File.write(';'.join(self.commands))        
        subprocess.call('xterm -e "'+';'.join(self.commands)+'"',shell=True)
