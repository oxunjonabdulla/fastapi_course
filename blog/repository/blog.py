from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from blog import models, schemas


def get_all_blog(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body,
                           user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"blog": new_blog, "status": status.HTTP_201_CREATED}


def destroy_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog and models.Blog.id.isalpha():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"THIS ID WITH BLOG IS NOT AVAILABLE")
    else:
        db.delete(blog)
        db.commit()
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"{blog.title} - successfully deleted")


def update_blog(id, db: Session, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return {"blog": blog, "status": status.HTTP_202_ACCEPTED}
