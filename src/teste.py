import os
os.environ.pop("SSL_CERT_FILE", None)

from dotenv import load_dotenv
from fastmcp import FastMCP
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from crewai import Agent, Task, Crew, Process
from crewai.memory import EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

load_dotenv()
mcp = FastMCP("multi-agent-server")


supabase_params = StdioServerParameters(
    command="npx",
    args=["-y", "@supabase/mcp-server-supabase@latest"],
    env={"SUPABASE_ACCESS_TOKEN": os.getenv("SUPABASE_ACCESS_TOKEN"), **os.environ},
)

supabase_adapter = MCPServerAdapter(supabase_params)
