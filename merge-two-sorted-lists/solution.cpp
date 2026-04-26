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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(0); // Make a dummy node with value 0;
        ListNode* cur = dummy; // Make a current node with the same address as the dummy
        while (list1 && list2){ // While the lists are not null
            if(list1->val > list2->val){ // If the value of the second list is smaller
                cur->next = list2; // Append the list to the current node
                list2 = list2->next; // Next the second list
            } else { // Baliktad lang
                cur->next = list1;
                list1 = list1->next;
            }
            cur = cur->next; // Iterate
        }
        cur->next = list1? list1: list2; // Kung aling list ang hindi pa empty, yun ang sagot
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};