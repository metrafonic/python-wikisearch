#!/usr/bin/python
from flask import Flask, jsonify, abort, request, redirect
from wiki import wikiSearch
app = Flask(__name__)

@app.route('/wikisearch', methods=['GET'])
def get_version():
    return "<h1>Wikipedia page search</h1><form action='/wikisearch/api/v1.0/page' method='POST'> Page: <input type='text' name='page' value='page'><br> Lang: <input type='text' name='lang' value='no'><br><input type='submit'></form>"


@app.route('/wikisearch/api/v1.0/page', methods=['POST'])
def create_task():
    return redirect(wikiSearch(request.form['page'], request.form['lang']), code=302)
    #return redirect("http://google.com", code=302)

if __name__ == '__main__':
    app.run( 
        host="0.0.0.0",
        port=int("5000")
  )
