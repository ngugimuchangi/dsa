#include <stdlib.h>
#include <stdio.h>
#include "list.h"

int main(void)
{
	struct ListNode *head = NULL, *head_two = NULL;
	struct ListNodeDouble *head_double = NULL, *head_double_two = NULL;
	int i;

	for (i = 0; i < 10; i++)
	{
		head = add_to_singly_linked_list(head, i);
		head_double = add_to_doubly_linked_list(head_double, i);
	}

	for (i = 0; i < 2; i++)
	{
		head_two = add_to_singly_linked_list(head_two, i);
		head_double_two = add_to_doubly_linked_list(head_double_two, i);
	}

	printf("head one:\n");
	print_list(head);
	head = swapNodes(head, 10);
	print_list(head);
	printf("\n");

	printf("head two:\n");
	print_list(head_two);
	head_two = swapNodes(head_two, 2);
	print_list(head_two);
	printf("\n");

	printf("head double:\n");
	print_doubly_linked_list(head_double);
	head_double = swapNodesDouble(head_double, 10);
	print_doubly_linked_list(head_double);
	printf("\n");

	printf("head double two:\n");
	print_doubly_linked_list(head_double_two);
	head_double_two = swapNodesDouble(head_double_two, 2);
	print_doubly_linked_list(head_double_two);

	return (EXIT_SUCCESS);
}
