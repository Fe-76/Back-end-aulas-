from fastapi import APIRouter, HTTPException
from model import Tarefa, tarefa_model
from view import TarefaCreat, TarefaUpdate, TarefaResponse


router = APIRouter(prefix="/tarefas", tags= ["Tarefas"])

def _buscar_ou_404(tarefa_id: int) -> Tarefa:
    tarefa = tarefa_model.buscar_por_id(tarefa_id)
    if tarefa is none:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

@router.post("/", response_model=TarefaResponse, status_code=201)
def criar_tarefa(dados: TarefaCreat):
    tarefa = tarefa_model.criar(dados.titulo)
    return tarefa 

@router.get("/", response_model=list[TarefaResponse])
def listar_tarefas():
    return tarefa_model.listar_todas()

@router.get("/{tarefa_id}", response_model=TarefaResponse)
def buscar_tarefa(tarefa_id: int): 
    return _buscar_ou_404(tarefa_id)



