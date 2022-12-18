from flask import Flask, render_template

app = Flask(__name__)


Posts = [
    {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
    {
        'creator':'jaushik',
        'title':'monday',
        'content':'clowday',
        'date_posted':'june 26,1990'
        },
    {
        'creator':'haushik',
        'title':'monday',
        'content':'clowday',
        'date_posted':'june 26,1990'
        },
    {
        'creator':'gaushik',
        'title':'monday',
        'content':'clowday',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        },
         {
        'creator':'kaushik',
        'title':'monday',
        'content':'The 2014 FIFA World Cup Final was the final match of the 2014 World Cup. The match between Germany and Argentina was played at the Maracanã Stadium in Rio de Janeiro, Brazil, on 13 July 2014',
        'date_posted':'june 26,1990'
        }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=Posts)

 
@app.route("/about")
def about():

    return render_template('about.html')





    if __name__ == '__main__':
        app.run(debug=True)