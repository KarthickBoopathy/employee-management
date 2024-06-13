from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, create_engine
from sqlalchemy.sql.ddl import CreateSchema
from yoyo import get_backend, read_migrations
import os

db = SQLAlchemy(engine_options={"pool_pre_ping" : True})
db_schema = "employee.db"
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_FILE = os.path.join(basedir, db_schema)
sqlite_db_url = 'sqlite:///' + DATABASE_FILE


engine = create_engine(sqlite_db_url)

# Create an inspector
inspector = inspect(engine)

# Get the names of all tables under a specific schema
schema_name = None  # None for default schema, or specify schema name if applicable
tables = inspector.get_table_names(schema=schema_name)

# Print the list of tables


def create_schema():
    if not inspect(db.engine).has_schema(basedir):
        with db.engine.begin() as connection:
            connection.execute(CreateSchema(db_schema))

def apply_db_migrations(db_uri):
    backend = get_backend(db_uri)
    migrations = read_migrations('./migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    db.session.commit()

def db_init(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # create_schema()
    print("Tables under schema {}: {}".format(schema_name or 'default', tables))
    apply_db_migrations(db_uri=sqlite_db_url)




