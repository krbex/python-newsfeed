from app.models import User
from app.db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
