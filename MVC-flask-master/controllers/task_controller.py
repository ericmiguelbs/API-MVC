from flask import render_template, request, redirect, url_for
# Importa o db diretamente do seu arquivo principal ou de onde ele está
from models.task import db 
from models.task import Task
from models.user import User


class TaskController:
    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        # Corrige o nome da variável para 'tasks' para corresponder ao template HTML
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form.get('description')
            user_id = request.form['user_id']
            
            nova_tarefa = Task(
                title=title,
                description=description,
                user_id=user_id
            )
            db.session.add(nova_tarefa)
            db.session.commit()
            return redirect(url_for('list_tasks'))

        users = User.query.all()
        return render_template('create_task.html', users=users)
    
    @staticmethod
    def update_task_status(task_id):
        tarefa = Task.query.get(task_id)
        if tarefa:
            tarefa.status = 'Concluído' if tarefa.status == 'Pendente' else 'Pendente'
            db.session.commit()
        return redirect(url_for('list_tasks'))

    @staticmethod
    def delete_task(task_id):
        tarefa = Task.query.get(task_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
        return redirect(url_for('list_tasks'))
