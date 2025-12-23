import asyncio
import logging
from asyncua import Server

_logger = logging.getLogger(__name__)


async def main():
    _logger.info("Starting OPC UA server...")
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # set up our own namespace, not mandatory but good practice
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = await objects.add_object(idx, "MyObject")
    myvar = await myobj.add_variable(idx, "MyVariable", 6.7)
    await myvar.set_writable()  # Set MyVariable to be writable by clients

    _logger.info("Starting server!")
    async with server:
        while True:
            await asyncio.sleep(1)

def run_server():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

if __name__ == "__main__":
    run_server()
