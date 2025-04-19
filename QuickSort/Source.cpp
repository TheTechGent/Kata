#include "QuickSort.h";
#include <iostream>;

using namespace std;

int main()
{
	int arr[] = { 10, 7, 8, 9, 1, 5, 12, 2, 22, 31, 19, 17 };
	constexpr int n = sizeof(arr) / sizeof(arr[0]);

	QuickSort::Sort(arr, 0, n - 1);

	cout << "Sorted array: ";
	for (const int i : arr)
	{
		cout << i << " ";
	}
	return 0;
}