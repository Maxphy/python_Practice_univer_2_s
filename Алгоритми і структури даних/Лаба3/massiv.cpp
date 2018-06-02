////////////////////////////////////////////////////////////////////////////////
//
//            prepared by Maxym_Shylo(https://github.com/Maxphy)
//
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>

using namespace std;

class Example{

public:
int number;
string key;
string* array;


~Example();                                            //деструктор
void set_array();
void show_array();                                   //вивести з голови
void add_s();                           //додати елемент на початок
void add_e();                                //додати елемент в кінець
void search_element();                      //додати елемент
void del_s();                                       //видалити останній елемент
void del_e();
void f();
void f_3();
};

Example::~Example(){
    delete[] array;
    cout<<"Array has deleted successfully ...";
}

void Example::set_array(){
    cout<<"Type |array|: ";
	cin>>number;
	array=new string[number];
	for(int i=0;i<number;i++)
	{
		cin>>array[i];
	}
}

void Example::show_array()
{
    cout<<"Array: ";
		for (int i = 0; i < number; i++)
	{
		cout << "  " << array[i] << "  ";
	}
	cout << endl;
}

void Example::add_s()
{
    cout << "Type key: ";
    cin >> key;
    string *new_array=new string[number+1];
	new_array[0]=key;
	for(int i=0;i<number;i++)
	{
 	 new_array[i+1] = array[i];
	}
    delete[] array;
	array = new_array;
}
void Example::add_e(){
    cout << "Type key: ";
    cin >> key;
    string *new_array =new string[number+1];
	new_array[number]=key;
	for(int i=0;i<number;i++)
	{
 	new_array[i]=array[i];
	}
    delete[] array;
	array = new_array;
}

void Example::search_element()
{
cout << "Type key to look for: ";
cin >> key;
for(int i=0;i<number;i++)
	{
		if (array[i]==key)
		{
			cout<<"The element"<<key<<" has been founded at the index: "<<i;
		}
		else{
		    cout<<"Not found"<<endl;
		}
	}
}

void Example::del_s()
{
    string* new_array = new string[number];
    for(int i=1;i<number;i++)
	{
 	new_array[i]=array[i];
	}
    delete[] array;
	array = new_array;

}

void Example::del_e(){
    string* new_array =new string[number];
	for(int i=0;i<number-1;i++)
	{
 	new_array[i]=array[i];
	}
    delete[] array;
	array = new_array;
}

void Example::f(){
	for(int i=0;i<number+1;i++){
    if(array[i].length()%2!=0)
	{
	array[i].erase(0,1);
	array[i].erase(array[i].length()-1,1);
	}
	}
}


int main()
{
    setlocale(0,"rus");
    Example a;
    a.set_array();
    a.show_array();
    //a.f();

    //a.show_array();
    //a.add_s();
    a.del_e();
	a.show_array();
    //a.search_element();
    //a.del_s();
    //a.del_e();
    cout<<endl;
    return 0;
}
