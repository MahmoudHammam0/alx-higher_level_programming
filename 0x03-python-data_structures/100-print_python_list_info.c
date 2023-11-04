#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *x = (PyListObject *)p;
	int idx;
	long int s = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", x->allocated);
	for (idx = 0; idx < s; idx++)
		printf("Element %i: %s\n", idx, Py_TYPE(x->ob_item[idx])->tp_name);
}
