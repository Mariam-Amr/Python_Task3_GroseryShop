
shop={"products":[["apples",20,"Cost in EGP =",35],["bannaa",30,"Cost in EGP =",15],["cherry",50,"Cost in EGP =",55]]}
while(1):
	print("               welcome to ITI  Grosery shop")
	print("1- customr")
	print("2- Admin")
	print("3- Exit")
	choice=int(input("Select Mode For customer press 1 , for Admin press 2 , to Exist press 0 :"))
	if choice ==1:
		print("Welcome Customr")
		print("- To show  products       press 1")
		print("- To Buy   products   press 2")
		print("- To exit                     press 0")
		op1=int(input(" your choice: "))
		if op1==1:
			print(shop)
		elif op1==2:
			sum=0
			print(my_shop)
			buy_list=input("please enter the  number of product you wanna  buy seperatd by space :").split(" ")
			j=0
			for i in buy_list:									
				val=int(shop["products"][j][1])														
				if int(i) > int(shop["products"][j][1]):		 
					print(" your request is out of stock "+str(i))
				else:
					val=val-(int(i))							
					shop["products"][j][1]=val				
					price=int(shop["products"][j][3])		
					sum=sum+(price)*(int(i))					
					j+=1										
					
			print("your total bill value is ="+str(sum)+"$")		
			print(shop)
		elif op1==0:
			print("Thank you")
		else:
			print("invalid choice")
	elif choice ==2:
		print("Welcome Admain")
		print("- To Add new products         press 1")
		print("- To Show Products           press 2")
		print("- To Change cost             press 3")
		print("- To delete product          press 4")	
		print("- To exit                     press 0")
		op2=int(input(" your choice :"))
		if op2==1:
			print("Warnning!! be  careful during entering products details")
			add=input("Enter the product name ,stock , Cost in EGP = , cost Seperated by space :").split(" ")
			shop["products"].append(add)	
		elif op2==2:
			print(shop)
		elif op2==3:
			name_of_product=input(" name of the product to change its price :")		
			for i in shop["products"]:					
				if name_of_product == i[0]:						
					new_cost=input("please enter the new cost :")
					i[3]=new_cost						
				else:
					print("product name not found")
					break;
		elif op2==4:
			prod=input(" product name to delete :")
			removed=0										
			for i in shop["products"]:					
				if prod == i[0]:							 	
					shop["products"].remove(i)			
					removed=1								
					break;		
			if removed ==0:					
				print("product name not found")
			else:	
				print("removed succefully")	
		elif op2==0:
			print("thank you !")		
		else:
			print("invalid choice")			
	elif choice ==0:	
		print("thank you ")
	else :
		print("invalid choice")
