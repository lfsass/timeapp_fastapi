from datetime import datetime
import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/')
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return {"now": now}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')
