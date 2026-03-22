def test_crud_ops(social_api_client):
    social_api_client.get("/user/all", headers={"Content-Type": "application/json"})
