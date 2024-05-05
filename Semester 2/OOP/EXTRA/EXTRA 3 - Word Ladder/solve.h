//
// Created by Larian on 5/4/2024.
//

#include "graph.h"
#include "wild_card.h"

#include <unordered_set>
#include <queue>

//create the graph with words as nodes and edges between words that differ by one letter
void createGraph(Graph<string>& graph, int nrLetters);

//returns the shortest path between two words using BFS
vector<string> shortestPath(Graph<string>& graph, const string& start, const string& target);
