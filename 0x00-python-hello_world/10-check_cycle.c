#include "lists.h"
/**
 * check_cycle - check for cycles in linked list
 * @list: pointer to header node
 * Return: 1 in case of cycle 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *curr, *head = list;

	if (list == NULL)
		return (0);
	curr = head;
	while (curr != NULL)
	{
		ptr = curr;
		if (curr->next == head || curr->next == ptr)
			return (1);
		curr = curr->next;
	}
	return (0);
}
