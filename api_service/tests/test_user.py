import pytest


class TestUser:
    @pytest.mark.asyncio
    async def test_sign_up(self, client):
        data = {
            "name": "test_name",
            "password": "test_password",
            "email": "user@example.com"
        }
        response = await client.post("/")
        print(response.status_code)
        print(response.json())
