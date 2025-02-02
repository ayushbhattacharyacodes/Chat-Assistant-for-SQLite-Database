# Chat-Assistant-for-SQLite-Database
An interactive QnA based chat assistant, that responds to the question provided by the user, based on the uploaded database.

## Folder structure

```
📦 Chat-Assistant-for-SQLite-Database
├─ .gitignore
├─ README.md
├─ app.py        # Consists of code integrated with streamlit application
├─ database      # consists of database files(you can experiment with the db provided below or add yours)
│  ├─ employee.db
│  ├─ employee.sql
│  └─ employee.txt
├─ requirements.txt
└─ utils.py  #Contains functions to retrieve data from database and to generate SQL commands from user input
```
## Steps to Run the app locally:

+ To run the app , clone the repository into your system
  
+ Next upload your database (with .db extension) 
  in the database folder
  
+ In the next step , create a virtual environment using the command below in your preferred Command Prompts(Anaconda Prompt/Git Bash/ CMD etc.) (Ensure that Anaconda navigator
  is installed in your system and necessary PATH variables for Anaconda Navigator is set):

  ### command:
      "conda create -p venv python==3.xx -y"
      Here the xx is the Python version (preferably >=3.10) 

+ Once the virtual environment is created then activate it using the command below:
  ### command:
      "conda activate ./venv"
  
+ Install the Python libraries mentioned in the requirements file  using the command below:
  ### command:
      "pip install -r requirements.txt"

+ Create a .env file and create a db constant using the database that you have stored in the database folder
  ### constant:
      db = "filename".db

+ After creating the environment variable,setup the Ollama library by installing the OLLAMA library from the link given below:
  https://github.com/ollama/ollama?tab=readme-ov-file
  Once installed , download the llama3.2-vision package in your CMD (Ensure to follow the steps mentioned in the link above, in case llama3.2-vision
  does not work in your system, you can switch to other LLM models offered by OLLAMA with fewer parameters. Also don't forget to change your LLM model name
  inside the ChatOllama class of utils.py file).

+ After setting up of llama model, add the BASE_URL constant in the .env folder (you can find the BASE URL link, in the OLLAMA documentation)
  ### constant:
      BASE_URL = http://localhost:xxxxx/  xxxxx denoting the port number
  
+ Once all the steps are completed, then you can run the streamlit application using the command below:
### command:
    "streamlit run app.py".

### Please Note, the link mentioned in the description (https://chat-assistant-for-app-database-4ja32tvuksfjetchfyfuiu.streamlit.app/), only displays the end app and 
### does not work at the moment due to network issue, however the app will work by running the steps above.
    
