from flask import render_template, url_for, redirect, jsonify
from . import home
from . forms import ContactMessageForm
from .. models import Message
from .. import db

@home.route('/')
def index():

    contact_form = ContactMessageForm()

    return render_template('home/index.html', contact_form=contact_form)

@home.route("/send/message", methods=["POST"])
def send_message():
    data = {}
    contact_form = ContactMessageForm()
    if contact_form.validate_on_submit():
        message = Message(contact_form.first_name.data, contact_form.last_name.data,
                         contact_form.email.data, contact_form.phone_number.data,
                         contact_form.message.data)
        db.session.add(message)
        db.session.commit()
        data['first_name'] = contact_form.first_name.data
        data['last_name'] = contact_form.last_name.data
        data['email'] = contact_form.email.data
        data['phone_number'] = contact_form.phone_number.data
        data["message"] = contact_form.message.data
        return jsonify(data)
    data['errors'] = contact_form.errors
    return jsonify(data)
