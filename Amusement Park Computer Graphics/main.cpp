#include <stdio.h>
#include <windows.h>
#include <math.h>
#include <stdlib.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <time.h>
#include <iostream>
using namespace std;

float translate_x = 0.0;
float translate_y = 0.0;
float translate_z = 0.0;
static GLfloat spin = 0.0;
float spin_x=1.0;
float spin_y=0.0;
float spin_z=0.0;
int day=1;
bool rain=false;
bool winter=false;
bool carv=false;
bool planev=false;
bool top=false;
int flag=0;
bool help=false;


void *currentfont;

void otherCircle(GLfloat x, GLfloat y,GLfloat z, GLfloat radius,int r,int g,int b)//Mursalin Khan
{
    int i;
    int triangleAmount = 200; //# of triangles used to draw circle

    //GLfloat radius = 0.8f; //radius
    GLfloat twicePi = 2.0f * 3.1416;
    int counter=0;
    glColor3ub(r,g,b);
    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(x, y,z); // center of circle
    for(i = 0; i <= triangleAmount; i++)
    {
        counter+=1;
        glVertex3f(
            x + (radius * cos(i *  twicePi / triangleAmount)),
            y + (radius * sin(i * twicePi / triangleAmount)),z
        );
    }
    glEnd();
}
//Sun and Moon
void Circle(GLfloat x, GLfloat y,GLfloat z, GLfloat radius,int r,int g,int b)//Mursalin Khan
{
    int i;
    int triangleAmount = 200; //# of triangles used to draw circle

    //GLfloat radius = 0.8f; //radius
    GLfloat twicePi = 2.0f * 3.1416;
    int counter=0;
    glColor3ub(r,g,b);
    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(x, y,z); // center of circle
    for(i = 0; i <= triangleAmount; i++)
    {
        counter+=1;
        glVertex3f(
            x + (radius * cos(i *  twicePi / triangleAmount)),
            y + (radius * sin(i * twicePi / triangleAmount)),z
        );
    }
    glEnd();

}

void drawFilledCircle(GLfloat x, GLfloat y,GLfloat z, GLfloat radius,int color)//Mursalin Khan
{
    int i;
    int triangleAmount = 50; //# of triangles used to draw circle

    //GLfloat radius = 0.8f; //radius
    GLfloat twicePi = 2.0f * 3.1416;
    int counter=0;
    glColor3ub(color,color,color);
    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(x, y,z); // center of circle
    for(i = 0; i <= triangleAmount; i++)
    {
        counter+=1;
        glVertex3f(
            x + (radius * cos(i *  twicePi / triangleAmount)),
            y + (radius * sin(i * twicePi / triangleAmount)),z
        );
        if(counter<25)
        {
            color+=3;
            glColor3ub(color,color,color);
        }
        else
        {
            color-=3;
            glColor3ub(color,color,color);
        }
    }
    glEnd();

}
void Road()
{
    glColor3ub(78,78,78);
    glBegin(GL_QUADS);
    glVertex3i(-200,0,0);
    glVertex3i(1324,0,0);
    glVertex3i(1324,120,0);
    glVertex3i(-200,120,0);
    glEnd();
}
void clouds(float x,float y,float z,int m,int l,int n)
{
    static float a=-1250.0f;
    if(a>=1324)
    {
        a=-1250.0f;

    }
    else
    {
        a+=0.02f;
        //glColor3ub(r,g,b);
    }
    glPushMatrix();
    glTranslatef(a,0,0);
    //cloud1
    otherCircle(x,y,z,50.0f,m,l,n);
    otherCircle(x-50,y,z,40.0f,m,l,n);
    otherCircle(x+50,y,z,40.0f,m,l,n);
    glPopMatrix();
    glutPostRedisplay();
}
void plane()
{
    static float a=-300.0f;
    static float b=0.0f;
    if(a>=1324)
    {
        a=-300.0f;
        b=0.0f;

    }
    else
    {
        a+=0.1f;
        b+=0.005f;
        //glColor3ub(r,g,b);
    }
    //Body
    glColor3ub(66, 66, 66);
    glPushMatrix();
    glTranslatef(a,b,0);
    glBegin(GL_QUADS);
    glVertex3i(30,700,0);
    glVertex3i(100,700,0);
    glVertex3i(100,715,0);
    glVertex3i(35,715,0);
    glEnd();

    //front
    glBegin(GL_TRIANGLES);
    glVertex3i(100,700,0);
    glVertex3i(110,707,0);
    glVertex3i(100,715,0);
    glEnd();

    //fanback
    glBegin(GL_QUADS);
    glVertex3i(37,715,0);
    glVertex3i(57,715,0);
    glVertex3i(40,730,0);
    glVertex3i(20,730,0);
    glEnd();

    //fanFrontUp
    glBegin(GL_QUADS);
    glVertex3i(70,715,0);
    glVertex3i(80,715,0);
    glVertex3i(60,735,0);
    glVertex3i(50,735,0);
    glEnd();

    //FanFrontDown
    glBegin(GL_QUADS);
    glVertex3i(70,700,0);
    glVertex3i(80,700,0);
    glVertex3i(60,680,0);
    glVertex3i(50,680,0);
    glEnd();

    //window
    glColor3ub(255,255,255);
    glBegin(GL_POINTS);
    glVertex3i(95,710,0);
    glVertex3i(90,710,0);
    glVertex3i(85,710,0);
    glVertex3i(80,710,0);
    glVertex3i(75,710,0);
    glVertex3i(70,710,0);
    glVertex3i(65,710,0);
    glVertex3i(60,710,0);
    glVertex3i(55,710,0);
    glEnd();
    glPopMatrix();
    glutPostRedisplay();

}
void planeTwo()
{
    static float a=550.0f;
    static float b=0.0f;
    if(a<=-1300)
    {
        a=550.0f;
        b=0.0f;

    }
    else
    {
        a-=0.2f;
        b-=0.02f;
        //glColor3ub(r,g,b);
    }
    //Body
    glColor3ub(128, 128, 128);
    glPushMatrix();
    glTranslatef(a,-b,0);
    glBegin(GL_QUADS);
    glVertex3i(919,650,0);
    glVertex3i(989,650,0);
    glVertex3i(989,665,0);
    glVertex3i(919,665,0);
    glEnd();

    //Front
    glBegin(GL_TRIANGLES);
    glVertex3i(919,650,0);
    glVertex3i(909,657,0);
    glVertex3i(919,665,0);
    glEnd();

    //FanBack
    glBegin(GL_QUADS);
    glVertex3i(987,665,0);
    glVertex3i(1010,680,0);
    glVertex3i(990,680,0);
    glVertex3i(967,665,0);
    glEnd();

    //FanFrontUp
    glBegin(GL_QUADS);
    glVertex3i(949,665,0);
    glVertex3i(959,665,0);
    glVertex3i(979,685,0);
    glVertex3i(969,685,0);
    glEnd();

    //FanFrontDown
    glBegin(GL_QUADS);
    glVertex3i(949,650,0);
    glVertex3i(969,630,0);
    glVertex3i(979,630,0);
    glVertex3i(959,650,0);
    glEnd();

    int x=924;
    //Window
    glColor3ub(255,255,255);
    glBegin(GL_POINTS);
    for(int i=9; i>=0; i--)
    {
        glVertex3i(x,660,0);
        x+=5;
    }
    glEnd();
    glPopMatrix();
    glutPostRedisplay();

}
//Marzana & Istiaq
void playGround(int r,int g,int b)
{
    //Field
    glColor3ub(r,g,b);
    glBegin(GL_QUADS);
    glVertex3i(-200,120,0);
    glVertex3i(1324,120,0);
    glVertex3i(1324,500,0);
    glVertex3i(-200,500,0);
    glEnd();


    //Marzana & Istiaq
    //Basketball Court
    glColor3ub(220, 220, 220);//Gainsboro
    glBegin(GL_QUADS);
    glVertex3i(10,230,0);
    glVertex3i(350,230,0);
    glVertex3i(290,380,0);
    glVertex3i(70,380,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(40,440,0);
    glVertex3i(50,440,0);
    glVertex3i(50,330,0);
    glVertex3i(40,305,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(40,430,0);
    glVertex3i(80,430,0);
    glVertex3i(80,440,0);
    glVertex3i(40,440,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(80,485,0);
    glVertex3i(90,485,0);
    glVertex3i(90,390,0);
    glVertex3i(80,390,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(50,440,0);
    glVertex3i(60,440,0);
    glVertex3i(80,460,0);
    glVertex3i(80,470,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(320,440,0);
    glVertex3i(310,440,0);
    glVertex3i(310,330,0);
    glVertex3i(320,305,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(280,430,0);
    glVertex3i(320,430,0);
    glVertex3i(320,440,0);
    glVertex3i(280,440,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(270,485,0);
    glVertex3i(280,485,0);
    glVertex3i(280,390,0);
    glVertex3i(270,390,0);
    glEnd();

    glColor3ub(245, 245, 245);//White Smoke
    glBegin(GL_QUADS);
    glVertex3i(310,440,0);
    glVertex3i(300,440,0);
    glVertex3i(280,460,0);
    glVertex3i(280,470,0);
    glEnd();

    glLineWidth(3);
    glBegin(GL_LINES);
    glColor3f(1.0f, 1.0f, 1.0f); // White
    glVertex2f(30, 240);
    glVertex2f(330, 240);
    glVertex2f(30, 240);
    glVertex2f(80, 370);
    glVertex2f(80, 370);
    glVertex2f(280, 370);
    glVertex2f(280, 370);
    glVertex2f(330, 240);
    glVertex2f(180, 240);
    glVertex2f(180, 370);

    glVertex2f(50, 290);
    glVertex2f(130, 290);

    glVertex2f(130, 290);
    glVertex2f(130, 310);

    glVertex2f(130, 310);
    glVertex2f(58, 310);

    glVertex2f(310, 290);
    glVertex2f(230, 290);

    glVertex2f(230, 290);
    glVertex2f(230, 310);

    glVertex2f(230, 310);
    glVertex2f(302, 310);
    glEnd();


    //Marzana & Istiaq //Bench

    //Bench 01
    //glColor3ub(178, 34, 34);//Fire Brick // upper
    //glBegin(GL_QUADS);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(1080,440,0);
    glVertex3i(1210,440,0);
    glVertex3i(1210,430,0);
    glVertex3i(1080,430,0);
    glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(1100,470,0);
    glVertex3i(1190,470,0);
    glVertex3i(1210,440,0);
    glVertex3i(1080,440,0);
    glEnd();


    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(1105,430,0);
    glVertex3i(1115,430,0);
    glVertex3i(1115,400,0);
    glVertex3i(1105,400,0);
    glEnd();

    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(1175,430,0);
    glVertex3i(1185,430,0);
    glVertex3i(1185,400,0);
    glVertex3i(1175,400,0);
    glEnd();

    //Bench 02
    //glColor3ub(178, 34, 34);//Fire Brick // upper
    //glBegin(GL_QUADS);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(880,440,0);
    glVertex3i(1010,440,0);
    glVertex3i(1010,430,0);
    glVertex3i(880,430,0);
    glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(900,470,0);
    glVertex3i(990,470,0);
    glVertex3i(1010,440,0);
    glVertex3i(880,440,0);
    glEnd();


    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(905,430,0);
    glVertex3i(915,430,0);
    glVertex3i(915,400,0);
    glVertex3i(905,400,0);
    glEnd();

    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(975,430,0);
    glVertex3i(985,430,0);
    glVertex3i(985,400,0);
    glVertex3i(975,400,0);
    glEnd();
    //Bench 03
    //glColor3ub(178, 34, 34);//Fire Brick // upper
    //glBegin(GL_QUADS);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(680,440,0);
    glVertex3i(810,440,0);
    glVertex3i(810,430,0);
    glVertex3i(680,430,0);
    glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(700,470,0);
    glVertex3i(790,470,0);
    glVertex3i(810,440,0);
    glVertex3i(680,440,0);
    glEnd();

    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(705,430,0);
    glVertex3i(715,430,0);
    glVertex3i(715,400,0);
    glVertex3i(705,400,0);
    glEnd();

    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(775,430,0);
    glVertex3i(785,430,0);
    glVertex3i(785,400,0);
    glVertex3i(775,400,0);
    glEnd();
    //Bench 04
    //glColor3ub(178, 34, 34);//Fire Brick // upper
    //glBegin(GL_QUADS);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glVertex3i(0,0,0);
    //glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(480,440,0);
    glVertex3i(610,440,0);
    glVertex3i(610,430,0);
    glVertex3i(480,430,0);
    glEnd();

    glColor3ub(165, 42, 42);//Brown // lower
    glBegin(GL_QUADS);
    glVertex3i(500,470,0);
    glVertex3i(590,470,0);
    glVertex3i(610,440,0);
    glVertex3i(480,440,0);
    glEnd();


    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(505,430,0);
    glVertex3i(515,430,0);
    glVertex3i(515,400,0);
    glVertex3i(505,400,0);
    glEnd();

    glColor3ub(139, 105, 105);//Rosy Brown 4 // stand
    glBegin(GL_QUADS);
    glVertex3i(575,430,0);
    glVertex3i(585,430,0);
    glVertex3i(585,400,0);
    glVertex3i(575,400,0);
    glEnd();

    //Marzana & Istiaq //Food Cart
    //Food Cart 01
    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(950,140,0);
    glVertex3i(940,140,0);
    glVertex3i(940,200,0);
    glVertex3i(950,200,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(850,140,0);
    glVertex3i(840,140,0);
    glVertex3i(840,200,0);
    glVertex3i(850,200,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(810,200,0);
    glVertex3i(980,200,0);
    glVertex3i(980,210,0);
    glVertex3i(810,210,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(840,200,0);
    glVertex3i(950,200,0);
    glVertex3i(950,170,0);
    glVertex3i(840,170,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(950,210,0);
    glVertex3i(940,210,0);
    glVertex3i(940,260,0);
    glVertex3i(950,260,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(850,210,0);
    glVertex3i(840,210,0);
    glVertex3i(840,250,0);
    glVertex3i(850,250,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(950,250,0);
    glVertex3i(950,270,0);
    glVertex3i(840,270,0);
    glVertex3i(840,250,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(980,280,0);
    glVertex3i(980,270,0);
    glVertex3i(810,270,0);
    glVertex3i(810,280,0);
    glEnd();

    glColor3ub(160, 82, 45);//Sienna
    glBegin(GL_QUADS);
    glVertex3i(970,280,0);
    glVertex3i(950,295,0);
    glVertex3i(840,295,0);
    glVertex3i(820,280,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(810,270,0);
    glVertex3i(820,270,0);
    glVertex3i(815,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(820,270,0);
    glVertex3i(830,270,0);
    glVertex3i(825,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(830,270,0);
    glVertex3i(840,270,0);
    glVertex3i(835,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(840,270,0);
    glVertex3i(850,270,0);
    glVertex3i(845,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(850,270,0);
    glVertex3i(860,270,0);
    glVertex3i(855,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(860,270,0);
    glVertex3i(870,270,0);
    glVertex3i(865,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(870,270,0);
    glVertex3i(880,270,0);
    glVertex3i(875,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(880,270,0);
    glVertex3i(890,270,0);
    glVertex3i(885,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(890,270,0);
    glVertex3i(900,270,0);
    glVertex3i(895,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(900,270,0);
    glVertex3i(910,270,0);
    glVertex3i(905,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(910,270,0);
    glVertex3i(920,270,0);
    glVertex3i(915,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(920,270,0);
    glVertex3i(930,270,0);
    glVertex3i(925,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(930,270,0);
    glVertex3i(940,270,0);
    glVertex3i(935,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(940,270,0);
    glVertex3i(950,270,0);
    glVertex3i(945,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(950,270,0);
    glVertex3i(960,270,0);
    glVertex3i(955,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(960,270,0);
    glVertex3i(970,270,0);
    glVertex3i(965,265,0);
    glEnd();

    glColor3ub(255, 255, 0);//Yellow
    glBegin(GL_TRIANGLES);
    glVertex3i(970,270,0);
    glVertex3i(980,270,0);
    glVertex3i(975,265,0);
    glEnd();
    //Food Cart 02
    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1140,240,0);
    glVertex3i(1120,240,0);
    glVertex3i(1120,290,0);
    glVertex3i(1140,290,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1160,240,0);
    glVertex3i(1140,240,0);
    glVertex3i(1140,290,0);
    glVertex3i(1160,290,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1180,240,0);
    glVertex3i(1160,240,0);
    glVertex3i(1160,290,0);
    glVertex3i(1180,290,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1200,240,0);
    glVertex3i(1180,240,0);
    glVertex3i(1180,290,0);
    glVertex3i(1200,290,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1220,240,0);
    glVertex3i(1200,240,0);
    glVertex3i(1200,290,0);
    glVertex3i(1220,290,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1240,240,0);
    glVertex3i(1220,240,0);
    glVertex3i(1220,290,0);
    glVertex3i(1240,290,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1260,240,0);
    glVertex3i(1240,240,0);
    glVertex3i(1240,290,0);
    glVertex3i(1260,290,0);
    glEnd();

    glColor3ub(255, 99, 71);//Tomato // stand
    glBegin(GL_QUADS);
    glVertex3i(1127,290,0);
    glVertex3i(1133,290,0);
    glVertex3i(1133,330,0);
    glVertex3i(1127,330,0);
    glEnd();

    glColor3ub(255, 99, 71);//Tomato // stand
    glBegin(GL_QUADS);
    glVertex3i(1247,290,0);
    glVertex3i(1253,290,0);
    glVertex3i(1253,330,0);
    glVertex3i(1247,330,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1140,330,0);
    glVertex3i(1120,330,0);
    glVertex3i(1120,370,0);
    glVertex3i(1140,370,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1160,330,0);
    glVertex3i(1140,330,0);
    glVertex3i(1140,370,0);
    glVertex3i(1160,370,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1180,330,0);
    glVertex3i(1160,330,0);
    glVertex3i(1160,370,0);
    glVertex3i(1180,370,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1200,330,0);
    glVertex3i(1180,330,0);
    glVertex3i(1180,370,0);
    glVertex3i(1200,370,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1220,330,0);
    glVertex3i(1200,330,0);
    glVertex3i(1200,370,0);
    glVertex3i(1220,370,0);
    glEnd();

    glColor3ub(255, 140, 0);//Dark Orange
    glBegin(GL_QUADS);
    glVertex3i(1240,330,0);
    glVertex3i(1220,330,0);
    glVertex3i(1220,370,0);
    glVertex3i(1240,370,0);
    glEnd();

    glColor3ub(255, 69, 0);//Orange Red
    glBegin(GL_QUADS);
    glVertex3i(1260,330,0);
    glVertex3i(1240,330,0);
    glVertex3i(1240,370,0);
    glVertex3i(1260,370,0);
    glEnd();


    //Food Cart 03
    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-30,320,0);
    glVertex3i(-170,320,0);
    glVertex3i(-170,330,0);
    glVertex3i(-30,330,0);
    glEnd();

    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-30,260,0);
    glVertex3i(-170,260,0);
    glVertex3i(-170,270,0);
    glVertex3i(-30,270,0);
    glEnd();
    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-45,270,0);
    glVertex3i(-155,270,0);
    glVertex3i(-155,320,0);
    glVertex3i(-45,320,0);
    glEnd();
    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-50,330,0);
    glVertex3i(-55,330,0);
    glVertex3i(-55,390,0);
    glVertex3i(-50,390,0);
    glEnd();
    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-145,330,0);
    glVertex3i(-150,330,0);
    glVertex3i(-150,390,0);
    glVertex3i(-145,390,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_QUADS);
    glVertex3i(-150,390,0);
    glVertex3i(-170,390,0);
    glVertex3i(-170,410,0);
    glVertex3i(-150,410,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_QUADS);
    glVertex3i(-130,390,0);
    glVertex3i(-150,390,0);
    glVertex3i(-150,410,0);
    glVertex3i(-130,410,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_QUADS);
    glVertex3i(-130,390,0);
    glVertex3i(-110,390,0);
    glVertex3i(-110,410,0);
    glVertex3i(-130,410,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_QUADS);
    glVertex3i(-110,390,0);
    glVertex3i(-90,390,0);
    glVertex3i(-90,410,0);
    glVertex3i(-110,410,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_QUADS);
    glVertex3i(-90,390,0);
    glVertex3i(-70,390,0);
    glVertex3i(-70,410,0);
    glVertex3i(-90,410,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_QUADS);
    glVertex3i(-70,390,0);
    glVertex3i(-50,390,0);
    glVertex3i(-50,410,0);
    glVertex3i(-70,410,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_QUADS);
    glVertex3i(-50,390,0);
    glVertex3i(-30,390,0);
    glVertex3i(-30,410,0);
    glVertex3i(-50,410,0);
    glEnd();
    glColor3ub(176, 48, 96);//Maroon
    glBegin(GL_QUADS);
    glVertex3i(-170,410,0);
    glVertex3i(-30,410,0);
    glVertex3i(-60,440,0);
    glVertex3i(-140,440,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_TRIANGLES);
    glVertex3i(-30,390,0);
    glVertex3i(-40,380,0);
    glVertex3i(-50,390,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_TRIANGLES);
    glVertex3i(-50,390,0);
    glVertex3i(-60,380,0);
    glVertex3i(-70,390,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_TRIANGLES);
    glVertex3i(-70,390,0);
    glVertex3i(-80,380,0);
    glVertex3i(-90,390,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_TRIANGLES);
    glVertex3i(-90,390,0);
    glVertex3i(-100,380,0);
    glVertex3i(-110,390,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_TRIANGLES);
    glVertex3i(-110,390,0);
    glVertex3i(-120,380,0);
    glVertex3i(-130,390,0);
    glEnd();
    glColor3ub(219, 112, 147);//Pale Violet Red
    glBegin(GL_TRIANGLES);
    glVertex3i(-130,390,0);
    glVertex3i(-140,380,0);
    glVertex3i(-150,390,0);
    glEnd();
    glColor3ub(255, 182, 193);//Light Pink
    glBegin(GL_TRIANGLES);
    glVertex3i(-150,390,0);
    glVertex3i(-160,380,0);
    glVertex3i(-170,390,0);
    glEnd();
    //Grass
    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(-150,130,0);
    glVertex3i(-160,130,0);
    glVertex3i(-170,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(-110,130,0);
    glVertex3i(-100,130,0);
    glVertex3i(-90,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(-130,130,0);
    glVertex3i(-120,175,0);
    glVertex3i(-110,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(-130,130,0);
    glVertex3i(-140,175,0);
    glVertex3i(-150,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(150,130,0);
    glVertex3i(160,130,0);
    glVertex3i(170,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(110,130,0);
    glVertex3i(100,130,0);
    glVertex3i(90,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(130,130,0);
    glVertex3i(120,175,0);
    glVertex3i(110,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(130,130,0);
    glVertex3i(140,175,0);
    glVertex3i(150,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(350,130,0);
    glVertex3i(360,130,0);
    glVertex3i(370,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(310,130,0);
    glVertex3i(300,130,0);
    glVertex3i(290,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(330,130,0);
    glVertex3i(320,175,0);
    glVertex3i(310,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(330,130,0);
    glVertex3i(340,175,0);
    glVertex3i(350,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(550,130,0);
    glVertex3i(560,130,0);
    glVertex3i(570,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(510,130,0);
    glVertex3i(500,130,0);
    glVertex3i(490,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(530,130,0);
    glVertex3i(520,175,0);
    glVertex3i(510,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(530,130,0);
    glVertex3i(540,175,0);
    glVertex3i(550,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(750,130,0);
    glVertex3i(760,130,0);
    glVertex3i(770,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(710,130,0);
    glVertex3i(700,130,0);
    glVertex3i(690,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(730,130,0);
    glVertex3i(720,175,0);
    glVertex3i(710,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(730,130,0);
    glVertex3i(740,175,0);
    glVertex3i(750,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(950,130,0);
    glVertex3i(960,130,0);
    glVertex3i(970,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(910,130,0);
    glVertex3i(900,130,0);
    glVertex3i(890,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(930,130,0);
    glVertex3i(920,175,0);
    glVertex3i(910,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(930,130,0);
    glVertex3i(940,175,0);
    glVertex3i(950,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1150,130,0);
    glVertex3i(1160,130,0);
    glVertex3i(1170,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1110,130,0);
    glVertex3i(1100,130,0);
    glVertex3i(1090,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1130,130,0);
    glVertex3i(1120,175,0);
    glVertex3i(1110,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1130,130,0);
    glVertex3i(1140,175,0);
    glVertex3i(1150,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1350,130,0);
    glVertex3i(1360,130,0);
    glVertex3i(1370,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1310,130,0);
    glVertex3i(1300,130,0);
    glVertex3i(1290,165,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1330,130,0);
    glVertex3i(1320,175,0);
    glVertex3i(1310,130,0);
    glEnd();

    glColor3ub(34, 139, 34);//Forest Green
    glBegin(GL_TRIANGLES);
    glVertex3i(1330,130,0);
    glVertex3i(1340,175,0);
    glVertex3i(1350,130,0);
    glEnd();

}


//dynamic lamp post function
void lampPost(int x,int y,int z)
{
    //verticle
    glColor3ub(222,250,50);
    glBegin(GL_QUADS);
    glVertex3i(x,y,z);
    glVertex3i(x+7,y,z);
    glVertex3i(x+7,y+100,z);
    glVertex3i(x,y+100,z);
    glEnd();

    //horizontal
    glColor3ub(222,250,50);
    glBegin(GL_QUADS);
    glVertex3i(x,y+93,z);
    glVertex3i(x+70,y+93,z);
    glVertex3i(x+70,y+100,z);
    glVertex3i(x,y+100,z);
    glEnd();

    //lightcarry
    glColor3ub(222,250,50);
    glBegin(GL_TRIANGLES);
    glVertex3i(x+50,y+85,z);
    glVertex3i(x+70,y+85,z);
    glVertex3i(x+60,y+93,z);
    glEnd();
}


void toplampPost(int x,int y,int z)//Mursalin Khan
{
    otherCircle(x+60,y+3,0,5,222,250,50);
    glColor3ub(222,250,50);
    glBegin(GL_QUADS);
    glVertex3i(x,y,z);
    glVertex3i(x+70,y,z);
    glVertex3i(x+70,y+5,z);
    glVertex3i(x,y+5,z);
    glEnd();
}
//Car

void topCar()//Mursalin Khan
{
    static float a=-400.0f;
    if(a>=1324)
    {
        a=-500.0f;

    }
    else
    {
        a+=0.5f;
        //glColor3ub(r,g,b);
    }
    glPushMatrix();
    glTranslatef(a,0,0);
    otherCircle(-100,18,0,23,255,0,0);
    otherCircle(-130,18,0,23,255,0,0);
    glColor3ub(255,0,0);
    glBegin(GL_QUADS);
    glVertex3i(-100,0,0);
    glVertex3i(-135,0,0);
    glVertex3i(-135,40,0);
    glVertex3i(-100,40,0);
    glEnd();
    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(-105,5,0);
    glVertex3i(-90,10,0);
    glVertex3i(-90,30,0);
    glVertex3i(-105,35,0);
    glEnd();

    glPopMatrix();
    glutPostRedisplay();
}

void setFont(void *font)//Mursalin Khan
{
    currentfont=font;
}

void drawstring(float x,float y,float z,char *string)//Mursalin Khan
{
    char *c;
    glRasterPos3f(x,y,z);

    for(c=string; *c!='\0'; c++)
    {
        glutBitmapCharacter(currentfont,*c);
    }
}
void Full(int r,int g,int b)//Mursalin Khan
{
    glColor3ub(r,g,b);
    glBegin(GL_QUADS);
    glVertex3i(-200,0,0);
    glVertex3i(1324,0,0);
    glVertex3i(1324,768,0);
    glVertex3i(-200,768,0);
}
void RoadLine(int x,int y,int z)//Mursalin Khan
{
    glColor3ub(255,255,255);
    glBegin(GL_QUADS);
    glVertex3i(x,y,z);
    glVertex3i(x+50,y,z);
    glVertex3i(x+50,y+10,z);
    glVertex3i(x,y+10,z);
    glEnd();
    //Sleep(50);
    //TranslateRoadLine(x,y,z);
}

void myInit (void)//Mursalin Khan
{
    glClearColor(1.0, 1.0, 1.0, 0.0);
    glColor3f(0.0f, 0.0f, 0.0f);
    glPointSize(2.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 1024, 0.0, 768.0);
}
void topView(int x,int y,int z)//Mursalin Khan
{
    int roadlineX=-300;
    int LamppostX=-350;
    int treeXf=-350;
    int treeXl=528;
//    Road
    glColor3ub(58,58,58);
    glBegin(GL_QUADS);
    glVertex3i(-200,0,0);
    glVertex3i(1324,0,0);
    glVertex3i(1324,100,0);
    glVertex3i(-200,100,0);
    glEnd();

    for(int i=25; i>0; i--)
    {
        roadlineX+=100;
        RoadLine(roadlineX,40,0);
    }
    //RoadBorder
    glColor3ub(255,255,255);
    glBegin(GL_QUADS);
    glVertex3i(-200,95,0);
    glVertex3i(1324,95,0);
    glVertex3i(1324,110,0);
    glVertex3i(-200,110,0);
    glEnd();

    for(int i=10; i>0; i--)
    {
        toplampPost(LamppostX,100,0);
        LamppostX+=310;
    }
    topCar();
    //topTruck();
    //PlayGround
    glColor3ub(52,135,37);
    glBegin(GL_QUADS);
    glVertex3i(-200,110,0);
    glVertex3i(1324,110,0);
    glVertex3i(1324,240,0);
    glVertex3i(-200,240,0);
    glEnd();
    //walkway
    glColor3ub(150,90,50);
    glBegin(GL_QUADS);
    glVertex3i(-200,240,0);
    glVertex3i(1324,240,0);
    glVertex3i(1324,260,0);
    glVertex3i(-200,260,0);
    glEnd();
    //Tree
    for(int i=5; i>=0; i--)
    {
        treeXf+=120;
        otherCircle(treeXf,250,0,10,70,180,50);

    }
    for(int i=5; i>=0; i--)
    {
        treeXl+=120;
        otherCircle(treeXl,250,0,10,70,180,50);

    }
    //Top Tin Shade
//    a1
    //left
    glColor3ub(42,85,66);
    glBegin(GL_QUADS);
    glVertex3i(0,260,0);
    glVertex3i(396,260,0);
    glVertex3i(396,360,0);
    glVertex3i(0,360,0);
    glEnd();
    glColor3ub(25,25,25);
    glBegin(GL_QUADS);
    glVertex3i(-200,260,0);
    glVertex3i(0,260,0);
    glVertex3i(0,320,0);
    glVertex3i(-200,320,0);
    glEnd();
    //right
    glColor3ub(42,85,66);
    glBegin(GL_QUADS);
    glVertex3i(628,260,0);
    glVertex3i(1324,260,0);
    glVertex3i(1324,360,0);
    glVertex3i(628,360,0);
    glEnd();
    //white shade bottom
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(0,260,0);
    glVertex3i(1324,260,0);
    glVertex3i(1324,265,0);
    glVertex3i(0,265,0);
    glEnd();
    //white shade top
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(0,360,0);
    glVertex3i(1324,360,0);
    glVertex3i(1324,355,0);
    glVertex3i(0,355,0);
    glEnd();
    //middle
    glColor3ub(42,105,86);
    glBegin(GL_QUADS);
    glVertex3i(396,255,0);
    glVertex3i(628,255,0);
    glVertex3i(628,365,0);
    glVertex3i(396,365,0);
    glEnd();
    //white shade middle
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(396,255,0);
    glVertex3i(628,255,0);
    glVertex3i(628,260,0);
    glVertex3i(396,260,0);
    glEnd();
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(396,360,0);
    glVertex3i(628,360,0);
    glVertex3i(628,365,0);
    glVertex3i(396,365,0);
    glEnd();
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(396,255,0);
    glVertex3i(400,255,0);
    glVertex3i(400,365,0);
    glVertex3i(396,365,0);
    glEnd();
    glColor3ub(242,255,255);
    glBegin(GL_QUADS);
    glVertex3i(624,255,0);
    glVertex3i(628,255,0);
    glVertex3i(628,365,0);
    glVertex3i(624,365,0);
    glEnd();
//    A2
    glColor3ub(42,85,45);
    glBegin(GL_QUADS);
    glVertex3i(-200,320,0);
    glVertex3i(0,320,0);
    glVertex3i(0,410,0);
    glVertex3i(-200,410,0);
    glEnd();
//    white shade
    //bottom
    glColor3ub(255,255,225);
    glBegin(GL_QUADS);
    glVertex3i(-200,320,0);
    glVertex3i(0,320,0);
    glVertex3i(0,325,0);
    glVertex3i(-200,325,0);
    glEnd();
//    top
    glColor3ub(255,255,225);
    glBegin(GL_QUADS);
    glVertex3i(-200,405,0);
    glVertex3i(0,405,0);
    glVertex3i(0,410,0);
    glVertex3i(-200,410,0);
    glEnd();
    //Right
    glColor3ub(255,255,225);
    glBegin(GL_QUADS);
    glVertex3i(-5,260,0);
    glVertex3i(0,260,0);
    glVertex3i(0,410,0);
    glVertex3i(-5,410,0);
    glEnd();
    //Coridor
    glColor3ub(40,90,100);
    glBegin(GL_QUADS);
    glVertex3i(0,340,0);
    glVertex3i(100,340,0);
    glVertex3i(100,400,0);
    glVertex3i(0,400,0);
    glEnd();
    //Middle Coridor Top
    glColor3ub(42,105,85);
    glBegin(GL_QUADS);
    glVertex3i(0,400,0);
    glVertex3i(200,400,0);
    glVertex3i(200,410,0);
    glVertex3i(0,410,0);
    glEnd();
//    middle coridor Top
    glColor3ub(42,105,85);
    glBegin(GL_QUADS);
    glVertex3i(0,410,0);
    glVertex3i(200,410,0);
    glVertex3i(200,510,0);
    glVertex3i(0,510,0);
    glEnd();
    ///garden front
    glColor3ub(0,255,0);
    glBegin(GL_QUADS);
    glVertex3i(250,410,0);
    glVertex3i(290,410,0);
    glVertex3i(290,550,0);
    glVertex3i(250,550,0);
    glEnd();
    ///pool
    glColor3ub(0,255,0);
    glBegin(GL_POLYGON);
    glVertex3i(350,410,0);
    glVertex3i(650,410,0);
    glVertex3i(650,550,0);
    glVertex3i(350,550,0);
    glEnd();
//    a3
    glColor3ub(42,95,45);
    glBegin(GL_QUADS);
    glVertex3i(-200,510,0);
    glVertex3i(200,510,0);
    glVertex3i(200,770,0);
    glVertex3i(-200,770,0);
    glEnd();

//    A4


    glColor3ub(42,95,45);
    glBegin(GL_QUADS);
    glVertex3i(100,610,0);
    glVertex3i(300,610,0);
    glVertex3i(300,770,0);
    glVertex3i(100,770,0);
    glEnd();
    //roadline
    glColor3ub(42,105,85);
    glBegin(GL_QUADS);
    glVertex3i(300,610,0);
    glVertex3i(500,610,0);
    glVertex3i(500,650,0);
    glVertex3i(300,650,0);
    glEnd();

//    a 5
    glColor3ub(42,85,45);
    glBegin(GL_QUADS);
    glVertex3i(500,610,0);
    glVertex3i(700,610,0);
    glVertex3i(700,770,0);
    glVertex3i(500,770,0);
    glEnd();

    //Ashiq Chattor
    glColor3ub(42,90,45);
    glBegin(GL_QUADS);
    glVertex3i(700,610,0);
    glVertex3i(800,610,0);
    glVertex3i(800,650,0);
    glVertex3i(700,650,0);
    glEnd();

    glColor3ub(42,85,45);
    glBegin(GL_QUADS);
    glVertex3i(750,610,0);
    glVertex3i(900,610,0);
    glVertex3i(900,770,0);
    glVertex3i(750,770,0);
    glEnd();



    drawFilledCircle(1000,520,0,110,177);

}
void roadBorder()
{
    glColor3ub(255,255,255);
    glBegin(GL_QUADS);
    glVertex3i(-200,120,0);
    glVertex3i(1324,120,0);
    glVertex3i(1324,130,0);
    glVertex3i(-200,130,0);
    glEnd();
}
//void circleLine()
//{
//    glColor3ub(240,240,240);
//    glBegin(GL_LINES);
//    glLineWidth(5.0f);
//    glVertex3i(780,500,0);
//    glVertex3i(1120,500,0);
//    glVertex3i(788,550,0);
//    glVertex3i(1112,550,0);
//    glVertex3i(812,600,0);
//    glVertex3i(1088,600,0);
//    glVertex3i(788,450,0);
//    glVertex3i(1112,450,0);
//    glVertex3i(812,400,0);
//    glVertex3i(1088,400,0);
//    glEnd();
//}
void truck()
{
    static float a=650.0f;
    if(a<=-1300)
    {
        a=550.0f;

    }
    else
    {
        a-=0.2f;
        //glColor3ub(r,g,b);
    }
    glColor3ub(0,0,255);
    //frontbumper
    glPushMatrix();
    glTranslatef(a,0,0);
    otherCircle(780.0f,130.0f,0.0f,41.0f,0,0,255);
    //main body
    glBegin(GL_QUADS);
    glVertex3i(750,90,0);
    glVertex3i(1000,90,0);
    glVertex3i(1000,140,0);
    glVertex3i(750,140,0);
    glEnd();


    glBegin(GL_QUADS);
    glVertex3i(750,140,0);
    glVertex3i(860,140,0);
    glVertex3i(860,160,0);
    glVertex3i(750,160,0);
    glEnd();
    //window
    glBegin(GL_QUADS);
    glVertex3i(750,160,0);
    glVertex3i(860,160,0);
    glVertex3i(860,190,0);
    glVertex3i(800,190,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(760,160,0);
    glVertex3i(855,160,0);
    glVertex3i(855,185,0);
    glVertex3i(800,185,0);
    glEnd();

    //handle
    glBegin(GL_QUADS);
    glVertex3i(840,145,0);
    glVertex3i(855,145,0);
    glVertex3i(855,150,0);
    glVertex3i(840,150,0);
    glEnd();

    //gril
    glColor3ub(0,0,0);
    glBegin(GL_LINES);
    glVertex3i(860,160,0);
    glVertex3i(1000,160,0);
    glVertex3i(860,159,0);
    glVertex3i(1000,159,0);
    glVertex3i(1000,160,0);
    glVertex3i(1000,140,0);
    glVertex3i(990,160,0);
    glVertex3i(990,140,0);
    glVertex3i(980,160,0);
    glVertex3i(980,140,0);
    glVertex3i(970,160,0);
    glVertex3i(970,140,0);
    glVertex3i(960,160,0);
    glVertex3i(960,140,0);
    glVertex3i(950,160,0);
    glVertex3i(950,140,0);
    glVertex3i(940,160,0);
    glVertex3i(940,140,0);
    glVertex3i(930,160,0);
    glVertex3i(930,140,0);
    glVertex3i(920,160,0);
    glVertex3i(920,140,0);
    glVertex3i(910,160,0);
    glVertex3i(910,140,0);
    glVertex3i(900,160,0);
    glVertex3i(900,140,0);
    glVertex3i(890,160,0);
    glVertex3i(890,140,0);
    glVertex3i(880,160,0);
    glVertex3i(880,140,0);
    glVertex3i(870,160,0);
    glVertex3i(870,140,0);
    glEnd();



    //wheel
    otherCircle(800.0f,90.0f,0.0f,21.0f,0,0,0);
    otherCircle(800.0f,90.0f,0.0f,15.0f,131,131,131);
    otherCircle(950.0f,90.0f,0.0f,21.0f,0,0,0);
    otherCircle(950.0f,90.0f,0.0f,15.0f,131,131,131);

    //backlight
    glColor3ub(255,0,0);
    glBegin(GL_QUADS);
    glVertex3i(1000,110,0);
    glVertex3i(1005,110,0);
    glVertex3i(1005,120,0);
    glVertex3i(1000,120,0);
    glEnd();

    //frontlignt
    glColor3ub(255,255,0);
    glBegin(GL_QUADS);
    glVertex3i(740,90,0);
    glVertex3i(750,90,0);
    glVertex3i(750,102,0);
    glVertex3i(740,102,0);
    glEnd();
}
void tprint(int x, int y,int z, char *string)
{
//set the position of the text in the window using the x and y coordinates
    glRasterPos2f(x,y);
//get the length of the string to display
    int len = (int) strlen(string);



//loop to display character by character
    for (int i = 0; i < len; i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,string[i]);
    }
};
void ttprint(int x, int y,int z, char *string)
{
    //set the position of the text in the window using the x and y coordinates
    glRasterPos2f(x,y);
    //get the length of the string to display
    int len = (int) strlen(string);

    //loop to display character by character
    for (int i = 0; i < len; i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,string[i]);
    }
};

void car()
{
    static float a=-400.0f;
    if(a>=1324)
    {
        a=-400.0f;

    }
    else
    {
        a+=0.2f;
        //glColor3ub(r,g,b);
    }
    glColor3ub(255,0,0);
    glPushMatrix();
    glTranslatef(a,0,0);
    glBegin(GL_QUADS);
    glVertex3i(20,40,0);
    glVertex3i(220,40,0);
    glVertex3i(220,80,0);
    glVertex3i(20,80,0);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3i(40,80,0);
    glVertex3i(200,80,0);
    glVertex3i(160,110,0);
    glVertex3i(80,110,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(115,80,0);
    glVertex3i(190,80,0);
    glVertex3i(155,105,0);
    glVertex3i(115,105,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(45,80,0);
    glVertex3i(110,80,0);
    glVertex3i(110,105,0);
    glVertex3i(80,105,0);
    glEnd();

    //handle
    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(115,70,0);
    glVertex3i(135,70,0);
    glVertex3i(135,75,0);
    glVertex3i(115,75,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(45,70,0);
    glVertex3i(65,70,0);
    glVertex3i(65,75,0);
    glVertex3i(45,75,0);
    glEnd();

    //backbumper
    otherCircle(30.0f,60.0f,0.0f,19.0f,255,0,0);
    //front bumper
    otherCircle(210.0f,60.0f,0.0f,19.0f,255,0,0);

//Light
    glColor3ub(250,250,0);
    glBegin(GL_QUADS);
    glVertex3i(225,55,0);
    glVertex3i(230,55,0);
    glVertex3i(230,65,0);
    glVertex3i(225,65,0);
    glEnd();

    //carlight
    if(day==2)
    {
        glColor3ub(200,200,200);
        glBegin(GL_QUADS);
        glVertex3i(230,55,0);
        glVertex3i(280,20,0);
        glVertex3i(280,95,0);
        glVertex3i(225,65,0);
        glEnd();
    }

    otherCircle(60.0f,40.0f,0.0f,18.0f,0,0,0);
    otherCircle(60.0f,40.0f,0.0f,10.0f,137,137,137);
    otherCircle(170.0f,40.0f,0.0f,18.0f,0,0,0);
    otherCircle(170.0f,40.0f,0.0f,10.0f,137,137,137);

    glPopMatrix();
    glutPostRedisplay();
}


void car2()
{
    static float a=-1100.0f;
    if(a>=1324)
    {
        a=-1100.0f;

    }
    else
    {
        a+=0.2f;
        //glColor3ub(r,g,b);
    }
    glColor3ub(0,0,255);
    glPushMatrix();
    glTranslatef(a,0,0);
    glBegin(GL_QUADS);
    glVertex3i(20,40,0);
    glVertex3i(220,40,0);
    glVertex3i(220,80,0);
    glVertex3i(20,80,0);
    glEnd();

    glBegin(GL_QUADS);
    glVertex3i(40,80,0);
    glVertex3i(200,80,0);
    glVertex3i(160,110,0);
    glVertex3i(80,110,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(115,80,0);
    glVertex3i(190,80,0);
    glVertex3i(155,105,0);
    glVertex3i(115,105,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(45,80,0);
    glVertex3i(110,80,0);
    glVertex3i(110,105,0);
    glVertex3i(80,105,0);
    glEnd();

    //handle
    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(115,70,0);
    glVertex3i(135,70,0);
    glVertex3i(135,75,0);
    glVertex3i(115,75,0);
    glEnd();

    glColor3ub(0,0,0);
    glBegin(GL_QUADS);
    glVertex3i(45,70,0);
    glVertex3i(65,70,0);
    glVertex3i(65,75,0);
    glVertex3i(45,75,0);
    glEnd();

    //backbumper
    otherCircle(30.0f,60.0f,0.0f,19.0f,0,0,255);
    //front bumper
    otherCircle(210.0f,60.0f,0.0f,19.0f,0,0,255);

    //Light
    glColor3ub(250,250,0);
    glBegin(GL_QUADS);
    glVertex3i(225,55,0);
    glVertex3i(230,55,0);
    glVertex3i(230,65,0);
    glVertex3i(225,65,0);
    glEnd();

    //carlight
    if(day==2)
    {
        glColor3ub(200,200,200);
        glBegin(GL_QUADS);
        glVertex3i(230,55,0);
        glVertex3i(280,20,0);
        glVertex3i(280,95,0);
        glVertex3i(225,65,0);
        glEnd();
    }

    otherCircle(60.0f,40.0f,0.0f,18.0f,0,0,0);
    otherCircle(60.0f,40.0f,0.0f,10.0f,137,137,137);
    otherCircle(170.0f,40.0f,0.0f,18.0f,0,0,0);
    otherCircle(170.0f,40.0f,0.0f,10.0f,137,137,137);

    glPopMatrix();
    glutPostRedisplay();
}

void rainf()
{
    int x=0;
    int y=778;
    static float a=-760.0f;
    if(a<=-768)
    {
        a=-760.0f;

    }
    else
    {
        a-=0.5f;
        //glColor3ub(r,g,b);
    }
    glColor3ub(255,255,255);
    glPushMatrix();
    glTranslatef(0.0f,a,0.0f);
    glBegin(GL_LINES);

    for(int i=500; i>=0; i--)
    {
        for(int j=0; j<=i; j++)
        {
            glVertex3i(x,y,0);
            glVertex3i(x+3,y+10,0);
            x+=rand()%1050;
        }
        y+=rand()%15;
        x=0;

    }
    glEnd();
    glPopMatrix();
    glutPostRedisplay();

}

int snow(float x, float y, float r)
{
    int i;
    int triangleAmount=100;
    GLfloat twicePi=2.0f*3.1416;
    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0f,1.0f,1.0f);
    glVertex2f(x,y);
    for(i=0; i<triangleAmount; i++)
    {
        glVertex2f(x+(r*cos(i*twicePi/triangleAmount)),y+(r*sin(i*twicePi/triangleAmount)));
    }
    glEnd();
    glFlush();
}



GLfloat position = 768.0f;
GLfloat speed = 0.05f;
void update(int value)
{



    if(position <=-768.0)
        position = -760.0f;



    position -= speed;



    glutPostRedisplay();
    glutTimerFunc(100, update, 0);
}
void winterf()
{
    glPushMatrix();
    glTranslatef(position,position, 0.0f);
    snow(150.0f,100.0f,5.0f);
    snow(-100.0f,95.0f,5.0f);
    snow(175.0f,150.0f,5.0f);
    snow(-200.0f,180.0f,5.0f);
    snow(-150.0f,75.0f,5.0f);
    snow(-185.0f,190.0f,5.0f);
    snow(250.0f,55.0f,5.0f);
    snow(1000.0f,65.0f,5.0f);
    snow(1200.0f,150.0f,5.0f);
    snow(300.0f,100.0f,5.0f);
    snow(450.0f,95.0f,5.0f);
    snow(550.0f,150.0f,5.0f);
    snow(1250.0f,300.0f,5.0f);
    int    x=150;int y=100;
    for(int i=500; i>=0; i--)
    {
        for(int j=0; j<=i; j++)
        {
            glVertex3i(x,y,0);
            glVertex3i(x+3,y+10,0);
            x+=rand()%1050;
        }
        y+=rand()%15;
        x=0;

    }
    glPopMatrix();
    glutTimerFunc(100, update, 0);
    glFlush();

}
void dayMode()
{
    int roadlineX=-300;
    int treeXf=-350;
    int treeXl=528;
    int lamp=-350;
    int light=-350;

    Full(131,183,231);
    //Road
    Road();
    //RoadLine
    for(int i=55; i>0; i--)
    {
        roadlineX+=100;
        RoadLine(roadlineX,55,0);
    }
    //cloud0
    clouds(-100.0f,630.0f,0.0f,250,250,250);
    //cloud1
    clouds(150.0f,670.0f,0.0f,250,250,250);
    if(planev)
    {
        plane();
        planeTwo();
    }
    //sun
    Circle(750.0f,700.0f,0.0f,50.0f,255,255,0);
    //cloud2
    clouds(450.0f,600.0f,0.0f,250,250,250);
    //cloud3
    clouds(750.0f,690.0f,0.0f,250,250,250);
    //cloud4
    clouds(1050.0f,710.0f,0.0f,250,250,250);
    //Play Ground
    playGround(107, 142, 35);
    for(int i=9; i>=0; i--)
    {
        lamp+=310;
        lampPost(lamp,130,0);
    }

    roadBorder();

    glColor3ub(255, 218, 185); //Peach Puff
    ttprint(870,180,0,"Juice");

    glColor3ub(139, 69, 19); //Chocolate4
    ttprint(1145,255,0,"Pop Corn");

    glColor3ub(255, 192, 203); //Pink
    ttprint(-150,290,0,"Ice Cream");

    if(carv)
    {
        truck();
        car();
        car2();
    }
    glPopMatrix();

    if(rain)
    {
        rainf();
    }
    if(winter)
    {
        winterf();
    }
}
void nightMode()
{
    int roadlineX=-300;
    int treeXf=-350;
    int treeXl=528;
    int lamp=-350;
    int light=-350;

    Full(0,0,0);
    //Road
    Road();
    //RoadLine
    for(int i=55; i>0; i--)
    {
        roadlineX+=100;
        RoadLine(roadlineX,55,0);
    }

    //cloud0
    clouds(-100.0f,630.0f,0.0f,105,105,105);
    //cloud1
    clouds(150.0f,670.0f,0.0f,105,105,105);
    if(planev)
    {
        plane();
        planeTwo();
    }
    //Moon
    Circle(750.0f,700.0f,0.0f,40.0f,255,255,255);
    //cloud2
    clouds(450.0f,600.0f,0.0f,105,105,105);
    //cloud3
    clouds(750.0f,690.0f,0.0f,105,105,105);
    //cloud4
    //clouds(1050.0f,710.0f,0.0f,105,105,105);
    //Play Ground
    playGround(42,95,17);

    for(int i=9; i>=0; i--)
    {
        lamp+=310;
        lampPost(lamp,130,0);
    }
    //light
    roadBorder();

    glColor3ub(255, 218, 185); //Peach Puff
    ttprint(870,180,0,"Juice");

    glColor3ub(139, 69, 19); //Chocolate4
    ttprint(1145,255,0,"Pop Corn");

    glColor3ub(255, 192, 203); //Pink
    ttprint(-150,290,0,"Ice Cream");
    //TinShade();
    //circleLine();
    glColor3ub(0,0,255);
    //ttprint(330,433,0,"Antu");
    if(carv)
    {
        truck();
        car();
        car2();
    }
    glPopMatrix();

    if(rain)
    {
        rainf();
    }
    if(winter)
    {
        winterf();
    }
}
void topViewf()//Mursalin Khan
{
    Full(181,153,131);
    topView(0,0,0);
    glPopMatrix();

}
void startscreen(void)//Mursalin Khan
{
    setFont(GLUT_BITMAP_TIMES_ROMAN_24);
    glClearColor(0.000, 0.000, 0.000,0);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0,1,0);
    drawstring(200.0,700.0,0.0,"AMERICAN INTERNATIONAL UNIVERSITY-BANGLADESH");
    glColor3f(0,0,1);
    drawstring(200,650,0.0,"FACULTY OF SCIENCE AND INFORMATION TECHNOLOGY");
    glColor3f(0.7,0.7,0.7);
    drawstring(450,530,0.0,"PROJECT ON");
    drawstring(250,500,0.0,"COMPUTER GRAPHICS: Amusement Parks");
    glColor3f(1,0.5,0);
    drawstring(100,400,0.0,"SUBMITTED BY:");
    glColor3f(1,1,1);
    drawstring(100,370,0.0,"MURSALIN KHAN                   (20-43035-1)");
    drawstring(100,340,0.0,"ABRAR SHAHRIAR AYON     (20-42146-1)");
    drawstring(100,310,0.0,"MARZANA BINTAY TUBA    (20-42158-1)");
    drawstring(100,280,0.0,"MD.ISTIAQ AHMED                (20-43788-2)");
    drawstring(100,250,0.0,"RUBAIBA HOSSAIN                (20-42148-1)");
//   drawstring(100,290,0.0,"");
//   drawstring(100,210,0.0,"");
//   drawstring(100,130,0.0,"");
    glColor3f(1,0.5,0);
    drawstring(700,400,0.0,"SUBMITTED TO:");
    glColor3f(1,1,1);
    drawstring(660,370,0.0,"DR. MD SIYAMUL ISLAM");
    glColor3f(0,1,0);
    drawstring(400,80,0.0,"PRESS ENTER TO START");
    glFlush();
}
void controlsScreen()//Mursalin Khan
{
    setFont(GLUT_BITMAP_TIMES_ROMAN_24);
    glClearColor(0.000, 0.000, 0.000,0);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.596, 0.984, 0.596);
    drawstring(370.0,700.0,0.0,"INSTRUCTIONS");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,640.0,0.0,"DAY MODE");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,640.0,0.0,"PRESS 'D'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,640.0,0.0,"DAY MODE");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,640.0,0.0,"PRESS 'D'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,600.0,0.0,"NIGHT MODE");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,600.0,0.0,"PRESS 'N'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,560.0,0.0,"CAR MOVING");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,560.0,0.0,"PRESS 'C'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,520.0,0.0,"RAIN MODE");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,520.0,0.0,"PRESS 'R'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,480.0,0.0,"NO RAIN");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,480.0,0.0,"PRESS 'E'");
    glColor3f(1.000, 0.980, 0.941);
    //Winter
    drawstring(250.0,520.0,0.0,"Winter MODE");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,520.0,0.0,"PRESS 'W'");
    glColor3f(1.000, 0.980, 0.941);
    //////
    drawstring(250.0,440.0,0.0,"TOP VIEW");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,440.0,0.0,"PRESS 'T'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,400.0,0.0,"PLANE MOVEMENT");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,400.0,0.0,"PRESS 'P'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,360.0,0.0,"Help");

    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,360.0,0.0,"PRESS 'H'");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(250.0,320.0,0.0,"Escape");
    glColor3f(1.000, 0.980, 0.941);
    drawstring(600.0,320.0,0.0,"PRESS 'ESC'");
    glColor3f(0.596, 0.984, 0.596);
    drawstring(360.0,200.0,0.0,"NOW PRESS ENTER");
    glFlush();
}

void display()//Mursalin Khan
{
    glPushMatrix();
    glTranslatef(translate_x,translate_y,translate_z);

    if(day==2)
    {
        nightMode();
    }
    else if(day==1)
    {
        //startscreen();
        //controlsScreen();

        dayMode();
        //topViewf();
    }

     else if(day==3)
     {
         topViewf();
         //dayMode();

     }

    glFlush();
    glutSwapBuffers();
}
//Main Display Function
void myDisplay()//Mursalin Khan
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    if(flag==0)
    {
        startscreen();
        //controlsScreen();
        //display();

    }
    if(flag==1)
        controlsScreen();

    if(flag>1)
        display();

    glFlush();
    glutSwapBuffers();

    //1 front view (name) controlsScreen();
    //2  instruction controlsScreen();
    //3 2d view display();
}
void keyboard(unsigned char key, int x, int y)//Mursalin Khan
{
    if(key=='d')
    {
        day=1;
    }
    else if(key=='n')
    {
        day=2;
    }
    else if(key=='t')
    {
        day=3;
    }
    else if(key=='r')
    {
        rain=true;
    }

    else if(key=='w')
    {
        winter=true;
    }

    else if(key=='e')
    {
        rain=false;
    }
    else if(key=='c')
    {
        carv=true;
    }
    else if(key=='v')
    {
        carv=false;
    }
    else if(key=='p')
    {
        planev=true;
    }
    else if(key=='o')
    {
        planev=false;
    }
    else if(key==13)
    {
        flag++;
        myDisplay();
    }
    else if(key=='h')
    {
        flag=1;
        myDisplay();
    }
    else if(key==27)
    {
        exit(0);
    }

}
void SpecialKeys(int key, int x, int y)//Mursalin Khan
{
    switch (key)
    {
    case GLUT_KEY_LEFT:
        if(translate_x<200)
        {
            translate_x+=5;
            glutPostRedisplay();
        }
        break;

    case GLUT_KEY_RIGHT:
        if(translate_x>-300)
        {
            translate_x-=5;
            glutPostRedisplay();
        }
        break;

    case GLUT_KEY_UP:
        spin-=5;
        if(spin>=360)
        {
            spin=0;
        }
        glutPostRedisplay();
        break;

    case GLUT_KEY_DOWN:
        spin+=5;
        if(spin<=360)
        {
            spin=0;
        }
        glutPostRedisplay();
        break;
    }
}

int main(int argc, char** argv)//Mursalin Khan
{
    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize (1024, 768);
    glutInitWindowPosition (0, 0);
    glutCreateWindow ("Amusement Parks");
    myInit();
    glutDisplayFunc(myDisplay);
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(SpecialKeys);
    glutMainLoop();
    return 0;
}

