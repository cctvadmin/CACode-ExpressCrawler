from flask import Flask, render_template, request, Response
import util.selenium_main as _run
import json

app = Flask(__name__)


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/run', methods=['GET'])
def run_method():
    print(1)
    _data_links = request.args.get('links')
    _data_scripts = request.args.get('scripts')
    _start_sleep = request.args.get('start_sleep')
    if _start_sleep == '':
        _start_sleep = 2
    _sleep_second = request.args.get('sleep_second')
    if _sleep_second == '':
        _sleep_second = 0
    _links = str(_data_links).split('\n')
    _scripts = str(_data_scripts).split('\n')
    try:
        _result = _run.run_multiple(urls=_links, js=_scripts, start_sleep=int(_start_sleep),
                                    sleep_second=int(_sleep_second))
    except Exception as e:
        _result = str(e)
    return Response(json.dumps(_result), mimetype='application/json')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
