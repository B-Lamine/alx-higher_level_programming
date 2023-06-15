#include "lists.h"

/**
  * check_cycle - check if linked list is cyclic.
  * @list: pointer to first node.
  * Return: 1 if cyclic, 0 otherwise.
  */
int check_cycle(listint_t *list)
{
	listint_t *cursor1;

	cursor1 = list;
	while (cursor1 != NULL)
	{
		if (cursor1->next == list)
			return (1);
		cursor1 = cursor1->next;
	}
	return (0);
}
