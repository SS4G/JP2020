/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy_node;
        ListNode* dummy_node_ptr = &dummy_node;
        ListNode* insert_ptr = &dummy_node;

        ListNode* cur_ptr = head;

        while (cur_ptr != nullptr) {
            if (cur_ptr -> val != insert_ptr -> val || insert_ptr == dummy_node_ptr) {
                insert_ptr -> next = cur_ptr;
                insert_ptr = insert_ptr -> next;
            }
            cur_ptr = cur_ptr -> next;
        }

        if (insert_ptr -> next != nullptr) {
            insert_ptr -> next = nullptr;
        }
        return dummy_node_ptr -> next;
    }
};