from enum import auto
from googletrans import Translator



class G_Translator:
    def __init__(self):
        # defining the Translator object
        self.translate = Translator()

    def detect_the_language(self,message):
        language = self.translate.detect(message).lang
        return language
    def get_text(self,message,code):
        language = self.translate.translate(message,dest=f'{code}').text
        return language


# g = G_Translator()
# code = (g.detect_the_language("وَلاَ تَجْهَرْ بِصَلاتِكَ وَلاَ تُخَافِتْ بِهَا وَابْتَغِ بَيْنَ ذَلِكَ سَبِيلاً"))
# print(code)
# print(g.get_text("是面向极客的计算机科学门户",code))
# translator = Translator()
# translation = translator.translate("Hola como estas ?", dest='en')
# print(translation.text)
print("hello world")