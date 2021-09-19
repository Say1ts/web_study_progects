from flask import Flask
from random import randrange


app = Flask(__name__)

a, b, c, d, e = True, True, True, True, True
first = True


@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    global a, b, c, d, e, first
    if not first:
        a = (randrange(2) == 1)
        b = (randrange(2) == 1)
        c = (randrange(2) == 1)
        d = (randrange(2) == 1)
        e = (randrange(2) == 1)
    my_str = ""
    if a or b or c or d or e:
        my_str = my_str + "Вариант 4. Разработайте игру, которая " \
                          "заключается в следующем. На странице размещены" \
                          " пять кнопок(Button).При нажатии на кнопку " \
                          "некоторые кнопки становятся видимыми, а другие " \
                          "– невидимыми. Цель игры – скрыть все кнопки. "
    else:
        my_str = my_str + "victory"
    my_str = my_str + "<form>"
    if a:
        my_str = my_str + "<input type='submit' name='button' value='Button1'>"
    if b:
        my_str = my_str + "<input type='submit' name='button' value='Button2'>"
    if c:
        my_str = my_str + "<input type='submit' name='button' value='Button3'>"
    if d:
        my_str = my_str + "<input type='submit' name='button' value='Button4'>"
    if e:
        my_str = my_str + "<input type='submit' name='button' value='Button5'>"
    my_str = my_str + "</form>"
    first = False

    return my_str


if __name__ == '__main__':
    app.run()
