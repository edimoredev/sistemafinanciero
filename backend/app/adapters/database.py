import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABAS_URL = 'postgresql+psycopg2:'
POSTGRES_URL = "localhost:5432"
POSTGRES_USER = "postgres"
POSTGRES_PW = "HVMG35TIONAR"
POSTGRES_DB = "financiera"

engine = _sql.create_engine('{database}//{user}:{pw}@{url}/{db}'.format(database=DATABAS_URL,
                                                                        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB), echo=False, pool_size=30, max_overflow=0)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()
