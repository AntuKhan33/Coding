omega={(i,j) for i in range(1,7) for j in range(1,7)}

sum_gt_10={ pair for pair in omega if pair[0]+pair[1]>10}
x=len(sum_gt_10)
print(x)
print(f"Probability: {len(sum_gt_10)/len(omega):.2f}")


desc = "Playway: Playway is a producer of computer games."
word_list=desc.lower().replace(":",'').replace(".",'').split()
word_unique={word for word in word_list}
print(len(word_unique))
 
for x in range(1,7):
    for y in range(1,7):
        print(x,y)
        
