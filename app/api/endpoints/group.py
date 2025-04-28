from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.group import Group
from app.core.database import db

router = APIRouter()

@router.post("/groups", response_model=Group)
async def create_group(group: Group):
    """
    Endpoint to create a new group.
    """
    # Check if group with the same ID already exists
    existing_group = await db.groups.find_one({"groupId": group.groupId})
    if existing_group:
        raise HTTPException(status_code=400, detail="Group with this ID already exists")
    
    # Insert the new group into the database
    await db.groups.insert_one(group.dict())
    return group

@router.get("/users/{user_id}/groups", response_model=List[Group])
async def get_groups_by_user(user_id: str):
    """
    Endpoint to fetch all groups of a specific user.
    """
    # Find all groups where the user is a member
    print(db.groups.find())
    user_groups_cursor = db.groups.find({"userIds": user_id})
    user_groups = await user_groups_cursor.to_list(length=100)
    
    if not user_groups:
        raise HTTPException(status_code=404, detail="No groups found for this user")
    
    return user_groups