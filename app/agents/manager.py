from app.agents.learning.agent import LearningAgent
from app.agents.career.agent import CareerAgent
from app.agents.coding.agent import CodingAgent


class AgentManager:

    @staticmethod
    def route(context: dict):

        category = context.get("category", "General")

        if category == "Learning":
            return LearningAgent()

        elif category == "Career":
            return CareerAgent()

        elif category == "Development":
            return CodingAgent()

        return LearningAgent()