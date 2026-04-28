#include <iostream>
#include <algorithm>
usingnamespace std;
struct Item {
	int value, weight;
};
bool cmp(Itema, Itemb) {
	return (double)a.value/ a.weight > (double)b.value/ b.weight;
}
double knapsack(int W, Itemarr[], int n) {
	sort(arr, arr+n, cmp);
	double total = 0.0;
	for(int i=0; i<n; i++) {
		if(arr[i].weight <= W) {
			W -= arr[i].weight;
			total += arr[i].value;
		} else {
			total += arr[i].value * ((double)W/ arr[i].weight);


			break;
		}
	}
	return total;
}
int main() {
	Itemarr[] = {{60,10},{100,20},{120,30}};
	cout << knapsack(50, arr, 3);
}
}