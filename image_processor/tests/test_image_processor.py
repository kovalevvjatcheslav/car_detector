import pytest


class TestUser:
    @pytest.mark.asyncio
    async def test_process_image(self, client):
        with open("fixtures/test_image.jpg", "rb") as image:
            files = {"image": image}
            params = {"pipeline_id": 42}
            response = await client.post("/process_image", files=files, params=params)
            print("-" * 100)
            print(response.status_code)
            print(response.text)
            print("-" * 100)
