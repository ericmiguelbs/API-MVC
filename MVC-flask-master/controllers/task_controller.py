from flask import render_template, request, redirect, url_for
from models.task import tasks, db
from models.user import User


class TaskController:
    @staticmethod
    def list_tasks():
        tarefas = tasks.query.all()
        return render_template('tasks.html', tarefas=tarefas)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form['tittle']
            description = request.form.get('description')
            user_id = request.form['user_id']
            
            nova_tarefa = tasks(
                title=title,
                description=description,
                user_id=user_id
            )
            db.session.add(nova_tarefa)
            db.session.commit()
            return redirect(url_for('listar_tarefas'))

        usuarios = User.query.all()
        return render_template('create_task.html', usuarios=usuarios)
    
    @staticmethod
    def update_task_status(task_id):
        tarefa = tasks.query.get(task_id)
        if tarefa:
            tarefa.status = 'Concluído' if tarefa.status == 'Pendente' else 'Pendente'
            db.session.commit()
        return redirect(url_for('listar_tarefas'))

    @staticmethod
    def delete_task(task_id):
        tarefa = tasks.query.get(task_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
        return redirect(url_for('listar_tarefas'))


