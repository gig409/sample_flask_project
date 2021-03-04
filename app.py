from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

class TrainerForm(FlaskForm):
    trainer_name = StringField("What trainer do you want?")
    nike_boolean = BooleanField("Do you like Nike?")
    trainer_choice = RadioField("Choose your shoe:", choices=[('nike_id', 'Nike'),('adidas_id','Adidas')])
    submit = SubmitField("Submit")

class ChlothesForm(FlaskForm):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    trainer_name = False
    nike_boolean = False
    trainer_choice = False
    form = TrainerForm()
    if form.validate_on_submit():
        trainer_name = form.trainer_name.data
        nike_boolean = form.nike_boolean.data
        trainer_choice = form.trainer_choice.data
        # Calculate code result = Correct / Incorrect
    return render_template('index.html', form=form, trainer_name=trainer_name, nike_boolean=nike_boolean, trainer_choice=trainer_choice)

@app.route('/news')
def news():
    form = ChlothesForm()
    return render_template('news.html')

@app.route('/news/<num>')
def news_num(num):
    return render_template('newsnum.html', num=num)

if __name__ == '__main__':
    app.run(debug=True)
