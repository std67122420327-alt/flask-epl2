from epl import app, db
from epl.models import Club, Players
from flask import render_template

@app.route('/')
def home():
    clubs = Club.query.all()
    return render_template('index.html', clubs=clubs)

@app.route('/club/<int:club_id>')
def club_detail(club_id):
    club = Club.query.get_or_404(club_id)
    players = Players.query.filter_by(club_id=club_id).all()
    return render_template('club_detail.html', club=club, players=players)