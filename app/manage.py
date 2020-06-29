from flask.cli import FlaskGroup

from app import app, db, Check

cli = FlaskGroup(app)

# @cli.command('create_db')
# def create_db():
# 	db.drop_all()
# 	db.create_all()
# 	db.session.commit()

@cli.command('init_db')
def init_db():
	res = db.engine.dialect.has_table(db.engine, 'checks')
	if not res:
		print('Creating {} table'.format('checks'))
		db.drop_all()
		db.create_all()
		db.session.commit()

@cli.command('seed_db')	
def seed_db():
	db.session.add(Check(url='https://yandex.ru/', status=200))
	db.session.commit()

if __name__ == '__main__':
	cli()