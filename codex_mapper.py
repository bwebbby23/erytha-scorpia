import networkx as nx

class CodexKnowledgeGraph:
    """
    The Codex Method: Narrative-Based STEM Pedagogy.
    Maps O(n) abstractions to narrative metaphors for optimized retention.
    """
    def __init__(self):
        self.graph = nx.DiGraph()
        self._build_schema_library()
        
    def _build_schema_library(self):
        # Mappings from 'The Codex Method BPW draft 1.pdf'
        
        # 1. Computer Science
        self.graph.add_node("Array", type="Abstract", complexity=0.8)
        self.graph.add_node("Apartment Complex", type="Narrative", valence=0.9)
        self.graph.add_edge("Array", "Apartment Complex", relation="embodies", weight=0.95)
        
        # 2. Big-O Notation
        self.graph.add_node("O(n^2)", type="Abstract", complexity=0.9)
        self.graph.add_node("Traffic Jam", type="Narrative", valence=0.2)
        self.graph.add_edge("O(n^2)", "Traffic Jam", relation="analogous_to", weight=0.85)
        
        # 3. Mathematics
        self.graph.add_node("Logarithm", type="Abstract", complexity=0.7)
        self.graph.add_node("Undo Button", type="Narrative", valence=0.95)
        self.graph.add_edge("Logarithm", "Undo Button", relation="functional_map", weight=1.0)

    def retrieve_metaphor(self, concept: str) -> str:
        """
        Retrieves the optimal narrative anchor for a given abstract concept
        to minimize cognitive load.
        """
        if concept not in self.graph:
            return "NO_SCHEMA_FOUND"
            
        # Find neighbors with type='Narrative'
        neighbors = self.graph.neighbors(concept)
        for n in neighbors:
            if self.graph.nodes[n]['type'] == 'Narrative':
                return n
        return None

if __name__ == "__main__":
    codex = CodexKnowledgeGraph()
    print(f"Concept: Logarithm -> Schema: {codex.retrieve_metaphor('Logarithm')}")
