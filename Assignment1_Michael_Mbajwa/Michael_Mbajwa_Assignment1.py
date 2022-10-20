# Dataset 5
# NAME: MICHAEL MBAJWA
# STUDENT NUMBER: 0210152807

# Import packages
import snap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import defaultdict
import numpy as np


# Store file paths
facebook_edges_filepath = "/Users/michaelmbajwa/Desktop/Semester3/ComplexNetworks/Complex-Networks_exercise-main/Datasets/Group5/Facebook-Ego/686.edges"
twitter_edges_filepath = "/Users/michaelmbajwa/Desktop/Semester3/ComplexNetworks/Complex-Networks_exercise-main/Datasets/Group5/Twitter-Ego/1435461.edges"


# Load the /.edges files
# Facebook is an undirected network
graphFacebook = snap.LoadEdgeListStr(snap.TUNGraph, facebook_edges_filepath, 0, 1)

# Twitter is a directed network
graphTwitter = snap.LoadEdgeListStr(snap.TNGraph, twitter_edges_filepath, 0, 1)


# Get general sense of graphs
graphFacebook.PrintInfo()
graphTwitter.PrintInfo()


## QUESTION A
# Nodes and edges in the Networks
def nodes_edges(graph, id):
    nodes = "Number of nodes in {0} Network: {1}".format(id, graph.GetNodes())
    edges = "Number of edges in {0} Network: {1}".format(id, graph.GetEdges())
    result = nodes + "\n" + edges
    return result

QnA_facebook = nodes_edges(graphFacebook, "Facebook")
QnA_twitter = nodes_edges(graphTwitter, "Twitter")
print("\n" + QnA_facebook + "\n" + QnA_twitter + "\n\n")



## QUESTION B
# What are the maximum degree and the average degree of the Networks
def maxD_avgD(graph, id):
    graphDegrees = [item.GetVal1() for item in graph.GetDegCnt()]
    maxDeg = max(graphDegrees)
	
	# Average Degree by definition in class ==> 2E/N
    avgDeg = (2 * graph.GetEdges())/graph.GetNodes()

    result1 = "The maximum degree of the {0} Network is: {1}".format(id, maxDeg)
    result2 = "The average degree of the {0} Network is: {1}".format(id, avgDeg)

    return result1 + "\n" + result2
    
QnB_facebook = maxD_avgD(graphFacebook, 'Facebook')
QnB_Twitter = maxD_avgD(graphTwitter, 'Twitter')

print(QnB_facebook + "\n\n" + QnB_Twitter)



## QUESTION C
# Extract partial network from Facebook and Twitter networks
facebookSubGraph = graphFacebook.GetRndSubGraph(8)
twitterSubGraph = graphTwitter.GetRndSubGraph(5)


# Function to construct an adjacency matrix for any partial network
def adjacency_matrix(SubGraph, id):
    # Step1: Get the Nodes of the subgraph
    SubGraphNodes = [NI.GetId() for NI in SubGraph.Nodes()]
    print("\nThe Nodes in the {0}SubGraph are: {1}".format(id, SubGraphNodes))
    # Note: The node at each position of the list SubGraphNodes will take similar position in the adjacency matrix.


    # Create a dictionary that has its key as the node and has its values as a list of edges
    # Note: For undirected graphs, we can construct adjacency matrix with the InEdges or OutEdges since InEdges=OutEdges
    # For directed graphs, we only use OutEdges. To make this function simpler, I will use OutEdges since it solves the problem without considering if the graph is directed or not 
    SubGraphDict=defaultdict(list)
    for NI in SubGraph.Nodes():
        SubGraphDict[NI.GetId()] = list(NI.GetOutEdges())

    n_nodes = len(SubGraphNodes)

    AdjacentMatrix = np.zeros((n_nodes, n_nodes))


    for i in range(n_nodes):
        current_node = SubGraphNodes[i]
        for j in range(n_nodes):
            other_node = SubGraphNodes[j]
            if other_node in SubGraphDict[current_node]:
                AdjacentMatrix[i][j] = 1
            else:
                AdjacentMatrix[i][j] = 0

    
    return AdjacentMatrix
    

adjacencyMatrixFacebook = adjacency_matrix(facebookSubGraph, "Facebook")
print("\nFacebook subgraph Adjacency matrix:\n", adjacencyMatrixFacebook)

adjacencyMatrixTwitter = adjacency_matrix(twitterSubGraph, "Twitter")
print("\nTwitter subgraph adjacency matrix:\n", adjacencyMatrixTwitter)
print("\n\n")


# You can further inspect the subgraphs with the following print statements

#FACEBOOK
print("For Facebook Subgraph:\n")
for sub in facebookSubGraph.Edges():
    print("edge({}, {})".format(sub.GetSrcNId(), sub.GetDstNId()))
for NI in facebookSubGraph.Nodes():
    print("node: {0}, in-edges: {1}, out-edges: {2}".format(NI.GetId(), list(NI.GetInEdges()), list(NI.GetOutEdges())))

#TWITTER
print("\n\nFor Twitter Subgraph:\n")
for sub_tw in twitterSubGraph.Edges():
    print("edge({}, {})".format(sub_tw.GetSrcNId(), sub_tw.GetDstNId()))
    
for NI in twitterSubGraph.Nodes():
    print("node: {0}, in-edges: {1}, out-edges: {2}".format(NI.GetId(), list(NI.GetInEdges()), list(NI.GetOutEdges())))
