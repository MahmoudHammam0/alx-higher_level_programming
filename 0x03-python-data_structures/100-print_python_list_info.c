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
	long int s = PyList_Size(p);
	int idx;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (idx = 0; idx < s; idx++)
		printf("Element %i: %s\n", idx, Py_TYPE(obj->ob_item[i])->tp_name);
}
