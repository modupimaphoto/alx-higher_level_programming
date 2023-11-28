#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	struct listint_t *slow_ptr = head;
	struct listint_t *fast_ptr = head;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
