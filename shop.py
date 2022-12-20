 
'''
#this project was edited by notepad++ using python 
'''
shop = {"products":[["apples",100,"Cost in EGP =",25],["bannaa",100,"Cost in EGP =",13],["cherry",100,"Cost in EGP =",40]]}
while(1):
	print("********************welcome to ITI  Grosery shop***********************")
	print("1- customr")
	print("2- Admin")
	print("3- Exit")
	choice = int (input(" 1- If you are a Customer  , 2- If you are An Admin  , 0- If you want to Exist "))
	if choice == 1:
		print("Welcome Dear Customr")
		print(" Press--1-- To show products")
		print(" Press--2-- To Buy products")
		print(" Press--0-- To Exit")
		option1 =int(input(" your choice: "))
		if option1 ==1:
			print(shop)
		elif option1 ==2:
			sum=0
			print(my_shop)
			To_buy_list=input("please enter the number of product you wanna buy seperatd by space :").split(" ")
			x=0
			for i in To_buy_list:									
				value=int(shop["products"][x][1])														
				if int(y) > int(shop["products"][x][1]):		 
					print(" your request is out of stock "+str(y))
				else:
					value = value-(int(y))							
					shop["products"][x][1] = value				
					price=int(shop["products"][x][3])		
					sum=sum+(price)*(int(y))					
					x+=1										
					
			print("your total bill value is ="+str(sum)+"EGP")		
			print(shop)
		elif option1 ==0:
			print("Thank you")
		else:
			print("invalid choice")
	elif choice ==2:
		print("Welcome Admain")
		print("1- To Add new products ")
		print("2- To Show Products")
		print("3- To Change cost")
		print("4- To delete product")	
		print("5- Exit")
		option2 =int(input("Enter your choice :"))
		if option2 ==1:
			print("Warnning!! be  careful during entering products details")
			add=input("Enter the product name ,stock , Cost in EGP = , cost Seperated by space :").split(" ")
			shop["products"].append(add)	
		elif option2==2:
			print(shop)
		elif option2==3:
			product_name =input(" name of the product to change its price :")		
			for y in shop["products"]:					
				if product_name == y[0]:						
					new_cost =input("please enter the new cost :")
					y[3]= new_cost						
				else:
					print("product name not found")
					break;
		elif option2==4:
			product =input(" product name to delete :")
			removed=0										
			for i in shop["products"]:					
				if product == y[0]:							 	
					shop ["products"].remove(y)			
					removed =1								
					break;		
			if removed ==0:					
				print("product name not found")
			else:	
				print("removed succefully")	
		elif option2==0:
			print("thank you !")		
		else:
			print("invalid choice")			
	elif choice ==0:	
		print("thank you ")
	else :
		print("invalid choice")
