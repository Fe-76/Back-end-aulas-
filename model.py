from typing import Optional

class Tarefa: 
    def __init__(self, id: int, titulo: str, concluida: bool = False):
        self.id = id
        self.titulo = titulo
        self.concluida = concluida

def concluir(self):
    if self.concluida:
            raise ValueError("Essa tarefa ja esta concluida")
    self.concluida = True

def renomear(self, novo_titulo: str):
    if not novo_titulo.strip():
        raise ValueError("O titulo nao pode ser vazio")
    self.titulo = novo_titulo

class TarefaModel:
    def __init__(self):
        self._tarefas: dict[int, Tarefa] = {}
        self._proximo_id = 1

    def criar(self, titulo: str) -> Tarefa:
        tarefa = Tarefa(id=self._proximo_id, titulo=titulo)
        self._tarefas[tarefa.id] = tarefa
        self._proximo_id += 1
        return tarefa

    def buscar_por_id(self, tarefa_id: int) -> Optional[tarefa]:
        return self._tarefas.get(tarefa_id)

    def listar_todas(self) -> list[Tarefas]:
        return list(self._tarefas.values())

    def remover(self,tarefa_id: int) -> bool:
        if tarefa_id in self._tarefas:
            del self._tarefas[tarefa_id]
            return True 
        return False 

tarefa_model = TarefaModel()


