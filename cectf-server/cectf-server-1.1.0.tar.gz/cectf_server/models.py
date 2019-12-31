from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

from .database import db


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description
        }


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), unique=True)  # , nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer())
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        'Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    solves = db.relationship('Solve', cascade='save-update, merge, delete')
    challenges = db.relationship(
        'Challenge', secondary='solve', backref=db.backref('users', lazy='dynamic'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'roles': [role.serialize for role in self.roles]
        }


class Challenge(db.Model):
    __tablename__ = 'challenge'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Text(), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    solution = db.Column(db.String(255), nullable=False)
    previous_challenge = db.relationship('Challenge')
    previous_challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=True)
    solves = db.relationship(
        'Solve', cascade='save-update, merge, delete')

    def serialize(self, solve):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'author': self.author,
            'body': self.body,
            'solved': solve.solved
        }
    
    def serialize_admin(self):
        _dict = {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'author': self.author,
            'body': self.body,
            'solution': self.solution
        }
        if self.previous_challenge_id:
            _dict['previousChallenge'] = self.previous_challenge_id
        return _dict



class Solve(db.Model):
    __tablename__ = 'solve'
    __mapper_args__ = {
        # TODO find a way to get rid of this
        'confirm_deleted_rows': False
    }
    id = db.Column(db.Integer(), primary_key=True)
    solved = db.Column(db.Boolean(), nullable=False)
    user_id = db.Column(
        'user_id', db.Integer(), db.ForeignKey('user.id'))
    user = db.relationship('User')
    challenge_id = db.Column(
        'challenge_id', db.Integer(), db.ForeignKey('challenge.id'))
    challenge = db.relationship('Challenge')


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
