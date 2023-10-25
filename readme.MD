

# Introduction
  

This repository contains code and data for my article "[iGEM, GCP, and Neo4j: Where Synthetic Biology Meets Artificial Intelligence](https://dgg32.medium.com/igem-gcp-and-neo4j-where-synthetic-biology-meets-artificial-intelligence-e9e28a333a3f)". 

1. The chatbot.py Python script is the frontend for the chatbot. Agent.py is the script that powers the chatbot.

2. convert_xml_to_csv.py converts the XML download data from iGEM into a sanitized TSV file. It is ready for import into BigQuery.

3. caregory_relation.py generates the node and edge files for Neo4j.

4. agents_vertexai.py is my failed attempt to use VertexAI as the LLM for the chatbot.

# Prerequisite

Neo4j Desktop or AuraDB

OpenAI account

GCP account
  

# Run the chatbot
1. Set up the databases as described in "[iGEM, GCP, and Neo4j: Where Synthetic Biology Meets Artificial Intelligence](https://dgg32.medium.com/igem-gcp-and-neo4j-where-synthetic-biology-meets-artificial-intelligence-e9e28a333a3f)". 
  
2. Install the necessary Python libraries

3. Fill the necessary API key information in config.yaml

4. Run 
```
streamlit run chatbot.py
```


## Authors

  

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
