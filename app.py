from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
import glob
import json
import locale

app = Flask(__name__)


if __name__ == '__main__':
    app.run('0.0.0.0.', port=5000, debug=True)

    # app_lang = locale.getdefaultlocale()[0]
    # if app_lang == 'en_SG':
    #     app_lang = 'en'
    # elif app_lang == 'zh_SG':
    #     app_lang = 'zh'

    # app.config['BABEL_DEFAULT_LOCALE'] = app_lang
    # app.config['BABEL_DEFAULT_TIMEZONE'] = 'Asia/Singapore'

    app_language = 'en_SG'
    locale.setlocale(locale.LC_ALL, app_language)

    languages = {}  # a dictionary to hold the translated data from languages
    stats = {}  # a disctionary to hold relevant data, such as number of files, number of lines, etc
    currencies = {}  # a dictionary to hold the currency data
    date_format = '%d %b %Y %H:%M:%S %Z'
    # last_updated = datetime.datetime.now().strftime(date_format)
    last_updated = ""