# Cohere Platform: 

Modular PaaS platform for developers to build their custom LLM models.

Eg
    - General Lang model (txt input -> generated text).
    - Representational Lang model (input -> embedding).
    - Summarizations 
    - Prompts usecase
        - tuning task description
        - adding examples in the prompt
        - adding the examples in the prompt
    - Classification
        - message -> Language understanding : message classification -> response based on users definition.
    
    - Semantic Similarity:
        -  input (with relevant nature of facts to be compared) -> checking the similarity. 


## Components : 

1. **Playground**: 
    - Similar to the openAI playground with the possiblity to train , deploy and test the models with various types of text prompts
    - also consist of the advanced parameters that integrates the hyperparameters defined by the package developed (tf/ nn) which can be managed with more granular way.


2. **Embed**: 
    - This is the output layer showing the embeddings of the various categories of results and helps for the visualisation for model evaluation.
    - Similar to the KNN and other open source algorithm based visualization by py


3. **Classifier**:
    - Allows you to create the instruction trained model from a few labeled examples.


## For developers 
- [understanding the Cohere SDK in py, nodejs, etc](https://cohere-sdk.readthedocs.io/en/latest/).
- Divided into following steps:
    - Initiating with hte given model and inputs (along with examples if already imported). 
    - Defining the example and labels.
    - Then providing the input, and based on the category of model and prediction you will fetch the result.


## integrations with the other ecosystem providers 

1. Vector / tensor databases : 
    - Qdrant 
    - Marqo (TODO: i will be sharing the open-source integration).
    - Weaviate: Allows storing the Open source vectors / search engine.
    - Pinecone: 
    - Milvus:
    - Zilliz:
    
2. Mlops / lifecycle products:
    - Surge AI: labeling platform for labeled dataset    
    - Scale: Provides the sabelled dataset. 

