#include "quickSort.h"
#include <iostream>

using namespace std;

QuickSort::QuickSort()
{
}

int QuickSort::Partition(int arr[], const int low, const int high)
	{
		/*
		Describe function
		*/
		const int pivot = arr[high]; // choosing the last element as pivot
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

void QuickSort::Sort(int arr[], const int low, const int high)
{
	if (low < high)
	{
		const int pi = Partition(arr, low, high);
		Sort(arr, low, pi - 1);
		Sort(arr, pi + 1, high);
	}
}