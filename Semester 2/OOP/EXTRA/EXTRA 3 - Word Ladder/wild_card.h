//
// Created by Larian on 5/4/2024.
//

#pragma once

#include <unordered_map>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

vector<string> createWildCards(const string& word);

void createWildCardsMap(const string& path, unordered_map<string, vector<string>>& wildCardsMap, int nrLetters);
