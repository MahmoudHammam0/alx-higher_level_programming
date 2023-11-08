#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - print python info about bytes
 * @p: object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	long int length, idx = 0, max;
	char *str;

	length = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", length);
	printf("  trying string: %s\n", str);
	if (length >= 10)
		max = 10;
	else
		max = length + 1;
	printf("  first %ld bytes:", max);
	while (idx < max)
	{
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 256 + str[idx]);
		idx++;
	}
	printf("\n");
}
/**
 * print_python_list - print python list
 * @p: object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *temp;
	long int length, idx = 0;
	PyObject *ptr;

	temp = (PyListObject *)p;
	length = ((PyVarObject *)(p))->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", temp->allocated);
	while (idx < length)
	{
		ptr = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((ptr)->ob_type)->tp_name);
		if (PyBytes_Check(ptr))
			print_python_bytes(ptr);
		idx++;
	}
}
