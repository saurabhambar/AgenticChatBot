from langgraphagenticai.state import State

class BasicChatbotNode():
    """
    Basic Chatbot login Implementation
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state:State) -> dict:
        """
        Process the input state and generate a chatbot response."""
        # For demonstration purposes, this chatbot simply echoes the input text.
        return {"message": self.llml.invoke(state["messages"])}