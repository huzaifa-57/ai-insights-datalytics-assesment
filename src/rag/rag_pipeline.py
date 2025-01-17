from transformers import pipeline
from transformers.pipelines.base import Pipeline

class RAGPipeline:

    LLM: Pipeline = None

    def __init__(self, model_name="gpt2"):
        if RAGPipeline.LLM is None: # Creating a static single model for all the clients
            self.initialize_llm(model_name)
            RAGPipeline.LLM = self.LLM
        else:
            self.LLM = RAGPipeline.LLM

    @classmethod
    def initialize_llm(cls, model_name: str):
        cls.LLM = pipeline("text-generation", model=model_name)

    def generate_answer(self, context, question):
        input_prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
        return self.LLM(input_prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]