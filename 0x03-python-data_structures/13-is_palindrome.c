#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int *arr;
	int count = 1, idx = 0, j, i;

	if (!head || !*head)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	arr = malloc(sizeof(int) * count);
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	for (i = 0; i <= j; i++)
	{
		for (j = count - 1; j >= 0; j++)
		{
			if (arr[i] != arr[j])
				return (0);
		}
	}
	free(arr);
	return (1);
}
