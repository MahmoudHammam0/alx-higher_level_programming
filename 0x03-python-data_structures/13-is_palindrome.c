#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int idx = 0, i;
	int arr[2047];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	for (i = 0; i < idx / 2; i++, idx--)
	{
		if (arr[i] != arr[idx - 1])
			return (0);
	}
	return (1);
}
