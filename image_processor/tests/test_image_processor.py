from unittest.mock import AsyncMock, Mock

import pytest
import image_processor


def get_mocked_client(return_value):
    class MockedClient:
        async def __aenter__(self):
            client = AsyncMock(**{"post.return_value": Mock(**{"json.return_value": return_value})})
            return client

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    return MockedClient


class TestUser:
    @pytest.mark.asyncio
    async def test_process_image(self, client, monkeypatch):
        with open("image_processor/tests/fixtures/test_image.jpg", "rb") as image:
            files = {"image": image}
            params = {"pipeline_id": 42}
            response = await client.post("/process_image", files=files, params=params)
            assert response.status_code == 404
            assert response.json() == {"detail": "Pipeline not found"}

            monkeypatch.setattr(
                image_processor.router.httpx,
                "AsyncClient",
                value=get_mocked_client({"conf": 0.33, "label": 0}),
            )
            params = {"pipeline_id": 1}
            response = await client.post("/process_image", files=files, params=params)
            assert response.status_code == 200
            assert response.json() == {"conf": 0.33, "label": 0}

    @pytest.mark.asyncio
    async def test_get_all_pipelines(self, client):
        response = await client.get("/pipelines")
        assert response.status_code == 200
        assert response.json() == [
            {
                "pipeline_id": 1,
                "stages": [
                    {"meth_name": "to_np_array", "args": []},
                    {"meth_name": "decode_img", "args": []},
                    {"meth_name": "resize_img", "args": []},
                    {"meth_name": "normalize_img", "args": []},
                    {"meth_name": "to_base64", "args": []},
                ],
            }
        ]
