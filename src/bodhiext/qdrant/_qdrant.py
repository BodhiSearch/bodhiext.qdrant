"""Bodhilib plugin for Qdrant Vector DB LLM Service module."""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from bodhilib import BaseLLM, Prompt, PromptStream, Service, prompt_output, service_provider
from bodhilib.logging import logger

from ._version import __version__


class Qdrant(BaseLLM):
    """Bodhilib plugin for Qdrant Vector DB LLM Service implementation."""

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs: Dict[str, Any]) -> None:
        """Initialize the LLM service.

        Args:
            model: model name to use for the LLM service
            api_key: API key to use for the LLM service
            kwargs: additional configs to pass to the LLM service
        """
        self.model = model
        self.api_key = api_key
        self.kwargs = kwargs

    def _generate(
        self,
        prompts: List[Prompt],
        *,
        stream: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        n: Optional[int] = None,
        stop: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        user: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> Union[Prompt, PromptStream]:
        """Generate a response to the given prompt.

        Args:
            prompts: input prompt(s) to LLM to generate a reply
            kwargs: additional configs to pass to the LLM
        Returns:
            Prompt: generated response from the LLM service
        """
        single_prompt = "\n".join([p.text for p in prompts])
        logger.info(f"Received prompt: {single_prompt}")
        return prompt_output("The Answer to the Great Question Of Life, the Universe and Everything Is Forty-two")


@service_provider
def bodhilib_list_services() -> List[Service]:
    """List all services provided by this plugin for bodhilib to register.

    Returns:
        List[:class:`~bodhilib.Service`]: list of services provided by this plugin
    """
    return [
        Service(
            service_name="qdrant",
            service_type="llm",
            publisher="bodhisearch",
            service_builder=bodhiext_qdrant_llm_service_builder,
            version=__version__,
        )
    ]


def bodhiext_qdrant_llm_service_builder(
    *,
    service_name: Optional[str] = None,
    service_type: Optional[str] = "llm",
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    **kwargs: Dict[str, Any],
) -> Qdrant:
    """LLM service builder for Bodhilib plugin for Qdrant Vector DB.

    Returns:
        Qdrant: Bodhilib LLM service implementation for Bodhilib plugin for Qdrant Vector DB
    """
    return Qdrant(model=model, api_key=api_key, **kwargs)
