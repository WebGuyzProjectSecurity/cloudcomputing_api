from flask_wtf import Form
from wtforms import TextField, validators

class MessageForm(Form):
   message = TextField(u'Enter a sentence (Example: I feel bad/happy/neutral)', [validators.optional(), validators.length(max=200)])
