#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - check if its a cycle
*
* @list: pointer to list
*
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
  listint_t *sl = list, *fa = list;
  while (fa && fa->next)
{
sl = sl->next;
fa = fa->next->next;
if (sl == fa)
	return (1);
}
  return (0);
}
