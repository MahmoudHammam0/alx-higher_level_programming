#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: pointer to head node
 * Return: 1 if palindrome or 0 otherwise
 */
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
	while (ptr && arr && ptr->n)
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