from flask import Blueprint, render_template, request, jsonify
from datetime import datetime

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "title": "The Hangover",
        "title_ru": "Мальчишник в Вегасе",
        "year": "2009",
        "description": "Они мечтали устроить незабываемый мальчишник в Вегасе. Но теперь им необходимо вспомнить, \
            что именно произошло: что за ребенок сидит в шкафу номера отеля? Как в ванную попал тигр? Почему у одного \
            из них нет зуба? И, самое главное, куда делся жених? То, что парни вытворяли на вечеринке, не идет ни в \
            какое сравнение с тем, что им придется сделать на трезвую голову, когда они будут шаг за шагом \
            восстанавливать события прошлой ночи."
    },
    {
        "title": "Holidate",
        "title_ru": "Пара на праздники",
        "year": "2020",
        "description": "Они не знакомы, но устали проводить праздники в одиночестве. Тогда эти двое решают \
            поддерживать отношения круглый год. Только сердцу не прикажешь."
    },
    {
        "title": "The Grinch",
        "title_ru": "Гринч",
        "year": "2018",
        "description": "Любой бы на месте Гринча позеленел и взбесился. Как порядочный интроверт он живёт в тёмной \
            пещере на самой вершине горы подальше ото всех, но эти «все» готовят грандиознейшее празднование нового \
            года. Они шумят, всё украшают и дико бесят. Кто бы отказал себе в удовольствии испортить праздник? \
            Гринч решает украсть Новый год."
    },
    {
        "title": "F1",
        "title_ru": "Формула 1",
        "year": "2025",
        "description": "В 1990-х Сонни Хейс был восходящей звездой «Формулы-1», но после серьёзной аварии ушёл из \
            большого спорта. 30 лет спустя Сонни живёт в трейлере и зарабатывает участием в различных гонках и \
            чемпионатах. Однажды к нему обращается старый друг Рубен Сервантес, тоже в прошлом гонщик, а ныне \
            владелец гоночной команды-аутсайдера, с просьбой присоединиться к ним в качестве второго пилота \
            и наставника для молодого многообещающего новичка."
    },
    {
        "title": "Knives Out",
        "title_ru": "Достать ножи",
        "year": "2019",
        "description": "На следующее утро после празднования 85-летия известного автора криминальных романов \
            Харлана Тромби виновника торжества находят мёртвым. Налицо — явное самоубийство, но полиция по \
            протоколу опрашивает всех присутствующих в особняке членов семьи, хотя, в этом деле больше \
            заинтересован частный детектив Бенуа Блан. Тем же утром он получил конверт с наличными от \
            неизвестного и заказ на расследование смерти Харлана. Не нужно быть опытным следователем, чтобы \
            понять, что все приукрашивают свои отношения с почившим главой семейства, но Блану достаётся \
            настоящий подарок — медсестра покойного, которая физически не выносит ложь."
    },
]


def validate_film_data(film_data):
    errors = {}
    
    title_ru = film_data.get('title_ru', '').strip()
    if not title_ru:
        errors['title_ru'] = 'Русское название обязательно'
    
    title = film_data.get('title', '').strip()
    if not title and not title_ru:
        errors['title'] = 'Название на оригинальном языке обязательно, если русское название пустое'
    
    year_str = film_data.get('year', '')
    try:
        year = int(year_str)
        current_year = datetime.now().year
        if year < 1895 or year > current_year:
            errors['year'] = f'Год должен быть от 1895 до {current_year}'
    except (ValueError, TypeError):
        errors['year'] = 'Год должен быть числом'
    
    description = film_data.get('description', '').strip()
    if not description:
        errors['description'] = 'Описание обязательно'
    elif len(description) > 2000:
        errors['description'] = 'Описание не должно превышать 2000 символов'
    
    return errors

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_films_by_id(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Фильм не найден"}), 404

    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Фильм не найден"}), 404

    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Фильм не найден"}), 404
    
    film_data = request.get_json()
    
    if not film_data:
        return jsonify({"error": "Не предоставлены данные для обновления"}), 400
    
    errors = validate_film_data(film_data)
    if errors:
        return jsonify(errors), 400
    
    title = film_data.get('title', '').strip()
    title_ru = film_data.get('title_ru', '').strip()
    if not title.strip() and title_ru.strip():
        film_data['title'] = title_ru

    if 'description' not in film_data or not film_data['description'].strip():
        return jsonify({'description': 'Заполните описание'}), 400
    
    films[id] = film_data
    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film_data = request.get_json()
    
    if not film_data:
        return jsonify({"error": "Не предоставлены данные фильма"}), 400
    
    errors = validate_film_data(film_data)
    if errors:
        return jsonify(errors), 400
    
    title = film_data.get('title', '').strip()
    title_ru = film_data.get('title_ru', '').strip()
    if not title.strip() and title_ru.strip():
        film_data['title'] = title_ru
        
    if 'description' not in film_data or not film_data['description'].strip():
        return jsonify({'description': 'Заполните описание'}), 400
    
    films.append(film_data)
    
    new_id = len(films) - 1
    return jsonify({"id": new_id}), 201