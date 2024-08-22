from langserve import RemoteRunnable
import sys

if len(sys.argv) < 2:
    print("missing input")
elif len(sys.argv) > 2:
    print("only one input accepted")
else:
    remote_chain = RemoteRunnable("http://localhost:8000/holberton_school_chatbot/")

    print(remote_chain.invoke(sys.argv[1]))
