//
// Created by Larian on 5/2/2024.
//

#include "solve.h"


//create the graph with words as nodes and edges between words that differ by one letter
void createGraph(Graph<string>& graph, int nrLetters) {
    unordered_map<string, vector<string>> wildCardsMap;
    createWildCardsMap("Words.txt", wildCardsMap, nrLetters);


    //add nodes to the graph
    for (auto& pair : wildCardsMap) {
        for (auto& word : pair.second)
            graph.addNode(word);

        //add edges between words that differ by one letter
        for (int i = 0; i < pair.second.size() - 1; i++) {
            for (int j = i + 1; j < pair.second.size(); j++) {
                if (pair.second[i] != pair.second[j])
                    graph.addEdge(pair.second[i], pair.second[j]);
            }
        }
    }
}

//returns the shortest path between two words using BFS
vector<string> shortestPath(Graph<string>& graph, const string& start, const string& target) {
    // Create a visited set to keep track of visited nodes
    unordered_set<string> visited;

    // Create a queue for BFS
    queue<pair<string, vector<string>>> q;

    // Mark the starting node as visited and enqueue it with an empty path
    visited.insert(start);
    q.push({ start, {start} });

    // Loop until the queue is empty
    while (!q.empty()) {
        // Dequeue a vertex from queue and get its path
        string curr = q.front().first;
        vector<string> path = q.front().second;
        q.pop();

        // If the dequeued vertex is the target, return its path
        if (curr == target)
            return path;

        // Get all adjacent vertices of the dequeued vertex curr
        vector<string> neighbors = graph.getAdjacencyList()[curr];

        // Traverse through all adjacent vertices
        for (const auto& neighbor : neighbors)
        {
            // If a neighbor is not visited, mark it visited and enqueue it with the current path plus the neighbor
            if (visited.find(neighbor) == visited.end())
            {
                visited.insert(neighbor);
                vector<string> newPath = path;
                newPath.push_back(neighbor);
                q.push({ neighbor, newPath });
            }
        }
    }

    // If the target is not reachable from the starting node, return an empty path
    return {};
}
