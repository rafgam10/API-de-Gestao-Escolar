from fastapi import APIRouter

Aluno_router = APIRouter(prefix="/alunos", tags=["alunos"], responses={404: {"description": "Not found"}})

@Aluno_router()
async def listar_todos_alunos():
    pass