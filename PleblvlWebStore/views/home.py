from flask import (Blueprint, flash, g, jsonify, redirect, render_template,
                   request, session, url_for)

# from pleblvlSales.utils import request_wants_json

mod = Blueprint('home', __name__)


@mod.route('/')
def index():
	return render_template("home/index.html")
@mod.route('/about')
def about():
	return render_template("home/about.html")
