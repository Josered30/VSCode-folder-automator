# VS Code folder automator

This is a script to create folders/filters and open them in VS Code 


## How to use it

There are 3 commands: ne, on and nfe:
- ne -> Note name and extension
- on -> Open note
- nfe -> Note, folder and extension

Recommended directory structure:


* VS Projects
    * Automator
        * General
        * notes.py
    * Project1
    * Project2

_________________

### NE

The ne command creates a file in the General folder

<html>
    <table>
        <tr>
            <th>Position</th>
            <th>Parameter</th>
        </tr>
        <tr>
            <td>1</td>
            <td>File name</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Extension</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Open option</td>
        </tr>
    </table>
</html>

>Example: note.py ne text txt d

                
    

### ON

The on command open a folder/file in the parent folder. If the file doesn't exist it will create it. 


<html>
    <table>
        <tr>
            <th>Position</th>
            <th>Parameter</th>
        </tr>
        <tr>
            <td>1</td>
            <td>File name</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Folder name</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Open option</td>
        </tr>
    </table>
</html>

>Example: note.py on main python-proyect



### NFE

The nfe command creates a folder/file in the parent folder of the script 

<html>
    <table>
        <tr>
            <th>Position</th>
            <th>Parameter</th>
        </tr>
        <tr>
            <td>1</td>
            <td>File name</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Folder name</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Extension name</td>
        </tr>

    </table>
</html>

>Example: note.py nfe main python-proyect pythonf d



## Extensions supported

- "python" : python
- ".py" : python
- "text" : text
- ".txt" : text
- "java" : java
- ".java" : java
- "dart" : dart
- "flutter" : dart
- ".dart" : dart
- "yaml" : yaml
- ".yaml" : yaml
- "json" : json
- "jason" : json
- ".json" : json
- "org" : org
- ".org" : org
- "markdown" : markdown
- ".md" : markdown
- "php" : php
- ".php" : php
- "ruby" : ruby
- ".rb" : ruby
- "javascript" : javascript
- "js" : javascript
- ".js" : javascript
- "ts" : typescript
- "xml" : xml
- ".xml" : xml
- "html" : html
- ".html": html
- "css" : css
- ".css" : css
- "c++": cpp
- ".cpp": cpp
- "c": c


## Open options

- d -> Opens the folder in VS Code 
- f -> Opens the file in VS Code