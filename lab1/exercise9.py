from googletrans import Translator
import pandas as pd

translator = Translator()
p0 = '-----------------------------'
p1 = 'Good morning.'
p2 = 'It is a pleasure to meet you.'
p3 = 'Please call me tomorrow.'
p4 = 'Have a nice day!'
p5 = 'Hi,how are you?'
p6 = 'How is it going?'

phrases = {
    'English': [p0,
                p1,
                p2,
                p3,
                p4,
                p5,
                p6,
                p0],
    'Italian': [p0,
                (translator.translate(p1, dest='it')).text,
                (translator.translate(p2, dest='it')).text,
                (translator.translate(p3, dest='it')).text,
                (translator.translate(p4, dest='it')).text,
                (translator.translate(p5, dest='it')).text,
                (translator.translate(p6, dest='it')).text,
                p0]
}

print(pd.DataFrame(phrases))
