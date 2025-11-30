def build_user_profile(user_id:int,**kwargs)->dict:
    """Создает профиль пользователя с ID и дополнительными данными."""
    return{'user_id':user_id,**kwargs}