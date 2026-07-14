from google import genai

from app.config import settings


class LLMService:

    client = genai.Client(
        api_key=settings.GOOGLE_API_KEY
    )

    @classmethod
    def generate(
        cls,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        prompt = f"""
        {system_prompt}

        User:
        {user_prompt}
        """

        response = cls.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text