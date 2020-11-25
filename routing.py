#this is a script to find the routing route

print("This script finds the best match for an IPV4 address for the next hop. You give it an address, a subnet number, and a then the highest subnet choice available. The script will tell you if it is a match. It it is not a match, try the second highest subnet address.")

#input
num1=int(input("Type block1 of the IPV4 to be routed pls as 4 blocks i.e. 10.0.11.65 you would start with 10: "))
num2=int(input("Type block2 of the IPV4 to be routed pls as 4 blocks i.e. 10.0.11.65 you would start with 0: "))
num3=int(input("Type block3 of the IPV4 to be routed pls as 4 blocks i.e. 10.0.11.65 you would start with 11: "))
num4=int(input("Type block4 of the IPV4 to be routed pls as 4 blocks i.e. 10.0.11.65 you would start with 65: "))

print("Your input is the following IPV4 to be routed: ")
print(str(num1)+"."+str(num2)+"."+str(num3)+"."+str(num4))
print("##################################################################")
print("")

subnet=int(input("What is the highest subnet number (32-0) i.e. the number after the /? or the number of 1's in 255.255.240.0 i.e 20 -- Your subnet is : "))
print("##################################################################")
print("")

choice_block1=int(input("Type block1 of the IPV4 of the addy with that subnet: "))
choice_block2=int(input("Type block2 of the IPV4 of the addy with that subnet: "))
choice_block3=int(input("Type block3 of the IPV4 of the addy with that subnet: "))
choice_block4=int(input("Type block4 of the IPV4 of the addy with that subnet: "))

print("Your routing table addy with the highest remaining subnet is the following IPV4: ")
print(str(choice_block1)+"."+str(choice_block2)+"."+str(choice_block3)+"."+str(choice_block4))
print("##################################################################")
print("")


#apply subnet binary Addition
#convert highest subnet IPV4 into binary
#compare and print match/no match


#DecimalToBinary(nums)
num1_bi=(format(num1, 'b').zfill(8))
num2_bi=(format(num2, 'b').zfill(8))
num3_bi=(format(num3, 'b').zfill(8))
num4_bi=(format(num4, 'b').zfill(8))
print("IPV4 to be routed in binary is: ")
nums_bi=(str(num1_bi)+str(num2_bi)+str(num3_bi)+str(num4_bi))
print(nums_bi)
print("")

#subnet to binary
sub_bi=str("1"*subnet)+(32-subnet)*"0"
print("The subnet in binary is: ")
print(sub_bi)
print("")

#need to convert into binary for & and return a binary
print("The address to be routed after subnet binary-and is: ")
nums_bi_AND_sub_bi=bin(int(nums_bi,2) & int(sub_bi,2))
print(nums_bi_AND_sub_bi)



#DecimalToBinary(choice_blocks)
choice_block1_bi=(format(choice_block1, 'b').zfill(8))
choice_block2_bi=(format(choice_block2, 'b').zfill(8))
choice_block3_bi=(format(choice_block3, 'b').zfill(8))
choice_block4_bi=(format(choice_block4, 'b').zfill(8))
print("IPV4 of routing table choice address in binary is: ")
choice_blocks_bi=(str(choice_block1_bi)+str(choice_block2_bi)+str(choice_block3_bi)+str(choice_block4_bi))
print(choice_blocks_bi)
print("")

#choice_blocks_bi=format(int(choice_blocks_bi),'b')
choice_blocks_bi_AND_sub_bi=bin(int(choice_blocks_bi,2) & int(sub_bi,2))
print("IPV4 of routing table choice after subnet binary-and is: ")
print(choice_blocks_bi_AND_sub_bi)


#compare
if (choice_blocks_bi_AND_sub_bi==nums_bi_AND_sub_bi):
    print("Yes - the two addresses are in the same subnet.")
else:
    print("NO - not a match. The addresses are not in the same subnet.")

