from app import db
from app.models import Admin

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table')
        session.execute(table.delete())
    session.commit()

def create_admin(user_name, password):
	admin = Admin(username=user_name)
	admin.set_password(password)
	admin.get_token()
	db.session.add(admin)
	db.session.commit()
	print(admin)

def reset_database(user_name, password):
	clear_data(db.session)
	create_admin(user_name, password)
