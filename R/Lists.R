thislist<- list("apple", "banana","Cherry")

thislist[1]<- "blackberry"
thislist
length(thislist)
"apple" %in% thislist
"banana" %in% thislist

append(thislist ,"orange")
thislist
thislist <- list("apple", "banana", "cherry")

append(thislist, "orange",after=2)

thislist

newlist <- thislist [-1]

newlist
thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
thislist[1:5]
for (x in thislist){
  print(x)
}
list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3<- c(list1,list2)
list3
paste(list1,list2)
