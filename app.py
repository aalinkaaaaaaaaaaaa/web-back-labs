from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route("/")

@app.route("/lab1")
def lab1():
    return """<!doctype html>
        <html>
            <body>
                <ul>
                    <h1>Лабораторная работа 1</h1>
                    <li><a href="/lab1/author">author</a></li>
                    <li><a href="/lab1/web">web</a></li>
                    <li><a href="/lab1/image">image</a></li>
                    <li><a href="/lab1/counter">counter</a></li>
                </ul>
            </body>
        </html>"""    

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Геворкян Алина Константиновна"
    group = "ФБИ-33"
    faculty = "ФБ"
    
    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/image') 
def image():
    path = url_for("static", filename="oak.jpeg")
    css_path = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
    <body>
        <h1>Дyб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter') 
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + url + '''<br>
        Ваш IP-адрес: ''' + client_ip + '''<br>
        <br>
        <a href="/reset_counter">Очистить счётчик</a>
    </body>
</html>
'''

@app.route('/reset_counter')
def reset_counter():
    global count
    count = 0
    return redirect('/counter')

@app.route("/lab1/info")
def info():
    return redirect("/author")

@app.route("/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201