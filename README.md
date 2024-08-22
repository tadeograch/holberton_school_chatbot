# Holberton School chatbot

A chatbot assistant that uses the RAG architecture to answer questions only about Holberton School using the
content of the [Holberton School Uruguay](https://holbertonschool.uy/) website, based on the LangChain library. 

## Technologies
This chatbot was built in python, using LangChain framework and OpenAI model. Based on [LangChain documentation](https://python.langchain.com/v0.1/docs/get_started/quickstart/) and deployed with Railway.
## Architecture
<img src="https://github.com/tadeograch/holberton_school_chatbot/blob/dev/docs/holberton_school_chatbot_diagram.drawio.png?raw=true">

## Installation

Clone the repository of the Holberton School chatbot project
```bash
git clone https://github.com/tadeograch/holberton_school_chatbot.git
```
Cd into holberton school chatbot directory
```bash
cd holberton_school_chatbot
```
Install requirements
```bash
pip install -r requirements.txt
```
## Basic usage

If you want to run the chatbot locally:
```bash
python service.py
```
And to ask something you can run the client.py with your custom question, for example:
```bash
python client.py "How can I apply to Holberton School?"
```
Or you can interact with LangServe Playground on your browser:
```bash
http://localhost:8000/holberton_school_chatbot/playground
```

## Aditional

### [Holberton School Chatbot](https://holbertonschoolchatbot-production.up.railway.app/holberton_school_chatbot/playground/)

Check the Holberton School chatbot running in Railway

## Overview

I've recently begun exploring Retrieval-Augmented Generation (RAG) and its applications. To deepen my understanding, I decided to create a practical project. As a former Holberton School student, I thought it would be ideal to develop something related to Holberton.

This application is quite basic, reflecting the concepts I've learned so far and building upon a previous project. I hope it not only helps me apply my knowledge but also provides valuable insights to anyone interested in learning more about Holberton School!

## Authors

Tadeo Grach