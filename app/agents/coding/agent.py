class CodingAgent:

    def process(
        self,
        message: str,
        context: dict,
    ):

        return {
            "agent": "Coding Agent",
            "response": f"Coding Agent received: {message}",
            "context": context
        }