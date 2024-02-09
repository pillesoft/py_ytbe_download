import os
from urllib.parse import unquote_plus
from flask import Flask, render_template, send_file, request, flash

from .download import MediaFile, Download, ConvertError

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='a19c0b12dece6a0bd9123618659622553046c26014a830d1',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.get("/")
    def home_get():
        # filenames = ['file 1', 'file 2']
        return render_template("index.html")

    @app.post("/")
    def home_post():
        url = request.form['txturl']
        url = url.strip()
        error = None

        if len(url) == 0:
            error = "Kérlek, adj meg Youtube linket, amit le tudok tölteni!"

        if error is not None:
            flash(error, category='warning')

        d: Download = Download()
        filenames: list[MediaFile] = []
        
        urls = url.split(os.linesep)
        # print(urls)
        try:
            if "btnmp3" in request.form:
                d.download_mp3(urls)
            elif "btnmp4" in request.form:
                d.download_mp4(urls)
            filenames = d.Files
            # print(filenames)
        except ConvertError as e:
            flash("OOPS! an error occured {}".format(e.error_code), category='error')
    
        return render_template("index.html", downloaded = filenames)

    @app.route("/progress")
    def download_progress():
        ...

    @app.route("/download")
    def file_download():
        fullname = request.args['fullname']
        nameext = request.args['nameext']

        fullname = unquote_plus(fullname)
        nameext = unquote_plus(nameext)

        return send_file(fullname, download_name=nameext, as_attachment=True, mimetype='audio/mpeg' )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
