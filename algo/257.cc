/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include "listnode.h"
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        
    }

    bool isleaf(TreeNode* root) {
        return (root -> left == nullptr && root -> right == nullptr);
    }

    void add_path() {

    }

    void helper(TreeNode* root, vector<string>& paths, vector<int> path_stack) {
        if (isleaf(root)) {
            path_stack.push_back(root -> val);
            
            path_stack.pop_back();
        } else {
            path_stack.push_back(root -> val);
            helper(root -> left);
            helper(root -> right);
            path_stack.pop_back();
        }
    }
};