#include "lists.h"
#include <stdlib.h>
listint_t *reverse_list(listint_t **head)
{
	listint_t *curr, *prev, *h;

	h = *head;
	curr = h->next;
	prev = h;
	h->next = NULL;
	while (curr != NULL)
	{
		h = curr;
		curr = curr->next;
		h->next = prev;
		prev = h;
	}
	return (h);
}
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr2, *cp, *rev;

	if (!*head || !(*head)->next)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		if (ptr->n == ptr->next->n)
			break;
		ptr = ptr->next;
	}
	ptr2 = ptr->next;
	rev = reverse_list(&ptr2);
	ptr->next = rev;
	ptr = *head;
	cp = *head;
	while (ptr != NULL)
	{
		if (ptr->n == cp->n)
			break;
		ptr = ptr->next;
	}
	while (ptr && cp)
	{
		if (ptr->n != cp->n)
			return (0);
		ptr = ptr->next;
		cp = cp->next;
	}
	return (1);
}
