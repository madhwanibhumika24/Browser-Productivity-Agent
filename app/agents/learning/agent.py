class LearningAgent:

    def process(
        self,
        message: str,
        context: dict,
    ):

        return {
            "agent": "Learning Agent",
            "response": f"Learning Agent received: {message}",
            "context": context
        }