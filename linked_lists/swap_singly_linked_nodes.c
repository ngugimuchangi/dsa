#include "list.h"

ListNode_t *swap(ListNode_t **head, ListNode_t *node_one, ListNode_t *node_one_prev,
                 ListNode_t *node_two, ListNode_t *node_two_prev);

/**
 * @brief Swaps two nodes in a singly linked list
 *
 * @param head - pointer to the head of the list
 * @param k - the position of the node to be swapped
 * @return ListNode_t* - pointer to the head of the list
 */
ListNode_t *swapNodes(ListNode_t *head, int k)
{
    ListNode_t *temp, *node_one, *node_one_prev, *node_two, *node_two_prev;
    int number_of_nodes = 1;
    temp = node_one = node_one_prev = node_two = node_two_prev = NULL;
    temp = head;

    while (temp)
    {
        if (number_of_nodes == k - 1)
            node_one_prev = temp;
        if (number_of_nodes == k)
            node_one = temp;
        number_of_nodes += 1;
        temp = temp->next;
    }

    number_of_nodes -= 1;

    if (k > number_of_nodes)
        return (head);

    temp = head;
    while (temp && number_of_nodes >= k)
    {
        if (number_of_nodes == k + 1)
            node_two_prev = temp;
        if (number_of_nodes == k)
            node_two = temp;
        number_of_nodes -= 1;
        temp = temp->next;
    }
    return swap(&head, node_one, node_one_prev, node_two, node_two_prev);
}

/**
 * @brief - Does actual swapping of nodes
 *
 * @param head - pointer to the head of the list
 * @param node_one - pointer to the first node
 * @param node_one_prev - pointer to the previous node of the first node
 * @param node_two - pointer to the second node
 * @param node_two_prev - pointer to the previous node of the second node
 * @return ListNode_t* - pointer to the head of the list
 */
ListNode_t *swap(ListNode_t **head, ListNode_t *node_one, ListNode_t *node_one_prev,
                 ListNode_t *node_two, ListNode_t *node_two_prev)
{
    ListNode_t *temp = NULL;
    if (node_one == node_two || !node_one || !node_two)
        return (*head);
    if (node_one_prev)
        node_one_prev->next = node_two;
    else
        *head = node_two;
    if (node_two_prev)
        node_two_prev->next = node_one;
    else
        *head = node_one;

    temp = node_two->next;
    node_two->next = node_one->next;
    node_one->next = temp;
    return (*head);
}
