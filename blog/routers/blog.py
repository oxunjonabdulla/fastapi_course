from typing import List

from fastapi import APIRouter, status
from fastapi import Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..oauth2 import get_current_user
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)


@router.get('/', status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowBlog])
async def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all_blog(db)


@router.get('/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
async def show(id: int, db: Session = Depends(get_db)):
    return blog.show_blog(id, db)


@router.delete(path='/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: Session = Depends(get_db)):
    return blog.destroy_blog(id, db)


@router.put(path='/{id}/', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id, db, request)
