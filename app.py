from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField,EmailField,TextAreaField
from wtforms.validators import DataRequired

FAI=Flask(__name__)
class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()
    age=IntegerField()
    address=TextAreaField()
    email=EmailField()

@FAI.route('/webform',methods=['GET','POST'])
def webform():
    NFO=NameForm()
    if request.method=='POST':
        NFD=NameForm(request.form)
        if NFD.validate():
            return NFD.data
    return render_template('webforms.html',NFO=NFO)

if __name__=='__main__':
    FAI.run(debug=True)               