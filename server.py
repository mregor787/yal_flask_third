from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/load_photo', methods=['GET', 'POST'])
def photo():
    if request.method == 'GET':
        return f'''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
                    rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
                    crossorigin="anonymous">
                    <link href="{url_for('static', filename='css/style.css')}"
                    rel="stylesheet">
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                    <h1>Загрузка фотографии</h1>
                    <h2>для участия в миссии</h2>
                    <form method="post" enctype="multipart/form-data" class="photo_form">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <img src="{url_for('static', filename='img/photo.png')}" style="width: 100%">
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </body>
            </html>
            '''
    elif request.method == 'POST':
        file = request.files['file']
        file.save('static/img/photo.png')
        return redirect('/load_photo')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
