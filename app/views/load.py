from flask import Blueprint, redirect, request, flash
from src.external import s3
import src.logger as log
from src.extract.extractor import Extractor

routes = Blueprint('load', __name__, url_prefix='/load')


@routes.route('/new', methods=['POST'])
def file_upload_handler():
    file_type = request.form.get('file_type')
    input_files = request.files.to_dict(flat=False).get('input_files')

    for input_file in input_files:
        try:
            extractor = Extractor.from_file(input_file, file_type)
            blob = extractor.extract()
        except Exception as err:
            log.error(err)
            flash(str(err))
    return redirect('/')
