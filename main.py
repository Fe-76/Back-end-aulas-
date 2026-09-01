from fastapi import FastAPI
from controller import router as tarefas_router


app = FastAPI(tittle="Exemplo de MVC")


app.include_router(tarefas_router)

@app.get("/")
def raiz():
 return {"mensagem": "API RODANDO"}

