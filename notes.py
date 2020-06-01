import sys
import os 
from pathlib import Path


class NoteAutomator: 
    ruby = ".rb"
    php = ".php"
    javascript = ".js"
    typescript = ".ts"
    python = ".py"
    java = ".java"
    csharp = ".cs"
    dart = ".dart"
    text = ".txt"
    yaml = ".yaml"
    xml = ".xml"
    html = ".html"
    css = ".css"
    json = ".json"
    org = ".org"
    markdown = ".md"
    cpp = ".cpp"
    c = ".c"

    extensions = {
        "python" : python,
        ".py" : python,
        "text" : text,
        ".txt" : text,
        "java" : java,
        ".java" : java,
        "dart" : dart,
        "flutter" : dart,
        ".dart" : dart,
        "yaml" : yaml,
        ".yaml" : yaml,
        "json" : json,
        "jason" : json,
        ".json" : json,
        "org" : org,
        ".org" : org,
        "markdown" : markdown,
        ".md" : markdown,
        "php" : php,
        ".php" : php,
        "ruby" : ruby,
        ".rb" : ruby,
        "javascript" : javascript,
        "js" : javascript,
        ".js" : javascript,
        "ts" : typescript,
        "xml" : xml,
        ".xml" : xml,
        "html" : html,
        ".html": html,
        "css" : css,
        ".css" : css,
        "c++": cpp,
        ".cpp": cpp,
        "c": c
    }

    extension = ""
    folderName = ""
    fileName = ""
    foundFileExtension = ""
    path = ""

    def getArgs(self, ext_num, fold_num):
        try:
            self.extension = str(sys.argv[ext_num]).lower()
            self.extension = self.extensions[self.extension]
        except Exception:
            self.extension = ".txt"
        try:
            self.folderName = str(sys.argv[fold_num])
        except Exception:
            self.folderName = "General"
        try:
            self.fileName = str(sys.argv[2])
        except Exception:
            print("Name your note")
            sys.exit()


    def createNoteAndFolder(self, dir_path):
        os.chdir(dir_path)

        self.fileName = self.fileName + self.extension

        if os.path.isdir("./" + self.folderName):
            os.chdir("./" + self.folderName)
        else:
            os.mkdir(self.folderName)
            os.chdir("./" + self.folderName)
    
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()
     
        os.system('code .')



    def findFileInFolder(self, folder, open_option = "d"):
        if os.path.isdir(self.path + "/" + folder):
            self.path = self.path + "/" + folder
        else:
            self.path = self.findFolder(folder, self.path)
            if self.path == None:
                print("Not found")
                return 
        
        self.findFile(self.fileName, self.path, open_option)
        os.system(f'code "{self.path}"')



    def findFolder(self, folderName, thepath):
        pathToFolder = None

        for subdir, dirs, files in os.walk(thepath):
            for dir_ in dirs:
                if dir_.lower() == self.folderName.lower():        
                    pathToFolder = subdir + "/" + self.folderName

        return pathToFolder



    def findFile(self, fileToFind, thepath, open_option):
        fileExists = False
    
        for subdir, dirs, files in os.walk(thepath):
            for file_ in files:
                name = ""
                #Check if more than the 80% of the file name is equal to the file to find
                for i in range(len(str(file_))):     
                    if len(str(self.fileName)) > i:
                        if str(file_).lower()[i] == str(self.fileName).lower()[i]:
                            name = name + str(file_)[i]

                            if len(name) > len(self.fileName) * 0.8:
                                if open_option == "f":
                                    self.path = os.path.join(subdir, file_)
                                elif open_option == "d":
                                    self.path = subdir
                                fileExists = True
                                break

        if not fileExists:
            file_path = os.path.join(thepath ,self.fileName + self.extension)
            print(file_path)

            open(file_path, "a").close()
        
            if open_option == "f":
                self.path = file_path
            elif open_option == "d":    
                self.path = thepath




if __name__ == "__main__":
    notes = NoteAutomator()
    dir_path = os.path.dirname(os.path.realpath(__file__))

    command = str(sys.argv[1])


    if command == "nfe":
        notes.getArgs(4, 3)
        notes.createNoteAndFolder(str(Path(dir_path).parent))

    if command == "on":
        notes.getArgs(10, 3)    
        try: 
            notes.path = str(Path(dir_path).parent)
            notes.findFileInFolder(str(sys.argv[3]),str(sys.argv[4]))
        except Exception:
            notes.path = dir_path
            notes.findFileInFolder("General")

    if command == "ne":
        notes.path = dir_path
        notes.getArgs(3, 10)
        notes.findFileInFolder("General",str(sys.argv[4]))
        

