from fastapi import APIRouter, Depends, HTTPException
from OSUCS461.Models import UserCreate, UserPostCreate, User, UserPost
from OSUCS461.Classes.Database import create_user, create_user_post, get_user, get_user_posts

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate):
    create_user(user)
    return user

@router.post("/users/{user_uuid}/posts/", response_model=UserPost)
def create_user_post_endpoint(user_uuid: str, user_post: UserPostCreate):
    if user_uuid != user_post.user_uuid:
        raise HTTPException(status_code=400, detail="User UUID mismatch")
    create_user_post(user_post)
    return user_post

@router.get("/users/{user_uuid}", response_model=User)
def read_user_endpoint(user_uuid: str):
    user = get_user(user_uuid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/{user_uuid}/posts/", response_model=list[UserPost])
def read_user_posts_endpoint(user_uuid: str):
    return get_user_posts(user_uuid)
