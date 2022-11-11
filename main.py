# from pydoc import text
from ntpath import join
from time import sleep
from tkinter.messagebox import YES
from turtle import onkey
from bs4 import BeautifulSoup
from nltk import sent_tokenize, word_tokenize, download
import nltk
from info import *
from tkinter import * 
import pandas
path_to_file = 'demoreader/src/file-1.html'
csv_file_pathh = 'demoreader/src/html-file.csv'

print("=======html translation=========")
# now i am going to add the nltk_data path to the nltk
nltk.data.path.append('demoreader/src/nltk_data')
path_to_file = 'demoreader/src/file-1.html'
'''
# we are going detect every language and its code
# with the code we are going to store them in a seperate list'''

lang_code = 'af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw'
list_of_lang_code = lang_code.split(',')
def d_language(sentences):
    from langdetect import detect
    from pycountry import languages
    try:
        b = detect(sentences)
        lang_name = languages.get(alpha_2=str(b)).name
        return lang_name
    except:
        return "English"
    

def translate_the_word(words,avoid,t):
    setences =  word_tokenize(words)
    sentence = []
    for sen in setences:
        if sen == '(' or sen == ')' or sen == '{' or sen == '}' or sen == '[' or sen == ']':
            sentence.append(sen)
            pass
        else:
            if sen == "None":
                sentence.append(sen)
                pass
            else:
                if d_language(sen) == avoid[0]:
                    print(f"{avoid[0]} found so avoided")
                    sentence.append(sen)
                    pass
                else:
                    new_list = [data for data in setences if data != "None"]
                    t.send_the_text_to_google(sen)
                    t.send_the_text_to_google(" ")
                    if sen ==  new_list[len(new_list)-1]:
                        sentence.append(t.get_the_translated_data())
                    # t.send_the_text_to_google(sen) 
                    # t.send_the_text_to_google(" ")
                    # if sen == new_list[len(new_list)-1]:
                    #     translated_text = t.get_the_translated_data()
                    #     # print(translated_text)
                    #     sentence.append(translated_text)
                            
        
    return sentence


def large_trans(sentences,avoid,t):
    translated_sen = []
    words = sentences.split()
    for sen in words:
        if d_language(sen) == avoid:
            translated_sen.append(sen)
        else:
            translated_sen.append(sen)
    
    # TODO : WE NEED TO SEPARATE THE DATA THAT ARE INSIDE THE ANGLE BRACKET AND SEPARATE IT
    '''the algorithm is been created i call it {finding the end}'''
    # word = ['He', 'ﷺ', 'said', ',', '<', 'Didnt', 'Allah', 'say', '>', '-', 'Answer', 'Allah', '(', 'by', 'obeying', 'Him', ')', 'and', 'His', 'Messenger', 'when', 'he', '<', 'صلى', 'الله', 'عليه', 'وسلم', '>', 'calls', 'you', '.']
    word = translated_sen
    i = 0
    new_list_of_word = []
    bracket_list = []
    while i<= len(word)-1:
        if word[i] == "<":
            bracket_list.append(word[i])
            new_list_of_word.append("None")
            for j in range(i+1,len(word)):
                if word[j] == ">":
                    bracket_list.append(word[j])
                    new_list_of_word.append("None")
                    i= j
                    break
                else:
                    bracket_list.append(word[j])
                    new_list_of_word.append("None")
                    pass
        else:
            if word[i] == '(' or word[i] == ')' or word[i] == '{' or word[i] == '}' or word[i] == '[' or word[i] == ']':
                new_list_of_word.append(word[i])
                pass
            else:
                new_list_of_word.append(word[i])
        i += 1
    join_new_list_of_word = " ".join(new_list_of_word)
    the_sorted_list = translate_the_word(join_new_list_of_word,avoid,t)
    # print(the_sorted_list)
    i=0
    none_count = 0
    while i < len(the_sorted_list):
        if the_sorted_list[i] == "None":
            none_count +=1
            the_sorted_list[i] = "".join(bracket_list[none_count-1])
        else:
            pass
        i+=1
    
    # print(bracket_list)
    return "".join(the_sorted_list)



def trans(large_sentences):
    word_list_for_sentences = []
    sentences = []
    for sen in (sent_tokenize(large_sentences)):
        word_list_for_sentences.append(word_tokenize(sen))
        
    for i in range(len(word_list_for_sentences)):
        for j in word_list_for_sentences[i]:
            if j == '(' or j == ')' or j == '[' or j == ']' or j == '{' or j == '}':
                pass
            else:
                sentences.append(j)
    return " ".join(sentences)
            


def devide(large_sentences):
    
    word_list_for_sentences = []
    sentences = []
    # for sen in sent_tokenize(large_sentences):
    #     word_list_for_sentences.append(sen.split())
    for sen in (sent_tokenize(large_sentences)):
        word_list_for_sentences.append(word_tokenize(sen))
        
    for i in range(len(word_list_for_sentences)):
        for j in word_list_for_sentences[i]:
            sentences.append(j)
    # new_sentences = "".join(sentences)
    return " ".join(sentences)


nltk.data.path.append('demoreader/src/nltk_data')
def do_something(html_file_name,language,main_language,avoid):
    from os.path import exists, basename, splitext
    # in here we are checing if the file name are exists or not
    if exists(html_file_name):
        print(f"{html_file_name} file is founded the process is started")
        # keeping the file name inside another variable
        path_to_file = html_file_name
        with open(file=path_to_file, encoding="utf8") as file:
                sentences = file.readlines()
        for lan in language:
            word = []
            for sen in sentences:
                word.append(sen)
            # print(word)
            t = Translate(lan)
            # TODO: you have to call the cookie method
            t.select_the_language(main_language[0])
            with open(file=f"demoreader/src/translated_folder/{splitext(basename(html_file_name))[0]}-{lan}.html", encoding="utf8", mode='w') as file2:
                for w in range(len(word)):
                    sen = (devide(word[w]))
                    file2.write(large_trans(sen,avoid,t))
                    # print((large_trans(sen,avoid,t)))
                    t.clean_the_text()
                # print(trans(large_trans(sen)))
            t.close_driver()
                        
    else:
        print("dosent exists")




screen = Tk()
list_of_lan = []
list_of_main_lan = []
list_of_avoid_lan = []
screen.title("html file")
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
    # print(list_of_main_lan)
    # print(list_of_lan)
    '''this have to be fixed'''
    # 
    path_to_file = 'demoreader/src/Task-1-Translate-HTML-in-Column-B-to-other-Languages-create-new-HTML_JS.xlsx'

    import pandas
    import openpyxl
    wb = openpyxl.load_workbook(path_to_file)

    # grab the active worksheet
    ex_soup = wb['Data']
    html_file_list = []

    for row in ex_soup['B']:
        html_file_list.append(str(row.value))
    for html in html_file_list:
        if "html" in html:
            do_something(f'demoreader/src/html_folder/{html}',list_of_lan,list_of_main_lan,list_of_avoid_lan)
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




