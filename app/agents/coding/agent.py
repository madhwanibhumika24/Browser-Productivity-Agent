from app.services.llm_service import LLMService


class CodingAgent:

    SYSTEM_PROMPT = """
You are an Expert Software Engineer.

Help users with

Python

Java

JavaScript

C++

Algorithms

Data Structures

Debugging

System Design

Best Practices

Always produce clean production-quality code.
"""

    def process(
        self,
        message: str,
        context: dict,
    ):

        answer = LLMService.generate(
            self.SYSTEM_PROMPT,
            message
        )

        return {

            "agent": "Coding Agent",

            "response": answer,

            "context": context

        }