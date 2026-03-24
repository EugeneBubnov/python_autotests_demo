def test_crud_ops(auth_service, user_service, user):
    auth_service.reg(login=user.username, password=user.password)
    user.token = (
        auth_service.token(login=user.username, password=user.password)
        .json()
        .get("token")
    )
    user_service.delete(user)
