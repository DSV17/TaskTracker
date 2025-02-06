#!./venv/bin/python3

import argparse
import os
import json
from datetime import datetime
from uuid import uuid4

TASKS_FILE = "tasks.json"

def load_tasks():
    """Carrega as tarefas do arquivo JSON. Se o arquivo não existir, retorna uma lista vazia."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Adiciona uma nova tarefa à lista."""
    tasks = load_tasks()

    new_task = {
        "id": str(uuid4()),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    tasks.append(new_task)

    save_tasks(tasks)
    print(f"Tarefa adicionada: {new_task['description']} (ID: {new_task['id']})")

def main():
    parser = argparse.ArgumentParser(description="CLI para gerenciamento de tarefas.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    add_parser = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_parser.add_argument("description", type=str, help="Descrição da tarefa")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()