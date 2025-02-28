import tkinter
from functools import wraps
from tkinter import *
import json
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import Text
import nlpcloud
import requests



class NLPApp:

    def __init__(self):
        self.root=Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('resources/logo.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#344955')

        #calling login page function
        self.login_page()


        self.root.mainloop()


        # btn = tkinter.Button(self.root,text='Click Me')
        # btn.pack(pady=10)
    def login_page(self):

        self.clear()

        heading=Label(self.root,text='NLP App')
        heading.pack(pady=20)
        heading.configure(font=('lato',27,'bold'),bg='#344955',fg='#c6d7eb',relief="ridge", bd=5)

        heading = Label(self.root, text='Login')
        heading.pack(pady=20)
        heading.configure(font=('lato', 27, 'bold'), bg='#344955', fg='#FFFFFF')

        label1=Label(self.root,text='Enter Email :')
        label1.pack(pady=(40,30))
        label1.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6')

        self.login_email = Entry(self.root, width=40, bg='#D3D3D3',font=('lato', 10, 'bold'))
        self.login_email.pack(pady=0,ipady=5)

        label1 = Label(self.root, text='Enter Password :')
        label1.pack(pady=(30, 30))
        label1.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6')

        self.login_pw = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'),show='*')
        self.login_pw.pack(pady=0, ipady=5)

        login_btn = Button(self.root,text='Login',font=(('lato', 10, 'bold')),command=self.check_login_info)
        login_btn.pack(pady=25,ipady=5,ipadx=15)

        login_btn = Button(self.root,text='SignUp',font=('lato', 10, 'bold'),command=self.new_registration)
        login_btn.pack(pady=1,ipady=5,ipadx=10)

    def new_registration(self):
        self.clear()

        heading = Label(self.root, text='Register YourSelf')
        heading.pack(pady=20)
        heading.configure(font=('lato', 27, 'bold'), bg='#344955', fg='#FFFFFF')

        label1 = Label(self.root, text='Enter Name :')
        label1.pack(pady=(40,10))
        label1.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6')

        self.name = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'))
        self.name.pack(pady=(10,10), ipady=5)


        label1 = Label(self.root, text='Enter Email :')
        label1.pack(pady=(5,5))
        label1.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6')

        self.email = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'))
        self.email.pack(pady=(5,5), ipady=5)

        label1 = Label(self.root, text='Enter Password :')
        label1.pack(pady=(10,10))
        label1.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6')

        self.password = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'),show='*')
        self.password.pack(pady=(10,10), ipady=5)

        login_btn = Button(self.root, text='SignUp', font=('lato', 10, 'bold'),command=self.write_to_file)
        login_btn.pack(pady=25, ipady=5, ipadx=15)

        login_btn1 = Button(self.root, text='Click Here To Login!', font=(('lato', 10, 'bold')), command=self.login_page)
        login_btn1.pack(pady=25, ipady=5, ipadx=15)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def write_to_file(self):

        with open('user_details.json','r') as fr:
            emails = json.load(fr)
        if self.email.get() in emails:
            messagebox.showinfo('Failed','Email Already Exists')
        else:
            emails[self.email.get()]=[self.name.get(), self.password.get()]
            with open('user_details.json','w') as f:
                json.dump(emails,f,indent=4)
            messagebox.showinfo('Sucess','Registered Sucessfully!')

    def check_login_info(self):
        u_email=self.login_email.get()
        u_pw=self.login_pw.get()
        with open('user_details.json','r') as fr:
            emails = json.load(fr)
            print(u_email)
            if str(u_email) in emails:
                if emails[u_email][1]==u_pw:
                    self.login_page_view()
            else:
                messagebox.showinfo('Failed', 'Username/Password Incorrect!')

    def login_page_view(self):
        self.clear()
        self.root.configure(bg='#375E97')
        preference = Label(self.root, text='Select Your Preference')
        preference.pack(pady=20)
        preference.configure(font=('lato', 25, 'bold'), bg='#375E97', fg='#F1F1F2',wraplength=200, justify="center")

        ner_btn = Button(self.root, text='NER', font=(('lato', 15, 'bold')), bg='#AFDDE5', fg='#962E2A', relief="ridge", bd=1
                         ,command=self.ner_module,wraplength=100, justify="center")
        ner_btn.pack(pady=10,ipadx=30)

        sentiment_btn = Button(self.root, text='Spelling Correction', font=(('lato', 15, 'bold')), bg='#AFDDE5', fg='#962E2A', relief="ridge",bd=1
                               ,command=self.grammer_module,wraplength=100, justify="center")
        sentiment_btn.pack(pady=10, ipadx=30)

        emotional_btn = Button(self.root, text='Code Generation', font=(('lato', 14, 'bold')), bg='#AFDDE5', fg='#962E2A',relief="ridge", bd=1
                               ,command=self.generate_code_module,wraplength=150, justify="center")
        emotional_btn.pack(pady=10, ipadx=30)

        emotional_btn = Button(self.root, text='Sentiment Analysis', font=(('lato', 14, 'bold')), bg='#AFDDE5',
                               fg='#962E2A', relief="ridge", bd=1
                               , command=self.generate_sentiment_analysis, wraplength=150, justify="center")
        emotional_btn.pack(pady=10, ipadx=30)

        ner_submit_btn = Button(self.root, text='Logout', font=(('lato', 10, 'bold')), bg='#66FCF1', fg='#962E2A',
                                relief="ridge", bd=5, wraplength=100, justify="center",
                                command=self.login_page)
        ner_submit_btn.pack(pady=50, ipadx=50)

    def ner_module(self):
        self.clear()

        user_string = Label(self.root, text='Enter the String')
        user_string.pack(pady=(50, 10))
        user_string.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6',wraplength=200, justify="center")

        self.string = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'))
        self.string.pack(pady=(10, 10), ipady=5)


        user_entity = Label(self.root, text='Enter the Entity You Want To Search')
        user_entity.pack(pady=(10, 10))
        user_entity.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6',wraplength=200, justify="center")

        self.entity = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'))
        self.entity.pack(pady=(10, 10), ipady=5)


        ner_submit_btn = Button(self.root, text='Search', font=(('lato', 15, 'bold')), bg='#FFBB00', fg='#962E2A',
                               relief="ridge", bd=5, wraplength=200, justify="center",command=self.ner_api_response)
        ner_submit_btn.pack(pady=10, ipadx=50)

        ner_submit_btn = Button(self.root, text='Home', font=(('lato', 10, 'bold')), bg='#B5FFFF', fg='#962E2A',
                                relief="ridge", bd=5, wraplength=100, justify="center",
                                command=self.login_page_view)
        ner_submit_btn.pack(pady=10, ipadx=50)

    def grammer_module(self):
        self.clear()

        user_string_grammer = Label(self.root, text='Enter the String')
        user_string_grammer.pack(pady=(50, 10))
        user_string_grammer.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6',wraplength=200, justify="center")

        self.string_grammer_val = Entry(self.root, width=40, bg='#D3D3D3', font=('lato', 10, 'bold'))
        self.string_grammer_val.pack(pady=(10, 10), ipady=15)

        ner_submit_btn = Button(self.root, text='Correct', font=(('lato', 15, 'bold')), bg='#FFBB00', fg='#962E2A',
                               relief="ridge", bd=5, wraplength=200, justify="center",command=self.grammer_api_response)
        ner_submit_btn.pack(pady=10, ipadx=50)

        ner_submit_btn = Button(self.root, text='Home', font=(('lato', 10, 'bold')), bg='#B5FFFF', fg='#962E2A',
                                relief="ridge", bd=5, wraplength=100, justify="center",
                                command=self.login_page_view)
        ner_submit_btn.pack(pady=10, ipadx=50)

    def generate_code_module(self):
        self.clear()

        user_string_instruction = Label(self.root, text='Enter the Instruction')
        user_string_instruction.pack(pady=(50, 10))
        user_string_instruction.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6',wraplength=200, justify="center")

        self.text_box = tkinter.Text(self.root, height=5, width=40, wrap="word")  # wrap="word" ensures proper word wrapping
        self.text_box.pack(pady=10)

        ner_submit_btn = Button(self.root, text='Generate', font=(('lato', 15, 'bold')), bg='#FFBB00', fg='#962E2A',
                               relief="ridge", bd=5, wraplength=200, justify="center",command=self.generate_code_api_response)
        ner_submit_btn.pack(pady=10, ipadx=50)

        ner_submit_btn = Button(self.root, text='Home', font=(('lato', 10, 'bold')), bg='#B5FFFF', fg='#962E2A',
                                relief="ridge", bd=5, wraplength=100, justify="center",
                                command=self.login_page_view)
        ner_submit_btn.pack(pady=10, ipadx=50)

    def generate_sentiment_analysis(self):
        self.clear()

        user_string_instruction_sentiment = Label(self.root, text='Enter the Instruction')
        user_string_instruction_sentiment.pack(pady=(50, 10))
        user_string_instruction_sentiment.configure(font=('lato', 18, 'bold'), bg='#344955', fg='#a2d5c6',wraplength=200, justify="center")

        self.text_box_val = tkinter.Text(self.root, height=5, width=40, wrap="word")  # wrap="word" ensures proper word wrapping
        self.text_box_val.pack(pady=10)

        ner_submit_btn = Button(self.root, text='Generate', font=(('lato', 15, 'bold')), bg='#FFBB00', fg='#962E2A',
                               relief="ridge", bd=5, wraplength=200, justify="center",command=self.generate_sentiment_api_response)
        ner_submit_btn.pack(pady=10, ipadx=50)

        ner_submit_btn = Button(self.root, text='Home', font=(('lato', 10, 'bold')), bg='#B5FFFF', fg='#962E2A',
                                relief="ridge", bd=5, wraplength=100, justify="center",
                                command=self.login_page_view)
        ner_submit_btn.pack(pady=10, ipadx=50)

    def ner_api_response(self):

        string_val = self.string.get()
        entity_val = self.entity.get()
        client = nlpcloud.Client("finetuned-llama-3-70b", "25c8717fab9a0a2dddf4c31e1b09531480e548ec", gpu=True)
        ner_response = client.entities(string_val,
            searched_entity=entity_val
        )
        messagebox.showinfo('NER', ner_response)

    def grammer_api_response(self):

        string_grammer_val=self.string_grammer_val.get()
        client = nlpcloud.Client("finetuned-llama-3-70b", "25c8717fab9a0a2dddf4c31e1b09531480e548ec", gpu=True)
        grammer_response=client.gs_correction(
               string_grammer_val
        )
        result=grammer_response['correction']
        output = Label(self.root, text=result)
        output.pack(pady=(50, 10))
        output.configure(font=('lato', 13, 'bold'), bg='#344955', fg='#a2d5c6', wraplength=200,
                                  justify="center")

    def generate_code_api_response(self):
        string_instruction_val = self.text_box.get("1.0", tkinter.END)
        client = nlpcloud.Client("finetuned-llama-3-70b", "25c8717fab9a0a2dddf4c31e1b09531480e548ec", gpu=True)
        code=client.code_generation(
            string_instruction_val
        )

        code_result= code['generated_code']
        code_output = Text(self.root, height=10, width=50, wrap="word", font=('lato', 13), bg='#344955', fg='#a2d5c6')
        code_output.pack(expand=True,side='left')

        scrollbar = Scrollbar(self.root, command=code_output.yview)
        scrollbar.pack(side="right", fill="y")

        code_output.config(yscrollcommand=scrollbar.set)

        code_output.insert('1.0',str(code_result))

        # code_output.configure(font=('lato', 13, 'bold'), bg='#344955', fg='#a2d5c6', wraplength=200,
        #                  justify="center")

        # messagebox.showinfo('Code', string_instruction_val)

    def generate_sentiment_api_response(self):
        sentiment_text=self.text_box_val.get("1.0", tkinter.END)
        API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
        HEADERS = {"Authorization": "Bearer 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"}

        data = {"inputs": sentiment_text}
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response=response.json()
        code_output1 = Text(self.root, height=10, width=40, wrap="word", font=('lato', 13,'bold'), bg='#344955', fg='#FFFFFF')
        code_output1.pack(expand=False, side='left')
        str2 = ''

        for item in response:
            i = 0
            for j in item:
                str2 = str2 + f"Sentiment: {item[i]['label']}, Score: {item[i]['score']:.2f}\n"
                i += 1
        code_output1.insert('1.0',str(str2))


        # messagebox.showinfo('Sentiment',response.json())



nlpapp=NLPApp()

