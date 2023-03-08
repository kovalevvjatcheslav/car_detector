from base64 import b64encode
import typing as t

import numpy as np
import cv2

from dto import StageDTO


class Pipeline:
    @staticmethod
    def to_np_array(buffer: bytes) -> np.ndarray:
        return np.frombuffer(buffer, np.uint8)

    @staticmethod
    def decode_img(data: np.ndarray) -> np.ndarray:
        return cv2.imdecode(data, cv2.IMREAD_UNCHANGED)

    @staticmethod
    def resize_img(data: np.ndarray, width: int = 640, height: int = 640) -> np.ndarray:
        return cv2.resize(data, (width, height))

    @staticmethod
    def normalize_img(
        data: np.ndarray, alpha: int = 0, beta: int = 255, norm_type: int = cv2.NORM_MINMAX
    ) -> np.ndarray:
        return cv2.normalize(src=data, dst=None, alpha=alpha, beta=beta, norm_type=norm_type)

    @staticmethod
    def to_base64(data: np.ndarray) -> str:
        return b64encode(data.tobytes()).decode()

    @classmethod
    def run(cls, data: bytes, stages: t.List[StageDTO]) -> t.Union[np.ndarray, str]:
        for stage in stages:
            data = getattr(cls, stage.meth_name)(data, *stage.args)
        return data
