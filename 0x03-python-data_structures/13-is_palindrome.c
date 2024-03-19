#include"lists.h"
/**
 * length - elrijf
 * @head: worufh
 * Return: lofjiv
 */
int length(listint_t **head)
{
int len = 0;
listint_t *current = *head;
while (current != NULL)
{
len++;
current = current->next;
}
return (len);
}
/**
 * is_palindrome - ugku
 * @head: kujgh
 * Return: ljkh
 */
int is_palindrome(listint_t **head)
{
int n = length(head);

if (n == 0)
	return (1);
if (n % 2 != 0 || !head)
	return (0);

int array[n];
listint_t *ptr = *head;
for (int i = 0; i < n; i++)
{
array[i] = ptr->n;
ptr = ptr->next;
}

int i = 0, j = n - 1;
while (i < j)
{
if (array[i] != array[j])
	return (0);
i++;
j--;
}
return (1);
}
