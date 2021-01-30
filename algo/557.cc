class Solution {
public:
    string reverseWords(string s) {
        istringstream ss(s);
        string word, result;
        vector<string> words;
        while (ss >> word) {
            reverse(word.begin(), word.end());
            result += word;
            result += " ";
        }
        return result.substr(0, result.length() - 1);
    }
};