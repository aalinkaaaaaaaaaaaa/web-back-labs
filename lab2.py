from flask import Blueprint, url_for, request, redirect, render_template, abort
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = [
    {'name': 'роза', 'price': 300},
    {'name': 'тюльпан', 'price': 310},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 330},
    {'name': 'георгин', 'price': 300},
    {'name': 'гладиолус', 'price': 310}
]
@lab2.route('/lab2/flowers/')
def flowers_list():
    return render_template('flowers.html', flowers=flower_list)


@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):  
    if flower_id >= len(flower_list):
        abort(404)
    flower_list.pop(flower_id)
    return redirect(url_for('flowers_list'))
    

@lab2.route('/lab2/add_flower/', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            # есть ли такой цветок
            for flower in flower_list:
                if flower['name'] == name:
                    # если есть, увеличиваем цену на 10 рублей
                    flower['price'] += 10
                    break
            else:
                # если нет, добавляем новый цветок с ценой 300
                flower_list.lab2end({'name': name, 'price': 300})
        return redirect(url_for('flowers_list'))
    return redirect(url_for('flowers_list'))


@lab2.route('/lab2/flowers/all')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Все цветы</h1>
        <p>Количество цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list}</p>
        <a href="/lab2/flowers/clear">Очистить список</a>
    </body>
</html>
'''


@lab2.route('/lab2/flowers/clear')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('flowers_list'))


@lab2.route('/lab2/example')
def example():
    name = 'Алина Геворкян'
    group = 'ФБИ-33'
    course = '3 курс'
    number = '2'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('example.html', 
                           name=name, number=number, group=group, 
                           course=course, fruits=fruits)


@lab2.route('/lab2/')
def lab22():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
<body>
    <h1>Расчёт с параметрами:</h1>
    <div class="result">
        {a} + {b} = {a + b}<br>
        {a} - {b} = {a - b}<br>
        {a} × {b} = {a * b}<br>
        {a} / {b} = {a / b if b != 0 else 'на ноль делить нельзя'}<br>
        {a}<sup>{b}</sup> = {a ** b}
    </div>
    <p><a href="/lab2/calc/">Попробовать с другими числами</a></p>
</body>
</html>
'''


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(f'/lab2/calc/{a}/1')


books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 671},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Роман-эпопея', 'pages': 1300},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Фантастика', 'pages': 480},
    {'author': 'Антон Чехов', 'title': 'Рассказы', 'genre': 'Классическая проза', 'pages': 350},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 240},
    {'author': 'Николай Гоголь', 'title': 'Мёртвые души', 'genre': 'Поэма', 'pages': 352},
    {'author': 'Иван Тургенев', 'title': 'Отцы и дети', 'genre': 'Роман', 'pages': 288},
    {'author': 'Александр Солженицын', 'title': 'Архипелаг ГУЛАГ', 'genre': 'Историческая проза', 'pages': 1424},
    {'author': 'Владимир Набоков', 'title': 'Лолита', 'genre': 'Роман', 'pages': 336},
    {'author': 'Михаил Лермонтов', 'title': 'Герой нашего времени', 'genre': 'Роман', 'pages': 224},
]
@lab2.route('/lab2/books/')
def books_list():
    return render_template('books.html', books=books)


cats = [
    {
        'name': 'Британская короткошёрстная',
        'image': 'british.jpg',
        'description': 'Спокойная и аристократичная порода с плюшевой шерстью'
    },
    {
        'name': 'Мейн-кун',
        'image': 'maine_coon.jpg',
        'description': 'Крупная порода с кисточками на ушах и дружелюбным характером'
    },
    {
        'name': 'Сиамская',
        'image': 'siamese.jpg',
        'description': 'Элегантная и разговорчивая порода с ярко-голубыми глазами'
    },
    {
        'name': 'Сфинкс',
        'image': 'sphynx.jpg',
        'description': 'Бесшёрстная порода с морщинистой кожей и тёплым телом'
    },
    {
        'name': 'Персидская',
        'image': 'persian.jpg',
        'description': 'Длинношёрстная порода с приплюснутой мордочкой'
    },
    {
        'name': 'Шотландская вислоухая',
        'image': 'scottish_fold.jpg',
        'description': 'Порода с загнутыми вперёд ушами и круглыми глазами'
    },
    {
        'name': 'Бенгальская',
        'image': 'bengal.jpg',
        'description': 'Порода с леопардовым окрасом и активным характером'
    },
    {
        'name': 'Русская голубая',
        'image': 'russian_blue.jpg',
        'description': 'Элегантная порода с серебристо-голубой шерстью и зелёными глазами'
    },
    {
        'name': 'Норвежская лесная',
        'image': 'norwegian_forest.jpg',
        'description': 'Крупная порода с густой водонепроницаемой шерстью'
    },
    {
        'name': 'Ориентальная',
        'image': 'oriental.jpg',
        'description': 'Стройная порода с большими ушами и грациозным телом'
    },
    {
        'name': 'Рэгдолл',
        'image': 'ragdoll.jpg',
        'description': 'Крупная порода, которая расслабляется на руках как тряпичная кукла'
    },
    {
        'name': 'Абиссинская',
        'image': 'abyssinian.jpg',
        'description': 'Древняя порода с тикированным окрасом и активным нравом'
    },
    {
        'name': 'Бирманская',
        'image': 'birman.jpg',
        'description': 'Порода с белыми "носочками" на лапах и шелковистой шерстью'
    },
    {
        'name': 'Турецкий ван',
        'image': 'turkish_van.jpg',
        'description': 'Порода, любящая воду, с характерным красно-белым окрасом'
    },
    {
        'name': 'Сибирская',
        'image': 'siberian.jpg',
        'description': 'Русская порода с гипоаллергенной шерстью и мощным телом'
    },
    {
        'name': 'Корниш-рекс',
        'image': 'cornish_rex.jpg',
        'description': 'Порода с волнистой шерстью и стройным телом'
    },
    {
        'name': 'Девон-рекс',
        'image': 'devon_rex.jpg',
        'description': 'Порода с большими ушами и волнистой шерстью, похожая на эльфа'
    },
    {
        'name': 'Тонкинская',
        'image': 'tonkinese.jpg',
        'description': 'Гибрид сиамской и бурманской пород с аквамариновыми глазами'
    },
    {
        'name': 'Бурманская',
        'image': 'burmese.jpg',
        'description': 'Порода с шелковистой шерстью и выразительными золотыми глазами'
    },
    {
        'name': 'Египетская мау',
        'image': 'egyptian_mau.jpg',
        'description': 'Древняя порода с пятнистым окрасом и зелёными глазами'
    }
]
@lab2.route('/lab2/cats/')
def cats_list():
    return render_template('cats.html', cats=cats)