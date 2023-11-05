#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Python object list
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int length = Py_SIZE(p);
	int idx;
	PyObject *ptr = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", ptr->allocated);
	for (idx = 0; idx < length; idx++)
	{
		ptr = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(ptr)->tp_name)
	}
}
