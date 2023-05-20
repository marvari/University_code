#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import flask
from flask import Flask, request
from eu_algoritm import my_gcd
from prime_test import is_prime

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def main_page():
    return flask.render_template('main_page.html')


@app.route('/prime_test', methods=['GET', 'POST'])
def prime():
    if request.method == 'GET':
        return flask.render_template('prime.html')
    
    elif request.method == 'POST':

        prime_output = is_prime(int((request.form.get('num'))))
            

        return flask.render_template(
            'answer_prime.html',
            num=request.form.get('num'),
            value=prime_output,
            method=request.method)


@app.route('/euclidean_algorithm', methods=['GET', 'POST'])
def algo():
    if request.method == 'GET':
        return flask.render_template('algo.html')
    
    elif request.method == 'POST':

        algo_result = my_gcd(int(request.form.get('num1')), int(request.form.get('num2')))


        return flask.render_template(
            'answer_algo.html',
            num1=request.form.get('num1'),
            num2=request.form.get('num2'),
            value= algo_result,
            method=request.method)


@app.route('/akhalteke')
def akhalteke():
    return flask.render_template('akhalteke.html')


@app.route('/horses')
def horses():
    return flask.render_template('horses.html')


@app.route('/i')
def i():
    return flask.render_template('i.html')


if __name__ == '__main__':
   app.run(debug = True)
   
