from app.services.llm_service import LLMService


class LearningAgent:

    SYSTEM_PROMPT = """
You are an expert AI Learning Assistant.

Your responsibilities:

- Teach concepts clearly.
- Explain step-by-step.
- Give beginner-friendly answers.
- Use examples.
- Help students prepare for interviews.
- Keep answers structured.
"""

    def process(
        self,
        message: str,
        context: dict,
    ):

        prompt = f"""
Website : {context.get('website')}

Category : {context.get('category')}

Question :

{message}
"""

        answer = LLMService.generate(
            self.SYSTEM_PROMPT,
            prompt
        )

        return {

            "agent": "Learning Agent",

            "response": answer,

            "context": context

        }