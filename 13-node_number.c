#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *temp = *head;

    if (head == NULL)
        return (NULL);
    new_node = malloc(sizeof(listint_t));
    new_node->n = number;

    if (*head == NULL)
    {
        *head = new_node;
        new_node->next = NULL;
    }
    while (temp)
    {
        if (temp->n >= number)
        {
            new_node->next = temp;
            return (new_node);
        }

        if (temp->next && temp->next->n >= number)
        {
            new_node->next = temp->next; 
            temp->next = new_node;
            return (new_node);
        }
        temp = temp->next;
    }
    return (NULL);
}
