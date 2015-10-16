from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for
)

from app import app, db
from app.sections.forms import CreateSectionForm
from app.sections.models import Sections


mod_sec = Blueprint('sec', __name__, url_prefix='/sec')


@mod_sec.route('/create_sections/', methods=['GET', 'POST'])
def create_section():
    form = CreateSectionForm(request.form)
    if form.validate_on_submit():
        section = Sections(form.section.data, form.description.data)
        db.session.add(section)
        db.session.commit()
        flash("sections created")
        return render_template("sections/create_sections.html",form = form)
    return render_template("sections/create_sections.html",form = form)

@mod_sec.route('/views_sections/')
def views_sections():
	sections = Sections.query.filter().all()
	return render_template("sections/view_sections.html", sections = sections)