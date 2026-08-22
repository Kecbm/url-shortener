from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import sqlite3
from base62 import encode

app = FastAPI(title="URL Shortener MVP")

# Define the JSON format for the API will be recived
class URLRequest(BaseModel):
    # url: str
    url: HttpUrl

@app.get("/")
def read_root():
    return{"message": "Say hi to URL Shortner MVP!"}

@app.post("/shorten")
def create_short_url(request: URLRequest):
    target_url = str(request.url)
    # Connect to the local db
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    try:
        # Verification: the url alredy exists?
        cursor.execute("SELECT short_hash FROM urls WHERE original_url = ?", (target_url,))
        existing_hash = cursor.fetchone()

        if existing_hash:
            # Return the saved link
            return {
                "original_url": target_url,
                "short_url": f"http://127.0.0.1:8000/{existing_hash[0]}"
            }

        # If thr url is new, save the original url and get the id generate automatically
        cursor.execute("INSERT INTO urls (original_url) VALUES (?)", (target_url,))
        url_id = cursor.lastrowid

        # Transform the id in a Base62 hash
        short_hash = encode(url_id)

        # Refresh db, saving the hash with the original url
        cursor.execute("UPDATE urls SET short_hash = ? WHERE id = ?", (short_hash, url_id))
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error: {e}")
    finally:
        # Closes the connection to avoid locking the db
        conn.close()

    # Send the response with the link ready for use
    return {
        "original_url": request.url,
        "short_url": f"http://127.0.0.1:8000/{short_hash}"
    }

@app.get("/{short_hash}")
def redirect_to_original(short_hash: str):
    # 1. Connect to db
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    try:
        # 2. Search the original url of have this hash
        cursor.execute("SELECT original_url FROM urls WHERE short_hash = ?", (short_hash))
        result = cursor.fetchone()

        # 3. If not find anything, return error 404 (not found)
        if result is None:
            raise HTTPException(status_code=404, detail="URL not found.")

        # 4. Get the url of the result
        original_url = result[0]

        # 5. Make the redirect (status 302: found/temporary redirect)
        return RedirectResponse(url=original_url, status_code=302)

    except HTTPException:
        # Show the error 404 to the user
        raise
    except Exception as e:
        print("Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
    finally:
        conn.close()