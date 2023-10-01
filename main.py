from lerbanco import LerBanco, MontandoJson
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substitua pelo domínio do seu aplicativo
    allow_credentials=True,
    allow_methods=["GET"],  # Você pode especificar métodos permitidos, como ["GET", "POST"]
    allow_headers=["Authorization"],  # Você pode especificar cabeçalhos permitidos, como ["Authorization"]
)


@app.get('/')
def select_all():
    data = LerBanco()
    response = MontandoJson(data)
    return {"return": True, "Todos_Personagens": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
