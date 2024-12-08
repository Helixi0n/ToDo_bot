from database import init_db, get_connection

class TaskModel:
    @staticmethod
    def add_task(user_id, task_text):
        connection = get_connection()
        cursor = connection.execute(
            f'''
            INSERT INTO tasks (User_ID, Task_Text)
            VALUES({user_id}, {task_text})
            '''
        )
        connection.commit()
        connection.close()

    @staticmethod
    def get_tasks(user_id):
        connection = get_connection()
        cursor = connection.execute(
            f'''
            SELECT ID, Task_Text, Status 
            FROM tasks
            WHERE User_ID = {user_id}
            '''
        )
        connection.commit()
        connection.close()

    @staticmethod
    def delete_task(id):
        connection = get_connection()
        cursor = connection.execute(
            f'''
            DELETE FROM tasks
            WHERE ID = {id}
            '''
        )

        connection.commit()
        connection.close()

    @staticmethod
    def update_task(id, new_text=None, new_status=None):
        connection = get_connection()
        if new_text:
            connection.execute(
                f'''
                UPDATE tasks 
                SET Task_Text = {new_text}
                WHERE ID = {id}
                '''
            )

        if new_status:
            connection.execute(
                f'''
                UPDATE tasks 
                SET Status = {new_status}
                WHERE ID = {id}
                '''
            )
        
        connection.commit()
        connection.close()