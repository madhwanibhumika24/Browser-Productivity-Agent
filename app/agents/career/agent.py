class CareerAgent:

    def process(
        self,
        message: str,
        context: dict,
    ):

        return {
            "agent": "Career Agent",
            "response": f"Career Agent received: {message}",
            "context": context
        }