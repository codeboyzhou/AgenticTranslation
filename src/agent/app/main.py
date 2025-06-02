import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Agentic Translation")


# Define the agent
@fast.agent(
    name="Agentic Translation",
    servers=["mcp_server_translation"]
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
