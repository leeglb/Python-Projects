from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
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

@app.get("/posts/latest") #structure the paths in order -> so you dont match another request
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}") #path parameter 
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post {id} was not found")
    return {"this is your post": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = find_index_post(id)

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} does not exist")
    my_posts.pop(post)



    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": post_dict}