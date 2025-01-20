import networkx as nx
import matplotlib.pyplot as plt

# Define data structures and their properties
data_structures = {
    'array': {
        'ordered': True,
        'indexed': True,
        'mutable': True,
        'fast_access': True,
        'low_memory_usage': True,
        'O(1) access': True,
        'O(n) insertion': True,
        'O(n) deletion': True,
        'O(n) search': True,
        'pros': ["Fast access (O(1) complexity for indexed elements).", "Low memory usage for static data."],
        'cons': ["Slow insertion and deletion (O(n) complexity).", "Not ideal for frequent updates."],
    },
    'linked_list': {
        'ordered': True,
        'mutable': True,
        'fast_insertion': True,
        'fast_deletion': True,
        'low_memory_usage': True,
        'O(n) access': True,
        'O(1) insertion': True,
        'O(1) deletion': True,
        'pros': ["Efficient insertion and deletion at known positions (O(1) complexity)."],
        'cons': ["Slow access (O(n) complexity).", "Memory overhead due to pointers."],
    },
    'hash_table': {
        'unordered': True,
        'fast_access': True,
        'fast_insertion': True,
        'fast_deletion': True,
        'moderate_memory_usage': True,
        'O(1) access': True,
        'O(1) insertion': True,
        'O(1) deletion': True,
        'pros': ["Fast access, insertion, and deletion (O(1) average complexity).", "Ideal for key-value pairs."],
        'cons': ["Unordered structure.", "Memory intensive due to hashing."],
    },
    'binary_tree': {
        'ordered': True,
        'mutable': True,
        'hierarchical': True,
        'O(log n) access': True,
        'O(log n) insertion': True,
        'O(log n) deletion': True,
        'moderate_memory_usage': True,
        'pros': ["Efficient sorted access (O(log n) complexity).", "Maintains order."],
        'cons': ["Higher memory usage due to pointers.", "Balancing adds overhead."],
    },
    'b_tree': {
        'ordered': True,
        'mutable': True,
        'hierarchical': True,
        'O(log n) access': True,
        'O(log n) insertion': True,
        'O(log n) deletion': True,
        'high_memory_usage': True,
        'pros': ["Efficient access and insertion for large datasets.", "Minimizes disk access."],
        'cons': ["High memory usage due to multiple children per node.", "More complex structure to maintain."],
    },
    'trie': {
        'ordered': True,
        'hierarchical': True,
        'fast_search': True,
        'moderate_memory_usage': True,
        'prefix_search': True,
        'pros': ["Ideal for prefix-based searches like autocomplete.", "Efficient O(length) search for words."],
        'cons': ["Moderate memory usage due to large branching.", "Complex to implement."],
    },
    'deque': {
        'ordered': True,
        'mutable': True,
        'fast_insertion': True,
        'fast_deletion': True,
        'low_memory_usage': True,
        'O(1) insertion': True,
        'O(1) deletion': True,
        'FIFO': True,
        'LIFO': True,
        'pros': ["Supports both LIFO and FIFO operations.", "Efficient O(1) insertion and deletion at both ends."],
        'cons': ["Access in the middle is O(n).", "Not ideal for indexed access."],
    },
    'graph': {
        'network': True,
        'nodes': True,
        'edges': True,
        'high_memory_usage': True,
        'pros': ["Ideal for representing networks with complex relationships."],
        'cons': ["High memory usage for dense graphs.", "Complex traversal algorithms."],
    },
    'heap': {
        'ordered': True,
        'fast_retrieval': True,
        'fast_sorting': True,
        'moderate_memory_usage': True,
        'O(log n) insertion': True,
        'O(log n) deletion': True,
        'pros': ["Efficient min/max retrieval.", "Good for priority queues."],
        'cons': ["Not suitable for random access.", "Non-constant time complexity for insertions and deletions."],
    },
    'radix_sort': {
        'fast_sorting': True,
        'stable_sorting': True,
        'high_memory_usage': True,
        'O(n) insertion': True,
        'pros': ["Very fast sorting for integers or strings with similar lengths (O(n) complexity).", "Stable sort."],
        'cons': ["High memory usage.", "Not comparison-based, so limited to certain data types."],
    },
    'stack': {
        'LIFO': True,
        'fast_insertion': True,
        'fast_deletion': True,
        'low_memory_usage': True,
        'O(1) insertion': True,
        'O(1) deletion': True,
        'pros': ["O(1) time complexity for insertion and deletion.", "Ideal for LIFO access."],
        'cons': ["Only top element accessible.", "Not suitable for random access."],
    },
    'queue': {
        'FIFO': True,
        'fast_insertion': True,
        'fast_deletion': True,
        'moderate_memory_usage': True,
        'O(1) insertion': True,
        'O(1) deletion': True,
        'pros': ["O(1) complexity for enqueue and dequeue.", "Ideal for FIFO access."],
        'cons': ["Only front or rear accessible.", "Not suitable for random access."],
    },
}




# Visualization code (e.g., for graph, heap, binary_tree)
def visualize_structure(structure):
    G = nx.Graph()

    if structure == 'binary_tree':
        G.add_edges_from([("Root", "Left Child"), ("Root", "Right Child")])
    elif structure == 'graph':
        G.add_edges_from([("Node 1", "Node 2"), ("Node 2", "Node 3"), ("Node 1", "Node 3")])
    elif structure == 'heap':
        G.add_edges_from([("Root", "Left Child"), ("Root", "Right Child"), ("Left Child", "Leaf 1"), ("Right Child", "Leaf 2")])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000)
    plt.title(f"{structure.capitalize()} Visualization")
    plt.show()
