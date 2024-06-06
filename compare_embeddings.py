from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import openai
import os

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

def main():
    
    print("here1")
    
    # Get embedding for a word.
    # uses text-embedding-ada-002
    embedding_function = OpenAIEmbeddings()
    
    print(f"here2 {embedding_function}")
    
    vector = embedding_function.embed_query("apple")
    
    print("here3")
    
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("apple", "iphone")
    distance_in_vector_space = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    
    print(f"Comparing ({words[0]}, {words[1]}): {distance_in_vector_space}")


if __name__ == "__main__":
    main()
