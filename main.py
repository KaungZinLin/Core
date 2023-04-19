import webbrowser
from tkinter import Tk, Label, Button, messagebox, Toplevel

def about_app():
    def open_github():
        webbrowser.open("https://github.com/KaungZinLin/Core")

    about_window = Toplevel()
    about_window.title("About")
    about_window.resizable(False, False)
    # about_window.geometry("500x300")
    about_window.config(padx=20, pady=20)

    about_label = Label(about_window, text="Core", font=('Areal', 35))
    about_label.grid(row=0, column=0, columnspan=3)

    appstore_label_2 = Label(about_window, text="App Store")
    appstore_label_2.grid(row=1, column=0, columnspan=3)

    text_about_label = Label(about_window, text="\nCore is an app created by ThatMacCat (KaungZinLin) to easily manage and install apps from ThatMacCat's GitHub Repository.")
    text_about_label.grid(row=2, column=0)

    text_about_label_2 = Label(about_window, text="\nApp Version: Core (App Store) for Mac (v0.1 Developer Preview)")
    text_about_label_2.grid(row=3, column=0)

    text_about_label_3 = Label(about_window, text="This version is created for macOS by a macOS user.")
    text_about_label_3.grid(row=4, column=0)

    text_about_label_4 = Label(about_window, text="\nHUGE THANKS FOR USING THIS APP!!!\n")
    text_about_label_4.grid(row=5, column=0)

    github_button = Button(about_window, text="GitHub", width=35, command=open_github)
    github_button.grid(row=6, column=0)

def download_pixtools():
    webbrowser.open("https://github.com/KaungZinLin/PixTools/releases/download/v0.2/PixTools.for.Mac.X.dmg")

def download_pyprime():
    webbrowser.open("https://github.com/KaungZinLin/PyPrime/releases/download/v1.4_stable/PyPrime_1.4.zip")

def download_py_translator():
    webbrowser.open("https://github.com/KaungZinLin/PyTranslator/archive/refs/heads/main.zip")

def download_pysnake():
    messagebox.showerror("Error!", "!WIP! - WORK IN PROGRESS!")

def download_py_speedtest():
    webbrowser.open("https://github.com/KaungZinLin/py_speedtest/archive/refs/heads/main.zip")

def github_pixtools():
    webbrowser.open("https://github.com/KaungZinLin/PixTools")

def github_pyprime():
    webbrowser.open("https://github.com/KaungZinLin/PyPrime")

def github_py_translator():
    webbrowser.open("https://github.com/KaungZinLin/PyTranslator")

def github_pysnake():
    messagebox.showerror("Error!", "!WIP! - WORK IN PROGRESS!")

def github_py_speedtest():
    webbrowser.open("https://github.com/KaungZinLin/py_speedtest")

# GUI Setup
window = Tk()
window.title("Core")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Labels
welcome_label = Label(window, text="Core", font=("Areal", 25))
welcome_label.grid(row=0, column=0, columnspan=3, sticky='w')

appstore_label = Label(window, text="App Store")
appstore_label.grid(row=1, column=0, sticky='w')

developer_label = Label(window, text="\nDEVELOPER: ThatMacCat (KaungZinLin)")
developer_label.grid(row=2, column=0, sticky='w')

pix_tools_label = Label(window, text="PixTools for Mac X")
pix_tools_label.grid(row=3, column=0, sticky='w')

py_prime_label = Label(window, text="PyPrime")
py_prime_label.grid(row=4, column=0, sticky='w')

py_translater_label = Label(window, text="PyTranslater (UNSTABLE)")
py_translater_label.grid(row=5, column=0, sticky='w')

py_snake_label = Label(window, text="PySnake (UNSTABLE)")
py_snake_label.grid(row=6, column=0, sticky='w')

py_speedtest_label = Label(window, text="PySpeedtest (UNSTABLE)")
py_speedtest_label.grid(row=7, column=0, sticky='w')

# Buttons
about_button = Button(window, text="About", width=10, command=about_app)
about_button.grid(row=0, column=3)

pix_tools_download_button = Button(window, text="Download", width=10, command=download_pixtools)
pix_tools_download_button.grid(row=3, column=1)

pyprime_download_button = Button(window, text="Download", width=10, command=download_pyprime)
pyprime_download_button.grid(row=4, column=1)

py_translator_download_button = Button(window, text="Download", width=10, command=download_py_translator)
py_translator_download_button.grid(row=5, column=1)

py_snake_download_button = Button(window, text="Download", width=10, command=download_pysnake)
py_snake_download_button.grid(row=6, column=1, sticky='e')

py_speedtest_download_button = Button(window, text="Download", width=10, command=download_py_speedtest)
py_speedtest_download_button.grid(row=7, column=1)

pix_tools_github_button = Button(window, text="GitHub", width=10, command=github_pixtools)
pix_tools_github_button.grid(row=3, column=3)

pyprime_github_button = Button(window, text="GitHub", width=10, command=github_pyprime)
pyprime_github_button.grid(row=4, column=3)

py_translator_github_button = Button(window, text="GitHub", width=10, command=github_py_translator)
py_translator_github_button.grid(row=5, column=3)

py_snake_github_button = Button(window, text="GitHub", width=10, command=github_pysnake)
py_snake_github_button.grid(row=6, column=3)

py_speedtest_github_button = Button(window, text="GitHub", width=10, command=github_py_speedtest)
py_speedtest_github_button.grid(row=7, column=3)

# GUI Loop
window.mainloop()
