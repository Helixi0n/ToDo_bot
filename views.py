class View:
    @staticmethod
    def format_tasks(tasks):
        if not tasks:
            return "У вас нет задач."
        result = []
        for i in range(len(tasks)):
            status = "✅" if tasks[i][2] else "❎"
            result.append(f"{i+1}. {tasks[i][1]} ({tasks[i][0]}) {status}")
        return "\n".join(result)
