import subprocess

class Files:
    def delete_files_in_folder(self, mydir, endwith):
        import os
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        for f in filelist:
            os.remove(os.path.join(mydir, f))

class Browsers:
    def kill_all_browsers(self):
        prog = subprocess.Popen("taskkill /im coccocdriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog = subprocess.Popen("taskkill /im chromedriver.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        prog.communicate()