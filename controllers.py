from telebot import types
from models import TaskModel
from views import View


class Controller:
    def __init__(self, bot):
        self.bot = bot

    def register_handlers(self):
        @self.bot.message_handler(commands=["start", "help"])
        def send_welcome(message):
            self.bot.reply_to(
                message,
                "Добро пожаловать в Todo-бот! Используйте команды \n/add \n/list \n/delete \n/update",
            )

        @self.bot.message_handler(commands=["add"])
        def add_task(message):
            msg = self.bot.reply_to(message, "Введите текст задачи:")
            self.bot.register_next_step_handler(
                msg, lambda m: self._add_task_handler(m, message.from_user.id)
            )

        @self.bot.message_handler(commands=["list"])
        def list_tasks(message):
            tasks = TaskModel.get_tasks(message.from_user.id)
            self.bot.reply_to(message, View.format_tasks(tasks))

        @self.bot.message_handler(commands=["delete"])
        def delete_task(message):
            msg = self.bot.reply_to(message, "Введите ID задачи для удаления:")
            self.bot.register_next_step_handler(
                msg, lambda m: self._delete_task_handler(m, message.from_user.id)
            )

        @self.bot.message_handler(commands=["update"])
        def update_task(message):
            msg = self.bot.reply_to(message, "Введите ID задачи для обновления:")
            self.bot.register_next_step_handler(
                msg, lambda m: self._update_task_handler(m, message.from_user.id)
            )

    def _add_task_handler(self, message, user_id):
        TaskModel.add_task(user_id, message.text)
        self.bot.reply_to(message, "Задача добавлена!")

    def _delete_task_handler(self, message, user_id):
        try:
            TaskModel.delete_task(int(message.text))
            self.bot.reply_to(message, "Задача удалена!")
        except ValueError:
            self.bot.reply_to(message, "ID задачи должен быть числом.")

    def _update_task_handler(self, message, user_id):
        try:
            task_id = int(message.text)
            msg = self.bot.reply_to(
                message, "Введите новый текст или статус (true/false):"
            )
            self.bot.register_next_step_handler(
                msg, lambda m: self._finalize_update_handler(m, task_id)
            )
        except ValueError:
            self.bot.reply_to(message, "ID задачи должен быть числом.")

    def _finalize_update_handler(self, message, task_id):
        if message.text.lower() in ["true", "false"]:
            new_status = message.text.lower() == "true"
            TaskModel.update_task(task_id, new_status=new_status)
            self.bot.reply_to(message, "Статус задачи обновлен!")
        else:
            TaskModel.update_task(task_id, new_text=message.text)
            self.bot.reply_to(message, "Текст задачи обновлен!")
