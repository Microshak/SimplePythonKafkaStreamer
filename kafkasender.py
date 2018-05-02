from BuildData import BuildData
from kafka import KafkaProducer
import json
MessagesToSend = 0

if __name__ == '__main__':  
    
    producer = KafkaProducer(bootstrap_servers='[Your Public Ip Address]:9092')

    buildData = BuildData()
    template = buildData.loadTemplate("template.json")
    

    x = 0
    while(x < MessagesToSend or MessagesToSend == 0):
        x = x+ 1
        message = buildData.getDistribution(template)
        if(x%1000 == 0):
            print(str(x) + ' ' + message)
        producer.send('test',bytes(json.dumps(message), encoding='utf-8'))
     