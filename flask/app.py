from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route("/ivy", methods=['GET', 'POST'])
def ivy():
    return "hi ivy!"




@app.route("/template")
def template_test():


    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


# def main():
#     hello()
#     ivy()

if __name__ == "__main__":
    app.run(host= '0.0.0.0')