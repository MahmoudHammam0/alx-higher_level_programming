#include "lists.h"
int is_palindrome(listint_t **head)
{
	int i, idx = 0, length;
	int *arr;
	listint_t *ptr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	arr = malloc(sizeof(int) * 2000);
	ptr = *head;
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	arr[idx] = NULL;
	length = idx;
	for (i = 0; i < length / 2; i++, idx--)
	{
		if (arr[i] != arr[idx - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
