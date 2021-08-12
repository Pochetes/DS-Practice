#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct BSTnode {
    int data;
    struct BSTnode* left;
    struct BSTnode* right;
};

struct BSTnode* Insert(struct BSTnode* root, int data);
bool Search(struct BSTnode* root, int data);
struct BSTnode* getNewNode(int data);
int getMax(struct BSTnode* root);
int getMin(struct BSTnode* root);

int main() {
    int input;
    struct BSTnode* rootPtr = NULL;
    rootPtr = Insert(rootPtr, 10);
    rootPtr = Insert(rootPtr, 22);
    rootPtr = Insert(rootPtr, 24);
    rootPtr = Insert(rootPtr, 1);
    rootPtr = Insert(rootPtr, 12);
    rootPtr = Insert(rootPtr, 18);
    rootPtr = Insert(rootPtr, 20);

    printf("Max value: %d\n", getMax(rootPtr));
    printf("Min value: %d\n", getMin(rootPtr));

    printf("Search a value: ");
    scanf("%d", &input);
    if (Search(rootPtr, input) == true) {
        printf("Found");
    } else { printf("Not found"); }
    
}

struct BSTnode* getNewNode(int data) {
    struct BSTnode* newNode = (struct BSTnode*)malloc(sizeof(struct BSTnewNode*));

    (*newNode).data = data;
    (*newNode).left = (*newNode).right = NULL;
    return newNode;
}

struct BSTnode* Insert(struct BSTnode* root, int data) {
    if (root == NULL) {
        root = getNewNode(data);
    } else if (data <= (*root).data) {
        root->left = Insert(root->left, data);
    } else {
        root->right = Insert(root->right, data);
    } return root;
}

bool Search(struct BSTnode* root, int data) {
    if (root == NULL) {
        return false;
    } else if (data == root->data) {
        return true;
    } else if (data <= (*root).data) {
        return Search(root->left, data);
    } else {
        return Search(root->right, data);
    }
}

// since BST, max val is at upmost right leaf node 
int getMax(struct BSTnode* root) {
    if (root == NULL) {
        printf("Empty tree");
        return -1;
    } else if (root->right == NULL) {
        return root->data;
    }
    
    return getMax(root->right);
}

// since BST, goes to upmost left leaf node where min val is
int getMin(struct BSTnode* root) {
    if (root == NULL) {
        printf("Empty tree");
        return -1;
    } else if (root->left == NULL) {
        return root->data;
    }

    return getMin(root->left);
}