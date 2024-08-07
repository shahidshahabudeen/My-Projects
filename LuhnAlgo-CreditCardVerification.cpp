#include <iostream>
using namespace std;

int sumofevendigits(string number, int len)
{
    int i=0, temp=0, rem=0, sum = 0;
    for (i=0; i<=14; i+=2)
    {
        int num = number[i] - 48;
        temp = num*2;
        if(temp>=10)
        {
            //cout<<temp<<" "<<'\n';
            rem = temp%10;
            temp = temp/10;
            //cout<<"Rem: "<<rem<<"temp :"<<temp<<'\n';
            sum = sum + rem + temp;
            //cout<<"Sum in if: "<<sum<<'\n';
        }
        else
            sum = sum + temp;
    }
    //cout<<"Final Sum: "<<sum<<'\n';
    return sum;
}

int sumofoddigits(string number, int len)
{
    int i=0, temp=0, rem=0, sum = 0;
    for (i=1; i<=15; i+=2)
    {
        int num = number[i] - 48;
        sum = sum + num;
    }
    //cout<<"Final Sum: "<<sum<<'\n';
    return sum;
}

int main() {
    // Write C++ code here
    string number;
    int sumeven, sumodd;
    cout<<"Enter Credit Card Number: ";
    getline(cin,number);
    int len = number.length();
    //cout<<len<<'\n';
    
    sumeven = sumofevendigits(number,len);
    sumodd = sumofoddigits(number,len);
    //cout<<"Sum in step 1: "<<sum<<'\n';
    
    int total = sumeven+sumodd;
    if(total%10 == 0)
    {
        cout<<"Credit Card is Valid!!"<<'\n';
    }
    else
    {
        cout<<"invalid Credit Card!"<<'\n';
    }
    return 0;
}