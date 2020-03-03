import redis
cnn=redis.Redis()
print('Washer is staring')
dishes=['salad','bread','entree','dessert']
# num=len(dishes)
for num,dish in enumerate(dishes,start=1):
    msg=dish.encode('utf8')
    cnn.rpush('dishes',msg)
    print('Washed',num)
cnn.rpush('dishes','quit')
print('Washer is done')