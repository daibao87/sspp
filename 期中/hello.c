# py2c_transpiler/output/hello.c
// 執行 main.py 後會自動產生此檔案，例：
// gcc hello.c -o hello && ./hello
#include <stdio.h>

int main() {
    printf("%d\n", (1 + (2 * 3)));
    return 0;
}
