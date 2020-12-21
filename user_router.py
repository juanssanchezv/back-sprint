from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

import user_db
import user_models
from db_connection import get_db


router = APIRouter()

@router.post(f"/user/auth/")
async def auth_user(user_in: user_models.UserIn, db: Session = Depends(get_db)):

    user_in_db = db.query(user_db.UserInDB).get(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return  {"Autenticado": True}


