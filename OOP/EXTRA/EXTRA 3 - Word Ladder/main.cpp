#include "solve.h"

#include <iostream>

#include <chrono>
#include <ctime>
#include <fstream>

#include <sstream>
#include <unordered_set>

using namespace std;


string getRandomWord(Graph<string>& graph) {
    vector<string> words;
    for (auto& pair : graph.getAdjacencyList()) {
        words.push_back(pair.first);
    }
    return words[rand() % words.size()];
}

bool findWord(Graph<string> graph, const string& word, const string& toFind) {
    for (auto& pair : graph.getAdjacencyList())
        if (pair.first == word)
            for (auto& wrd : pair.second)
                if(wrd == toFind)
                    return true;
    return false;
}

void getHint(vector<string> path, string start) {
    string hint;
    cout << "hint: ";

    for (int i = 0; i < path.size() - 1; i++)
        if (path[i] == start)
        {
            hint = path[i + 1];
            break;
        }

    for (int i = 0; i < hint.size(); i++)
        if (hint[i] != start[i])
            /// print the letter colored in red
            cout << "\033[1;31m" << hint[i] << "\033[0m";  /// it should be start[i] but it is easier to see the difference
        else
            cout << start[i];
    cout << '\n';
}

void gameTime(char time_buffer[26]) {
    const auto now = chrono::system_clock::now();
    const time_t t_c = chrono::system_clock::to_time_t(now);
    ctime_s(time_buffer, 26, &t_c);
}

void saveData(const string& name, int nrOfHints, int nrOfMoves, int minNrMoves, const string& start, const string& target, const vector<string>& userSolution, const vector<string>& optimalSolution) {
    ofstream file;

    // Open file for append
    file.open("username.csv", ios_base::app);

    if (!file)
    {
        cerr << "Error opening file!\n";
        return;
    }

    // Write data to file
    char time_buffer[26];
    gameTime(time_buffer);

    file << "Name: " << name << '\n';
    file << "Start word: "<< start << '\n';
    file << "Target word: "<< target << '\n';
    file << "Date and time: " << time_buffer;
    file << "Number of hints: "<< nrOfHints << '\n';
    file << "Number of moves: "<< nrOfMoves << '\n';
    file << "Minimum number of moves: "<< minNrMoves << '\n';
    file << "User solution: ";
    for (auto& word : userSolution) {
        if (word == userSolution.back())
            file << word;
        else
            file << word << " -> ";
    }
    file << "\n";
    file << "Optimal solution: ";
    for (auto& word : optimalSolution) {
        if (word == optimalSolution.back())
            file << word;
        else
            file << word << " -> ";
    }

    file << "\n";
    file << "\n";
    file << "\n";

    // Close file
    file.close();
}

void automaticMode() {
    cout << "AUTOMATIC MODE\n";

    cout << "Enter the starting word: ";
    string start;
    cin >> start;

    cout << "Enter the target word: ";
    string target;
    cin >> target;

    if (start.size() != target.size())
        cout << "The words must have the same size.\n";
    else
    {
        Graph<string> graph;
        createGraph(graph, int(start.size()));

        vector<string> path = shortestPath(graph, start, target);

        if (path.empty())
            cout << "No solution found.\n" << '\n';
        else
        {
            cout << "Solution: ";
            for (auto& word : path) {
                if (word == path.back())
                    cout << word;
                else
                    cout << word << " -> ";
            }
            cout << '\n' << '\n';
        }
    }
}

void playMode() {
    cout << "PLAY MODE\n";

    cout << "You can ask for hints by pressing 'h'\n";

    cout << "Enter your name: ";
    string name;
    cin >> name;

    cout << "Enter the number of letters of the words: ";
    int nrLetters;
    cin >> nrLetters;

    /// Create the graph of words of given length
    Graph<string> graph;
    createGraph(graph, nrLetters);

    /// Randomly choose the start and target words
    string start;
    string target;
    vector<string> path;

    while (true)
    {
        start = getRandomWord(graph);
        target = getRandomWord(graph);

        if (start != target)
            if (!shortestPath(graph, start, target).empty())
                break;
    }

    /// Get the shortest path between the two words
    path = shortestPath(graph, start, target);

    cout << "The starting word is: " << start << '\n';
    cout << "The target word is: " << target << '\n' << '\n';

    vector<string> userSolution;

    string userInput;
    cout << "Enter the next word: ";
    cin >> userInput;

    string current = start;
    userSolution.push_back(current);

    int nrOfHints = 0;
    int nrOfMoves = 1;

    while (current != target)
    {
        if (userInput == "h" || userInput == "H")
        {
            vector<string> remainingPath = shortestPath(graph, current, target);
            getHint(remainingPath, current);
            nrOfHints++;
        }
        else if (findWord(graph, current, userInput))
        {
            current = userInput;
            userSolution.push_back(current);

        }
        else
            cout << "Invalid word.\n";
        nrOfMoves++;
        cout << "Enter the next word: ";
        cin >> userInput;

        if (userInput == target && findWord(graph, current, userInput))
            break;
    }
    userSolution.push_back(target);

    char time_buffer[26];
    gameTime(time_buffer);

    cout << "\nCongratulations, " << name << "!\n";
    cout << "You have found the target word!\n";
    cout << "Start word: " << start << '\n';
    cout << "Target word: " << target << '\n';
    cout << "Date and time: " << time_buffer;
    cout << "Number of hints: " << nrOfHints << '\n';
    cout << "Number of moves: " << nrOfMoves << '\n';
    cout << "Minimum number of moves: " << path.size() - 1 << '\n';
    cout << "Your solution is: ";
    for (auto& word : userSolution) {
        if (word == userSolution.back())
            cout << word;
        else
            cout << word << " -> ";
    }
    cout << '\n';
    cout << "Best solution is: ";
    for (auto& word : path) {
        if (word == path.back())
            cout << word;
        else
            cout << word << " -> ";
    }
    cout << '\n';

    saveData(name, nrOfHints, nrOfMoves, int(path.size()) - 1, start, target, userSolution, path);
}

void analyticsMode() {
    cout << "ANALYTICS MODE\n";

    cout << "Enter your name: ";
    string name;
    cin >> name;

    ifstream file;
    file.open("username.csv", ios_base::app);

    if (!file)
    {
        cerr << "Error opening file!\n";
        return;
    }

    bool ok = false;
    string line;
    string data;
    unordered_set<string> userSolution;
    string currentName;
//    int nrOfHints;
//    int nrOfMoves;
//    int minNrMoves;

    while (getline(file, line))
    {
        istringstream lineStream(line);
        string key, value;

        if (getline(lineStream, key, ':') && getline(lineStream, value))
        {
            if (key == "Name")
            {
                // Remove leading and trailing double quotes from the value
                value = value.substr(1, value.size() - 1);
                currentName = value;
            }

            if (currentName == name)
            {
                ok = true;
                string line1;
                while (getline(file, line1))
                {

                    istringstream lineStream1(line1);
                    string key1, value1;

                    if (getline(lineStream1, key1, ':') && getline(lineStream1, value1))
                    {
//                        if (key1 == "number of hints")
//                        {
//                            nrOfHints = stoi(value1);
//                        }
//                        if (key1 == "number of moves")
//                        {
//                            nrOfMoves = stoi(value1);
//                        }
//                        if (key1 == "minimum number of moves")
//                        {
//                            minNrMoves = stoi(value1);
//                        }
                        if (key1 == "User solution")
                        {
                            value1 = value1.substr(1,value1.size()-1);

                            istringstream iss(value1);
                            string word;
                            while (getline(iss, word, ' '))
                            {
                                if (word != "->")
                                    userSolution.insert(word);
                            }
                        }
                    }
                }
                break;
            }
        }
    }

    if (!ok)
    {
        cout << "There is no user with this name." << '\n';
        return;
    }

    cout << "The user " << name << " has used "<< "\033[1;32m" << userSolution.size() << "\033[0m"<< "\033[1;34m" << " unique words"<< "\033[0m" << '\n';
//    cout << "The user " << name << " has used " << "\033[1;32m" << nrOfHints << "\033[0m" << "\033[1;34m" << " hints" << "\033[0m" << '\n';
//    cout << "The user " << name << " has made " << "\033[1;32m" << nrOfMoves << "\033[0m" << "\033[1;34m" << " moves" << "\033[0m" << '\n';
//    cout << "The " << "\033[1;34m" <<"minimum number of moves " << "\033[0m" <<"was " << "\033[0m" << "\033[1; 32m" << minNrMoves << "\033[0m" << '\n';
    cout << '\n';


}

//void testGraph() {
//    Graph<int> graph;
//    graph.addNode(1);
//    graph.addNode(3);
//    graph.addNode(1);
//
//    graph.addEdge(1, 2);
//    graph.addEdge(1, 3);
//    graph.addEdge(2, 3);
//
//    graph.removeNode(3);
//
//    for (auto &pair : graph.getAdjacencyList()) {
//        cout << pair.first << ": ";
//        for (auto &node : pair.second) {
//            cout << node << " ";
//        }
//        cout << '\n';
//    }
//
//    graph.removeEdge(1, 2);
//}

void printMenu() {
    cout << "\033[1;31mWORD GAME\033[0m\n";
    cout << "1. Automatic mode\n";
    cout << "2. Play mode\n";
    cout << "3. Analytics mode\n";
    cout << "0. Exit\n";
}

int main() {
    printMenu();
    bool ok = true;
    while (ok) {
        cout << "Enter an option: ";
        int option;
        cin >> option;
        cout << '\n';

        switch (option) {
            case 1:
                automaticMode();
                break;
            case 2:
                playMode();
                break;
            case 3:
                analyticsMode();
                break;
            case 0:
                cout << "THE END!\n";
                ok = false;
                break;
            default:
                cout << "Invalid option.\n";
        }
    }
    return 0;
}
