#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a sorted list
 * @head: the list taking the insertion
 * @number: the element to be added
 *
 * Return: the address of the new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new;

	tmp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return NULL;
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return new;
	}

	while (tmp->next != NULL && tmp->next->n < number)
	{
		tmp = tmp->next;
	}

	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
