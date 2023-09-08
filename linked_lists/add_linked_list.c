#include <stdlib.h>
#include "list.h"

/**
 * @brief Add a node to a singly linked list
 *
 * @param head: pointer to the head of the list
 * @param value: value of the node
 * @return ListNode_t*
 */
ListNode_t *add_to_singly_linked_list(ListNode_t *head, int value)
{
	ListNode_t *new = malloc(sizeof(ListNode_t));
	new->val = value;
	new->next = NULL;
	if (head)
		new->next = head;
	head = new;
	return (head);
}

/**
 * @brief Add a node to a doubly linked list
 *
 * @param head: pointer to the head of the list
 * @param value: value of the node
 * @return ListNodeDouble_t*
 */
ListNodeDouble_t *add_to_doubly_linked_list(ListNodeDouble_t *head, int value)
{
	ListNodeDouble_t *new = malloc(sizeof(ListNodeDouble_t));
	new->val = value;
	new->next = NULL;
	new->prev = NULL;
	if (head)
	{
		new->next = head;
		head->prev = new;
	}
	head = new;
	return (head);
}
