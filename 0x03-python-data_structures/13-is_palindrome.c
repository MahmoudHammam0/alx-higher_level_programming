#include "lists.h"
#include <stdlib.h>
void list_rev(listint_t **head)
{
	listint_t *link = NULL, *curr = *head, *back = NULL;

	while (curr != NULL)
	{
		link = curr->next;
		curr->next = back;
		back = curr;
		curr = link;
	}
	*head = back;
}
int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head, *ptr2 = *head;

	if (!*head || !(*head)->next)
		return (1);
	while (ptr2 != NULL)
	{
		if (ptr2->n == ptr2->next->n)
			break;
		ptr2 = ptr2->next;
	}
	ptr2 = ptr2->next;
	list_rev(&ptr2);
	while (ptr1 && ptr2)
	{
		if (ptr1->n == ptr2->n)
		{
			ptr1 = ptr1->next;
			ptr2 = ptr2->next;
		}
		else
			return (0);
	}
	if (ptr2 == NULL)
		return (1);
	return (0);
}
int is_palindrome2(listint_t **head)
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
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
