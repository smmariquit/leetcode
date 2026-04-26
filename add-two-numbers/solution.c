/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* h1 = l1;
    struct ListNode* h2 = l2;
    struct ListNode* ans = NULL;
    struct ListNode* anshead = NULL;

    int num1, num2, sum;
    int carry = 0;
    while(h1 || h2){
        if(anshead){
            anshead->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            anshead = anshead->next;
        } else {
            ans = (struct ListNode*)malloc(sizeof(struct ListNode));
            anshead = ans;
        }
        if(h1){
            num1 = h1->val;
            h1 = h1->next;
        } else num1 = 0;
        if(h2){
            num2 = h2->val;
            h2 = h2->next;
        } else num2 = 0;
        sum = num1 + num2 + carry;
        if(sum>9){
            carry = 1;
            sum = sum-10;
        } else {
            carry = 0;
        }
        anshead->val = sum;
    }
    if(carry){
        anshead->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        anshead->next->val = 1;
        anshead->next->next = NULL;
        return ans;
    }
    anshead->next = NULL;
    return ans;
}