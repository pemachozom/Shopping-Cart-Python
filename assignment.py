product_list={'mask':18 ,'bag':112 ,'headphone':101}
ID=[110,100,101]
quantity_available=[3,4,2]		
cart={}
invoice={}
Quantity=[]
item_name=[]
totalA=[]
leftover_quantity=[3,4,2]

print("WELCOME TO FLIPKART")

user_details=input("Do you have an user account? Yes or No?:")
user_details=user_details.upper()

new_user=""
new_password=""	
if user_details=="NO":
	choice=input("Do you want to creat a account? yes or no: ")
	choice=choice.upper()
	if choice=="YES":
		ask=input("Account for BUYER or SELLER?:")
		ask=ask.upper()
		if ask=="BUYER":
			username=input("Name:")
			new_user=username
			passwd=input("PASSWORD:")
			new_password=passwd
			
		if ask=="SELLER":
			username=input("USERNAME:")
			new_user=username
			print("password")
			passwd=input("PASSWORD:")
			new_password=passwd
			
	if choice=="NO":
		print("Thank you!")	
		exit()

	login=input("Do you want to login to your new account? YES OR NO?:")		
	login=login.upper()
	if login=="YES":
		user=input("BUYER OR SELLER:")
		user=user.upper()	

		if user=="BUYER":
			username=input("USERNAME(Buyer):")
			if username!= new_user:
				print("invalid username")
				exit()
			password=input("PASSWORD:")
			if password != new_password:
				print("invalid password")
				exit()
		
			if user=="BUYER" or username==new_user and password==new_password:
				def showCatalog(n):
					return n
				print('catalog=',showCatalog(product_list))
				print("Product ID=",ID)
				print("quantity=",showCatalog(quantity_available))
						
				def addToCart(l):		
					
					for i in range(l):
						n=input("what you want to buy:")
						n=n.upper()
						item_name.append(n)
						
						if n=="MASK":
							m=int(input("quantity:"))
							invoice[n]=m
							Quantity.append(m)
							cart[n]=18*m
							
							
						if n=="BAG":
							m=int(input("quantity:"))
							invoice[n]=m
							Quantity.append(m)
							cart[n]=112*m
							

						if n=="HEADPHONE":
							m=int(input("quantity:"))
							invoice[n]=m
							Quantity.append(m)
							cart[n]=101*m
					print("Item added to your cart=", cart)
					return Quantity
				Buy=input("Do you wish to buy items from above catalog? yes or no?:")
				Buy=Buy.upper()
				if Buy=="YES":
					total_items=int(input("total items you want to buy from catalog:"))
					if total_items<4:
						k=print("Quantity in cart",addToCart(total_items))
					else:
						print("insufficient item")
						exit()
				else:
					print("Thank you!")
					exit()			

				def removeFromCart():
					total_items=int(input("Total items to be removed:"))
					for i in range(total_items):
						key=input("which item do you want to remove:")
						which_index=int(input("index of your item(start from 0 for first item and follows: )"))
						cart.pop(key)
						Quantity.pop(which_index)
						return cart
				verification=input("Do you want to remove items from cart? YES or NO?:")
				verification=verification.upper()
				if verification=="YES":
					print("New cart=",removeFromCart())
					print("New quantity=",Quantity)

				if verification=="NO":
					pass	
				
				def getTotalAmount(a):
					total_amount=0
					for i in a.values():
						total_amount+=i
						totalA.append(total_amount)
					return total_amount
				
				b=print('Total amount =NU.',getTotalAmount(cart))

				def printInvoice():
					print("Item name and the quantity you ordered=",invoice)

					return "Amount to be paid=NU.",getTotalAmount(cart)

				choose=input("Do you want to printInvoice! YES or NO?")
				choose=choose.lower()
				if choose=="yes":
					print(printInvoice())
				else:
					pass

				def buyItems():
					
					address=input("Address:")
					print("Phone number must be exactly 8")
					num=input("mobile number:")
					if len(num)==8:
						return item_name
					else:
						print("invalid phone number")
						exit()	

				confirmation=input("Are you sure that you want to buy the product? YES or NO:")
				confirmation=confirmation.upper()
				if confirmation=="YES":
					print("item name and amount (bill)=",buyItems(),"Total amount=NU.",getTotalAmount(cart))
					cart.clear()
					print("* Thank you, you have successfully bought the items. Your have no more items in cart.*")
					print("Items left in cart=",cart)

				else:
					exit()

		elif user=="SELLER":
			username=input("USER NAME:")
			if username!=new_user:
				print("invalid username")
				exit()

			password=input("PASSWORD:")
			if password != new_password:
				print("invalid password")
				exit()


			if user=='SELLER' and username==new_user and password==new_password:
				
				count=0
				while count>=0:	
					print("catalog=",product_list)
					print("quantity=",quantity_available)
					option=input("Add , Modify or Remove items:")
					option=option.upper()

					if option=="ADD":
						def addProductToCatalog(n):
							tot_i=int(input("total items you want to add:"))
							for i in range(tot_i):
								cata=input("what do you want to add:")
								price_per_piece=int(input("price per piece:"))
								product_list[cata]=price_per_piece
								product_id=int(input("Enter product ID:"))
								ID.append(product_id)

						
								Q=int(input("total quantity you want to add:"))
								quantity_available.append(Q)
								print("catalog=",product_list)
								print("product ID=",ID)
							return quantity_available

						add=input("Do you want to add items to catalog? If yes type y and if no type n")
						add=add.upper()
						print("New quantity available=",addProductToCatalog(add))

					if option=="MODIFY":
						def modify():
							catalog_or_quantity=input("Amount or Quantity:")
							catalog_or_quantity=catalog_or_quantity.lower()
							if catalog_or_quantity=="amount":
								amt_to_modify=int(input("how many amount you want to modify:"))
								for i in range(amt_to_modify):
									item=input("Amount of whic item you want to change:")
									item=item.lower()
									modified_amt=int(input("amount to be modified:"))
									catalog[item]=modified_amt
								return catalog


							if catalog_or_quantity=="quantity":
								no_of_quantity_to_change=int(input("Type total quantity you want to change:"))
								for i in range(no_of_quantity_to_change):
									index=print("0 for mask, 1 for bag and 2 for headphone:")
									which_index=int(input("From above index, for which item do you want to modify quantity:"))
									modified_quantity=int(input("Enter modified quantity:"))
									quantity_available[which_index]=modified_quantity
								return quantity_available
	
						print(modify())

					if option=="REMOVE":
						total_items=int(input("Total items to be removed:"))
						for i in range(total_items):
							key=input("which item do you want to remove:")
							index=print("0 for mask, 1 for bag and 2 for headphone:")
							which_index=int(input("From above index, for which quantity do you want to remove:"))
							product_list.pop(key)
							quantity_available.pop(which_index)
							print(product_list)
							print(quantity_available)

					again=input("Do you want to ADD,MODIFY OR REMOVE again?YES OR NO:")
					again=again.upper()
					if again=="YES":
						count+=1
					if again=="NO":
						print("* Thank you for your service! *")
						exit()	

	if login=="NO":
		exit()					
			
if user_details=="YES":
	

	user=input("BUYER OR SELLER?:")
	user=user.upper()

	if user=='BUYER':
		username=input("USER NAME:")
		if username!='pema':
			print("invalid username")
			exit()
		password=input("PASSWORD:")
		if password != 'pema123':
			print("invalid password")
			exit()
		
	elif user=="SELLER":
		username=input("USER NAME:")
		if username!='pema':
			print("invalid username")
			exit()

		password=input("PASSWORD:")
		if password != 'pema123':
			print("invalid password")
			exit()
	else:
		print("Enter valid user identification")
		exit()		

if user=='BUYER' and username=='pema' and password=='pema123':

	def showCatalog(n):
		return n
	print('catalog=',showCatalog(product_list))
	print("Product ID=",ID)
	print("quantity=",showCatalog(quantity_available))
			
	def addToCart(l):		
		for i in range(l):
			n=input("what you want to buy:")
			n=n.upper()
			item_name.append(n)
			
			if n=="MASK":
				m=int(input("quantity:"))
				invoice[n]=m
				Quantity.append(m)
				cart[n]=18*m
					
			if n=="BAG":
				m=int(input("quantity:"))
				invoice[n]=m
				Quantity.append(m)
				cart[n]=112*m
				
			if n=="HEADPHONE":
				m=int(input("quantity:"))
				invoice[n]=m
				Quantity.append(m)
				cart[n]=101*m
		
		print("Item added to your cart=", cart)
		return Quantity
	Buy=input("Do you wish to buy items from above catalog? yes or no?:")
	Buy=Buy.upper()
	if Buy=="YES":
		total_items=int(input("total items you want to buy from catalog:"))
		if total_items<4:
			k=print("Quantity in cart",addToCart(total_items))
		else:
			print("insufficient item")
			exit()
	else:
		print("Thank you!")
		exit()			

	def removeFromCart():
		total_items=int(input("Total items to be removed:"))
		for i in range(total_items):
			key=input("which item do you want to remove:")
			key=key.upper()
			index=print("0 for mask, 1 for bag, 2 for headphone")
			which_index=int(input("index of your item(start from 0 for first item and follows: )"))
			cart.pop(key)
			Quantity.pop(which_index)
			return cart
	verification=input("Do you want to remove items from cart? YES or NO?:")
	verification=verification.upper()
	if verification=="YES":
		print("New cart=",removeFromCart())
		print("New quantity=",Quantity)

	if verification=="NO":
		pass	
	
	def getTotalAmount(a):
		total_amount=0
		for i in a.values():
			total_amount+=i
			totalA.append(total_amount)
		return total_amount
	
	b=print('Total amount =NU.',getTotalAmount(cart))

	def printInvoice():
		print("Item name and the quantity you ordered=",invoice)

		return "Amount to be paid=NU.",getTotalAmount(cart)

	choose=input("Do you want to printInvoice! YES or NO?")
	choose=choose.lower()
	if choose=="yes":
		print(printInvoice())
	else:
		pass

	def buyItems():
		
		address=input("Address:")
		print("Phone number must be exactly 8")
		num=input("mobile number:")
		if len(num)==8:
			return item_name
		else:
			print("invalid phone number")
			exit()	

	confirmation=input("Are you sure that you want to buy the product? YES or NO:")
	confirmation=confirmation.upper()
	if confirmation=="YES":
		print("item name and amount (bill)=",buyItems(),"Total amount=NU.",getTotalAmount(cart))
		cart.clear()
		print("Thank you, you have successfully bought the items. Your have no more items in cart.")
		print("Items left in cart=",cart)

	if confirmation=="NO":
		exit()

if user=="SELLER" and username=='pema' and password=='pema123':
	count=0
	while count>=0:	
		print("catalog=",product_list)
		print("Product ID=",ID)
		print("quantity=",quantity_available)
		option=input("Add , Modify or Remove items:")
		option=option.upper()

		if option=="ADD":
			def addProductToCatalog(n):
				tot_i=int(input("total items you want to add:"))
				for i in range(tot_i):
					cata=input("what do you want to add:")
					price_per_piece=int(input("price per piece:"))
					product_list[cata]=price_per_piece
					product_id=int(input("Enter product ID:"))

					ID.append(product_id)

			
					Q=int(input("total quantity you want to add:"))
					quantity_available.append(Q)
					print("catalog=",product_list)
					print("product ID=",ID)
				return quantity_available

			add=input("Do you want to add items to catalog? If yes type y and if no type n:")
			add=add.upper()
			print("New quantity available=",addProductToCatalog(add))

		if option=="MODIFY":
			def modify():
				catalog_or_quantity=input("Amount or Quantity:")
				catalog_or_quantity=catalog_or_quantity.lower()
				if catalog_or_quantity=="amount":
					amt_to_modify=int(input("how many amount you want to modify:"))
					for i in range(amt_to_modify):
						item=input("Amount of whic item you want to change:")
						item=item.lower()
						modified_amt=int(input("amount to be modified:"))
						product_list[item]=modified_amt
					return product_list

				if catalog_or_quantity=="quantity":
					no_of_quantity_to_change=int(input("Type total quantity you want to change:"))
					for i in range(no_of_quantity_to_change):
						index=print("0=for apple, 1=for mango and 2=for watermelon:")
						which_index=int(input("From above index, for which item do you want to modify quantity:"))
						modified_quantity=int(input("Enter modified quantity:"))
						quantity_available[which_index]=modified_quantity
					return quantity_available
		
			print(modify())

		if option=="REMOVE":
			total_items=int(input("Total items to be removed:"))
			for i in range(total_items):
				key=input("which item do you want to remove:")
				index=print("0=for apple, 1=for mango and 2=for watermelon:")
				which_index=int(input("From above index, for which quantity do you want to remove:"))
				product_list.pop(key)
				quantity_available.pop(which_index)
				print(product_list)
				print(quantity_available)

		again=input("Do you want to ADD,MODIFY OR REMOVE again?YES OR NO:")
		again=again.upper()
		if again=="YES":
			count+=1
		if again=="NO":
			
			print("Thank you!")
			exit()	