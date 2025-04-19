#pragma once

class QuickSort
{
	// Algorithm Quick Sort, Big O = O(n log n)
public:

	QuickSort();

	static int Partition(int arr[], const int low, const int high);

	static void Sort(int arr[], const int low, const int high);

};

