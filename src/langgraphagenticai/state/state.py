from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict): # use TypeDict / Pydantic if preferred
    """
    Represent the structure of the state used in graph
    """
    # represents the state structure used in graph
    message: Annotated[list,add_messages]  # list / deque of messages
    
