data={1:'navin',2:'kiran',4:'harsh'}
print(data.get(3))
# it gives output as none
data.get('not found')
# gives not found
print(data.get(3,'not found')) # if we give get 3 then we get not found as 3 is not there this method gives something which we entered though the value or key is not present
print(data.get(1,'not found')) # it gives navin as for 1 value is mentioned if not present then only it returns not found
keys=['navin','kiran','harsh']
values=['python','java','js']
data=dict(zip(keys,values)) # merging 2 lists into dictionary
print(data)
# output is {'navin': 'python', 'kiran': 'java', 'harsh': 'js'}
