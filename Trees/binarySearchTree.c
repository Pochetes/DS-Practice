#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct BSTnode {
    int data;
    struct BSTnode* left;
    struct BSTnode* right;
};

struct BSTnode* getNewNode(int data);
struct BSTnode* Insert(struct BSTnode* root, int data);
bool Search(struct BSTnode* root, int data);
void Print(struct BSTnode* root);


int main() {
    struct BSTnode* rootPtr = NULL;
    rootPtr = Insert(rootPtr, 10);
    rootPtr = Insert(rootPtr, 25);
}

struct BSTnode* getNewNode(int data) {
    // allocates memory to a new node
    struct BSTnode* newNode = (struct BSTnode*)malloc(sizeof(struct BSTnode*));

    // assigns data value and left and right pointers to NULL
    (*newNode).data = data;
    (*newNode).left = (*newNode).right = NULL;
    return newNode;
}

// function that inserts value depending on number
struct BSTnode* Insert(struct BSTnode* root, int data) {
    if (root == NULL) { // if empty tree
        root = getNewNode(data);
        return root;
    } else if (data <= (*root).data) { // moves left if less/==
        (*root).left = Insert((*root).left, data);
    } else { // moves right if more
        (*root).right = Insert((*root).right, data);
    }
    return root;
}

// function that searches for number based on size
bool Search(struct BSTnode* root, int data) {
    if (root == NULL) {
        return false;
    } else if ((*root).data == data) {
        return true;
    } else if (data <= (*root).data) {
        return Search((*root).left, data);
    } else {
        return Search((*root).right, data);
    }
}



