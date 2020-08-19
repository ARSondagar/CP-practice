#include<iostream>
using namespace std;
int main()
{
    int t,G,I,N,Q;
    cin >> t;
    while(t--)
    {
        cin >> G;
        while(G--)
        {
            cin>>I>>N>>Q;
            if(N%2==0 || I==Q)
            {
                cout << N/2
            }
            else
            {
                cout<<N/2+1;
                cout<<"\n";
            }
        }
    }
    return 0;
}
