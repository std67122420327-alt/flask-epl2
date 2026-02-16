from flask import Blueprint, render_template, redirect, url_for, request, flash
from epl.extension import db
from epl.models import Club, Player

players_bp = Blueprint('players', __name__, template_folder='templates')

@players_bp.route('/')
def index():
  query = db.select(Player)
  players = db.session.scalars(query).all()
  return render_template('players/index.html',
                         title='Players Page',
                         players=players)

@players_bp.route('/new', methods=['GET', 'POST'])
def new_player():
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    nationality = request.form['nationality']
    img = request.form['img']
    goal = int(request.form.get('goal', 0))
    squad_no = request.form.get('squad_no')
    clean_sheet = int(request.form.get('clean_sheet', 0)) if position == 'Goalkeeper' else 0
    club_id = int(request.form['club_id'])
    
    player = Player(name=name, position=position, nationality=nationality, 
                    img=img, goal=goal, squad_no=squad_no, clean_sheet=clean_sheet, club_id=club_id)
    db.session.add(player)
    db.session.commit()
    
    flash('add new player successfully', 'success')
    return redirect(url_for('players.index'))
  
  query = db.select(Club)
  clubs = db.session.scalars(query).all()
  return render_template('players/new_player.html',
                         title='New Player Page',
                         clubs=clubs)

@players_bp.route('/search', methods=['GET', 'POST'])
def search_player():
  if request.method == 'POST':
    player_name = request.form['player_name']
    query = db.select(Player).where(Player.name.like(f'%{player_name}%'))
    players = db.session.scalars(query).all()

    return render_template('players/search_player.html',
                           title='Search Player Page',
                           players=players)

@players_bp.route('/<int:id>/info')
def info_player(id):
  player = db.session.get(Player, id)
  return render_template('players/info_player.html',
                         title='Info Player Page',
                         player=player)

@players_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update_player(id):
  player = db.session.get(Player, id)
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    nationality = request.form['nationality']
    img = request.form['img']
    goal = int(request.form.get('goal', 0))
    squad_no = request.form.get('squad_no')
    clean_sheet = int(request.form.get('clean_sheet', 0)) if position == 'Goalkeeper' else 0
    club_id = int(request.form['club_id'])

    player.name = name
    player.position = position
    player.nationality = nationality
    player.img = img
    player.goal = goal
    player.squad_no = squad_no
    player.clean_sheet = clean_sheet
    player.club_id = club_id

    db.session.add(player)
    db.session.commit()

    flash('update player successfully', 'success')
    return redirect(url_for('players.index'))
  
  query = db.select(Club)
  clubs = db.session.scalars(query).all()
  return render_template('players/update_player.html',
                         title='Update Player Page',
                         player=player,
                         clubs=clubs)