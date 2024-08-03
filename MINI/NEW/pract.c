#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(){

  pid_t pid;

  pid = fork();

  if(pid < 0){
    printf(stderr,"Fork Failed\n");
    return 1;
  }

  if(pid > 0){
    printf("Parent Process\n");
    printf("Parent PID:%d\n",getpid());
    printf("Parent's Parent PID:%d\n",getppid());
  }

  else{
    printf("Child Process\n");
    printf("Child PID:%d\n",getpid());
    printf("Parent  PID of the child:%d\n",getppid());

  }

  return 0;
}