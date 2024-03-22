import pyautogui
import time

def autotype(text, delay=0.05):
    # Wait for a few seconds to switch focus to the desired text input
    time.sleep(5)
    
    # Type the given text
    pyautogui.typewrite(text, interval=delay)

# Example usage
text_to_type = '''#include<bits/stdc++.h>
using namespace std;

struct Node {
int data;
int height;
Node* left;
Node* right;
};

int height(Node *N) {
if (N == NULL)
return 0;
return N->height;
}

int max(int a, int b) {
return (a > b)? a : b;
}

Node* newNode(int data) {
Node* node = new Node();
node->data = data;
node->left = NULL;
node->right = NULL;
node->height = 1;
return(node);
}

Node *rightRotate(Node *y) {
Node *x = y->left;
Node *T2 = x->right;
x->right = y;
y->left = T2;
y->height = max(height(y->left), height(y->right)) + 1;
x->height = max(height(x->left), height(x->right)) + 1;
return x;
}

Node *leftRotate(Node *x) {
Node *y = x->right;
Node *T2 = y->left;
y->left = x;
x->right = T2;
x->height = max(height(x->left), height(x->right)) + 1;
y->height = max(height(y->left), height(y->right)) + 1;
return y;
}

int getBalance(Node *N) {
if (N == NULL)
return 0;
return height(N->left) - height(N->right);
}

Node* insert(Node* node, int data) {
if (node == NULL)
return(newNode(data));
if (data < node->data)
node->left = insert(node->left, data);
else if (data > node->data)
node->right = insert(node->right, data);
else
return node;
node->height = 1 + max(height(node->left), height(node->right));
int balance = getBalance(node);
if (balance > 1 && data < node->left->data)
return rightRotate(node);
if (balance < -1 && data > node->right->data)
return leftRotate(node);
if (balance > 1 && data > node->left->data) {
node->left = leftRotate(node->left);
return rightRotate(node);
}
if (balance < -1 && data < node->right->data) {
node->right = rightRotate(node->right);
return leftRotate(node);
}
return node;
}

Node * minValueNode(Node* node) {
Node* current = node;
while (current->left != NULL)
current = current->left;
return current;
}

Node* deleteNode(Node* root, int data) {
if (root == NULL)
return root;
if ( data < root->data )
root->left = deleteNode(root->left, data);
else if( data > root->data )
root->right = deleteNode(root->right, data);
else {
if( (root->left == NULL) || (root->right == NULL) ) {
Node *temp = root->left ? root->left : root->right;
if(temp == NULL) {
temp = root;
root = NULL;
}
else
*root = *temp;
free(temp);
}
else {
Node* temp = minValueNode(root->right);
root->data = temp->data;
root->right = deleteNode(root->right, temp->data);
}
}
if (root == NULL)
return root;
root->height = 1 + max(height(root->left), height(root->right));
int balance = getBalance(root);
if (balance > 1 && getBalance(root->left) >= 0)
return rightRotate(root);
if (balance > 1 && getBalance(root->left) < 0) {
root->left = leftRotate(root->left);
return rightRotate(root);
}
if (balance < -1 && getBalance(root->right) <= 0)
return leftRotate(root);
if (balance < -1 && getBalance(root->right) > 0) {
root->right = rightRotate(root->right);
return leftRotate(root);
}
return root;
}

void printPostorder(Node* node, int& nodesPrinted, int totalNodes) {
if (node == NULL)
return;
printPostorder(node->left, nodesPrinted, totalNodes);
printPostorder(node->right, nodesPrinted, totalNodes);
cout << node->data;
nodesPrinted++;
if(nodesPrinted < totalNodes) {
cout << " ";
}
}

int main() {
Node* root = NULL;
int n;
cin >> n;
vector<int> scores(n);
for(int i=0; i<n; i++) {
cin >> scores[i];
root = insert(root, scores[i]);
}
Node* minNode = minValueNode(root);
root = deleteNode(root, minNode->data);
int nodesPrinted = 0;
printPostorder(root, nodesPrinted, n-1);
return 0;
}'''
autotype(text_to_type)