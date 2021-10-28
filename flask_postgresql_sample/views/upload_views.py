from posixpath import dirname
from flask import Blueprint, render_template, request, url_for, flash, send_from_directory
from werkzeug.utils import redirect, secure_filename
from flask_postgresql_sample.models import Question
from ..forms import QuestionForm
from datetime import datetime
from ..import db
from ..models import Building, Polygon, Object, BuildingSchema, PolygonSchema
from ..forms import QuestionForm, AnswerForm
import os

from io import TextIOWrapper
import csv
from flask import current_app, jsonify

bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/', methods=('GET', 'POST'))
def building():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')

        # This skips the first row of the CSV file.
        next(csv_reader)

        try:
            num_rows_deleted = db.session.query(Building).delete()
            print(num_rows_deleted)
            db.session.commit()
        except:
            db.session.rollback()

        for row in csv_reader:
            building = Building(
                id=row[1], name=row[2], desc=row[3], addr=row[4], height=row[5],
                xcoord=row[6], ycoord=row[7]
            )
            db.session.add(building)
            db.session.commit()
        return redirect(url_for('upload.building'))

    # GET
    page = 1
    building_list = Building.query.filter(Building.desc != '').paginate(page, per_page=1)
    polygon_list = Polygon.query.paginate(page, per_page=1)
    object_list = Object.query.all()

    return render_template('upload_csv.html',
        building_list=building_list,
        polygon_list=polygon_list,
        object_list=object_list,
    )


@bp.route('/polygon/', methods=('POST',))
def polygon():
    csv_file = request.files['file']
    csv_file = TextIOWrapper(csv_file, encoding='utf-8')
    csv_reader = csv.reader(csv_file, delimiter=',')

    # This skips the first row of the CSV file.
    next(csv_reader)

    try:
        num_rows_deleted = db.session.query(Polygon).delete()
        print(num_rows_deleted)
        db.session.commit()
    except:
        db.session.rollback()

    for row in csv_reader:
        polygon = Polygon(
            building_id=row[1], seq=row[2], area=row[3], xycoords=row[4]
        )
        db.session.add(polygon)
        db.session.commit()

    return redirect(url_for('upload.building'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'glb','gif'}

@bp.route('/object/', methods=('POST',))
def object():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # 모델 정보 저장
        building_id = request.form['building_id']

        try:
            Object.query.filter_by(building_id=building_id).delete()
            object = Object(building_id=building_id, file_name=filename, create_date=datetime.now())
            db.session.add(object)
            db.session.commit()
        except:
            db.session.rollback()

        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload.building'))

    return redirect(url_for('upload.building'))

@bp.route('/objects/<name>')
def download_file(name):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)


@bp.route('/objects/<int:building_id>', methods=["POST"])
def delete_object(building_id):
    object = Object.query.get(building_id)

    os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], object.file_name))
    db.session.delete(object)
    db.session.commit()
    return redirect(url_for('upload.building'))

@bp.route('/buildings/<id>')
def get_buildings(id):
    schema = BuildingSchema()
    building = Building.query.get(id)
    return schema.dump(building)

@bp.route('/buildings/<building_id>/polygons')
def get_polygons(building_id):
    schema = PolygonSchema(many=True)
    polygons = Polygon.query.filter_by(building_id=building_id).all()
    return jsonify(schema.dump(polygons))
