from flask import Flask, render_template
import database.basing as engineer
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pr.db'

@app.route("/")
def hello_world():
    cur_time = time.time_ns() // 1e14
    l_upd_time = int(open("kfg.txt").readline())//1e14
    if cur_time > l_upd_time:
        engineer.update()
        open("kfg.txt", "w+").write(str(time.time_ns()))
    return render_template("home.html")

@app.route("/res")
def result():
    you = engineer.ask()
    return render_template("result.html",
                           img_src = you[-1],
                           krep = str(you[1]),
                           krep_des = engineer.descryption(you))


if __name__ == "__main__":
    app.run(debug=False)