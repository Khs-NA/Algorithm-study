#include <iostream>

using namespace std;

int main() {
    int hour, minute;

    cin >> hour >> minute;

    if (minute >= 45) {

        cout << hour << " " << minute - 45 << endl;
    }
    else {
        if (hour == 0) {
            hour = 23;
        }
        else {
            hour -= 1;
        }
        
        minute += 60 ;
        cout << hour << " " << minute - 45 << endl;
    }
    
    return 0;
}
