from database import init_db, get_connection


class TaskModel:
    @staticmethod
    def add_task(user_id, task_text):
        connection = get_connection()
        cursor = connection.execute(
            f'''
			INSERT INTO tasks (user_id, task_text) 
            VALUES ({user_id}, '{task_text}')			
			'''
        )
        connection.commit()
        connection.close()

    @staticmethod
    def get_tasks(user_id):
        connection = get_connection()
        cursor = connection.execute(
            f'''
			SELECT id, task_text, status 
            FROM tasks 
            WHERE user_id = {user_id}			
			'''
        )
        tasks = cursor.fetchall()
        connection.close()
        return tasks

    @staticmethod
    def delete_task(task_id):
        connection = get_connection()
        cursor = connection.execute(
            f'''
			DELETE FROM tasks 
            WHERE id = {task_id}			
			'''
        )
        connection.commit()
        connection.close()

    @staticmethod
    def update_task(task_id, new_text=None, new_status=None):
        connection = get_connection()
        if new_text:
            connection.execute(
                f'''
                UPDATE tasks 
                SET task_text = "{new_text}"
                WHERE id = {task_id}
                '''
            )
        if new_status:
            connection.execute(
                f'''
                UPDATE tasks 
                SET status = {new_status} 
                WHERE id = {task_id}
                '''
            )
        connection.commit()
        connection.close()
