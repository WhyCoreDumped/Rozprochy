#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void addElement(struct Node **head, int data) {
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    if(new_node == NULL) return;

    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL)
        *head = new_node;
    else {
        struct Node *last = *head;
        while (last->next != NULL)
            last = last->next;
        last->next = new_node;
    }

    printf("Added %d to the list\n", data);
}

void deleteElement(struct Node **head, int data) {
    struct Node *temp = *head, *prev = NULL;
    if (temp != NULL && temp->data == data) {
        *head = temp->next;
        free(temp);
        printf("Deleted %d from the list\n", data);
        return;
    }

    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Can't find searched value %d.\n", data);
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("Deleted %d from the list\n", data);
}

void printList(struct Node *head) {
    printf("List: ");
    while (head != NULL) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

void freeList(struct Node *head) {
    struct Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main()
{
    struct Node *list = NULL;

    addElement(&list, 1);
    addElement(&list, 2);
    addElement(&list, 3);

    deleteElement(&list, 2);

    printList(list);

    freeList(list);
    return 0;
}