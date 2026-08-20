from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from base62 import encode

app = FastAPI(title="URL Shortener MVP")

# Define the JSON format for the API will be recived
class URLRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return{"message": "Say hi to URL Shortner MVP!"}

@app.post("/shorten")
def create_short_url(request: URLRequest):
    # 1. Connect to the local db
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    try:
        # 2. Save the original url and get the id generate automatically
        cursor.execute("INSERT INTO urls (original_url) VALUES (?)", (request.url,))
        url_id = cursor.lastrowid

        # 3. Transform the id in a Base62 hash
        short_hash = encode(url_id)

        # 4. Refresh db, saving the hash with the original url
        cursor.execute("UPDATE urls SET short_hash = ? WHERE id = ?", (short_hash, url_id))
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error.")
    finally:
        # 5. Closes the connection to avoid locking the db
        conn.close()

    # 6. Send the response with the link ready for use
    return {
        "original_url": request.url,
        "short_url": f"http://127.0.0.1:8000/{short_hash}"
    }