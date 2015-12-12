from app import db
from flask import request
from flask import redirect, current_app

class Sections(db.Model):

    __tablename__ = 'cms_sections'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement='ignore_fk')
    section_name = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.String(128),  nullable=True)

    def __init__(self, section_, description_):
       self.section_name = section_.title()
       self.description = description_

    def __repr__(self):
       return '<Sections %r>' % (self.section_name)


    @classmethod
    def all(cls):
        return Sections.query_order_by(desc(Sections.created)).all()


    @classmethod
    def find_by_id(cls, id):
        return Sections.query.filter(Sections.id == id).first()


    @classmethod
    def find_by_name(cls, name):
        return Sections.query.filter(Sections.section_name == name).all()

    @property
    def slug(self):
        return urlify(self.section_name)

