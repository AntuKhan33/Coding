
#this is comment
for (x in 1:10){
  print(x)
}

name <- "jon"

name

for (x in 1:10){
  print(x)
}

text1<-"i am awesome"
text2<-"i am good"

paste("i am good and ",text)

text <- "awesome"

paste("R is", text)

paste(text1,text2)

num1 <- 10
num2 <- 20
num1+num2

x<-y<-z<-10L

x

y
z
class(text1)
class(x)

x<-10.5
class(x)
x<-10L
class(x)
as.numeric(x)
as.integer(x)
as.complex(x)
class(x)
max(5,1,2,3,4,9,6,7)
min(5,1,2,3,4,9,6,7)
sqrt(16)
sqrt(3.7)
abs(-4.7)
ceiling(3.7)
floor(2.2)
str <- "Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."
str
cat(str)
nchar(str)

grepl("H",str)

str<-"we are the so called \" vikings\",from the northm"
str
cat(str)
var<-3
var<<-3
3->var
3->>var

a <- 200
b <- 33
c <- 500
if (b > a) {
  print("b is greater than a")
} else if (a == b) {
  print("a and b are equal")
} else {
  print("a is greater than b")
}

if (a>b | c>a)
{
  print("Both Condition are true")
  
}

i<-1

while(i<6){
  
  print(i)
  i<-i+1
  if(i==4){
    next
  }
  
}

for(x in 1:10){
  print(x)
}

fruits<- list("Apple","banana","Cherry")

for (x in fruits){
  print(x)}

my_function <- function (fname)
{
  print("hello world")
  paste(fname,"grifin")
}
my_function("antu")
my_function2 <-function(fname,lname){
  
  paste(fname,lname)
}
my_function2("antu","khan")

country <- function(country1="BD"){
  paste("i am from ",country1)
}
country("India")
country()
