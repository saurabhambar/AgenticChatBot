from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """
        Sets up the graph based on the selected use case.
        This method determines which graph-building method to call based on the 
        provided use case. Currently, it supports a 'basic_chatbot' use case, 
        which triggers the construction of a simple chatbot graph.

        Args:
            usecase (str): The selected use case for which to set up the graph.

        Raises:
            ValueError: If an unsupported use case is provided.
        """

        if usecase == "Basic ChatBot":
            self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")

        return self.graph_builder.compile()
