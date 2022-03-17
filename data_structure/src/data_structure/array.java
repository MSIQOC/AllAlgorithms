package data_structure;

public class array {
	public static void leftRotatebyOne(int arr[], int n) {
		int first = arr[0];
		for(int i=0; i<n-1; ++i) {
			arr[i] = arr[i+1];
		}
		arr[n-1] = first;
		for(int i=0; i<n; ++i)
			System.out.print(arr[i] + " ");
	}
	public static void main(String [] args) {
		int arr[] = { 1, 2, 3, 4, 5 };
		System.out.println(arr.length);
		int arrr[] = new int[3];
		System.out.println(arrr.length);
		leftRotatebyOne(arr, 5);
	}
}
