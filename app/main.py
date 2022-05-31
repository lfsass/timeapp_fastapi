from json.tool import main
import fastapi
import uvicorn
from datetime import datetime

app = fastapi.FastAPI()


@app.get('/')
def index():
    now = datetime.now()
    return {"now": now}

if __name__ == "__main__":
        uvicorn.run(app, port=8000, host='0.0.0.0')
