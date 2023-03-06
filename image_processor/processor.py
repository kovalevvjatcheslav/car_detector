import numpy as np
import cv2


def get_np_array(buffer: bytes) -> np.ndarray:
    return np.frombuffer(buffer, np.uint8)


def decode_img(data: np.ndarray) -> np.ndarray:
    return cv2.imdecode(data, cv2.IMREAD_UNCHANGED)


def resize_img(data: np.ndarray, width: int = 640, height: int = 640) -> np.ndarray:
    return cv2.resize(data, (width, height))


def normalize_img(
    data: np.ndarray, alpha: int = 0, beta: int = 255, norm_type: int = cv2.NORM_MINMAX
) -> np.ndarray:
    return cv2.normalize(src=data, dst=None, alpha=alpha, beta=beta, norm_type=norm_type)
