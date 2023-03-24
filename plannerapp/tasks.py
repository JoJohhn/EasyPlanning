from huey import crontab
from huey.contrib.djhuey import task, db_periodic_task, HUEY as huey
from plannerapp.models import Task
from users.models import MyUser
from tgbotapp.management.commands.bot import bot


@task()
def telegram_notification(chatId, my_message):
    bot.send_message(chatId, my_message)



# @periodic_task(crontab(minute='*/1'))
# def every_five_mins():
#     print('Every five minutes this will be printed by the consumer')


@db_periodic_task(crontab(minute='*/1'))
def reading_db():
    tasks_QuerySet = Task.objects.values_list('id', 'taskStartTime', 'userId', 'taskName')
    print(tasks_QuerySet)

    idtasksold = huey.get('test2')
    print(f'Список задач был: {idtasksold}')
    idtasks = list(list(zip(*tasks_QuerySet))[0])
    print(f'Список задач стал: {idtasks}')
    huey.put('test2', idtasks)

    if idtasksold == None:
        idtasksold = []
    task_QuerySet_new = [i for i in tasks_QuerySet if i[0] not in idtasksold]
    print(f'Эти задачи будут запланированы: {task_QuerySet_new}')


    for i in task_QuerySet_new:
        chatId = MyUser.objects.filter(user_id=i[2]).values_list('tgUser')[0][0]
        telegram_notification.schedule((chatId, f'Пора выполнять задачу: {i[3]}'),eta=i[1])
