#include <iostream>
#include <algorithm>
#define max_n 11
using namespace std;
int main() {
	int a[max_n], b[max_n];
	long n = 0, result = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a + n);
	while (next_permutation(a, a + n)) {
		long sum = 0;
		copy(begin(a), end(a), begin(b));
		for (int i = 0;i < n - 1;i++) {
			sum += b[i] ^ b[i + 1];
		}		
		result = max(sum, result);
	}
	cout << result << endl;
	return 0;
}
