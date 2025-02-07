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

def update_task(task_id, new_description):
    """Atualiza a descrição de uma tarefa existente."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarefa atualizada: {new_description} (ID: {task_id})")
            return

    print(f"Tarefa com ID {task_id} não encontrada.")

def delete_task(task_id):
    """Remove uma tarefa da lista."""
    tasks = load_tasks()

    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) < len(tasks):
        save_tasks(updated_tasks)
        print(f"Tarefa removida (ID: {task_id}).")
    else:
        print(f"Tarefa com ID {task_id} não encontrada.")

def mark_task_status(task_id, new_status):
    """Atualiza o status de uma tarefa."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Status da tarefa atualizado: {new_status} (ID: {task_id})")
            return

    print(f"Tarefa com ID {task_id} não encontrada.")

def list_tasks(status=None):
    """Lista todas as tarefas ou filtra por status."""
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print(f"Nenhuma tarefa encontrada{' com status ' + status if status else ''}.")
        return

    print(f"Tarefas{' com status ' + status if status else ''}:")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Descrição: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Criada em: {task['createdAt']}")
        print(f"Atualizada em: {task['updatedAt']}")
        print("-" * 30)

def main():
    parser = argparse.ArgumentParser(description="CLI para gerenciamento de tarefas.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    add_parser = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_parser.add_argument("description", type=str, help="Descrição da tarefa")

    update_parser = subparsers.add_parser("update", help="Atualiza uma tarefa existente")
    update_parser.add_argument("task_id", type=str, help="ID da tarefa a ser atualizada")
    update_parser.add_argument("new_description", type=str, help="Nova descrição da tarefa")

    delete_parser = subparsers.add_parser("delete", help="Remove uma tarefa existente")
    delete_parser.add_argument("task_id", type=str, help="ID da tarefa a ser removida")

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Marca uma tarefa como 'in-progress'"
    )
    mark_in_progress_parser.add_argument("task_id", type=str, help="ID da tarefa a ser atualizada")

    mark_done_parser = subparsers.add_parser(
        "mark-done", help="Marca uma tarefa como 'done'"
    )
    mark_done_parser.add_argument("task_id", type=str, help="ID da tarefa a ser atualizada")

    list_parser = subparsers.add_parser("list", help="Lista todas as tarefas ou filtra por status")
    list_parser.add_argument("status", nargs="?", type=str, help="Status das tarefas a serem listadas")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.new_description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "mark-in-progress":
        mark_task_status(args.task_id, "in-progress")
    elif args.command == "mark-done":
        mark_task_status(args.task_id, "done")
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()