import PyInstaller.__main__
User_inputPhath = input("Enter the file path remember that don't enter file name or q to Quit: ")
User_input = input("Enter file name and remember that end of the file enter '.py' or q to Quit: ")
while True:
    if User_inputPhath or User_input != 'q':
        PyInstaller.__main__.run([
        User_inputPhath+'\\'+User_input,
        '--onefile'
    ])
    elif User_input == 'q':
        break