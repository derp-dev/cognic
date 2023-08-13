// clipbridge.c
#include <stdio.h>

int main() {
  char buffer[1024];
  fgets(buffer, sizeof(buffer), stdin);  
  system("clip.exe < /dev/stdin"); 
  return 0;
}