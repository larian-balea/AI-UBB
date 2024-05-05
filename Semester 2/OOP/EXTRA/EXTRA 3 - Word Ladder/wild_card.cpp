//
// Created by Larian on 5/2/2024.
//

#include "wild_card.h"

using namespace std;

vector<string> createWildCards(const string& word) {
    vector<string> cards(word.length());
    for (int i = 0; i < word.length(); i++)   //replace each letter with '*'
    {
        string card = word;
        card[i] = '*';
        cards[i] = card;
    }
    return cards;
}

//create a dictionary with patterns as keys and a set of words as values
void createWildCardsMap(const string& path, unordered_map<string, vector<string>>& wildCardsMap, int nrLetters) {
    ifstream fin(path);

    string word;
    while (getline(fin, word))
    {
        if (word.size() != nrLetters)
            continue;
        vector<string> wildCards = createWildCards(word);
        for (auto& card : wildCards)
        {
            if (wildCardsMap.find(card) != wildCardsMap.end())
                    wildCardsMap[card].push_back(word);
            else
            {
                wildCardsMap.insert(pair<string, vector<string>>(card, vector<string>()));
                wildCardsMap[card].push_back(word);
            }
        }
    }

    fin.close();
}

