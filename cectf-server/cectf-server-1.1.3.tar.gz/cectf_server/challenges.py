from flask import Blueprint, jsonify, request
from flask_security.core import current_user
from flask_security.decorators import login_required, roles_required
from sqlalchemy.orm import aliased

from .database import db
from .models import Challenge, Solve

blueprint = Blueprint('challenges', __name__, url_prefix='/api/ctf')


@blueprint.route('/challenges')
@roles_required('contestant')
@login_required
def get_challenges():
    this_challenge = aliased(Challenge)
    previous_challenge = aliased(Challenge)
    previous_solves = aliased(Solve)
    solves = Solve.query\
        .join(Solve.challenge)\
        .filter(Solve.user_id == current_user.id)\
        .filter(Challenge.previous_challenge_id == None)\
        .union(Solve.query
               .join(this_challenge, Solve.challenge)
               .join(previous_challenge, this_challenge.previous_challenge_id == previous_challenge.id)
               .join(previous_solves, previous_challenge.solves)
               .filter(Solve.user_id == current_user.id)
               .filter(previous_solves.user_id == current_user.id)
               .filter(previous_solves.solved)
               )\
    .all()
    print("Unchained solves: ", [s.challenge_id for s in solves])

    print("All solves: " + str(solves))

    return jsonify([solve.challenge.serialize(solve) for solve in solves])


INCORRECT = 0
CORRECT = 1
ALREADY_SOLVED = 2


@blueprint.route('/challenges/<int:challenge_id>', methods=['GET', 'POST'])
@roles_required('contestant')
@login_required
def submit_flag(challenge_id):
    solve = Solve.query.filter_by(
        user_id=current_user.id, challenge_id=challenge_id).first()
    if (request.method == 'GET'):
        return jsonify(solve.challenge.serialize(solve))
    if solve.solved:
        return jsonify({'status': ALREADY_SOLVED})
    flag = request.get_json()['flag']
    print('Submitting flag %s', flag)
    if solve.challenge.solution == flag:
        solve.solved = True
        db.session.commit()
        return jsonify({'status': CORRECT, 'challenge': solve.challenge.serialize(solve)})
    else:
        print('it no match :(')
        return jsonify({'status': INCORRECT})


def init_app(app):
    app.register_blueprint(blueprint)
