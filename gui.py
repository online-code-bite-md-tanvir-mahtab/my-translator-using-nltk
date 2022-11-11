from msilib.schema import ListBox
from tkinter import MULTIPLE, Button, Label, Tk


# constant
list_of_lan = []
class Gui:
    def __init__(self):
        self.screen = Tk()
        # sizing the screen
        self.screen.minsize(width=300,height=100)
        self.screen.title("Language translator")
        self.design_the_screen()
        self.keep_the_screen()


    def design_the_screen(self):
        def showSelected():
            for i in lb.curselection():
                text=lb.get(i)
                list_of_lan.append(text)
            
            print(list_of_lan)
            list_of_lan.clear()
        langus = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'check', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', '(Simplified)', 'Chinese', '(Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'history', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian', 'Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', '(Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar', '(Burmese)', 'Nepali', 'Norwegian', 'Odia', '(Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots', 'Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

        lb = ListBox(self.screen,selectmode=MULTIPLE)
        lb.pack()
        for i in range(len(langus)):
            lb.insert(i,langus[i])

        Button(self.screen, text='Show Selected', command=showSelected).pack(pady=20)
        show = Label(self.screen)
        show.pack()

    def keep_the_screen(self):
        self.screen.mainloop()


g = Gui()
# g.design_the_screen()
# g.keep_the_screen()