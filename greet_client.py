import greet_pb2_grpc
import greet_pb2
import time
import grpc

class Clients:
    def __init__(self) -> None:
        self.msg_list = []
        self.channel = grpc.insecure_channel('localhost:50051')
        stub = greet_pb2_grpc.GreeterStub(self.channel)
        self.name = None
    def send(self) -> None:
        with self.channel as channel:
            stub = greet_pb2_grpc.GreeterStub(channel)
            self.name = input("Your username: ")
            rpc_call = ""
            while rpc_call != "EXIT":
                rpc_call = input("Message: ")
                hello_request = greet_pb2.HelloRequest(greeting = rpc_call, name = self.name)
                hello_reply = stub.SayHello(hello_request)
                print(hello_reply)
    def like(self, message) -> bool:
        pass

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        # print("1. SayHello - Unary")
        # print("2. ParrotSaysHello - Server Side Streaming")
        # print("3. ChattyClientSaysHello - Client Side Streaming")
        # print("4. InteractingHello - Both Streaming")
        # rpc_call = input("Which rpc would you like to make: ")
        # if rpc_call == "1":
        #     hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
        #     hello_reply = stub.SayHello(hello_request)
        #     print("SayHello Response Received:")
        #     print(hello_reply)
        # elif rpc_call == "2":
        #     hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
        #     hello_replies = stub.ParrotSaysHello(hello_request)

        #     for hello_reply in hello_replies:
        #         print("ParrotSaysHello Response Received:")
        #         print(hello_reply)
        # elif rpc_call == "3":
        #     delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

        #     print("ChattyClientSaysHello Response Received:")
        #     print(delayed_reply)
        # elif rpc_call == "4":
        #     responses = stub.InteractingHello(get_client_stream_requests())

        #     for response in responses:
        #         print("InteractingHello Response Received: ")
        #         print(response)
        with grpc.insecure_channel('localhost:50051') as channel:

            stub = greet_pb2_grpc.GreeterStub(channel)
            name = input("Your username: ")
            rpc_call = ""
            while rpc_call != "EXIT":
                rpc_call = input("Message: ")
                hello_request = greet_pb2.HelloRequest(greeting = rpc_call, name = name)
                hello_reply = stub.SayHello(hello_request)
                # print(hello_reply)
if __name__ == "__main__":
    run()