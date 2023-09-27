billTotal= float(input("Enter Bill total: ")) #asks user total of the bill
tip15= 0.15*billTotal
tip18 = 0.18*billTotal     #calculates all tip percentages
tip20 = 0.20*billTotal
tip25 = 0.25*billTotal
total15 = billTotal + tip15
total18 = billTotal + tip18
total20 = billTotal+ tip20      #calculates total of bill + tip for each percentage
total25 = billTotal + tip25
print (f"15%: /(Tip : {tip15:.2f}  Total: {total15:.2f})")
print (f"18%: /(Tip : {tip18:.2f}  Total: {total18:.2f})")
print (f"20%: /(Tip : {tip20:.2f}  Total: {total20:.2f})")      #shows tip percentage and bill total to user
print (f"25%: /(Tip : {tip25:.2f}  Total: {total25:.2f})")