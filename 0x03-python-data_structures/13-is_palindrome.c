#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int count = 0, idx = 0, i;

	if (!head || !*head)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		count++;
	}
	int arr[count];

	ptr = *head;
	while (ptr != NULL)
	{
		arr[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	for (i = 0; i < (count / 2); i++)
	{
		if (arr[i] != arr[count - i - 1])
			return (0);
	}
	return (1);
}
