def bitcoin_buyer():
    
    price = int(input('What is Bitcoin price today? '))
    funds = int(input('How much funds you want invested? '))
    result = ('%.7f' %((funds / (price / 100)) / 100))
    print(f'You can buy {result}BTC')


bitcoin_buyer()