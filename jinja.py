import os
from yahooweather import YahooWeather, UNIT_C
from jinja2 import Environment, FileSystemLoader
from translation import translate


path = os.path.dirname(os.path.abspath(__file__))

month_tr = {'Jan': 'Янв', 'Feb': 'Фев', 'Mar': 'Мар', 'Apr': 'Апр', 'May': 'Май', 'Jun': 'Июнь', 'Jul': 'Июль', 'Aug': 'Авг', 'Sep': 'Сен',
            'Oct': 'Окт', 'Nov': 'Ноя', 'Dec': 'Дек', 'Mon': 'ПН', 'Tue': 'ВТ', 'Wed': 'СР', 'Thu': 'ЧТ','Fri': 'ПТ', 'Sat': 'СБ', 'Sun': 'ВС'}

id = {'andijan': 2272526,'bukhara': 2272540,'djizakh': 2270294,'karakalpakistan': 2272619,'qashqadaryo': 2272581,'navoi': 2272618,
      'namangan': 2272617,'samarqand': 2272628,'termez': 2272644,'sirdaryo': 2271882,'tashkentobl': 2272645,'fergana': 2270088,'horezm': 2272594,
      'tashkent': 2272113 }

list = {}

for country_id in id:
    yweather = YahooWeather(id[country_id], UNIT_C)
    if yweather.updateWeather():
        forecast = yweather.Forecast, yweather.Atmosphere,yweather.Astronomy
        for item in yweather.Forecast:
            del item['text']
        list['{}'.format(country_id)] = forecast
    else:
        print('Не могу получить данные с сервера')


translate(list, month_tr)


env = Environment(loader=FileSystemLoader(path), trim_blocks=True)
render = env.get_template('template/templ.html').render(list)
with open('frontend/index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(render)
