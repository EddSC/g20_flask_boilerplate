from app import app, db
from app.routers import roles_router
from app.models import BaseModel


BaseModel.set_session(db.session)
