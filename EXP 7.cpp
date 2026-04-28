#include <iostream>
#include <queue>
usingnamespace std;
struct Node {
	char data;
	int freq;
	Node *left, *right;
	Node(char d, int f) {
		data = d;
		freq= f;
		left = right = NULL;
	}
};
struct compare {
	bool operator()(Node* l, Node* r) {
		return l->freq> r->freq;
	}
};
voidprint(Node* root, stringstr) {
	if(!root)return;


	if(root->data != '$')
		cout << root->data << ": " << str << endl;
	print(root->left, str+"0");
	print(root->right, str+"1");
}
voidhuffman(char data[], int freq[], int n) {
	priority_queue<Node*, vector<Node*>, compare> pq;
	for(int i=0; i<n; i++)
		pq.push(newNode(data[i], freq[i]));
	while(pq.size()!=1) {
		Node* l = pq.top();
		pq.pop();
		Node* r = pq.top();
		pq.pop();
		Node* top= newNode('$', l->freq+ r->freq);
		top->left = l;
		top->right = r;
		pq.push(top);
	}
	print(pq.top(),"");
}
int main() {
	char data[]= {'a','b','c','d','e','f'};
	int freq[]= {5,9,12,13,16,45};

	huffman(data,freq,6);
}