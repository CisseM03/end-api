from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import crud
import models
import schemas
import auth
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/america", response_model=schemas.America)
def create_americaname_for_user(owner: schemas.AmericaCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=owner.owner_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User does not exist")
    db_user = crud.get_america_by_ownerid(db, ownerid=owner.owner_id)
    if db_user:
        raise HTTPException(status_code=400, detail="This user already has a american name.")
    return crud.create_america(db=db, owner=owner)


@app.get("/america", response_model=list[schemas.America])
def read_americanames(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    names = crud.get_america(db, skip=skip, limit=limit)
    return names


@app.post("/japan", response_model=schemas.Japan)
def create_japanname_for_user(owner: schemas.JapanCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=owner.owner_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User does not exist")
    db_user = crud.get_japan_by_ownerid(db, ownerid=owner.owner_id)
    if db_user:
        raise HTTPException(status_code=400, detail="This user already has a japanese name.")
    return crud.create_japan(db=db, owner=owner)


@app.get("/japan", response_model=list[schemas.Japan])
def read_japannames(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    names = crud.get_japan(db, skip=skip, limit=limit)
    return names


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


@app.put("/users/{username}", response_model=schemas.User)
def edit_user(username: str, user: schemas.UserEdit, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #Controleer of er een order op dit id staat
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=400, detail="There is no User registered")
    db_user = crud.edit_username(db, user, username=username)
    return db_user

@app.delete("/users/{username}", response_model=schemas.User)
def delete_user(username: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #Controleer of er een order op dit id staat
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=400, detail="There is no User registered")
    users = crud.delete_user(db, username=username)
    if not users:
        raise HTTPException(status_code=400, detail="User is deleted")
    return users