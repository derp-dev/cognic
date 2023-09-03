CACHE_SIZE = 4000  # Max tokens in cache

cache = {}  # Initialize cache
knowledge_graph = {}  # Initialize knowledge graph
active_nodes = []  # Initialize active thoughts
def update_cache(input_message):  
    # Extract new knowledge from input message
    new_nodes = extract_nodes(input_message, knowledge_graph)
    new_connections = extract_connections(new_nodes, knowledge_graph)

    # Find relevant active nodes
    relevant_nodes = get_relevant_nodes(new_nodes, active_nodes)

    # Prune irrelevant active nodes
    irrelevant_nodes = set(active_nodes) - set(relevant_nodes)
    prune_nodes(irrelevant_nodes, cache)

    # Update knowledge graph and active nodes
    knowledge_graph.update(new_nodes)
    knowledge_graph.update(new_connections)
    active_nodes = relevant_nodes

    return knowledge_graph, active_nodes

def initialize_cache(size):
    cache = {}
    for i in range(size):
        cache[i] = ''
    return cache

# Functions to extract nodes, connections, find relevant nodes, prune nodes...

def extract_nodes(input_message, knowledge_graph):
    ...

def extract_connections(new_nodes, knowledge_graph):
    ...  

def get_relevant_nodes(new_nodes, active_nodes):
    ...  

def prune_nodes(irrelevant_nodes, cache):




def updateCache(inputMessage, cache, knowledgeGraph, activeNodes):
    newNodes = extractNodes(inputMessage, knowledgeGraph)
    newConnections = extractConnections(newNodes, knowledgeGraph)
    relevantNodes = getRelevantNodes(newNodes, activeNodes)
    irrelevantNodes = activeNodes - relevantNodes
    knowledgeGraph = knowledgeGraph + newNodes + newConnections
    activeNodes = relevantNodes
    pruneNodes(irrelevantNodes, cache)

def extractNodes(inputMessage, knowledgeGraph):
    nodes = []
    for node in inputMessage:
        if node not in knowledgeGraph:
            nodes.append(node)
            knowledgeGraph[node] = {}
    return nodes

def extractConnections(nodes, knowledgeGraph):
    connections = []
    for node1 in nodes:
        for node2 in nodes:
            if node1 != node2:
                connections.append((node1, node2))
    return connections

def getRelevantNodes(nodes, activeNodes):
    relevantNodes = []
    for node in nodes:
        if node in activeNodes:
            relevantNodes.append(node)
    return relevantNodes

def pruneNodes(irrelevantNodes, cache):
    cache[irrelevantNodes[0]] = {"relevance": 0, "pruned": True}
    for node in irrelev

def updateCache(inputMessage, cache, knowledgeGraph, activeNodes):
    newNodes = extractNodes(inputMessage, knowledgeGraph)
    newConnections = extractConnections(newNodes, knowledgeGraph)
    relevantNodes = getRelevantNodes(newNodes, activeNodes)
    irrelevantNodes = set(activeNodes) - set(relevantNodes)
    knowledgeGraph.update(newNodes)
    knowledgeGraph.update(newConnections)
    activeNodes.clear()
    activeNodes.extend(relevantNodes)
    pruneNodes(irrelevantNodes, cache)
    return (knowledgeGraph, activeNodes)

import random

CACHE = 3

def short_term_mem(m, s):
    if len(m) > CACHE:
        return chunk(m, CACHE, s)
    else:
        access(m, s)

def chunk(m, size, s):
    """Break m into chunks of size and access each chunk sequentially""" 
    chunks = [m[i:i+size] for i in range(0, len(m), size)]  
    for chunk in chunks:
         access(chunk, s)

def access(chunk, s): 
    """Access short term memory s with chunk"""
    s.update(chunk)
    print(f"Accessed chunk: {chunk}")

message = "012345"  
state = {}

short_term_mem(message, state)

