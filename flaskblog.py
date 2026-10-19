from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c59967376ecbf9ce6e5fce80a24bc4c0'

posts = [
    {
        'author' : 'Nischay K',
        'title' : 'Blog Post 1',
        'content' : 'First Blog Post Content',
        'date_posted' : 'April 20 ,2026'
    },
    {                                         
          'author' : 'Monish Krishnan',               
         'title' : 'Blog Post 2',              
          'content' : 'Second Blog Post Content',
          'date_posted' : 'April 25 ,2026'      
      }                                         
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html' , posts = posts)

@app.route('/about')                    
def about():                       
    return render_template('about.html' , title = 'About')

@app.route('/register' , methods = ['GET' , 'POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!!' , 'success')
        return redirect(url_for('home'))
    return render_template('register.html' , title = 'Register' , form = form)  

@app.route('/login' , methods = ['GET' , 'POST'])                                                       
def login():                                                               
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in ' , 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull! Please check your password and email' , 'danger')
    return render_template('login.html' , title = 'Login' , form = form)

if __name__ == '__main__':
    app.run(debug = True)