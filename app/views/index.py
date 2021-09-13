from flask import Blueprint, render_template
from src.extract.extractor import extractors


routes = Blueprint('index', __name__)


@routes.route('/')
def index():
    choices = {v.display_name: k for k, v in extractors.items()}
    return render_template(
        'index.html',
        choices=dict(sorted(choices.items())),
    )
