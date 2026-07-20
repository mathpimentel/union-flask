from models.task import Task

tasks = [
    Task(
        id=1,
        title="Estudar Flask",
        description="Aprender os conceitos básicos do Flask.",
        completed=False
    ),
    Task(
        id=2,
        title="Implementar API REST",
        description="Criar os endpoints GET, POST, PUT e DELETE.",
        completed=True
    ),
    Task(
        id=3,
        title="Documentar API",
        description="Gerar documentação utilizando Swagger/OpenAPI.",
        completed=False
    ),
    Task(
        id=4,
        title="Escrever testes",
        description="Criar testes unitários para os endpoints da API.",
        completed=False
    ),
    Task(
        id=5,
        title="Publicar projeto",
        description="Realizar o deploy da aplicação em um servidor.",
        completed=True
    )
]
