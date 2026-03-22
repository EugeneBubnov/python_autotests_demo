def test_crud_ops(api_client):
    print(f"\nURL: {api_client.base_url}\nSession: {api_client.session}")
    api_client.get("/user/all")
