from heapq import heappush, heappop
from src.utils import tokenize_problem, extract_constraints
from src.visualization import data_structures

# Heuristic function to calculate how well the data structure fits the constraints
# Heuristic function to calculate how well the data structure fits the constraints
def heuristic_value(data_structure, constraints):
    # Weights for constraints
    constraint_weights = {
        'O(1) access': 4, 'O(log n) access': 3, 'O(n) access': 1,
        'O(1) insertion': 4, 'O(log n) insertion': 3, 'O(n) insertion': 1,
        'O(1) deletion': 4, 'O(log n) deletion': 3, 'O(n) deletion': 1,
        'O(1) search': 4, 'O(log n) search': 3, 'O(n) search': 1,
        'fast_access': 3, 'fast_insertion': 3, 'fast_deletion': 3, 'fast_sorting': 3,
        'low_memory_usage': 2, 'moderate_memory_usage': 1, 'high_memory_usage': -2,
        'ordered': 1, 'unordered': 1, 'mutable': 1, 'immutable': -1,
        'LIFO': 2, 'FIFO': 2, 'hierarchical': 2, 'network': 3,
        'nodes': 2, 'edges': 2, 'key_value_store': 3, 'prefix_search': 3,
        'sorted_structure': 3, 'frequent_updates': 2,
    }
    
    # Initialize score
    score = 0
    penalty = 0

    # Calculate score based on constraints
    for constraint in constraints:
        if data_structures[data_structure].get(constraint, False):
            score += constraint_weights.get(constraint, 1)
        else:
            penalty += constraint_weights.get(constraint, 1)
    
    return score - penalty


# Constraint satisfaction with heuristic-driven search
def csp_heuristic_search(constraints):
    open_set = []
    heappush(open_set, (0, [], {}))  # (negative heuristic value, path, current_props)
    visited = set()

    best_solution = None
    best_heuristic = -1

    while open_set:
        # Get the best option from the priority queue
        neg_heuristic, path, current_props = heappop(open_set)
        current_heuristic = -neg_heuristic  # Convert back to positive heuristic value

        # Make sure the state (properties) is hashable by converting lists to tuples
        state = tuple((key, tuple(value) if isinstance(value, list) else value) for key, value in sorted(current_props.items()))

        if state in visited:
            continue
        visited.add(state)

        # Goal check: If all constraints are satisfied
        if constraints.issubset(current_props.keys()) and current_heuristic > best_heuristic:
            best_solution = path
            best_heuristic = current_heuristic

        # Explore neighboring data structures
        for ds, properties in data_structures.items():
            if ds in path:
                continue  # Skip already selected structures
            
            # Combine current properties with new data structure's properties
            new_props = current_props.copy()
            new_props.update(properties)
            
            # Calculate new heuristic value
            new_heuristic_value = heuristic_value(ds, constraints)
            
            # Add the new state to the priority queue with the negative heuristic for max-heap behavior
            new_path = path + [ds]
            heappush(open_set, (-new_heuristic_value, new_path, new_props))

    return best_solution if best_solution else None

# Usage in suggest_data_structure:
def suggest_data_structure(problem):
    tokens = tokenize_problem(problem)
    constraints = extract_constraints(tokens)
    
    if not constraints:
        return "No constraints could be extracted from the problem description."
    
    best_match = None
    best_score = 0

    for ds, properties in data_structures.items():
        # Initialize score for each data structure
        score = 0

        # Prioritize data structures that meet all required constraints
        for constraint in constraints:
            if properties.get(constraint, False):
                # Increase score for each matched constraint
                score += 1
                # Additional score if matching critical constraints like O(1) or O(log n)
                if constraint in ['O(1) access', 'O(log n) insertion', 'O(1) deletion', 'O(log n) deletion']:
                    score += 1  # Extra weight for critical constraints

        # Update the best match if this data structure has a higher score
        if score > best_score:
            best_score = score
            best_match = ds

    # Generate explanation if a suitable data structure is found
    if best_match:
        explanation = generate_explanation(best_match, constraints)
        return f"Suggested data structure: {best_match}\nExplanation:\n{explanation}"
    else:
        return "No suitable data structure found."

def generate_explanation(data_structure, constraints):
    properties = data_structures[data_structure]
    explanation = f"The data structure '{data_structure}' is recommended because it matches the following constraints:\n"

    # List constraints that match
    for constraint in constraints:
        if properties.get(constraint, False):
            explanation += f"- Matches '{constraint}'\n"

    # Check for pros and cons, and provide default messages if none exist
    explanation += "\nPros:\n"
    pros = properties.get('pros', [])
    if pros:
        for pro in pros:
            explanation += f"- {pro}\n"
    else:
        explanation += "- No specific pros identified.\n"

    explanation += "\nCons:\n"
    cons = properties.get('cons', [])
    if cons:
        for con in cons:
            explanation += f"- {con}\n"
    else:
        explanation += "- No specific cons identified.\n"

    return explanation


