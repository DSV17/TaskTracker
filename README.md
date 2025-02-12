# TaskTracker
Um projeto de CLI simples para gerenciar tarefas.


## Descrição
TaskTracker é uma cli para o gerenciamento de tarefas personalizadas, onde o usuário pode criar  editar
excluir tarefas marca como concluidos, dentre outras de uma forma direta.

Esse projeto é uma solução para o desafio proposto pelo [roadmap.sh](https://roadmap.sh/projects/task-tracker)


## Download
Para fazer o download podemos utilizar a ferramenta [git](https://git-scm.com/)
<br>
Com essa ferramenta instalada na sua máquina o download pode ser feito no diretório onde você quer que 
seja salvo o projeto fazendo:
``` git
git clone --depth 1 https://github.com/DSV17/TaskTracker.git
```


## Instalação
Para fazer a instalação desse projeto deve seguir so seguintes passos

### Criar e ativar o ambiente virtual (opcional)
Você pode criar um ambiente virtual para evitar conflito de versões. Para fazer isso primeiro execute
no diretório do projeto TaskTracker:

#### No Linux
``` bash
python -m venv venv
source venv/bin/activate
```

#### No Windows 
``` PowerShell
python -m venv venv
venv\Scripts\activate
```

### Instalar o projeto utilizando o pip
Agora basta instalar o projeto com o pip fazendo no diretório do projeto (mesmo diretorio do arquivo setup.py):
``` bash
pip install .
```


## Execução
Com isso já podemos usar a cli. Os comandos são:

### task-cli add
Para criar uma task usamos o comando add, fazendo por exempo:
``` bash
task-cli add "Buy groceries"
```

### task-cli update
Para atualizar uma task usamos o comando update, fazendo por exempo:
``` bash
task-cli update <ID> "Buy groceries and cook dinner"
```
Onde o ID é o id da task.


### task-cli delete
Para deletar uma task usamos o comando delete, fazendo por exempo:
``` bash
task-cli delete <ID>
```
Onde o ID é o id da task.


### task-cli mark-in-progress
Para Marcar uma task como em progresso usamos o comando mark-in-progress, fazendo por exempo:
``` bash
task-cli mark-in-progress <ID>
```
Onde o ID é o id da task.


### task-cli mark-done
Para Marcar uma task como em progresso usamos o comando mark-done, fazendo por exempo:
``` bash
task-cli mark-done <ID>
```
Onde o ID é o id da task.


### task-cli list
Para listar as tasks usamos o comando list, fazendo por exempo:
``` bash
task-cli list
```

### task-cli list done
Para listar as tasks concluidas usamos o comando adicional a list done, fazendo por exempo:
``` bash
task-cli list done
```


### task-cli list todo
Para listar as tasks a fazer usamos o comando adicional a list todo, fazendo por exempo:
``` bash
task-cli list todo
```


### task-cli list in-progress
Para listar as tasks em andamento usamos o comando adicional a list in-progress, fazendo por exempo:
``` bash
task-cli list in-progress
```


## Tecnologias
Para criar esse projeto foi utilizado a tecnologia:

1. [python](https://www.python.org/)