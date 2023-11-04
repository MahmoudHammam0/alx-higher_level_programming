#include "lists.h"
int is_palindrome(listint_t **head)
{
	int i, idx = 0, length;
	int arr[1750];
	listint_t *ptr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	length = idx;
	for (i = 0; i < length / 2; i++, idx--)
	{
		if (arr[i] != arr[idx - 1])
			return (0);
	}
	return (1);
}
