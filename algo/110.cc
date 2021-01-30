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
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        return helper(root).first;
    }

    std::pair<bool, int> helper(TreeNode* root) {
        if (root == nullptr) {
            return std::make_pair(true, 0);
        } 
        std::pair<bool, int> left_res = helper(root -> left);
        std::pair<bool, int> right_res = helper(root -> right);
        if (left_res.first && right_res.first && abs(left_res.second - right_res.second) <= 1) {
            return std::make_pair(true, std::max(left_res.second, right_res.second) + 1);
        } else {
            return std::make_pair(false, 0);
        } 
    }
};