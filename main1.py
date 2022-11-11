
import csv
from email import header
from itertools import count
from operator import index
from time import sleep
from turtle import onkey
import pandas
from translate import Translator
from tkinter import *
from info import Translate
from nltk import sent_tokenize, word_tokenize, download
import nltk
path_to_file = 'demoreader/src/Task-2-Translate-from-Excel-to-Excel_JS.xlsx'

nltk.data.path.append('demoreader/src/nltk_data')

def d_language(sentences):
    from langdetect import detect
    from pycountry import languages
    try:
        b = detect(sentences)
        lang_name = languages.get(alpha_2=str(b)).name
        return lang_name
    except:
        return "English"


def part(sentences):
    '''now i need to check if  the sentences languages and return it'''
    return d_language(sentences)


def  devide(sentences):
    list_of_sen = []
    for sen in sent_tokenize(sentences):
        # print(len(sen))
        list_of_sen.append(part(sen))
    return  list_of_sen


def trans(sentences,t):

    # t.find_the_pop()
    t.send_the_text_to_google(sentences)
    return t.get_the_translated_data()
    # return sentences




def save_file(language,main_language,avoid):
    for lan in language:
        import pandas
        import openpyxl
        wb = openpyxl.load_workbook(path_to_file)

        # grab the active worksheet
        soup = wb['Task-2-Translate-Excel']

        text_list = []

        for row in soup['B']:
            text_list.append(row.value)
        # count = 0
        long_sentences = []
        t = Translate(lan)
        t.select_the_language(main_language[0])
        with open(f"{lan}-translated_from_exel.html","w",encoding='utf-8') as file :
            file.write("<html>")
            file.write("<head>")
            file.write('<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">')
            file.write("<style>")
            file.write('body"{"font-family:/"Sofia", sans-serif";}"')
            file.write("</style>")
            file.write("/head")
            file.write("<body>")
            for i in range(len(text_list)):
                if i !=0 and i !=1:

                    if len(text_list[i]) <200:
                        # print(i,part(text_list[i]))
                        # if the detect is same as the userinput
                        if part(text_list[i]) == avoid[0]:
                            print("The avoid is detected")
                            file.write(f"<h1>{text_list[i]}</h1>")
                            print(f"<h1>{text_list[i]}</h1>")
                            pass
                        else:
                            print("There is no error !!")
                            file.write(f"<div>{trans(text_list[i],t)}</div>")
                            print(f"<div>{trans(text_list[i],t)}</div>")
                            t.clean_the_text()

                    else:
                        print("The error :")
                        print(f"<h2>{text_list[i]}</h2>")
                        t.clean_the_text()
                else:
                    print("The error :")
                    pass
            file.write("</body>")
            file.write("</html>")
        t.close_driver()
    


screen = Tk()
list_of_lan = []
list_of_main_lan = []
list_of_avoid_lan = []
screen.title("exels file")
screen.minsize(width=600,height=300)
def showSelected():
    from pycountry import languages
    for i in lb.curselection():
        text=lb.get(i)
        list_of_lan.append(text)
    for i in lb2.curselection():
        text=lb2.get(i)
        list_of_main_lan.append(text)
    for i in lb3.curselection():
        text = lb3.get(i)
        list_of_avoid_lan.append(text)
    save_file(list_of_lan,list_of_main_lan,list_of_avoid_lan)
    print(f"for {list_of_lan} is done")
    sleep(1)
    list_of_main_lan.clear()
    list_of_lan.clear()
    list_of_avoid_lan.clear()
     

langus = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'check', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', '(Simplified)', 'Chinese', '(Traditional)', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch','English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian', 'Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', '(Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar', '(Burmese)', 'Nepali', 'Norwegian', 'Odia', '(Oriya)', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots', 'Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']


label = Label(screen, text='Choose languages to translate:')
label.pack(side=LEFT)
lb = Listbox(screen,selectmode=MULTIPLE,exportselection=False)
# Adding Listbox to the left
# side of root window
lb.pack(side = LEFT, fill = BOTH)
  
# Creating a Scrollbar and 
# attaching it to root window
scrollbar2 = Scrollbar(screen)
  
# Adding Scrollbar to the right
# side of root window
scrollbar2.pack(side = LEFT, fill = BOTH)
for i in range(len(langus)):
    lb.insert(i,langus[i])
lb.config(yscrollcommand= scrollbar2.set)
scrollbar2.config(command=lb.yview)
label = Label(screen, text='Select Main language:')
label.pack(side=LEFT)


# for the sencode one
lb2 = Listbox(screen,selectmode=onkey,exportselection=False)
# Adding Listbox to the left
# side of root window
lb2.pack(side = LEFT, fill = BOTH)
  
# Creating a Scrollbar and 
# attaching it to root window
scrollbar = Scrollbar(screen)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = LEFT, fill = BOTH)

for i in range(len(langus)):
    lb2.insert(i,langus[i])
lb2.config(yscrollcommand= scrollbar.set )
scrollbar.config(command = lb2.yview)


# for the thred option
label = Label(screen, text='Select Main language to avoid:')
label.pack(side=LEFT)
lb3 = Listbox(screen,selectmode=onkey,exportselection=False)
lb3.pack(side=LEFT,fill=BOTH)
scrollbar3 = Scrollbar(screen)
scrollbar3.pack(side=LEFT,fill=BOTH)
for i in range(len(langus)):
    lb3.insert(i,langus[i])

lb3.config(yscrollcommand=scrollbar3.set)
scrollbar3.config(command= lb3.yview)


Button(screen, text='Show Selected', command=showSelected).pack(pady=20)

# for the thred option
screen.mainloop()

