#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!head || !*head)
		return (node);
	ptr = *head;
	while (ptr && ptr->next)
	{
		if (ptr->next->n > number)
			break;
		ptr = ptr->next;
	}
	node->next = ptr->next;
	ptr->next = node;
	return (node);
}
