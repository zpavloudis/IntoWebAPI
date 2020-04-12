from flask import Flask, escape, render_template, request, url_for
app = Flask(__name__)

from IntoWebAPI import views, values