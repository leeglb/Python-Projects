from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .model import models
from .database import engine 


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True 
    rating: Optional[int] = None

my_posts = [{"title": "Best areas in Australia", "content": "Robina", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
while True: 
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user='postgres', password='Bladehunter09',
                                cursor_factory=RealDictCursor)

        cursor = conn.cursor()

        print("Database connection was succesful")
        break

    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)
#adding a /with text behind is the url destination 

@app.get("/posts")
async def root():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)

    return {"this is your post": posts}


#get sends a request to the api which receives data

#post sends data and requests to the api to receive data

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(posts: Post):
    
    cursor.execute("""INSERT INTO posts (title, content, published)
                    VALUES (%s, %s, %s) RETURNING * """, (posts.title, posts.content, posts.published))

    new_post = cursor.fetchone()

    conn.commit()

    return {"this is new post": new_post}


#CRUD

"""
Create -> Post -> /posts -> @app.post("/post")
Read -> Get  -> /posts/:id or /posts -> @app.post("/posts/{id}")
Update -> Put/Patch -> /posts/:id -> @app.put("/posts/{id}")
Delete -> Delete -> /posts/:id -> @app.delete("/posts/{id}")
"""


@app.get("/posts/{id}") #path parameter 
def get_post(id: int, response: Response):

    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))

    received_post = cursor.fetchone()

    if not received_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} was not found")
    return {"this is your posts": received_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))

    received_post = cursor.fetchone()

    conn.commit()

    if received_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} does not exist")


    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute("""UPDATE posts SET id = %s, title = %s, content = %s, published = %s RETURNING * """, (post.title, post.content, post.published, (str(id))))

    updated_post = cursor.fetchone()

    conn.commit() 

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} does not exist")
    
    return {"data": updated_post}