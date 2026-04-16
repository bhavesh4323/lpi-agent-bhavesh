# LPI Agent - Bhavesh

## What this agent does
This agent connects to the LPI sandbox and answers user questions using multiple tools.

## Tools used
- query_knowledge
- get_insights

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

```bash
python agent.py
