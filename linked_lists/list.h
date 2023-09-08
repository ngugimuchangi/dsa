#ifndef LIST_H
#define LIST_H
#include <stdio.h>
/**
 * @brief Definition for singly-linked list.
 * @val: value of the node
 * @next: pointer to the next node
 */
typedef struct ListNode
{
    int val;
    struct ListNode *next;
} ListNode_t;

/**
 * @brief Definition for doubly-linked list.
 * @value: value of the node
 * @next: pointer to the next node
 * @prev: pointer to the previous node
 */
typedef struct ListNodeDouble
{
    int val;
    struct ListNodeDouble *next;
    struct ListNodeDouble *prev;
} ListNodeDouble_t;

/* Prototypes */
ListNode_t *add_to_singly_linked_list(ListNode_t *head, int value);
ListNodeDouble_t *add_to_doubly_linked_list(ListNodeDouble_t *head, int value);
ListNode_t *swapNodes(ListNode_t *head, int k);
ListNodeDouble_t *swapNodesDouble(ListNodeDouble_t *head, int k);
void print_list(ListNode_t *head);
void print_doubly_linked_list(ListNodeDouble_t *head);

#endif /* LIST_H */
