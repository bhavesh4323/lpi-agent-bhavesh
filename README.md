# LPI Agent - Bhavesh

## What this agent does
This agent connects to the LPI sandbox and answers user questions using multiple tools.

## Tools used
- query_knowledge
- get_insights

## Requirements
- Python 3.10+
- A running LPI sandbox/server
- `requests` library
## Install
bash 
pip install -r requirements.txt

## How it works
1. Accepts user query
2. Calls LPI tools
3. Combines results
4. Shows sources (explainable AI)

## Example
Question: What is a digital twin?

The agent:
- queries knowledge base
- gets insights
- combines results into answer

## How to run
Start the LPI sandbox/server first.

Then run:
python agent.py "Explain digital twins in simple terms"
If your server is not on the default URL, run:
python agent.py "Explain digital twins in simple terms" --base-url http://localhost:3333
You can also set an environment variable:
export LPI_BASE_URL=http://localhost:3333
python agent.py "Explain digital twins in simple terms"

## Example

The agent:

Accepts a user question
Calls query_knowledge
Calls get_insights
Prints both results
Shows the sources used

Important truth: your agent cannot be “run by anyone” with zero setup if it depends on a local LPI server. What you can do is make it easy for anyone to run by clearly documenting:
- they must start the LPI sandbox
- how to install dependencies
- how to pass the server URL

That is enough for a good Level 3 submission.

If you want, I can also give you a cleaner version that asks the question interactively instead of using command-line arguments.
