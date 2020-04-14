#include<stdio.h>
#include<strings.h>
#include<stdlib.h>
char * password="comparisionsShouldBeConstantTime";
char input[1024];

int runnable(char*input)
{       volatile long int temp;
        int i=0;
        int inplen=strlen(input);
        for(i=0;i<strlen(password);i++)
        {
            //delay(200);
            for (temp=0;temp<9999999;temp+=5){ temp-=3;temp*=6;temp/=2;temp/=3;}
            if(i>strlen(password)||i>=inplen||password[i]!=input[i]){
                printf("checking failed for password %s at %c\n",input,input[i]);
                return -1;
            }


        }

    printf("check passed");
    return 0;
}

