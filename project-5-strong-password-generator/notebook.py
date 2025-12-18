fruits = ["Apple","Orange","Mango","Pineapple"]
print(fruits)

print("for starts")
for fruit in fruits:
    print(fruit)
print("for ends")

student_scores = [1,2,3,4,5,6,7,8,9,0,5,8,2,6]
print(student_scores)
print(sum(student_scores))
print(max(student_scores))

max_val = 0
for score in student_scores:
    if score > max_val:
        max_val = score

print(max_val)

for num in range(1,100):
    print(num)

total = 0;
for num in range(4, 100,4):
    total+=num
print(total)