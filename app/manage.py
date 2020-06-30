from flask.cli import FlaskGroup

from app import app, db, Check

cli = FlaskGroup(app)

@cli.command('init_db')
def init_db():
	tablename = Check.__tablename__
	res = db.engine.dialect.has_table(db.engine, tablename)
	if not res:
		print('Creating {} table'.format(tablename))
		db.drop_all()
		db.create_all()
		db.session.commit()


if __name__ == '__main__':
	cli()