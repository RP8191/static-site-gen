

Build C++ programs on windows 10

1. install cygwin 

2. create simple c++ file (single.cpp in this example) in any editor.

```sh
#include <iostream>
using std::count;

int main(){
	cout<<"hello !";
	return 0;	
}
```

3. start cygwin command prompt. Type 
 
```sh
$ cd "C:"
```

4. User cd to desired directory where the cpp source file resides. Type

```sh
$ g++ -o single.exe single.cpp
```
5. This will create the output file single.exe

6. To run the single.exe, type :

```sh
$ chmod a+x single
$ ./single
```
7. Should display following message on the prompt.

```sh
hello !
```



