from flask import render_template

def clients():
    return render_template('clients.html', name='yoyoyo')
