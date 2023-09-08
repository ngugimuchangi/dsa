#include <stdio.h>
#include "list.h"

/**
 * @brief Print a singly linked list
 *
 * @param head: pointer to the head of the list
 */
void print_list(ListNode_t *head)
{
	ListNode_t *temp = head;
	while (temp)
	{
		if (temp != head)
			printf(", ");
		printf("%d", temp->val);
		temp = temp->next;
	}
	printf("\n");
}

/**
 * @brief Print a doubly linked list
 *
 * @param head: pointer to the head of the list
 */
void print_doubly_linked_list(ListNodeDouble_t *head)
{
	ListNodeDouble_t *temp = head;
	while (temp)
	{
		if (temp != head)
			printf(", ");
		printf("%d", temp->val);
		temp = temp->next;
	}
	printf("\n");
}
