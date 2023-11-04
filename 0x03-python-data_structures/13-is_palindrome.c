#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count = 0, *arr, idx = 0, i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	arr = malloc(sizeof(int) * count);
	if (arr == NULL)
		return (0);
	ptr = *head;
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	for (i = 0, j = count - 1; i < count / 2; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	free(arr);
	return (1);
}
