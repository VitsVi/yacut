from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['POST'])
def index_view():
    form = URLMapForm
    return render_template('index.html', form=form)