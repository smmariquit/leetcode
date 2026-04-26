#include<bits/stdc++.h>
using namespace std;
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // depth first search
        // make stack
        // make visited list
        // push root to stack
        // while stack is not empty
        // pop from stack
        // mark node as visited/ process node
        // for all neighbors in stack
        // if neighbor is not visited
        // push to stack
        vector<int> t;
        vector<int> u;
        stack<TreeNode*> nodesp;
        nodesp.push(p);
        while(!nodesp.empty()){
            TreeNode* tmp = nodesp.top();
            if(tmp == NULL) break;
            nodesp.pop();
            t.push_back(tmp->val);
            if(tmp->left != NULL){
                nodesp.push(tmp->left);
                t.push_back(tmp->val);
            }
            else t.push_back(INT_MIN);
            if(tmp->right != NULL){
                nodesp.push(tmp->right);
                t.push_back(tmp->val);
            }
            else t.push_back(INT_MIN);
        }
        stack<TreeNode*> nodesq;
        nodesq.push(q);
        while(!nodesq.empty()){
            TreeNode* tmp = nodesq.top();
            if(tmp == NULL) break;
            nodesq.pop();
            u.push_back(tmp->val);
            if(tmp->left != NULL){
                nodesq.push(tmp->left);
                u.push_back(tmp->val);
            }
            else u.push_back(INT_MIN);
            if(tmp->right != NULL){
                nodesq.push(tmp->right);
                u.push_back(tmp->val);
            }
            else u.push_back(INT_MIN);
        }
        return t == u;
    
    }
};