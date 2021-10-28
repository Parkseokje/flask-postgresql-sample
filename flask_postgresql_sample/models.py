from flask_postgresql_sample import db, ma

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref(
        'answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Building(db.Model):
    id = db.Column(db.String(25), primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(50))
    addr = db.Column(db.String(100))
    height = db.Column(db.Float())
    xcoord = db.Column(db.Float(), nullable=False)
    ycoord = db.Column(db.Float(), nullable=False)
    polygons = db.relationship(
        'Polygon', backref='building', passive_deletes=True)
    object = db.relationship('Object', backref='building',
                             passive_deletes=True, uselist=False)


class Polygon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.String(25), db.ForeignKey(
        'building.id', ondelete='CASCADE'), nullable=False)
    seq = db.Column(db.Integer)
    area = db.Column(db.Float())
    xycoords = db.Column(db.Text())



class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.String(25), db.ForeignKey(
        'building.id', ondelete='CASCADE'), nullable=False)
    file_name = db.Column(db.String(255))
    create_date = db.Column(db.DateTime(), nullable=False)


class PolygonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Polygon


class BuildingSchema(ma.SQLAlchemyAutoSchema):
    # polygons = ma.Nested(PolygonSchema, many=True)

    class Meta:
        model = Building
