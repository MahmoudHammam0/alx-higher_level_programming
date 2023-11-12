#include <stdio.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
	char *add[] = {"/usr/bin/git", "add", ".", NULL};
	char *comm[] = {"/usr/bin/git", "commit", "-m", argv[1], NULL};
	char *push[] = {"/usr/bin/git", "push", NULL};
	execve(add[0], add, NULL);
	execve(comm[0], comm, NULL);
	return (0);
}
