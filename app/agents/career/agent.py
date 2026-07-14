from app.services.llm_service import LLMService


class CareerAgent:

    SYSTEM_PROMPT = """
You are an AI Career Coach.

Help users with

- Resume
- LinkedIn
- Placements
- HR Interviews
- Career Advice
- Salary Negotiation

Always answer professionally.
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

            "agent": "Career Agent",

            "response": answer,

            "context": context

        }