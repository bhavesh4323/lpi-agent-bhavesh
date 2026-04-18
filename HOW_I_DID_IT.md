# HOW I DID IT

## 1) What I did
- **Building the Agent**: The agent was built using various programming languages and tools, primarily Python for scripting. I utilized frameworks such as Flask for building the web service and libraries such as Requests for API interaction.

## 2) Problems I hit
- **Initial Issues**:  One of the significant issues encountered was connecting to the LPI server. There were authentication issues due to incorrect API keys, which halted progress initially. In addition, structuring the agent to handle real-time requests posed challenges depending on how responses were returned.

## 3) How I solved them
- **Debugging and Testing**: To address these issues, extensive debugging was performed. I used logging to track request/response cycle and identified points of failure. After isolating the connection problems with the LPI server, I corrected the API keys and implemented retries for failed connections. Furthermore, I structured the logic to better handle potential faults during interaction with the server.

## 4) What I learned
- **Understanding the MCP Protocol**: Through this process, I gained a deeper understanding of the MCP protocol and its intricacies. I also learned various agent design patterns and principles of explainable AI, which promote transparency in AI-driven tools. This experience has also highlighted the importance of building tools that clearly show their sources and rationale behind their decisions.