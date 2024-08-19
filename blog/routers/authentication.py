from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import models
from blog.database import get_db
from blog.hashing import Hash
from blog.schemas import Token
from blog.token import create_access_token

router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or Invalid credentials"
        )
    if not Hash.verify(plain_password=request.password, hashed_password=user.password):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token, token_type="bearer")
