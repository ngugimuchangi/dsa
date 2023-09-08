#include "list.h"

ListNodeDouble_t *swapDouble(ListNodeDouble_t **head, ListNodeDouble_t *node_one, ListNodeDouble_t *node_one_prev,
							 ListNodeDouble_t *node_two, ListNodeDouble_t *node_two_prev);

/**
 * @brief Swaps two nodes in a doubly linked list
 *
 * @param head - pointer to the head of the list
 * @param k - the position of the node to be swapped
 * @return ListNodeDouble_t* - pointer to the head of the list
 */
ListNodeDouble_t *swapNodesDouble(ListNodeDouble_t *head, int k)
{
	ListNodeDouble_t *temp, *node_one, *node_one_prev, *node_two, *node_two_prev;
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
	return (swapDouble(&head, node_one, node_one_prev, node_two, node_two_prev));
}

/**
 * @brief - Does actual swapping of nodes
 *
 * @param head - pointer to the head of the list
 * @param node_one - pointer to the first node
 * @param node_one_prev - pointer to the previous node of the first node
 * @param node_two - pointer to the second node
 * @param node_two_prev - pointer to the previous node of the second node
 * @return ListNodeDouble_t* - pointer to the head of the list
 */
ListNodeDouble_t *swapDouble(ListNodeDouble_t **head, ListNodeDouble_t *node_one, ListNodeDouble_t *node_one_prev,
							 ListNodeDouble_t *node_two, ListNodeDouble_t *node_two_prev)
{
	ListNodeDouble_t *temp = NULL;
	if (node_one == node_two || !node_one || !node_two)
		return (*head);
	if (node_one_prev)
	{
		node_one_prev->next = node_two;
		node_two->prev = node_one_prev;
	}
	else
	{
		*head = node_two;
		node_two->prev = NULL;
	}
	if (node_two_prev)
	{
		node_two_prev->next = node_one;
		node_one->prev = node_two_prev;
	}
	else
	{
		*head = node_one;
		node_one->prev = NULL;
	}
	temp = node_one->next;
	node_one->next = node_two->next;
	if (node_one->next)
		node_one->next->prev = node_one;

	node_two->next = temp;
	if (temp)
		temp->prev = node_two;
	return (*head);
}
