from __future__ import annotations

import uuid

from typing import Dict

from CNB_application.core import cache
from CNB_application.core import config
from CNB_application.core import storage
from CNB_application.exceptions import UserNotFound
from CNB_application.models.social.user import User
from peewee import DoesNotExist


def get_all(search: str = '') -> list[User]:
    users = []
    if search is None or search == '':
        query = User.select()
    else:
        query = User.select().where(
            (User.first_name.contains(search)) | (
                User.last_name.contains(search)),
        )

    for user in query:
        profile, account_activated, first_login = user.get_data()
        users.append(
            {
                'profile': profile,
                'account_activated': account_activated,
                'first_login': first_login,
            },
        )

    return users


def get(user_id: str) -> User:
    try:
        user = User.get(User.id == user_id)
        return user
    except DoesNotExist:
        raise UserNotFound


def get_by_mail(mail: str) -> User:
    try:
        user = User.get(User.email == mail)
        return user
    except DoesNotExist:
        raise UserNotFound


def update_personal_info(user_id, field, info):
    user = get(user_id)
    setattr(user, field, info)
    user.save()
    return user.get_data()


def delete_user(user_id: str) -> bool:
    try:
        user = User.get(User.id == user_id)
        user.delete_instance(recursive=True)
        cache.set(f'user_{user_id}_valid', 'false')
        return True
    except DoesNotExist:
        raise UserNotFound


def update_profile_picture(user_id: str, profile_picture: str) -> Dict:
    user = get(user_id)
    if 'filepath' in user.picture:
        former_file_path = user.picture.split('=')[1]
        storage.delete_object(Key=former_file_path, Bucket='template-storage')
    new_picture_id = uuid.uuid4().hex
    file_path = f'profile-pictures/{new_picture_id}'
    storage.upload_fileobj(profile_picture, 'template-storage', file_path)
    user.picture = '{}/storage/download?filepath={}'.format(
        config['back_root_url'],
        file_path,
    )
    user.save()
    profile, account_activated, first_login = user.get_data()

    return {
        'profile': profile,
        'account_activated': account_activated,
        'first_login': first_login,
    }
