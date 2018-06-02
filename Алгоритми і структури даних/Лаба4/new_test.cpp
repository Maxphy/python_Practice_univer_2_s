////////////////////////////////////////////////////////////////////////////////
//
//            prepared by Maxym_Shylo(https://github.com/Maxphy)
//
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include<cstdlib>
#include<time.h>
#include<ctime>
using namespace std;

struct Node
{
int data;
Node *next;
};

struct Queue
{
int size; 				//розмір черги
Node *first;
Node *last;
};
void create(Queue *Q);
bool isfull(Queue *Q);
int first(Queue *Q);
void addelement(Queue *Q,int value);
void Delete(Queue *Q);
int size(Queue *Q);
void showq(Queue *Q);
void initialq(Queue *Q,int n);



int main()
{
setlocale(0,"rus");

Queue Q;
create(&Q);
initialq(&Q,4);
addelement(&Q,8);
showq(&Q);
cout<<first(&Q)<<endl;
Delete(&Q);
showq(&Q);


system("pause");
return 0;
}



void create(Queue *Q) //створення черги
{
Q->first=new Node;
Q->first->next=NULL;
Q->last=Q->first;
Q->size=0;
}

bool isfull(Queue *Q)
{
if (Q->first==Q->last)
{
	return true;
}
else
{
	return false;
}
}
int first(Queue *Q) 		//вивести перший елемент
{
return Q->first->next->data;
}

void addelement(Queue *Q,int value)
{

Q->last->next=new Node;
Q->last=Q->last->next;
Q->last->data=value; //додати в кінець
Q->last->next=NULL;
Q->size++;
cout<<"element added to queue"<<endl;
}
void Delete(Queue *Q)
{
Q->first=Q->first->next;
Q->size--;
cout<<"delete from queue"<<endl;

}
int size(Queue *Q)
{
return Q->size;
}

void initialq(Queue *Q,int n)
{
	srand(time(NULL));
	for(int i=0;i<n;i++)
	{
		addelement(Q,(rand()%100)+1);
	}

}

void showq(Queue *Q)
{
Node *temp;
temp=Q->first->next;
cout<<"Queue:"<<endl;
while (temp!=NULL)
{
	 cout<<temp->data<<" ";
	 temp=temp->next;
}
cout<<endl;
 }
