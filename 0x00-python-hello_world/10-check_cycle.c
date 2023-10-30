#include "lists.h"
/**
 * check_cycle - check for cycles in linked list
 * @list: pointer to header node
 * Return: 1 in case of cycle 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *curr;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	ptr = list->next->next;
	while (curr != NULL)
	{
		if (curr == ptr)
			return (1);
		curr = curr->next;
		ptr = ptr->next->next;
	}
	return (0);
}
