#include <iostream>

using namespace std;

// Algorithm Quick Sort, Big O = O(n log n)

int Partition(int arr[], int low, int high)
{
	/*
	What is happening here?
	*/
	int pivot = arr[high]; // choosing the last element as pivot
	int i = low - 1; // index of smaller element
	
	for (int j = low; j < high; j++)
	{
		if (arr[j] < pivot)
		{
			i++;
			swap(arr[i], arr[j]);
		}
	}
	
	swap(arr[i + 1], arr[high]);
	
	return i + 1;
}

void QuickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		int pi = Partition(arr, low, high);
		QuickSort(arr, low, pi - 1);
		QuickSort(arr, pi + 1, high);
	}
}

int main()
{
	int arr[] = { 10, 7, 8, 9, 1, 5 };
	int n = sizeof(arr) / sizeof(arr[0]);

	QuickSort(arr, 0, n - 1);

	cout << "Sorted array: ";
	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << " ";
	}
	return 0;
}
