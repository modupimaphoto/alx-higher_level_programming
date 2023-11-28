#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: singly linked list start
 * @number: number to insert
 * Return: a pointer or null on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (listint_t == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	listint_t *current = *head;

	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
