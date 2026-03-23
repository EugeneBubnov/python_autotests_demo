def test_crud_ops(auth_service, user):
    auth_service.reg(login=user.username, password=user.password)
