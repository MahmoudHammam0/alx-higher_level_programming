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
	{
		*head = node;
		return (node);
	}
	ptr = *head;
	if (ptr->n > number)
	{
		node->next = ptr;
		*head = node;
		return (node);
	}
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
