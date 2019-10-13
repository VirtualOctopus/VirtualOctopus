from typing import List, Callable
from tentacles.base.base_processor import BaseTargetProcessor
from contents.base_content import BaseContent


class BaseTargetDispatcher(object):

    def register_target_processor(
            self, accept: Callable, process_target: BaseTargetProcessor):
        raise NotImplementedError

    def get_processors(self,
                       content: BaseContent) -> List[BaseTargetProcessor]:
        raise NotImplementedError
