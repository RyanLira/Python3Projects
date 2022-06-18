## DECRYPT an encryption.

edgar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','!','?']

## input ###########################################
message = input("message: ")
first = input("key: ")


## enter key
key = [None] * len(first)
for n in range(len(first)):
    key[n] = first[n]
    
for n in range(len(key)):
    key[n] = edgar.index(key[n])

#take an encrypted string and turn into a list of numbers

message_as_a_list = [None] * len(message)

for n in range(len(message)):
    message_as_a_list[n] = edgar.index(message[n])

#decrypt the list of numbers
for n in range(len(message_as_a_list)):
    message_as_a_list[n] = (message_as_a_list[n] - key[n % len(key)]) % 31

#turn the list into a string
message_as = [None] * len(message_as_a_list)
    
for n in range(len(message_as_a_list)):
    message_as[n] = edgar[message_as_a_list[n]]
    
n = "".join(message_as)
print(n)