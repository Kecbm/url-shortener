from fastapi import FastAPI

app = FastAPI(title="URL Shortener MVP")

@app.get("/")
def read_root():
    return{"message": "Say hi to URL Shortner MVP!"}