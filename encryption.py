##ENCRYPT a word. BUT WITH A FULL ALPHABET

# data sets #
edgar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','!','?']


## input #####################################################
message = input("message: ")
first = input("key: ")

###  key ################################################

key = [None] * len(first)
for n in range(len(first)):
    key[n] = first[n]
    
for n in range(len(key)):
    key[n] = edgar.index(key[n])

## input #####################################################
message_as_a_list = [None] * len(message)

for n in range(len(message)):
    message_as_a_list[n] = edgar.index(message[n])

# encrypt message_as_a_list
for n in range(len(message_as_a_list)):
    message_as_a_list[n] = (message_as_a_list[n] + key[n % len(key)]) % 31

#translate encrypted numbers into encrypted letters
message_as = [None] * len(message_as_a_list)
    
for n in range(len(message_as_a_list)):
    message_as[n] = edgar[message_as_a_list[n]]
    
n = "".join(message_as)
print(n)