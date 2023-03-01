from tgbotapp.models import TgUserIds


def save_tg_user_ids(id, name):
    user = TgUserIds(id=id, name=name)
    user.save()