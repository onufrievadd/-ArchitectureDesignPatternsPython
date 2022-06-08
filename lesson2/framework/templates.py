"""
Используем шаблонизатор Jinja2
"""
from jinja2 import Template

def render(template_name, folder='templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    #   Открываем шаблон по имени
    with open(folder, template_name, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
        # рендерим шаблон с параметрами
    return template.render(**kwargs)

if __name__ == '__main__':
    # Пример использования
    output_test = render('index.html', object_list=[{'name': 'Mark'}, {'name':'Maria'}])
    print(output_test)
