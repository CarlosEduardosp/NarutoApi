from lerbanco import LerBanco, MontandoJson
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def select_all():
    data = LerBanco()
    response = MontandoJson(data)
    return {"return": True, "Todos_Personagens": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
