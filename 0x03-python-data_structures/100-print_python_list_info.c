#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Python object list
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	long int length = PyList_Size(p);
	int idx;
	PyListObject *ptr = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", ptr->allocated);
	for (idx = 0; idx < length; idx++)
	{
		ptr = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(ptr)->tp_name)
	}
}
