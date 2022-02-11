from django.shortcuts import render
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Create your views here.
def home(self):

    return render(self,'index.html')

fetch_data=[]
data={}
def getvalue(self):
    if self.POST:

        mesa=ChatBot('Name', read_only=True,logic_adapters=[
            {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry.',
            'maximum_similarity_threshold': 0.80
            }
        ])
        conversation = [
            'Hello',
            'Hello.',
            'What is your name?',
            'My name is chatbot',
            'I need to register a complaint',
            'What kind of complaint you want to register?',
            'Thank you',
            'Welcome',
            'I need to create an account.',
            'Sure, you can create your account from our website.',
            'Bye',
            'Bye, have a nice day.'  
        ]
          

        trainer = ListTrainer(mesa)

        trainer.train(conversation)
        
        
        msg=self.POST.get('msg')
        res = mesa.get_response(msg)
        global data
        data[msg]=res

        print(msg)
        print(res)

        return render(self,'index.html',{'chat':data})
