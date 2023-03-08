import random

import pytest


class TestUser:
    @pytest.mark.asyncio
    async def test_detect(self, client, monkeypatch):
        monkeypatch.setattr(random, "random", value=lambda: 0.33)
        request_data = {"pipeline_id": 1, "data": "test"}
        response = await client.post("/detect", json=request_data)
        assert response.status_code == 200, response.json()
        assert response.json() == {"conf": 0.33, "label": 0}

        monkeypatch.setattr(random, "random", value=lambda: 0.55)
        response = await client.post("/detect", json=request_data)
        assert response.status_code == 200
        assert response.json() == {
            "top_left_x": 42,
            "top_left_y": 42,
            "w": 100500,
            "h": 100500,
            "conf": 0.55,
            "label": 1,
        }
