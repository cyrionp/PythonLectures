sehirler=['Adana','Gaziantep']
plakalar=[1,27]

print(plakalar[sehirler.index('Gaziantep')])

plakalar={'Adana':1,'Gaziantep':27}
print(plakalar['Gaziantep'])

plakalar['Ankara']=6
print(plakalar)

users={'SudeSezen':{
        'age':36,
        'roles':['user'],
        'email':'aaaaa@aa.com',
        'address':'KOMPLE ADANA BİZİM',
        'phone':'01'
      },
      'KadirDurmaz':{
        'age':22,
        'roles':['admin','user'],
        'email':'kadir@aa.com',
        'address':'ANTEP BABA',
        'phone':'911'
}}

print(users['SudeSezen'])
print(users['SudeSezen']['address'])

print(users['KadirDurmaz']['roles'][0])
print(users['SudeSezen']['roles'][0])
