from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Chỉnh chuỗi kết nối PostgreSQL ở đây
# Ví dụ: postgresql://<user>:<password>@<host>:<port>/<database>
DATABASE_URL= "postgresql://postgres:123456@localhost:5432/postgres"

# Engine và session (synchronous SQLAlchemy)
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency cho FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
