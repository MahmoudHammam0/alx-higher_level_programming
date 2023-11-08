#include <stdio.h>
#include <Python.h>
void print_python_bytes(PyObject *p)
{
	long int length, idx, max;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	length = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", length);
	printf("  trying string: %s\n", str);
	if (lenght >= 10)
		max = 10;
	else
		max = length + 1;
	printf("  first %ld bytes:", max);
	for (idx = 0; i < max; idx++)
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 256 + str[idx]);
	printf("\n");
}
void print_python_list(PyObject *p)
{
	long int length, idx;
	PyListObject *temp;
	PyObject *ptr;

	length = ((PyVarObject *)(p))->ob_size;
	temp = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", temp->allocated);
	for (idx = 0; idx < length; idx++)
	{
		ptr = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((ptr)->ob_type)->tp_name);
		if (PyBytes_Check(ptr))
			print_python_bytes(ptr);
	}
}