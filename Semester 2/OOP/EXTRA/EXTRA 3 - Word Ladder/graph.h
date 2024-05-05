//
// Created by Larian on 4/29/2024.
//

#pragma once
#include <unordered_map>
#include <vector>
#include <cstdio>

using namespace std;

template <typename T>
class Graph {
private:
    unordered_map<T, vector<T>> adjacencyList;
public:

    void addNode(T node) {
        adjacencyList[node];
    }

    void addEdge(T node1, T node2) {
        adjacencyList[node1].push_back(node2);
        adjacencyList[node2].push_back(node1);
    }

    void removeNode(T node) {
        adjacencyList.erase(node);
        for (auto &pair : adjacencyList) {
            for (int i = 0; i < pair.second.size(); i++) {
                if (pair.second[i] == node) {
                    pair.second.erase(pair.second.begin() + i);
                    i--;
                }
            }
        }
    }

    void removeEdge(T node1, T node2) {
        for (int i = 0; i < adjacencyList[node1].size(); i++) {
            if (adjacencyList[node1][i] == node2) {
                adjacencyList[node1].erase(adjacencyList[node1].begin() + i);
                i--;
            }
        }
        for (int i = 0; i < adjacencyList[node2].size(); i++) {
            if (adjacencyList[node2][i] == node1) {
                adjacencyList[node2].erase(adjacencyList[node2].begin() + i);
                i--;
            }
        }
    }

    unordered_map<T, vector<T>> getAdjacencyList() {
        return adjacencyList;
    }
};