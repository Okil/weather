import re

def translate(big_data, translation):
    for item in big_data.values():
        a = item[0]
        for tr in a:
            b = tr['date'][3:6]
            c = tr['day']
            tr['date'] = re.sub(r'{}'.format(b), str(translation[b]), tr['date'])
            tr['day'] = re.sub(r'{}'.format(c), str(translation[c]), tr['day'])
    list = big_data
