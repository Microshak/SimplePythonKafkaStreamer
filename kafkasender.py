from BuildData import BuildData
from kafka import KafkaProducer
import json
MessagesToSend = 0

if __name__ == '__main__':  
    #producer = KafkaProducer(bootstrap_servers='wn0-microk.l1nji5hfpjbe5g4bvryy2aon2a.gx.internal.cloudapp.net:9092')
    producer = KafkaProducer(bootstrap_servers='iotlab-cluster7:9092')

    buildData = BuildData()
    template = buildData.loadTemplate("template.json")
    

    x = 0
    while(x < MessagesToSend or MessagesToSend == 0):
        x = x+ 1
        message = buildData.getDistribution(template)
        if(x%1000 == 0):
            print(str(x) + ' ' + message)
        producer.send('test',bytes(json.dumps(message), encoding='utf-8'))
     