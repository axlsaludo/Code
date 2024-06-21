#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>
 
void main() 
{
    int gd = DETECT, gm;
    int i, x, y, flag=0;
    initgraph(&gd, &gm, "C:\\TC\\BGI");
 
    x = getmaxx()/2;
    y = 30;
 
    while(!kbhit()) 
    {
        if(y >= getmaxy()-30 || y <= 30)
            flag = !flag;
        
        setcolor(RED);
        setfillstyle(SOLID_FILL, RED);
        circle(x, y, 30);
        floodfill(x, y, RED);
 
        delay(25);
        cleardevice();
        if(flag)
        {
            y = y + 2;
        } 
        else
        {
            y = y - 2;
        }
    }
 
    getch();
    closegraph();
}