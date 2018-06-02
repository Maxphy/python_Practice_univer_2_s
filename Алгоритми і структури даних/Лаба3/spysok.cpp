////////////////////////////////////////////////////////////////////////////////
//
//            prepared by Maxym_Shylo(https://github.com/Maxphy)
//
////////////////////////////////////////////////////////////////////////////////

#include<iostream>
#include<string>

using namespace std;

string function(string);

struct Node {
 string key;					  //інформація(ключ)
 Node *Next,*Prev; 			      //вказівник на наступній та попередній елемент
 };

class List{
Node *Tail,*Head;
public:
List():Head(NULL),Tail(NULL){};    //конструктор головик i хвоста
~List();                           //деструктор
void show_s();                     //вивести з голови
void show_e();                     //вивести з кінця
void add_s(string key);            //додати елемент на початок
void add_e(string key);            //додати елемент в кінець
void type_list();                  //ввести список
void del_list();                   //видалити список
Node* search_element(string key);  //додати елемент
void del_tail();                   //видалити останній елемент

};

List::~List(){
Node* temp;

while(Head)
{
  temp = Head->Next;
  delete Head;
  Head = temp;
}
}

void List::show_s()
 {

Node* temp=Head;
cout<<"Your list now is(from start): "<<endl;

while (temp!=NULL){
	 cout<<temp->key<<" ";
	 temp=temp->Next;
}
 }

void List::show_e(){

Node* temp=Tail;
cout<<"Your list now is(from end): "<<endl;

while (temp!=NULL)
{
	 cout<<temp->key<<" ";
	 temp=temp->Prev;
}
 }

void List::add_s(string key){
Node* temp = new Node;

temp->key = key;
temp->Next = Head;

if (Head!=0){
Head->Prev=temp;
}
Head=temp;
temp->Prev = NULL;
}

void List::add_e(string key){
Node* temp = new Node;

temp->key = key;
temp->Next = NULL;

if (Head!=0){
temp->Prev=Tail;
Tail->Next=temp;
Tail=temp;
}
else{
Tail=temp;
temp->Prev = NULL;
Head=Tail=temp;
}
}

void List::type_list(){

cout<<"Type count of elements: ";
int c;
cin>>c;
for(int i=0;i<c;i++)
{
string s;
cin>>s;
add_e(s);
}
}

void List::del_list(){
Node *temp;
while (Head)
  {
temp=Head->Next;
delete Head;
Head=temp;
}
}

Node* List::search_element(string key)
{
	Node *temp;
	temp=Head;
	while ((temp!=0) && (temp->key!=key))
	{
		temp=temp->Next;
	}
	return temp;
}

int main(){
setlocale(0,"rus");
List a;
a.type_list();
cout<<endl;
a.add_s("first");
cout<<endl;
a.add_e("last");
cout<<endl;
a.show_s();
cout<<endl;
cout<<a.search_element("l")<<endl;
a.show_e();
cout<<endl;
a.del_list();
cout<<endl;
return 0;
}
