from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    make_response, 
    json
)
from simplexml import dumps
from app import app, db, api
from app.sections.forms import CreateSectionForm, EditSectionForm
from app.sections.models import Sections
from flask_restful import Api, fields, marshal, Resource, abort, marshal_with, reqparse, inputs



api_db = Blueprint('api', __name__, url_prefix='/sec/')
api = Api(api_db)

#mod_sec = Blueprint('sec', __name__, url_prefix='/sec')

def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(dumps({'response' :data}), code)
    resp.headers.extend(headers or {})
    return resp

api.representations['application/xml'] = output_xml


parser = reqparse.RequestParser()
parser.add_argument('section_name', dest='section_name', location='form', type=str)
parser.add_argument('description', dest='description', location='form', type=str)

section_field = {
    'section_name': fields.String,
    'description': fields.String,
}

class Section(Resource):

    def get(self, id):
        s = Sections.query.get(id)
        if not s:
            abort(404)
        return marshal(s,section_field)

    def delete(self,id):
        s = Sections.query.get(id)
        if not s:
            abort(404)

        db.session.delete(s)
        db.session.commit()

        return '', 204

    @marshal_with(section_field)
    def put(self, id):
        args = parser.parse_args()
        s = Sections.query.get(id)
        if not s:
            abort(404)

        s.section_name = args['section_name']
        s.description = args['description']
        db.session.commit()

        return s, 201

class Sections_(Resource):
    @marshal_with(section_field)
    def get(seft):
        s = Sections.query.filter().all()
        return s

    @marshal_with(section_field)
    def post(self):
        args = parser.parse_args()
        #s = Sections(**args)
        section = Sections(args['section_name'], args['description'])
        db.session.add(section)
        db.session.commit()
        
        return  section


api.add_resource(Section, 'section/<int:id>')
api.add_resource(Sections_, 'sections')


@api_db.route('views_sections/')
def views_sections():
    sections = Sections.query.filter().all()
    return render_template("sections/view_sections.html", sections = sections)

@api_db.route('create_sections/', methods=['GET', 'POST', 'PUT'])
def create_section():
    form = CreateSectionForm(request.form)
    if form.validate_on_submit():
        section = Sections(form.section.data, form.description.data)
        db.session.add(section)
        db.session.commit()
        flash("sections created")
        return redirect("/sec/views_sections")
    return render_template("sections/create_sections.html",form = form)

'''
@mod_sec.route('/modify_sections/', methods=['GET','POST'])
def modify_sections():
    
    id_  = request.args.get('id',None)
    section = Sections.query.get(id_)

    form_edit = EditSectionForm(request.form)
    
    if form_edit.validate_on_submit():
        section.section_name = form_edit.section.data
        section.description =  form_edit.description.data
        db.session.commit()
        flash("Row edited")
        return redirect("/sec/views_sections")
    return render_template("sections/modify_sections.html",form = form_edit)

@mod_sec.route('/delete_sections/', methods=['GET'])
def delete_sections():
   
   id_  = request.args.get('id',None)
   section = Sections.query.get(id_)
   print section
   db.session.delete(section)
   db.session.commit()
   flash("Row Deleted")
   return redirect("/sec/views_sections")'''

