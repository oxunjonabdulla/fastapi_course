from fastapi import APIRouter, status
from fastapi import Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post(path='/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.User)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)
