import logging
import time
from typing import Callable, ParamSpec, TypeVar

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")

COUNT = 3
WAIT_FOR = 1.0


def retry(f: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs):
    exc = None
    for i in range(COUNT):
        if exc:
            logger.warning(
                f"{f.__name__} failed. Retrying ({i}/{COUNT}). Exception: {exc}"
            )
            time.sleep(WAIT_FOR)
        try:
            return f(*args, **kwargs)
        except Exception as e:
            exc = e
    raise Exception("Retried 3 times but still failed") from exc


AN_ERROR_TO_CONFIRM_TYPECHECKING_IS_WORKING: int = "asdf"
